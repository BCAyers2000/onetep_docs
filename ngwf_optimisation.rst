============================
NGWF optimisation in ONETEP
============================

:Author: Brad Ayers, University of Southampton
:Date:   July 2026

Overview
========

ONETEP's ground-state calculation is a nested pair of loops. The inner loop
optimises the density kernel :math:`K^{\alpha\beta}` at fixed NGWFs; the outer
loop then moves the NGWFs :math:`\{\phi_{\alpha}(\mathbf{x})\}` themselves. This
page concerns the outer loop, which is selected with

.. code::

   ngwf_cg_type : NGWF_FLETCHER    # conjugate gradients (default)
   ngwf_cg_type : NGWF_POLAK       # conjugate gradients, Hestenes-Stiefel
   ngwf_cg_type : NGWF_LBFGS       # limited-memory BFGS

The gradient and the metric
---------------------------

Differentiating the total energy with respect to the NGWF expansion
coefficients gives a *covariant* gradient :math:`g_{\alpha}`. Because the NGWFs
are not orthonormal, the corresponding search direction lives in the dual space
and is obtained by raising the index with the inverse overlap,

.. math::
   g^{\alpha} = \sum_{\beta} S^{\alpha\beta} g_{\beta} , \qquad
   S_{\alpha\beta} = \langle \phi_{\alpha} | \phi_{\beta} \rangle .

Every inner product below is the k-point-weighted pairing of a contravariant
object with a covariant one,

.. math::
   \langle u, v \rangle = \sum_{\mathbf{k}} w_{\mathbf{k}}
   \sum_{\alpha} u^{\alpha} v_{\alpha} ,

where :math:`u` is contravariant, :math:`v` is covariant, the inner sum runs
over the NGWFs and :math:`w_{\mathbf{k}}` is the weight of k-point
:math:`\mathbf{k}`. Every such contraction pairs one covariant object with one
contravariant one, so both channels are carried through the optimisation. The
sum itself is symmetric, so the order in which the two are written below
carries no meaning; which channel each is drawn from does.

Throughout, :math:`\alpha` and :math:`\beta` label NGWFs and are summed over
when repeated. The conjugate-gradient coefficient :math:`\beta^{(k)}` in the
next section is a separate quantity, and always carries its iteration label.

Convergence
-----------

All three optimisers are tested against the same quantity, the root-mean-square
NGWF gradient

.. math::
   \mathrm{RMS} = \sqrt{\frac{\bigl| \langle g, g \rangle \bigr|}{N}} ,

where :math:`N` is the number of psinc coefficients. Because the ruler is
shared, :ref:`ngwf-threshold-orig` transfers unchanged between the optimisers
and their iteration counts may be compared directly.

.. note::
   The pairing :math:`\langle g, g \rangle` is not positive definite in ONETEP,
   because the kinetic-energy preconditioner is applied to the covariant channel
   only, so close to a stationary point it can change sign. Hence the absolute
   value. This affects all three optimisers, and is discussed under
   :ref:`the-metric-is-indefinite`.

Conjugate gradients
===================

The search direction combines the current gradient with the previous direction,

.. math::
   d^{(k)} = -g^{(k)} + \beta^{(k)} d^{(k-1)} ,

and the two variants differ only in the coefficient :math:`\beta`. A line search
along :math:`d^{(k)}` then chooses how far to go.

The coefficient
---------------

``NGWF_FLETCHER``, the default, uses the Fletcher-Reeves form,

.. math::
   \beta^{(k)} = \frac{\langle g^{(k)}, g^{(k)} \rangle}
                      {\langle g^{(k-1)}, g^{(k-1)} \rangle} .

``NGWF_POLAK`` uses the gradient difference :math:`y^{(k)} = g^{(k)} -
g^{(k-1)}` and the curvature along the previous direction,

.. math::
   \beta^{(k)} = \frac{\langle g^{(k)}, y^{(k)} \rangle}
                      {\langle d^{(k-1)}, y^{(k)} \rangle} .

Despite the keyword name this is the Hestenes-Stiefel form; Polak-Ribiere
divides by :math:`\langle g^{(k-1)}, g^{(k-1)} \rangle` instead. The two are the
same when the line search finds the exact minimum along the direction.

The denominator here is not guaranteed positive, so :math:`\beta` may come out
negative, which would carry the previous direction backwards. It is therefore
truncated at zero, restarting along steepest descent for that step, as is
standard practice [GilbertNocedal1992]_ [HagerZhang2005]_.

Either coefficient is set to zero if it exceeds two in magnitude, which restarts
the search along the steepest-descent direction and prints a warning. The
direction is also restarted after :ref:`elec-cg-max` consecutive steps, and
whenever a line search fails.

Neither coefficient is generally better than the other, and neither costs
anything extra, so if the outer loop is dominating your run time both are worth
trying.

