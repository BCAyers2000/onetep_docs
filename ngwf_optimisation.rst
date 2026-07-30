============================
NGWF optimisation in ONETEP
============================

:Author: Brad Ayers, University of Southampton
:Date:   July 2026

Overview
========

A ground-state calculation in ONETEP is a pair of nested loops. The inner loop
optimises the density kernel :math:`K^{\alpha\beta}` with the NGWFs held
fixed, and the outer loop then relaxes the NGWFs
:math:`\{\phi_{\alpha}(\mathbf{x})\}` themselves. Everything on this page
concerns the outer loop. Three optimisers are available for it, and
``ngwf_cg_type`` chooses between them:

.. code::

   ngwf_cg_type : NGWF_FLETCHER    # conjugate gradients (default)
   ngwf_cg_type : NGWF_POLAK       # conjugate gradients, Polak-Ribiere
   ngwf_cg_type : NGWF_LBFGS       # limited-memory BFGS

Choosing an optimiser
---------------------

``NGWF_FLETCHER`` is the default and needs no further keywords. It differs
from ``NGWF_POLAK`` in a single scalar, and the two cost the same per
iteration, so which of the pair converges faster is a property of the system
rather than a general rule.

``NGWF_LBFGS`` approximates the inverse Hessian from the last
``ngwf_lbfgs_history`` steps, twelve of them by default, at the cost of one
extra set of NGWF-sized arrays per stored step. On metallic systems it usually
converges in fewer NGWF iterations than conjugate gradients does. Repeat runs
of the same input reproduce to the last digit.

One interaction is worth knowing about. Under :ref:`fast-density`,
``NGWF_LBFGS`` fixes :ref:`trimmed-boxes-threshold` at :math:`10^{-7}` rather
than leaving it adaptive. Setting that keyword yourself overrides the choice.

The gradient and the metric
---------------------------

Differentiating the total energy with respect to the NGWF expansion
coefficients gives a covariant gradient :math:`g_{\alpha}`. The NGWFs are not
orthonormal, so the search direction that corresponds to it lives in the dual
space, and is recovered by raising the index with the inverse overlap matrix,

.. math::
   g^{\alpha} = \sum_{\beta} S^{\alpha\beta} g_{\beta} , \qquad
   S_{\alpha\beta} = \langle \phi_{\alpha} | \phi_{\beta} \rangle .

Before either form is used, :math:`g_{\alpha}` is preconditioned. The default
is the modified Teter reciprocal-space kinetic-energy preconditioner of
:doc:`recip_precond`, which rescales the gradient by an approximation to the
inverse kinetic-energy operator so that high and low spatial frequencies
converge at comparable rates. It acts on :math:`g_{\alpha}` only, and never on
:math:`g^{\alpha}`.

Both forms are carried throughout the optimisation, since every inner product
below pairs a contravariant object with a covariant one and sums over
k-points,

.. math::
   \langle u, v \rangle = \sum_{\mathbf{k}} w_{\mathbf{k}}
   \sum_{\alpha} u^{\alpha} v_{\alpha} ,

where :math:`w_{\mathbf{k}}` is the weight of k-point :math:`\mathbf{k}`.

Measuring convergence
---------------------

All three optimisers are monitored by the same quantity, the root-mean-square
NGWF gradient

.. math::
   \mathrm{RMS} = \sqrt{\frac{\bigl| \langle g, g \rangle \bigr|}{N}} ,

where :math:`N` is the number of psinc coefficients. Because the measure is
shared, :ref:`ngwf-threshold-orig` transfers unchanged between the optimisers,
and their iteration counts may be compared directly.

.. note::
   :math:`\langle g, g \rangle` is not positive definite, because the
   preconditioner is applied to :math:`g_{\alpha}` and not to
   :math:`g^{\alpha}`. Close to a stationary point it can change sign, and
   that is why the test takes its absolute value.

Conjugate gradients
===================

Both conjugate-gradient variants build their search direction by mixing the
current gradient with the previous direction,

.. math::
   d^{(k)} = -g^{(k)} + \beta^{(k)} d^{(k-1)} ,

and then line search along :math:`d^{(k)}` to decide how far to go. The only
difference between them is the coefficient :math:`\beta`.

The coefficient
---------------

``NGWF_FLETCHER``, the default, takes the Fletcher-Reeves form,

.. math::
   \beta^{(k)} = \frac{\langle g^{(k)}, g^{(k)} \rangle}
                      {\langle g^{(k-1)}, g^{(k-1)} \rangle} ,

