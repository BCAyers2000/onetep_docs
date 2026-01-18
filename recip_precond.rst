========================================
Kinetic energy preconditioning in ONETEP
========================================

:Author: Chengcheng Xiao
:Date:   Dec 2025

ONETEP at the moment, by default uses a modified Teter reciprocal
preconditioning.

`The original Teter reciprocal preconditioning function <https://doi.org/10.1103/PhysRevB.40.12255>`__
is defined as:

.. math::
   P_{\mathbf{G}, \mathbf{G}^{\prime}}=\delta_{\mathbf{G}, \mathbf{G}^{\prime}} \frac{27+18 x+12 x^2+8 x^3}{27+18 x+12 x^2+8 x^3+16 x^4}

where

.. math::
   x=\frac{\left(\hbar^2|\mathbf{k}+\mathbf{G}|^2\right) / 2 m}{T_i}

and :math:`T_i=\left < \psi_i\left|\frac{-\hbar^2}{2 m} \nabla^2\right| \psi_i \right>`
which is related to the band :math:`i` that :math:`P` is applied to.

In ONETEP, by default we want to avoid calculating the kinetic energy
eigenvalues, :math:`x` is modified to be:

.. math::
   x=\frac{\frac{1}{2}|\mathbf{G}|^2}{\frac{1}{2}k_0^2}

and :math:`k_0` is a manually specified number.

Automatic selection of :math:`k_0`
==================================

Since ONETEP version 8, it is possible to perform calculations where :math:`k_0`
is calculated automatically based on the kinetic energy at each NGWF
optimisation step. I.e.,

.. math::
   k_0 = \sqrt{\mathrm{Max[Eig[KT]]}}

where :math:`K` is the density kernel and :math:`\mathrm{Max[Eig(KT)]}` gives
the max eigenvalue of the (occupation weighted) kinetic energy matrix in the
NGWF basis.

Note that in the case of multi-kpoint/spin-polarised calculation, k-point/spin
average is performed and a single :math:`k_0` is obtained for the whole system.

It is also possible to perfrom NGWF-specific preconditioning. In this case, each
NGWF will have its own :math:`k_0`. For example, if we use the kinetic energy
matrix weighted by the occupation numbers :math:`KT`, then for the :math:`i`-th
NGWF, we have

.. math::
   k_0^{i} = \sqrt{(KT)_{i}^i}

There are three options for the matrix to use for NGWF-specific preconditioning:

   1. The diagonal elements of :math:`KT`: Occupation weighted kinetic energy.
   2. The diagonal elements of :math:`S^{-1}T`: Tensor corrected kinetic energy.
   3. The diagonal elements of :math:`T`: Bare kinetic energy.

Testing is needed to determine which option is the best for specific systems.
Note that kinetic energy preconditioning can affect the total energy so one
should always check and make sure the convergence of total energy difference
(e.g. bettwen a pristine system and a distorted system) is correct.

Keywords
========

-  ``precond_recip`` [Basic, bool, default ``T``\ ] Turn on reciprocal space
   kinetic energy preconditioning? [Incompatible with ``precond_real``]

-  ``precond_real`` [Basic, bool, default ``F``\ ] Turn on real space
   kinetic energy preconditioning? [Incompatible with ``precond_recip`` and 
   automatic :math:`k_0` mode.]

-  ``precond_scheme`` [Basic, string, default ``TETER``\ ] The type of kinetic
   energy preconditioning scheme to use. Options are: `BG`, `MAURI`, `TETER` or
   `NONE`.

-  ``k_zero`` [Basic, physical 1/Bohr, default ``3.0``\ ] The :math:`k_0` value
   used in the kinetic energy preconditioning. If set to a negative value,
   ONETEP will automatically calculate the :math:`k_0` value based on the average
   kinetic energy of the system.

-  ``precond_array`` [Basic, bool, default ``F``\ ] Turn on NGWF-specific
   preconditioning where each NGWF has its own :math:`k_0` value based on its own kinetic
   energy expectation value? (requires ``k_zero`` to be negative).

-  ``precond_array_type`` [Basic, string, default ``KT``\ ] The type of kinetic
   energy to use for NGWF-specific preconditioning. Options are: ``KT``, ``INVST``,
   and ``T``. (requires ``precond_array`` to be ``T``).

- ``threads_precond`` [Basic, int, default same as ``threads_num_fftboxes``] How many threads to use for batch preconditioning.
  When ``precond_array=T``, the bigger ``threads_precond`` the more memory is required.