The line search
---------------

Each iteration prices a trial step of length :math:`\tau_{\mathrm{t}}` along
:math:`d`, giving the energy there in addition to the energy and slope already
known at the starting point. Fitting a parabola to those three pieces of
information,

.. math::
   c = \frac{2 \left[ F(\tau_{\mathrm{t}}) - F(0)
       - \tau_{\mathrm{t}} \langle g, d \rangle \right]}
       {\tau_{\mathrm{t}}^{2}} ,
   \qquad
   \tau^{\ast} = - \frac{\langle g, d \rangle}{c} ,

gives the step actually taken, subject to :ref:`ngwf-cg-max-step`. Should the
parabola's minimiser point the wrong way along :math:`d`, a second trial is
priced at :math:`2\tau_{\mathrm{t}}` and a cubic is fitted through the three
energies instead. The output reports whichever was used as ``Selected quadratic
step`` or ``Selected cubic step``.

The trial length carries over between iterations rather than being fixed. A
successful search sets

.. math::
   \tau_{\mathrm{t}} \leftarrow
   \sqrt{\tau_{\mathrm{t}} \, \tau^{\ast}} ,

so the next trial is the geometric mean of the current trial and the step just
taken, while a failed search halves it. It is never allowed below
:math:`10^{-4}`.

Limited-memory BFGS
===================

Conjugate gradients rebuilds its picture of the energy surface from scratch at
every iteration. ``NGWF_LBFGS`` instead keeps the last :math:`m` steps and the
gradient change across each, and uses them to approximate the inverse Hessian
[Liu1989]_. That lets it take a scaled Newton-like step immediately. ONETEP uses
the same scheme for geometry optimisation, storing atomic positions and forces
in place of NGWF coefficients and gradients (see :doc:`Geometry_Relaxation`).

One thing makes this harder for NGWFs than for atomic positions. Moving the
NGWFs invalidates the density kernel, so the energy only becomes meaningful
again once the inner loop has re-solved for :math:`K^{\alpha\beta}`. An energy
evaluated at the rotated kernel is cheap, but it belongs to a different surface
from the one being minimised, and a step accepted or rejected on that basis is
being judged against a surface the calculation immediately leaves behind.

The optimiser therefore does not judge its step when it takes it. It commits,
and assesses the result one iteration later, using the energy the outer loop
produces in any case.

The search direction
--------------------

Given :math:`m` stored curvature pairs :math:`(s_i, y_i)`, where :math:`s_i` is
a committed step and :math:`y_i` the gradient difference across it, the
direction comes from two sweeps over that history. Start from the current
gradient, :math:`q = g`. The first sweep runs from the newest pair to the
oldest, recording a scalar :math:`a_i` at each and subtracting that multiple of
:math:`y_i`:

.. math::
   a_i = \frac{\langle s_i, q \rangle}{\langle s_i, y_i \rangle} ,
   \qquad
   q \leftarrow q - a_i \, y_i .

Between the sweeps :math:`q` is scaled by the curvature of the newest pair,
which sets the size of the initial inverse-Hessian estimate:

.. math::
   \gamma = \frac{\langle s_m, y_m \rangle}{\langle y_m, y_m \rangle} ,
   \qquad
   q \leftarrow \gamma \, q .

The second sweep runs back from the oldest pair to the newest, adding to
:math:`q` the amount by which the first sweep over-corrected:

.. math::
   b_i = \frac{\langle y_i, q \rangle}{\langle s_i, y_i \rangle} ,
   \qquad
   q \leftarrow q + (a_i - b_i) \, s_i .

The search direction is then :math:`d = -q`.

Both channels of :math:`q` are carried through the first sweep, and :math:`y_i`
is stored in both, so the raise is never applied twice inside the recursion. The
second sweep needs the covariant channel alone, its partner in every dot product
being the pair's stored contravariant :math:`y`.

The deferred Wolfe verdict
--------------------------

The step commits at :math:`\tau = \min(1, R)`, where :math:`R` is a step-length
memory, with no verdict taken at the time. One iteration later, once an honest
energy :math:`F` exists, the step just taken is judged against the two Wolfe
conditions [NocedalWright]_

.. math::
   F^{(k)} - F^{(k-1)} \; \le \; w_1 \, \tau \,
   \langle g^{(k-1)}, d \rangle ,

.. math::
   \bigl| \langle g^{(k)}, d \rangle \bigr| \; \le \; w_2 \,
   \bigl| \langle g^{(k-1)}, d \rangle \bigr| ,

with :math:`w_1 = 0.01` and :math:`w_2 = 0.5`. The sufficient-decrease condition
alone decides acceptance; the curvature condition only doubles the rate at which
:math:`R` recovers towards unity.