while ``NGWF_POLAK`` takes the Polak-Ribiere form, written here in terms of
the gradient difference :math:`y^{(k)} = g^{(k)} - g^{(k-1)}`,

.. math::
   \beta^{(k)} = \frac{\langle g^{(k)}, y^{(k)} \rangle}
                      {\langle d^{(k-1)}, y^{(k)} \rangle} .

A negative Polak-Ribiere coefficient is truncated to zero
[GilbertNocedal1992]_, which restarts along steepest descent for that step.
Either coefficient is discarded, with a warning, if it exceeds two in
magnitude. The direction also restarts after :ref:`elec-cg-max` consecutive
steps, and whenever a line search fails.

The line search
---------------

Each iteration already knows the energy and the slope at the starting point,
and evaluates the energy once more at a trial step of length
:math:`\tau_{\mathrm{t}}` along :math:`d`. A parabola through those three
pieces of information,

.. math::
   c = \frac{2 \left[ F(\tau_{\mathrm{t}}) - F(0)
       - \tau_{\mathrm{t}} \langle g, d \rangle \right]}
       {\tau_{\mathrm{t}}^{2}} ,
   \qquad
   \tau^{\ast} = - \frac{\langle g, d \rangle}{c} ,

gives the step actually taken, subject to :ref:`ngwf-cg-max-step`. Should the
minimiser of that parabola point the wrong way along :math:`d`, a second trial
is taken at :math:`2\tau_{\mathrm{t}}` and a cubic is fitted through the three
energies instead. The output reports whichever fit was used, as ``Selected
quadratic step`` or ``Selected cubic step``.

The trial length is not fixed, but carries over from one iteration to the
next. A successful search sets

.. math::
   \tau_{\mathrm{t}} \leftarrow
   \sqrt{\tau_{\mathrm{t}} \, \tau^{\ast}} ,

the geometric mean of the current trial and the step just taken, while a
failed search halves it. It is never allowed below :math:`10^{-4}`.

Limited-memory BFGS
===================

Conjugate gradients rebuilds its picture of the energy surface from scratch at
every iteration. ``NGWF_LBFGS`` instead keeps the last :math:`m` steps and the
change in gradient across each of them, and uses that history to approximate
the inverse Hessian [Liu1989]_, which lets it take a scaled Newton-like step
straight away. ONETEP already uses the same scheme for geometry optimisation,
storing atomic positions and forces in place of NGWF coefficients and
gradients (see :doc:`Geometry_Relaxation`).

NGWFs make this harder than atomic positions do. Moving the NGWFs invalidates
the density kernel, so the energy only becomes meaningful again once the inner
loop has re-solved for :math:`K^{\alpha\beta}`. An energy evaluated at the
rotated kernel is cheap, but it belongs to a different surface from the one
being minimised.

The optimiser therefore does not judge a step when it takes it. It commits,
and assesses the result one iteration later, using the energy the outer loop
has to produce in any case.

The search direction
--------------------

The direction comes from two sweeps over the stored history of :math:`m`
curvature pairs :math:`(s_i, y_i)`, in which :math:`s_i` is a committed step
and :math:`y_i` the gradient difference across it. Both sweeps work on a
single vector, which starts at the current gradient, :math:`q = g`.

The first sweep runs from the newest pair to the oldest. At each pair it
records a scalar :math:`a_i` and subtracts that multiple of :math:`y_i`:

.. math::
   a_i = \frac{\langle s_i, q \rangle}{\langle s_i, y_i \rangle} ,
   \qquad
   q \leftarrow q - a_i \, y_i .

Between the sweeps, :math:`q` is scaled by the curvature of the newest pair,
which sets the size of the initial inverse-Hessian estimate:

.. math::
   \gamma = \frac{\langle s_m, y_m \rangle}{\langle y_m, y_m \rangle} ,
   \qquad
   q \leftarrow \gamma \, q .

The second sweep runs back from the oldest pair to the newest, restoring to
:math:`q` the amount by which the first sweep over-corrected:

.. math::
   b_i = \frac{\langle y_i, q \rangle}{\langle s_i, y_i \rangle} ,
   \qquad
   q \leftarrow q + (a_i - b_i) \, s_i .

The search direction is then :math:`d = -q`.

The deferred Wolfe verdict
--------------------------

The step commits at :math:`\tau = \min(1, R)`, where :math:`R` is a
step-length memory, and no verdict is taken at the time. One iteration later,
once an honest energy :math:`F` exists, the step just taken is judged against
the two Wolfe conditions [NocedalWright]_,

