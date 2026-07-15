===================================================
Meta-GGA functionals and pseudopotentials in ONETEP
===================================================

:Author: Joseph C. A. Prentice (with some functionality by James C. Womack
:Date:   July 2026


Since v 4.5.3.63, ONETEP has had the option to use a meta-GGA (mGGA)
exchange-correlation functional. mGGAs are the third rung of Jacob's
ladder of XC functionals, and are usually dependent on the density,
the gradient of the density, and the kinetic energy density (the
second derivative of the Kohn-Sham orbitals). The intention is that
such functionals will give greater accuracy than GGAs, for a very
modest increase in cost.

ONETEP's implementation makes use of the functional derivative of
orbitals (FDO) approach, which allows linear-scaling behaviour to be
maintained. [Womack2016]_

Available functionals and embedding
===================================

Before v 8.1.23, three mGGAs were available: the local-tau
approximation (LTA) [Ernzerhof1999]_, B97M-V [Mardirossian2015]_, and
PKZB [Perdew1999]_.

From v 8.1.23, the MS2 [Sun2013]_ and rSCAN [Bartok2019]_ mGGAs are
also available. The SCAN family of functionals [Sun2015]_ (of which
rSCAN is a member) have been shown to be particularly powerful for
improving a variety of different properties.

From v 8.1.23, mGGAs have also become compatible with EMFT.

Pseudopotentials
================

To get the full benefit of mGGAs, it is necessary to use mGGA-specific
pseudopotentials. These pseudopotentials contain not only the standard
core density and local potential, but also the core *kinetic energy
density* (:math:`\tau`) and local :math:`\tau`-dependent potential
:math:`V_\tau` (the functional derivative of the energy with respect
to :math:`\tau`). Using LDA or GGA pseudopotentials is perfectly
possible, but they will miss these important corrections to the KE
density and functional derivative of the energy with respect to the KE
density, and will give worse results. [Bartok2019-2]_

From v 8.1.23, ONETEP has the functionality to deal with these
mGGA-specific pseudopotentials and the new quantities they introduce,
for pseudopotentials in the `.usp` format. Unfortunately, there is not
currently an agreed format for these new quantities to be provided
in. In the absence of an agreed format, ONETEP reads in these
quantities from a separate file: if the `.usp` file is called
`pspot_name.usp`, this additional file should be called
`pspot_name_ke_dens.dat`. The core KE density and :math:`V_\tau` are
provided in exactly the same format as the core density and
:math:`V_{loc}` in the `.usp` file.

KE density initialisation
=========================

At the beginning of a mGGA calculation, we need to initialise the KE
density from the initial density. Assuming your calculation is
well-converged, how you do this should make no difference to your
final result, but might affect how long it takes to achieve
convergence.

The options for initialisation are:

1. Initialise to zero (`GGA`)
2. The uniform electron gas expression :math:`\tau = \frac{3}{10} (3\pi^2)^{\frac{2}{3}} \rho^{\frac{5}{3}}` (`UNIFORM`) [Sun2015]_
3. The von Weizsacker expression :math:`\tau = \frac{1}{8} \frac{|\nabla \rho|^2}{\rho}` (`WEIZSACKER`) [Acharya1980]_

The default is initialising to zero, although the uniform electron gas
expression has also been found to work well.

Keywords
========

- ``xc_functional`` [basic, string]: There are five mGGA options here:
   ``LTA``, ``PKZB``, ``B97M-V``, ``MS2``, and ``RSCAN``.

- ``active_xc_functional`` [basic, string]: See EMFT documentation for
   explanation of this keyword. It can take the same mGGA options as
   ``xc_functional``.

- ``use_core_ke_density`` [basic, logical, default = ``F``]: Toggles
   whether ONETEP will try to read the core KE density and
   :math:`V_\tau` from a file, as described above

- ``ke_density_init`` [advanced, logical, default = ``GGA``]: Decides
   how KE density is initialised. Options are ``GGA``, ``UNIFORM``,
   and ``WEIZSACKER``.



[Ernzerhof1999] M. Ernzerhof and G. E. Scuseria, J. Chem. Phys. **111**, 911 (1999).
   
[Mardirossian2015] N. Mardirossian and M. Head-Gordon, J. Chem. Phys. **142**, 074111 (2015).
   
[Perdew1999] J. P. Perdew, S. Kurth, A. Zupan, and P. Blaha, Phys. Rev. Lett. **82**, 2544 (1999).

[Sun2013] J. Sun, R. Haunschild, B. Xiao, I. W. Bulik, G. E. Scuseria, and J. P. Perdew, J. Chem. Phys. **138**, 044113 (2013)

[Bartok2019] A. P. Bartok and J. R. Yates, J. Chem. Phys. **150**, 161101 (2019).

[Sun2015] J. Sun, A. Ruzsinszky, and J. P. Perdew, Phys. Rev. Lett. **115**, 036402 (2015).

[Bartok2019-2] A. P. Bartok and J. R. Yates, Phys. Rev. B **99**, 235105 (2019).

[Acharya1980] P. K. Acharya, L. J. Bartolotti, S. B. Sears, and R. G. Parr, PNAS **77** 6978 (1980). 