A step failing sufficient decrease is rejected. The pre-step NGWFs, kernel and
Hamiltonian are restored in full, and the same direction is retaken at the
minimiser of the parabola through the start energy, the slope and the rejected
point,

.. math::
   \tau^{\ast} = \frac{- \tau^2 \langle g^{(k-1)}, d \rangle}
   {2 \left[ \Delta F - \tau \langle g^{(k-1)}, d \rangle \right]} ,
   \qquad \Delta F = F^{(k)} - F^{(k-1)} ,

clipped to :math:`[0.1\tau, 0.5\tau]`. The retry consumes an iteration and is
itself judged next time round.

Model quality is reported for each judged step as the ratio of the reduction
actually won to the one predicted by the quadratic model whose minimiser is the
full step,

.. math::
   \Delta F_{\mathrm{model}} = \langle g^{(k-1)}, d \rangle
   \left( \tau - \tfrac{1}{2}\tau^2 \right), \qquad
   \rho = \frac{\Delta F}{\Delta F_{\mathrm{model}}} ,

so :math:`\rho` reads as it would in a trust region, even though the verdict
arrives an iteration late.

Steepest-descent fallback
-------------------------

With no history yet, or after a direction that turned out to point uphill, the
step falls back to a scaled steepest descent sized by a shrinking probe loop. A
probe is taken at :math:`\tau = \min(1, R)` and shrunk by a factor of four
until the energy falls or the rise lies inside the noise floor, for at most six
trials. The parabola through the reference energy, the slope and the probe,

.. math::
   c = \frac{2 \left[ F(\tau) - F_{\mathrm{ref}}
   - \tau \langle g, d \rangle \right]}{\tau^2} , \qquad
   \tau^{\ast} = - \frac{\langle g, d \rangle}{c} ,

then sets the committed length, and :math:`R` answers the resulting model
quality: grown by a factor of two above :math:`\rho = 0.75`, shrunk by a factor
of four below :math:`\rho = 0.25`, and held within :math:`[10^{-3}, 4]`. Unlike
the quasi-Newton path, this fallback prices its own trials: along a
steepest-descent direction the cheap energy is enough to size a step it is not
asked to validate.

Curvature-pair hygiene
----------------------

Two mechanisms keep the stored history trustworthy.

**Admission.** A pair enters the history on a scale-free cosine floor rather
than on a bare sign test,

.. math::
   \langle s_i, y_i \rangle > \varepsilon \,
   \lVert s_i \rVert \, \lVert y_i \rVert ,
   \qquad \varepsilon = 10^{-8} ,

where the two norms are each taken within a single channel, covariant for
:math:`s_i` and contravariant for :math:`y_i`, rather than across the two. This
rejects the numerically meaningless pairs that a test on the sign of
:math:`\langle s_i, y_i \rangle` alone would admit.

**Retirement.** The secant condition a pair encodes is only local on the scale
of the step that measured it. Each pair therefore accumulates the motion
committed since it was formed, and retires once that drift exceeds a multiple of
its own length,

.. math::
   \mathrm{drift}_i > C \, \lVert s_i \rVert , \qquad C = 41 ,

where :math:`\lVert s_i \rVert` is again the covariant norm of the step that
formed the pair.

Retirement is what makes a deep history safe. Without it an old pair describes
curvature at a point the calculation has long since left.

Noise awareness
---------------

Energy differences below

.. math::
   \delta = 3 \times 10^{2} \, \epsilon_{\mathrm{mach}}
   \max \left( \lvert F \rvert, 1 \right)

carry no information. A step whose change falls below :math:`\delta` is recorded
as *neutral*: it is accepted, but its curvature pair is discarded, since a
:math:`y` made of noise would send :math:`\gamma` to infinity. Neither the
step-length memory nor the model quality responds to a sub-noise change.

Termination
-----------

``NGWF_LBFGS`` never aborts. Every iteration it banks the lowest-energy NGWFs it
has seen, and if the run ends unconverged it restores them, since the energy is
the only reliable way to rank two states. Instead of stopping on an error it
declares a numerical floor when any of the following holds:

-  neither a new RMS low nor a new energy best for 20 iterations;
-  three consecutive rejected steps;
-  three consecutive sub-noise steps;
-  two consecutive step-floor resets.

.. _the-metric-is-indefinite:

The metric is indefinite
========================

Because the kinetic-energy preconditioner is applied to the covariant channel
only, the pairing :math:`\langle \cdot, \cdot \rangle` is not an inner product,
and :math:`\langle g, g \rangle` can become negative near a stationary point.
The consequences differ by optimiser:

-  For conjugate gradients the coefficient can go out of range, which the
   :math:`\lvert \beta \rvert > 2` guard and the periodic restart absorb.