.. math::
   F^{(k)} - F^{(k-1)} \; \le \; w_1 \, \tau \,
   \langle g^{(k-1)}, d \rangle ,

.. math::
   \bigl| \langle g^{(k)}, d \rangle \bigr| \; \le \; w_2 \,
   \bigl| \langle g^{(k-1)}, d \rangle \bigr| ,

with :math:`w_1 = 0.01` and :math:`w_2 = 0.5`. Acceptance rests on the
sufficient-decrease condition alone. The curvature condition earns nothing
more than a doubling of the rate at which :math:`R` recovers towards unity.

A step that fails sufficient decrease is rejected. The pre-step NGWFs, kernel
and Hamiltonian are restored in full, and the same direction is retaken at the
minimiser of the parabola through the start energy, the slope and the rejected
point,

.. math::
   \tau^{\ast} = \frac{- \tau^2 \langle g^{(k-1)}, d \rangle}
   {2 \left[ \Delta F - \tau \langle g^{(k-1)}, d \rangle \right]} ,
   \qquad \Delta F = F^{(k)} - F^{(k-1)} ,

clipped to :math:`[0.1\tau, 0.5\tau]`. The retry consumes an iteration, and is
itself judged next time round.

Every judged step also reports a model quality, the ratio of the reduction
actually won to the reduction predicted by the quadratic model whose minimiser
is the full step,

.. math::
   \Delta F_{\mathrm{model}} = \langle g^{(k-1)}, d \rangle
   \left( \tau - \tfrac{1}{2}\tau^2 \right), \qquad
   \rho = \frac{\Delta F}{\Delta F_{\mathrm{model}}} ,

so :math:`\rho` reads exactly as it would in a trust region, even though the
verdict arrives an iteration late.

Steepest-descent fallback
-------------------------

With no history yet, or after a direction that turns out to point uphill, the
step falls back to a scaled steepest descent, sized by a shrinking probe loop.
A probe is taken at :math:`\tau = \min(1, R)` and shrunk by a factor of four
until the energy falls, for at most six trials. The parabola through the
reference energy, the slope and the probe,

.. math::
   c = \frac{2 \left[ F(\tau) - F_{\mathrm{ref}}
   - \tau \langle g, d \rangle \right]}{\tau^2} , \qquad
   \tau^{\ast} = - \frac{\langle g, d \rangle}{c} ,

then sets the committed length. The step-length memory answers the model
quality that results: :math:`R` grows by a factor of two above
:math:`\rho = 0.75`, shrinks by a factor of four below :math:`\rho = 0.25`,
and is held within :math:`[10^{-3}, 4]`. As on the quasi-Newton path, the
trial energies only size the step, and the verdict is still deferred.

Curvature-pair hygiene
----------------------

Two mechanisms keep the stored history trustworthy.

**Admission.** A pair enters the history on a scale-free cosine floor rather
than on a bare test of sign,

.. math::
   \langle s_i, y_i \rangle > \varepsilon \,
   \lVert s_i \rVert \, \lVert y_i \rVert ,
   \qquad \varepsilon = 10^{-8} ,

in which each norm contracts an object with itself, :math:`s_i` with
:math:`s_i` in covariant form and :math:`y_i` with :math:`y_i` in
contravariant form, rather than pairing the two. This rejects the numerically
meaningless pairs that a test on the sign of :math:`\langle s_i, y_i \rangle`
alone would let through.

**Retirement.** The secant condition a pair encodes is only local on the scale
of the step that measured it. Each pair therefore accumulates the motion
committed since it was formed, and retires once that drift exceeds a multiple
of its own length,

.. math::
   \mathrm{drift}_i > C \, \lVert s_i \rVert , \qquad C = 41 ,

where :math:`\lVert s_i \rVert` is again the covariant norm of the step that
formed the pair.

Retirement is what makes a deep history safe. Without it, an old pair goes on
describing curvature at a point the calculation left long ago.

Termination
-----------

``NGWF_LBFGS`` never aborts. It banks the lowest-energy NGWFs it has seen at
every iteration, and restores them if the run ends unconverged, since the
energy is the only reliable way to rank two states. Rather than stop on an
error, it declares a numerical floor when any one of the following holds:

-  neither a new RMS low nor a new energy best for 20 iterations,
-  three consecutive rejected steps,
-  three consecutive steps whose energy change was too small to judge,
-  two consecutive step-floor resets.

Keywords
========