-  For L-BFGS the two-loop direction can point uphill even though every stored
   pair satisfies :math:`\langle s_i, y_i \rangle > 0`. A scaled
   steepest-descent step covers that case, and three consecutive non-descent
   directions clear the stored history.

In practice this appears only in the closing iterations of a tightly converged
run. The signed value of :math:`\langle g, g \rangle` may be inspected with
``devel_code : NGWF_SIGNDIAG``.

Interaction with fast density
=============================

Under :ref:`fast-density` the trimming threshold is by default *adaptive*: it is
retuned each iteration from the current RMS gradient and never allowed to rise
again. Conjugate gradients is indifferent to this, because every energy it
compares is priced within a single iteration. The deferred verdict is not, since
it compares energies from consecutive iterations and forms a curvature pair from
the two: with a threshold that moves in between, the pair records the change in
accuracy surface as though it were curvature.

Selecting ``NGWF_LBFGS`` together with ``fast_density`` therefore defaults
:ref:`trimmed-boxes-threshold` to a fixed :math:`10^{-7}` rather than to the
adaptive ladder. Setting the keyword explicitly overrides this in either
direction, and a negative value restores adaptive behaviour.

.. caution::
   :math:`10^{-6}`, the value recommended for manual use at the default RMS
   target, is too loose at tighter targets. At
   ``ngwf_threshold_orig : 5E-7`` it costs a lithium cluster four extra
   iterations and leaves a platinum cluster unconverged.

Deterministic FFT planning
==========================

FFTW's ``MEASURE`` planner selects a transform plan by timing candidates at
runtime, so two runs of the same input on the same machine may take different
plans and diverge in the final digits. Conjugate gradients absorbs this; a
curvature memory does not, and the divergence can cost iterations. Planning
therefore switches to ``FFTW_ESTIMATE`` when, and only when, ``NGWF_LBFGS`` is
selected. Every other value of :ref:`ngwf-cg-type` retains ``MEASURE``
unchanged. The cost of the less aggressive planner has not been measurable on
the systems tested.

Keywords
========

``ngwf_cg_type``
   String, default ``NGWF_FLETCHER``. Chooses the outer-loop optimiser: one of
   ``NGWF_FLETCHER``, ``NGWF_POLAK`` or ``NGWF_LBFGS``. An unrecognised value
   stops the calculation.

``ngwf_lbfgs_history``
   Integer, default ``12``. How many curvature pairs ``NGWF_LBFGS`` stores.
   Drift retirement is what keeps a deep history trustworthy, so there is
   normally no reason to change this. Must be positive.

``devel_code : LBFGS_DIAG``
   Prints a diagnostic block for every L-BFGS step. Print-only; it never
   influences the step taken.

``devel_code : NGWF_SIGNDIAG``
   Prints the signed value of :math:`\langle g, g \rangle` at each inner
   iteration.

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
first, since that is the order in which the iteration performs them, followed by
the step actually taken:

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
steepest-descent fallback. ``Outcome`` is ``ACCEPTED``, ``REJECTED`` or
``NEUTRAL``, the last meaning the change fell below the noise floor. Events
raised during a step, such as a retired pair or a history reset, are printed
immediately above the block.

The diagnostic block
--------------------

With ``devel_code : LBFGS_DIAG`` each step additionally prints:

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

The fields most worth reading are ``signed <g,g>``, which shows whether the
metric is still positive; ``pair cosine``, the quantity tested on admission;
``stack drift max``, how close the oldest pair is to retirement; and the trial
table, which gives the true cost of the step in energy evaluations. ``step
verdict`` reads ``DEFERRED`` because the verdict for this step is delivered in
the next iteration's report.

Choosing an optimiser
=====================

-  ``NGWF_FLETCHER`` is the default, and the right starting point.

-  ``NGWF_LBFGS`` is worth trying where the outer loop is the bottleneck, and
   particularly on metallic systems, where a long tail of conjugate-gradient
   iterations is common. It stores one additional set of NGWF-sized arrays per
   curvature pair, so its memory footprint grows with ``ngwf_lbfgs_history``.

-  Repeat runs under ``NGWF_LBFGS`` are reproducible to the last digit, which
   the conjugate-gradient variants do not guarantee.

-  Between the two conjugate-gradient coefficients there is no general winner,
   and neither carries an extra cost worth weighing.

References
==========

.. [GilbertNocedal1992] Jean Charles Gilbert, Jorge Nocedal, "Global convergence
   properties of conjugate gradient methods for optimization", *SIAM J. Optim.*
   **1992**, 2, 21, https://doi.org/10.1137/0802003

.. [HagerZhang2005] William W. Hager, Hongchao Zhang, "A new conjugate gradient
   method with guaranteed descent and an efficient line search", *SIAM J.
   Optim.* **2005**, 16, 170, https://doi.org/10.1137/030601880