-  ``ngwf_cg_type`` [Basic, string, default ``NGWF_FLETCHER``\ ] The
   outer-loop optimiser: one of ``NGWF_FLETCHER``, ``NGWF_POLAK`` or
   ``NGWF_LBFGS``. An unrecognised value stops the calculation.

-  ``ngwf_lbfgs_history`` [Basic, integer, default ``12``\ ] How many
   curvature pairs ``NGWF_LBFGS`` stores. Must be positive.

-  ``devel_code : LBFGS_DIAG`` [Developer] Print a diagnostic block for every
   L-BFGS step.

-  ``devel_code : NGWF_SIGNDIAG`` [Developer] Print the signed value of
   :math:`\langle g, g \rangle` at each inner iteration.

Output
======

Conjugate gradients reports its line search:

.. code-block:: fortran

   RMS gradient                =       0.00033984428963
   Trial step length           =               0.533006
   Gradient along search dir.  =         -0.01362570404
   Functional at step 0        =      -6.25996862976909
   Functional at step 1        =      -6.26501393963314
   Functional predicted        =      -6.26591569801978
   Selected quadratic step     =               0.872919
   Conjugate gradients coeff.  =               0.185057
   --------------------------- NGWF line search finished --------------------------

L-BFGS reports one block per iteration. The verdict on the previous step comes
first, because that is the order in which the iteration performs them, and the
step actually taken follows:

.. code-block:: fortran

   --------------------------- Verdict on iteration 003 ---------------------------
   Outcome                     =               ACCEPTED
   Model quality (rho)         =               0.651822
   Energy change               =        -6.00691181E-03
   Sufficient decrease         =        -1.18746805E-04
   Curvature g . d             =        -2.80881302E-04
   ------------------------------- NGWF L-BFGS step -------------------------------
   RMS gradient                =       0.00016813908044
   Functional at step 0        =      -6.26552039073402
   Step type                   =                  LBFGS
   Step length                 =               1.000000
   Step memory                 =               1.000000
   Curvature pairs             =                      3
   Energy evaluations          =                      1
   Predicted total energy      =      -6.26677959921316

``Step type`` reads ``LBFGS`` for a quasi-Newton step and ``SD`` for the
steepest-descent fallback, and ``Outcome`` is ``ACCEPTED``, ``REJECTED`` or
``NEUTRAL``. Any event raised during a step, such as a retired pair or a
history reset, is printed immediately above the block.

The diagnostic block
--------------------

Adding ``devel_code : LBFGS_DIAG`` prints a further block with each step:

.. code-block:: fortran

   ============================================================================
   L-BFGS STEP DIAGNOSTIC                                  iteration       4
   ----------------------------------------------------------------------------
   direction          :            LBFGS  step verdict       :         DEFERRED
   curvature pairs    :           3 / 12  new pair stored    :              yes
   non-descent count  :            0 / 3  history reset      :               no
   ----------------------------------------------------------------------------
   RMS gradient       :     1.681391E-04  RMS grad ratio     :       0.41381247
   MAX gradient       :     0.000000E+00  signed <g,g>       :     3.246783E-03
   slope (g.d)        :    -1.629860E-03  chemical pot. mu   :      -0.35995427
   gamma              :       0.50513111  newest s.y         :     1.174888E-02
   newest y.y         :     2.325908E-02  energy evals       :                1
   newest s.s         :     1.561757E-02  pair cosine        :       0.65235523
   ----------------------------------------------------------------------------
      n        tau           pred          A(trial)        actual         rho
      1   1.000000   0.000000E+00       -6.26677960  1.259208E-03  0.0000E+00
   ----------------------------------------------------------------------------
   accepted           :              yes  step taken         :       1.00000000
   radius (in)        :       1.00000000  radius (out)       :       1.00000000
   A(start)           :      -6.26552039  A(predicted)       :      -6.26677960
   A(final)           :      -6.26552039  dA(actual)         :     0.000000E+00
   pairs retired      :                0  stack drift max    :       0.98545277
   ============================================================================

The fields worth reading first are ``signed <g,g>``, which shows whether the
metric is still positive, ``pair cosine``, the quantity tested on admission,
``stack drift max``, which says how close the oldest pair is to retirement,
and the trial table, which gives the true cost of the step in energy
evaluations. ``step verdict`` reads ``DEFERRED`` because the verdict on this
step is delivered in the next iteration's report.

References
==========

.. [GilbertNocedal1992] Jean Charles Gilbert, Jorge Nocedal, "Global
   convergence properties of conjugate gradient methods for optimization",
   *SIAM J. Optim.* **1992**, 2, 21, https://doi.org/10.1137/0802003
