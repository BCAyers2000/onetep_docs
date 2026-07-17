ONETEP Keyword List
===================

:Author: ONETEP Documentation Team
:Date: 2026-07-17

.. only:: html

   Use links marked "🔍︎" to search occurances of a keyword in all documentation pages.

.. _active-ke-density-gauge:

ACTIVE_KE_DENSITY_GAUGE
-----------------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`ACTIVE_KE_DENSITY_GAUGE`

Multiple of Laplacian of active region density to add to active region KE density in EMFT

.. _active-region:

ACTIVE_REGION
-------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`ACTIVE_REGION`

Defines which region is the active region used for the higher level calculation within an embedding mean field theory calculation

.. _active-xc-functional:

ACTIVE_XC_FUNCTIONAL
--------------------

:Type: String
:Default: Unknown
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`ACTIVE_XC_FUNCTIONAL`

Defines the xc functional used for the higher level calculation within an embedding mean field theory calculation

.. _anharmonic-calculate:

ANHARMONIC_CALCULATE
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`ANHARMONIC_CALCULATE`

Active the calculation of the IR spectrum

.. _anh-acf-factor:

ANH_ACF_FACTOR
--------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`ANH_ACF_FACTOR`

Prefactor for the autocorrelation function

.. _anh-apply-filter:

ANH_APPLY_FILTER
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`ANH_APPLY_FILTER`

Apply the gaussian filter

.. _anh-first-iter:

ANH_FIRST_ITER
--------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`ANH_FIRST_ITER`

First md iteration to include in the autocorrelation

.. _anh-last-iter:

ANH_LAST_ITER
-------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`ANH_LAST_ITER`

Last md iteration to include in the autocorrelation

.. _anh-md-temp:

ANH_MD_TEMP
-----------

:Type: Physical
:Default: 0.0
:Unit: kelvin
:Level: Basic
:Group: None
:Search: :searchlink:`ANH_MD_TEMP`

Temperature in the md simulation

.. _anh-plot-all:

ANH_PLOT_ALL
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`ANH_PLOT_ALL`

Plot the whole IR spectrum

.. _anh-plot-firstfreq:

ANH_PLOT_FIRSTFREQ
------------------

:Type: Physical
:Default: 0.0
:Unit: 1/cm
:Level: Basic
:Group: None
:Search: :searchlink:`ANH_PLOT_FIRSTFREQ`

First freq to be shown in the IR table

.. _anh-plot-lastfreq:

ANH_PLOT_LASTFREQ
-----------------

:Type: Physical
:Default: 0.0
:Unit: 1/cm
:Level: Basic
:Group: None
:Search: :searchlink:`ANH_PLOT_LASTFREQ`

Last freq to be shown in the IR table

.. _anh-qc-factor:

ANH_QC_FACTOR
-------------

:Type: String
:Default: 'HARMONIC'
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`ANH_QC_FACTOR`

Quantum correction factor in IR spectrum

.. _anh-type:

ANH_TYPE
--------

:Type: String
:Default: 'IR_CALCULATION'
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`ANH_TYPE`

Describe the type of calculation to perform

.. _augbox-pref:

AUGBOX_PREF
-----------

:Type: String
:Default: '0 0 0'
:Unit: None
:Level: Intermediate
:Group: GENERAL
:Search: :searchlink:`AUGBOX_PREF`

Preferred Augmentation box dimensions

.. _aug-funcs-recip:

AUG_FUNCS_RECIP
---------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`AUG_FUNCS_RECIP`

Construct Augmentation functions in recip space (T) or real (F)

.. _block-orthogonalise:

BLOCK_ORTHOGONALISE
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: IO
:Search: :searchlink:`BLOCK_ORTHOGONALISE`

Orthogonalise environment NGWFs wrt active subsystem

.. _bsunfld-calculate:

BSUNFLD_CALCULATE
-----------------

:Type: Boolean
:Default: None
:Unit: None
:Level: Intermediate
:Group: BS_UNFOLDING
:Search: :searchlink:`BSUNFLD_CALCULATE`

Logical flag for bandstructure unfolding calculation

.. _bsunfld-kpoint-path:

BSUNFLD_KPOINT_PATH
-------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: BS_UNFOLDING
:Search: :searchlink:`BSUNFLD_KPOINT_PATH`

Primitive-cell k-point path for bandstructure unfolding calculation

K-point path for bandstructure unfolding calculation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK BSUNFLD_KPOINT_PATH
      k1x k1y k1z
      k2x k2y k2z
       .   .   .
      kNx kNy kNz
      %ENDBLOCK BSUNFLD_KPOINT_PATH

   :Example:

   .. code::

      %BLOCK BSUNFLD_KPOINT_PATH
      0.0 0.0 0.0
      0.0 0.0 0.5
      %ENDBLOCK BSUNFLD_KPOINT_PATH

.. _bsunfld-num-atoms-prim:

BSUNFLD_NUM_ATOMS_PRIM
----------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: BS_UNFOLDING
:Search: :searchlink:`BSUNFLD_NUM_ATOMS_PRIM`

Number of atoms in implicit primitive-cell

.. _bsunfld-num-eigenvalues:

BSUNFLD_NUM_EIGENVALUES
-----------------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Intermediate
:Group: BS_UNFOLDING
:Search: :searchlink:`BSUNFLD_NUM_EIGENVALUES`

Enforce provided number of kpts per path

.. _bsunfld-num-kpts-path:

BSUNFLD_NUM_KPTS_PATH
---------------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Intermediate
:Group: BS_UNFOLDING
:Search: :searchlink:`BSUNFLD_NUM_KPTS_PATH`

Number of primitive-cell kpts sampled along each path

.. _bsunfld-restart:

BSUNFLD_RESTART
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: BS_UNFOLDING
:Search: :searchlink:`BSUNFLD_RESTART`

Restart a bs-unfolding calculation

.. _bsunfld-transformation:

BSUNFLD_TRANSFORMATION
----------------------

:Type: String
:Default: '1 0 0 0 1 0 0 0 1'
:Unit: None
:Level: Intermediate
:Group: BS_UNFOLDING
:Search: :searchlink:`BSUNFLD_TRANSFORMATION`

Transformation matrix (flattened) between primitive-cell and supercell lattice vectors

Transformation matrix (flattened) between primitive-cell and supercell lattice vectors when unfolding bandstructure

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK BSUNFLD_TRANSFORMATION
      S11 S12 S12
      S21 S22 S23
      S31 S32 S33
      %ENDBLOCK BSUNFLD_TRANSFORMATION

   :Example:

   .. code::

      %BLOCK BSUNFLD_TRANSFORMATION
      5 0 0
      0 5 0
      0 0 5
      %ENDBLOCK BSUNFLD_TRANSFORMATION

.. _bs-kpoint-path:

BS_KPOINT_PATH
--------------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`BS_KPOINT_PATH`

K-point path for bandstructure calculation

K-point path for bandstructure calculation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK BS_KPOINT_PATH
      k1x k1y k1z
      k2x k2y k2z
       .   .   .
      kNx kNy kNz
      %ENDBLOCK BS_KPOINT_PATH

   :Example:

   .. code::

      %BLOCK BS_KPOINT_PATH
      0.0 0.0 0.0
      0.0 0.0 0.5
      %ENDBLOCK BS_KPOINT_PATH

.. _bs-kpoint-path-spacing:

BS_KPOINT_PATH_SPACING
----------------------

:Type: Physical
:Default: 0.1889727
:Unit: 1/bohr
:Level: Intermediate
:Group: None
:Search: :searchlink:`BS_KPOINT_PATH_SPACING`

K-point spacing along bandstructure path

K-point spacing along the bandstructure path.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      BS_KPOINT_PATH_SPACING [Physical]

   :Example:

   .. code::

      BS_KPOINT_PATH_SPACING 0.004 "1/bohr"

.. _bs-method:

BS_METHOD
---------

:Type: String
:Default: 'TB'
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`BS_METHOD`

Method to use: 'PW' or 'TB'

The method to use for the calculation of band structures - either the tight-binding style method or the k.p perturbation theory style method.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      BS_METHOD [Integer]

   :Example:

   .. code::

      BS_METHOD kp

.. _bs-num-eigenvalues:

BS_NUM_EIGENVALUES
------------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`BS_NUM_EIGENVALUES`

Num of energy and occ. eigenvalues to print below and above the Fermi level from a bs calc

Number of energy and occupancy eigenvalues to print below and above the Fermi level from a bandstructure calculation. If left as default all eigenvalues (2 x number of occupied states) will be printed.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      BS_NUM_EIGENVALUES [Integer]

   :Example:

   .. code::

      BS_NUM_EIGENVALUES 10

.. _bs-perturbative-soc:

BS_PERTURBATIVE_SOC
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: BS
:Search: :searchlink:`BS_PERTURBATIVE_SOC`

Add perturbative spin-orbit couplings to the bandstructure calculation.

.. _bs-unfold:

BS_UNFOLD
---------

:Type: String
:Default: '0 0 0'
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`BS_UNFOLD`

Number of times to unfold Brillouin zone in each lattice direction

.. _cache-limit-for-dknblks:

CACHE_LIMIT_FOR_DKNBLKS
-----------------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Expert
:Group: HFX
:Search: :searchlink:`CACHE_LIMIT_FOR_DKNBLKS`

Max cache size for remote DKN blocks (in MiB)

.. _cache-limit-for-expansions:

CACHE_LIMIT_FOR_EXPANSIONS
--------------------------

:Type: Integer
:Default: 1024
:Unit: None
:Level: Expert
:Group: HFX
:Search: :searchlink:`CACHE_LIMIT_FOR_EXPANSIONS`

Max cache size for expanded potentials (in MiB)

.. _cache-limit-for-prods:

CACHE_LIMIT_FOR_PRODS
---------------------

:Type: Integer
:Default: 1024
:Unit: None
:Level: Expert
:Group: HFX
:Search: :searchlink:`CACHE_LIMIT_FOR_PRODS`

Max cache size for Aa-Dd NGWF products (in MiB) in HFx

.. _cache-limit-for-swops:

CACHE_LIMIT_FOR_SWOPS
---------------------

:Type: Integer
:Default: 1024
:Unit: None
:Level: Expert
:Group: SWX
:Search: :searchlink:`CACHE_LIMIT_FOR_SWOPS`

Max cache size for SWs or SWpots in PPDs (in MiB)

.. _cache-limit-for-swops2:

CACHE_LIMIT_FOR_SWOPS2
----------------------

:Type: Integer
:Default: 1024
:Unit: None
:Level: Expert
:Group: SWX
:Search: :searchlink:`CACHE_LIMIT_FOR_SWOPS2`

Max cache size for SWs or SWpots at points (in MiB)

.. _cdft-atom-charge:

CDFT_ATOM_CHARGE
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_ATOM_CHARGE`

Perform an ATOM-CHARGE-constrained CDFT simulation

Activate atom charge-constrained-DFT mode. This mode is incompatible with any other cDFT-mode.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_ATOM_CHARGE [Logical]

   :Example:

   .. code::

      CDFT_ATOM_CHARGE T

.. _cdft-atom-spin:

CDFT_ATOM_SPIN
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_ATOM_SPIN`

Perform an ATOM-SPIN-constrained CDFT simulation

Activate atom magnetic-moment-constrained-DFT mode. This mode is incompatible with any other cDFT-mode.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_ATOM_SPIN [Logical]

   :Example:

   .. code::

      CDFT_ATOM_SPIN T

.. _cdft-cg-max:

CDFT_CG_MAX
-----------

:Type: Integer
:Default: 5
:Unit: None
:Level: Expert
:Group: CDFT
:Search: :searchlink:`CDFT_CG_MAX`

Number of U-opt iterations to reset CG

Specifies the maximum number of constraining potential (Uq/s) conjugate gradient iterations between resets.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_CG_MAX [Real]

   :Example:

   .. code::

      CDFT_CG_MAX 1

.. _cdft-cg-max-step:

CDFT_CG_MAX_STEP
----------------

:Type: Double-Precision
:Default: 50.0
:Unit: None
:Level: Expert
:Group: CDFT
:Search: :searchlink:`CDFT_CG_MAX_STEP`

Maximum length of trial step for cDFT optimisation line search

Maximum length of trial step for the constraining potential (Uq/s) optimisation line search.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_CG_MAX_STEP [Real]

   :Example:

   .. code::

      CDFT_CG_MAX_STEP 10.0

.. _cdft-cg-threshold:

CDFT_CG_THRESHOLD
-----------------

:Type: Double-Precision
:Default: 0.001
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_CG_THRESHOLD`

RMS gradient convergence threshold for U-pot. in CDFT

Specifies the convergence threshold for the RMS gradient of the constraining potentials (Uq/s).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_CG_THRESHOLD [Real]

   :Example:

   .. code::

      CDFT_CG_THRESHOLD 0.01

.. _cdft-cg-type:

CDFT_CG_TYPE
------------

:Type: String
:Default: 'NGWF_FLETCHER'
:Unit: None
:Level: Expert
:Group: CDFT
:Search: :searchlink:`CDFT_CG_TYPE`

Type of CG coefficient for CDFT U-optimisation  NGWF_POLAK = Polak-Ribbiere formula;  NGWF_FLETCHER = Fletcher-Reeves formula.

Specifies the variant of the conjugate gradients algorithm used for the optimization of the constraining potentials (Uq/s), currently either NGWF_FLETCHER for Fletcher-Reeves or NGWF_POLAK for Polak-Ribiere.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_CG_TYPE [Text]

   :Example:

   .. code::

      CDFT_CG_TYPE NGWF_POLAK

.. _cdft-charge-acceptor-target:

CDFT_CHARGE_ACCEPTOR_TARGET
---------------------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_CHARGE_ACCEPTOR_TARGET`

Targeted group-CHARGE for GROUP-CHARGE-ACCEPTOR-constrained cDFT

Targeted acceptor-group electron population for acceptor-group charge-constrained-DFT mode [ :ref:`cdft-group-charge-acceptor` = T].

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_CHARGE_ACCEPTOR_TARGET [Real]

   :Example:

   .. code::

      ; Constrain Nup+Ndown=17 e in subspace.

.. _cdft-charge-donor-target:

CDFT_CHARGE_DONOR_TARGET
------------------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_CHARGE_DONOR_TARGET`

Targeted group-CHARGE for GROUP-CHARGE-DONOR-constrained cDFT

Targeted donor-group electron population for donor-group charge-constrained-DFT mode [ :ref:`cdft-group-charge-donor` = T]

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_CHARGE_DONOR_TARGET [Real]

   :Example:

   .. code::

      ; Constrain Nup+Ndown=17 e in subspace.

.. _cdft-continuation:

CDFT_CONTINUATION
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_CONTINUATION`

Logical to restart (from the *.cdft file) a cDFT U-optimisation

Continue a constraining potential (Uq/s) optimisation from a previous run using the .cdft file with the latest cDFT-potentials. :ref:`cdft-continuation` = T allows also to perform single-point cDFT runs ( :ref:`maxit-cdft-u-cg` = 0) reading atom-specific constraining potentials from .cdft file (instead of species-specific ones from the :ref:`constrained-dft` block). For :ref:`cdft-continuation` = T, the constraining potentials (Uq/s) are read from the .cdft file no matter the setting of :ref:`cdft-guru` .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_CONTINUATION [Logical]

   :Example:

   .. code::

      CDFT_CONTINUATION T

.. _cdft-elec-energy-tol:

CDFT_ELEC_ENERGY_TOL
--------------------

:Type: Physical
:Default: -0.0001
:Unit: hartree
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_ELEC_ENERGY_TOL`

Tolerance on total energy change during CDFT optimisation

Tolerance on energy change per atom during CDFT optimisation. If negative, the option is deactivated.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_ELEC_ENERGY_TOL [Value] [Unit]

   :Example:

   .. code::

      CDFT_ELEC_ENERGY_TOL 0.01 hartree

.. _cdft-group-charge-acceptor:

CDFT_GROUP_CHARGE_ACCEPTOR
--------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_GROUP_CHARGE_ACCEPTOR`

Perform an ACCEPTOR GROUP-CHARGE-constrained CDFT simulation

Activate acceptor-group charge-constrained-DFT mode. This mode is compatible with :ref:`cdft-group-charge-donor` and :ref:`cdft-group-spin-acceptor` / :ref:`cdft-group-spin-donor` cDFT-modes, and incompatible with :ref:`cdft-atom-charge` / :ref:`cdft-atom-spin` and :ref:`cdft-group-charge-diff` / :ref:`cdft-group-spin-diff` modes.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_GROUP_CHARGE_ACCEPTOR [Logical]

   :Example:

   .. code::

      CDFT_GROUP_CHARGE_ACCEPTOR T

.. _cdft-group-charge-diff:

CDFT_GROUP_CHARGE_DIFF
----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_GROUP_CHARGE_DIFF`

Perform a GROUP-CHARGE-DIFFERENCE-constrained CDFT simulation

Activate group charge-difference constrained-DFT mode. This mode is compatible with :ref:`cdft-group-spin-diff` cDFT mode only. Thus, it is incompatible with any other CDFT_ATOM_CHARGE/SPIN and CDFT_GROUP_CHARGE/SPIN_ACCEPTOR/DONOR cDFT modes.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_GROUP_CHARGE_DIFF [Logical]

   :Example:

   .. code::

      CDFT_GROUP_CHARGE_DIFF T

.. _cdft-group-charge-diff-target:

CDFT_GROUP_CHARGE_DIFF_TARGET
-----------------------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_GROUP_CHARGE_DIFF_TARGET`

Targeted :ref:`charge` difference (acceptor-donor) for  GROUP-CHARGE-DIFFERENCE-constrained cDFT

Targeted electron population difference between acceptor and donor group for group-charge-difference constrained-DFT mode [ :ref:`cdft-group-charge-diff` =T].

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_GROUP_CHARGE_DIFF_TARGET [Real]

   :Example:

   .. code::

      CDFT_GROUP_CHARGE_DIFF_TARGET 2

.. _cdft-group-charge-donor:

CDFT_GROUP_CHARGE_DONOR
-----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_GROUP_CHARGE_DONOR`

Perform a DONOR GROUP-CHARGE-constrained CDFT simulation

Activate donor-group charge-constrained-DFT mode. This mode is compatible with :ref:`cdft-group-charge-acceptor` and :ref:`cdft-group-spin-acceptor` / :ref:`cdft-group-spin-donor` cDFT-modes, and incompatible with :ref:`cdft-atom-charge` / :ref:`cdft-atom-spin` and :ref:`cdft-group-charge-diff` / :ref:`cdft-group-spin-diff` modes.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_GROUP_CHARGE_DONOR [Logical]

   :Example:

   .. code::

      CDFT_GROUP_CHARGE_DONOR T

.. _cdft-group-charge-down-only:

CDFT_GROUP_CHARGE_DOWN_ONLY
---------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_GROUP_CHARGE_DOWN_ONLY`

Logical to constrain only UP electrons

Constrain only SPIN-DOWN channel in :ref:`cdft-group-charge-acceptor` , :ref:`cdft-group-charge-donor` and :ref:`cdft-group-charge-diff` modes. To avoid disaster, make sure the specified CDFT_CHARGE_ACCEPTOR/DONOR_TARGET or CDFT_CHARGE_DIFF_TARGET keywords are consistent with the fact only one spin channel is being constrained. This functionality is NOT compatible with CDFT_GROUP_CHARGE_UP_ONLY, CDFT_ATOM_CHARGE/SPIN, and CDFT_GROUP_SPIN_ACCEPTOR/DONOR and :ref:`cdft-group-spin-diff` cDFT modes.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_GROUP_CHARGE_DOWN_ONLY [Logical]

   :Example:

   .. code::

      CDFT_GROUP_CHARGE_DOWN_ONLY T

.. _cdft-group-charge-up-only:

CDFT_GROUP_CHARGE_UP_ONLY
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_GROUP_CHARGE_UP_ONLY`

Logical to constrain only UP electrons

Constrain only SPIN-UP channel in :ref:`cdft-group-charge-acceptor` , :ref:`cdft-group-charge-donor` and :ref:`cdft-group-charge-diff` modes. To avoid disaster, make sure the specified CDFT_CHARGE_ACCEPTOR/DONOR_TARGET or CDFT_CHARGE_DIFF_TARGET keywords are consistent with the fact only one spin channel is being constrained. This functionality is NOT compatible with CDFT_GROUP_CHARGE_UP_ONLY, CDFT_ATOM_CHARGE/SPIN, and CDFT_GROUP_SPIN_ACCEPTOR/DONOR and :ref:`cdft-group-spin-diff` cDFT modes.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_GROUP_CHARGE_UP_ONLY [Logical]

   :Example:

   .. code::

      CDFT_GROUP_CHARGE_UP_ONLY T

.. _cdft-group-spin-acceptor:

CDFT_GROUP_SPIN_ACCEPTOR
------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_GROUP_SPIN_ACCEPTOR`

Perform an ACCEPTOR GROUP-SPIN-constrained CDFT simulation

Activate acceptor-group magnetic-moment-constrained-DFT mode. This mode is compatible with :ref:`cdft-group-spin-donor` and :ref:`cdft-group-charge-acceptor` / :ref:`cdft-group-charge-donor` cDFT-modes, and incompatible with :ref:`cdft-atom-charge` / :ref:`cdft-atom-spin` and :ref:`cdft-group-charge-diff` / :ref:`cdft-group-spin-diff` modes.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_GROUP_SPIN_ACCEPTOR [Logical]

   :Example:

   .. code::

      CDFT_GROUP_SPIN_ACCEPTOR T

.. _cdft-group-spin-diff:

CDFT_GROUP_SPIN_DIFF
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_GROUP_SPIN_DIFF`

Perform a GROUP-SPIN-DIFFERENCE-constrained CDFT simulation

Activate group magnetic-moment-difference constrained-DFT mode. This mode is compatible with :ref:`cdft-group-charge-diff` cDFT mode only. Thus, it is incompatible with any other CDFT_ATOM_CHARGE/SPIN and CDFT_GROUP_CHARGE/SPIN_ACCEPTOR/DONOR cDFT modes.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_GROUP_SPIN_DIFF [Logical]

   :Example:

   .. code::

      CDFT_GROUP_SPIN_DIFF T

.. _cdft-group-spin-diff-target:

CDFT_GROUP_SPIN_DIFF_TARGET
---------------------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_GROUP_SPIN_DIFF_TARGET`

Targeted :ref:`spin` difference (acceptor-donor) for  GROUP-SPIN-DIFFERENCE-constrained cDFT

Targeted magnetic-moment difference between acceptor and donor group for group-magnetic-moment-difference constrained-DFT mode [ :ref:`cdft-group-spin-diff` =T].

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_GROUP_SPIN_DIFF_TARGET [Real]

   :Example:

   .. code::

      CDFT_GROUP_SPIN_DIFF_TARGET 2

.. _cdft-group-spin-donor:

CDFT_GROUP_SPIN_DONOR
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_GROUP_SPIN_DONOR`

Perform a DONOR GROUP-SPIN-constrained CDFT simulation

Activate donor-group magnetic-moment-constrained-DFT mode. This mode is compatible with :ref:`cdft-group-spin-acceptor` and :ref:`cdft-group-charge-acceptor` / :ref:`cdft-group-charge-donor` cDFT-modes, and incompatible with :ref:`cdft-atom-charge` / :ref:`cdft-atom-spin` and :ref:`cdft-group-charge-diff` / :ref:`cdft-group-spin-diff` modes.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_GROUP_SPIN_DONOR [Logical]

   :Example:

   .. code::

      CDFT_GROUP_SPIN_DONOR T

.. _cdft-guru:

CDFT_GURU
---------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_GURU`

Let the user signal she/he does not need helpt with the cDFT U-initialisation

Tell ONETEP you are a cDFT-expert and prevent it from initialising the active |Uq/s| to the failsafe value of 1 eV, overwriting the values entered in the :ref:`constrained-dft` (Uq/s) block.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_GURU [Logical]

   :Example:

   .. code::

      CDFT_GURU T

.. _cdft-hubbard:

CDFT_HUBBARD
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_HUBBARD`

Perform a constrained-DFT+U simulation

Activate the constrained-DFT+U functionality. It requires specifications of a positive value for the Hubbard correction (Uh) in the :ref:`constrained-dft` Block.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_HUBBARD [Logical]

   :Example:

   .. code::

      CDFT_HUBBARD T

.. _cdft-max-grad:

CDFT_MAX_GRAD
-------------

:Type: Double-Precision
:Default: 0.001
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_MAX_GRAD`

Maximum permissible value of CDFT U-Gradient for convergence

Specifies the convergence threshold for the maximum value of the constraining-potential (Uq/s) gradient at any cDFT-site.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_MAX_GRAD [Real]

   :Example:

   .. code::

      CDFT_MAX_GRAD 0.01

.. _cdft-multi-proj:

CDFT_MULTI_PROJ
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_MULTI_PROJ`

Logical to use mutiple angular-momentum projectors on one cDFT-site

Activate the “as many cDFT-projectors as NGWFs” cDFT-mode. In this mode, the number of cDFT-projectors for a given cDFT-atom equals the number of NWGFs for that atom as specified in the :ref:`species` block. Both the cDFT-projectors and the NGWFs are localised within spheres of the same radius. When activated, this mode overwrites the L-projectors and Z-projectors settings in the :ref:`constrained-dft` block, and the cDFT-projectors are built according to the settings in the :ref:`species-atomic-set` block for that atom=cDFT-site.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_MULTI_PROJ [Logical]

   :Example:

   .. code::

      CDFT_MULTI_PROJ T

.. _cdft-print-all-occ:

CDFT_PRINT_ALL_OCC
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_PRINT_ALL_OCC`

Logical to have the occupancy-matrix of all the CDFT-atoms printed in stdout

Print detailed information of occupancies for al the cDFT-sites, for :ref:`output-detail` = VERBOSE.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_PRINT_ALL_OCC [Logical]

   :Example:

   .. code::

      CDFT_PRINT_ALL_OCC T

.. _cdft-read-projectors:

CDFT_READ_PROJECTORS
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_READ_PROJECTORS`

Logical to read cDFT-projectors from file

.. _cdft-spin-acceptor-target:

CDFT_SPIN_ACCEPTOR_TARGET
-------------------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_SPIN_ACCEPTOR_TARGET`

Targeted group-SPIN for GROUP-SPIN-ACCEPTOR-constrained cDFT

Targeted group magnetic-moment for acceptor-group magnetic-moment constrained-DFT mode [ :ref:`cdft-group-spin-acceptor` = T].

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_SPIN_ACCEPTOR_TARGET [Real]

   :Example:

   .. code::

      ; Constrain Nup-Ndown=-2 e in subspace.

.. _cdft-spin-donor-target:

CDFT_SPIN_DONOR_TARGET
----------------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_SPIN_DONOR_TARGET`

Targeted group-SPIN for GROUP-SPIN-DONOR-constrained cDFT

Targeted group magnetic-moment for donor-group magnetic-moment constrained-DFT mode [ :ref:`cdft-group-spin-donor` = T].

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_SPIN_DONOR_TARGET [Real]

   :Example:

   .. code::

      ; Constrain Nup-Ndown=-2 e in subspace.

.. _cdft-tight:

CDFT_TIGHT
----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_TIGHT`

Logical to activate tight NGWFs-cDFT optimisation

.. _cdft-trial-length:

CDFT_TRIAL_LENGTH
-----------------

:Type: Double-Precision
:Default: 0.1
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_TRIAL_LENGTH`

Trial length for cDFT line-search

Specifies initial trial length for first step of constraining-potential (Uq/s) conjugate gradients optimisation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CDFT_TRIAL_LENGTH [Real]

   :Example:

   .. code::

      CDFT_TRIAL_LENGTH 1.0

.. _cdft-write-potentials:

CDFT_WRITE_POTENTIALS
---------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CDFT_WRITE_POTENTIALS`

Logical to write cDFT-potentials into file

.. _charge:

CHARGE
------

:Type: Physical
:Default: 0.0
:Unit: e
:Level: Basic
:Group: None
:Search: :searchlink:`CHARGE`

The total charge of the system

Specifies the total :ref:`charge` of the system in units of the proton :ref:`charge` i.e. a positive :ref:`charge` corresponds to a system deficient of electrons.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CHARGE [Integer]

   :Example:

   .. code::

      CHARGE +1

.. _check-atoms:

CHECK_ATOMS
-----------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`CHECK_ATOMS`

Check atoms on top of each other

Perform a check on the atomic positions to ensure that no two atoms are unphysically close.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CHECK_ATOMS [Logical]

   :Example:

   .. code::

      CHECK_ATOMS F

.. _check-density:

CHECK_DENSITY
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`CHECK_DENSITY`

Check density is real when using complex NGWFs

.. _check-hermitian-mats:

CHECK_HERMITIAN_MATS
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`CHECK_HERMITIAN_MATS`

Check hermitian character of complex H/S/K matrices

.. _check-stack-size:

CHECK_STACK_SIZE
----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`CHECK_STACK_SIZE`

Check if stack size is sufficient? Set to F for valgrind.

.. _ci-cdft:

CI_CDFT
-------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CI_CDFT`

Perform a CONFIGURATION-INTERACTION CDFT simulation

Perform a Configuration Interaction calculation based on constrained-DFT configurations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CI_CDFT [Logical]

   :Example:

   .. code::

      CI_CDFT T

.. _ci-cdft-num-conf:

CI_CDFT_NUM_CONF
----------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CI_CDFT_NUM_CONF`

Number of cDFT-configurations for :ref:`ci-cdft` simulation

Specifies the number of constrained-DFT configuration available for a :ref:`ci-cdft` = T simulation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CI_CDFT_NUM_CONF [Integer]

   :Example:

   .. code::

      CI_CDFT_NUM_CONF 4

.. _classical-info:

CLASSICAL_INFO
--------------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`CLASSICAL_INFO`

Include classical atoms Coulomb interaction in the calculation

Introduce classical point charges in the system (no NGWFs are associated to them). The classical point charges interact via classical Coulomb interactions with the atoms and the rest of point charges. Specifies the atomic positions as Cartesian coordinates in atomic units (a0). In the above syntax, Si denotes the species of the charge (max 4 characters), Ri its position vector and Chi the charge in atomic units.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK CLASSICAL_INFO
      S1 R1x R1y R1z Ch1
      S2 R2x R2y R2z Ch2
       .   .   .   .       .
       .   .   .   .       .
      SN RNx RNy RNz ChN
      %ENDBLOCK CLASSICAL_INFO

   :Example:

   .. code::

      %BLOCK CLASSICAL_INFO
      O 19.7 21.8 22.6 -0.3
      H 17.6 22.1 22.6 0.12
      H 20.7 23.6 22.6 0.17
      %ENDBLOCK CLASSICAL_INFO

.. _comms-group-size:

COMMS_GROUP_SIZE
----------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`COMMS_GROUP_SIZE`

Number of procs in a group (determines comms efficiency)

To reduce comms bandwidth in an MPI job, groups of MPI processes are specified which pre-share matrix and cell-grid data between themselves before communications-heavy routines, such as sparse matrix algebra and cell extract/deposit routines. This integer specifies the size of these groups. This might often be most advantageously be set to the size of a physical "node" of a the parallel computer (ie the number of processes which share each chunk of physical memory).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COMMS_GROUP_SIZE [Text]

   :Example:

   .. code::

      COMMS_GROUP_SIZE 16

.. _cond-calc-eels:

COND_CALC_EELS
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_CALC_EELS`

Calculate matrix elements for electron energy loss spectra (EELS)

.. _cond-calc-max-eigen:

COND_CALC_MAX_EIGEN
-------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_CALC_MAX_EIGEN`

Calculate maximum conduction Hamiltonian eigenvalue

Calculate maximum conduction Hamiltonian eigenvalue at the start of each NGWF CG optimisation step, for use in updating the shift for the projected conduction Hamiltonian.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_CALC_MAX_EIGEN [Logical]

   :Example:

   .. code::

      COND_CALC_MAX_EIGEN

.. _cond-calc-optical-spectra:

COND_CALC_OPTICAL_SPECTRA
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_CALC_OPTICAL_SPECTRA`

Calculate matrix elements for optical absorption spectra

Calculate the optical matrix elements in the momentum representation, required for extended systems and molecules with large NGWF radii. If false the position representation is instead used.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_CALC_OPTICAL_SPECTRA [Logical]

   :Example:

   .. code::

      COND_CALC_OPTICAL_SPECTRA T

.. _cond-eels-fine-projectors:

COND_EELS_FINE_PROJECTORS
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_EELS_FINE_PROJECTORS`

Directly generate core wavefunctions on the fine grid

.. _cond-eels-realspace:

COND_EELS_REALSPACE
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_EELS_REALSPACE`

Compute matrix elements for EELS spectra using realspace method

.. _cond-energy-gap:

COND_ENERGY_GAP
---------------

:Type: Physical
:Default: 0.001
:Unit: ha
:Level: Intermediate
:Group: None
:Search: :searchlink:`COND_ENERGY_GAP`

Energy gap between highest optimised and lowest unoptimised cond state

Energy gap required above states that will be optimised during a conduction NGWF optimisation. The number of states may be increased until such a gap is found.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_ENERGY_GAP [Physical]

   :Example:

   .. code::

      COND_ENERGY_GAP 0.1 eV

.. _cond-energy-range:

COND_ENERGY_RANGE
-----------------

:Type: Physical
:Default: -1.0
:Unit: ha
:Level: Intermediate
:Group: None
:Search: :searchlink:`COND_ENERGY_RANGE`

Energy range of optimised cond states measured from HOMO

Energy range of states that will be optimised during a conduction NGWF optimisation. This is counted as the number of states measured from the highest occupied molecular orbital (HOMO). Negative values mean this range is not used in determining the occupancy of the conduction kernel.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_ENERGY_RANGE [Physical]

   :Example:

   .. code::

      COND_ENERGY_RANGE 5.0 eV

.. _cond-fixed-shift:

COND_FIXED_SHIFT
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_FIXED_SHIFT`

Fixed projected conduction Hamiltonian shift

Keep shift for projected conduction Hamiltonian constant in COND task

.. _cond-init-shift:

COND_INIT_SHIFT
---------------

:Type: Physical
:Default: 0.0
:Unit: hartree
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_INIT_SHIFT`

Initial shifting factor for projected conduction Hamiltonian

Initial shifting factor for projected conduction Hamiltonian, added to each eigenvalue.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_INIT_SHIFT [Physical]

   :Example:

   .. code::

      COND_INIT_SHIFT 0.1 "hartree"

.. _cond-kernel-cutoff:

COND_KERNEL_CUTOFF
------------------

:Type: Physical
:Default: 1000.0
:Unit: bohr
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_KERNEL_CUTOFF`

Conduction density kernel radius

Specifies the conduction density kernel spatial cutoff in atomic units (a0). Matrix elements are only included if the corresponding conduction NGWF centres are closer than this distance.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_KERNEL_CUTOFF [Physical]

   :Example:

   .. code::

      COND_KERNEL_CUTOFF 25.0 "bohr"

.. _cond-maxit-lnv:

COND_MAXIT_LNV
--------------

:Type: Integer
:Default: 10
:Unit: None
:Level: Intermediate
:Group: COND
:Search: :searchlink:`COND_MAXIT_LNV`

Max number of LNV iterations during conduction NGWF optimisation

Max number of LNV iterations during conduction NGWF optimisation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_MAXIT_LNV [Integer]

   :Example:

   .. code::

      COND_MAXIT_LNV 20

.. _cond-minit-lnv:

COND_MINIT_LNV
--------------

:Type: Integer
:Default: 10
:Unit: None
:Level: Intermediate
:Group: COND
:Search: :searchlink:`COND_MINIT_LNV`

Min number of LNV iterations during conduction NGWF optimisation

Minimum number of LNV iterations during conduction NGWF optimisation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_MINIT_LNV [Integer]

   :Example:

   .. code::

      COND_MINIT_LNV 15

.. _cond-num-extra-its:

COND_NUM_EXTRA_ITS
------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: COND
:Search: :searchlink:`COND_NUM_EXTRA_ITS`

Number of NGWF iterations with extra conduction states for 'preconditioning'

The number of iterations for which the conduction NGWFs are optimised for :ref:`cond-num-states` + :ref:`cond-num-extra-states` during an initial pre-optimisation stage to help avoid becoming trapped in local minima. If :ref:`cond-num-extra-states` = 0 this is ignored.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_NUM_EXTRA_ITS [Integer]

   :Example:

   .. code::

      COND_NUM_EXTRA_ITS 5

.. _cond-num-extra-states:

COND_NUM_EXTRA_STATES
---------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: COND
:Search: :searchlink:`COND_NUM_EXTRA_STATES`

Number of extra conduction states for initial 'preconditioning'

The number of additional conduction states to be optimised during an initial pre-optimisation stage to help avoid becoming trapped in local minima. This follows the same guidelines as :ref:`cond-num-states` . See also :ref:`cond-num-extra-its` .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_NUM_EXTRA_STATES [Integer]

   :Example:

   .. code::

      COND_NUM_EXTRA_STATES 10

.. _cond-num-states:

COND_NUM_STATES
---------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_NUM_STATES`

Number of conduction states to be optimised for

The number of conduction states to be optimised (spin up + down). For non-spin-polarised calculations, this should be an even number.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_NUM_STATES [Integer]

   :Example:

   .. code::

      COND_NUM_STATES 20

.. _cond-plot-joint-orbitals:

COND_PLOT_JOINT_ORBITALS
------------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_PLOT_JOINT_ORBITALS`

Plot orbitals in the joint basis following a conduction calculation

Plot orbitals in the joint valence-conduction NGWF basis following a conduction calculation. Applies to :ref:`homo-plot` and :ref:`lumo-plot` . See also :ref:`cond-plot-vc-orbitals` .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_PLOT_JOINT_ORBITALS [Logical]

   :Example:

   .. code::

      COND_PLOT_JOINT_ORBITALS F

.. _cond-plot-vc-orbitals:

COND_PLOT_VC_ORBITALS
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_PLOT_VC_ORBITALS`

Plot orbitals in the val and cond NGWF basis sets after a cond calc

Plot orbitals in separate val cond bases following COND task

.. _cond-read-denskern:

COND_READ_DENSKERN
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_READ_DENSKERN`

Read in conduction density kernel

Read in the conduction density kernel from disk. If the input filename is rootname.dat then the conduction density kernel filename is rootname.dkn_cond .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_READ_DENSKERN [Logical]

   :Example:

   .. code::

      COND_READ_DENSKERN T

.. _cond-read-tightbox-ngwfs:

COND_READ_TIGHTBOX_NGWFS
------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_READ_TIGHTBOX_NGWFS`

Read in universal tightbox conduction NGWFs

Read in the conduction NGWFs from disk. If the input filename is rootname.dat then the conduction NGWFs filename is rootname.tightbox_ngwfs_cond .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_READ_TIGHTBOX_NGWFS [Logical]

   :Example:

   .. code::

      COND_READ_TIGHTBOX_NGWFS T

.. _cond-shift-buffer:

COND_SHIFT_BUFFER
-----------------

:Type: Physical
:Default: 0.1
:Unit: hartree
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_SHIFT_BUFFER`

Additional buffer for updating projected Hamiltonian shift

Additional buffer to add to the highest calculated eigenvalue when updating the shift for the projected conduction Hamiltonian.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_SHIFT_BUFFER [Physical]

   :Example:

   .. code::

      COND_SHIFT_BUFFER 0.5 "hartree"

.. _cond-spec-calc-mom-mat-els:

COND_SPEC_CALC_MOM_MAT_ELS
--------------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_SPEC_CALC_MOM_MAT_ELS`

Calculate momentum matrix elements (default true otherwise use position)

Calculate the optical matrix elements in the momentum representation, required for extended systems and molecules with large NGWF radii. If false the position representation is instead used.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_SPEC_CALC_MOM_MAT_ELS [Logical]

   :Example:

   .. code::

      COND_SPEC_CALC_MOM_MAT_ELS F

.. _cond-spec-calc-nonloc-comm:

COND_SPEC_CALC_NONLOC_COMM
--------------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_SPEC_CALC_NONLOC_COMM`

Calculate nonlocal commutator for momentum matrix elements (default true)

Calculate the commutator between the nonlocal potential and the position operator, required for accurate calculation of optical absorption spectra when :ref:`cond-spec-calc-mom-mat-els` = true.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_SPEC_CALC_NONLOC_COMM [Logical]

   :Example:

   .. code::

      COND_SPEC_CALC_NONLOC_COMM F

.. _cond-spec-cont-deriv:

COND_SPEC_CONT_DERIV
--------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_SPEC_CONT_DERIV`

Calculate non-local commuator using continuous deriv in k-space (default true)

Calculate the commutator between the nonlocal potential and the position operator (when :ref:`cond-spec-calc-nonloc-comm` : true ) using a continuous derivative in k-space. If false a finite difference is instead used in k-space.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_SPEC_CONT_DERIV [Logical]

   :Example:

   .. code::

      COND_SPEC_CONT_DERIV F

.. _cond-spec-nonloc-comm-shift:

COND_SPEC_NONLOC_COMM_SHIFT
---------------------------

:Type: Double-Precision
:Default: 0.0001
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_SPEC_NONLOC_COMM_SHIFT`

Finite difference shift for non-local commutator if calculating using finite difference

Finite difference shift used for calculating the commutator between the nonlocal potential and the position operator if calculating using finite differences (i.e. when :ref:`cond-spec-cont-deriv` : false ).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COND_SPEC_NONLOC_COMM_SHIFT [Real]

   :Example:

   .. code::

      COND_SPEC_NONLOC_COMM_SHIFT 0.00001

.. _cond-spec-opt-smear:

COND_SPEC_OPT_SMEAR
-------------------

:Type: Physical
:Default: Unknown
:Unit: hartree
:Level: Intermediate
:Group: COND
:Search: :searchlink:`COND_SPEC_OPT_SMEAR`

Half width of smearing Gaussians for JDOS and imag. diel. fn.

.. _cond-spec-print-mat-els:

COND_SPEC_PRINT_MAT_ELS
-----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`COND_SPEC_PRINT_MAT_ELS`

Write optical matrix elements to file

.. _cond-spec-scissor-op:

COND_SPEC_SCISSOR_OP
--------------------

:Type: Physical
:Default: Unknown
:Unit: hartree
:Level: Intermediate
:Group: COND
:Search: :searchlink:`COND_SPEC_SCISSOR_OP`

Scissor operator for JDOS and imag. diel. fn.

.. _confined-ngwfs:

CONFINED_NGWFS
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`CONFINED_NGWFS`

Whether to use the hybrid confinement method

.. _confined-ngwfs-barrier:

CONFINED_NGWFS_BARRIER
----------------------

:Type: Double-Precision
:Default: 2000.0
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`CONFINED_NGWFS_BARRIER`

The barrier potential (in Ha) for NGWF confinement

.. _constant-efield:

CONSTANT_EFIELD
---------------

:Type: String
:Default: '0.0 0.0 0.0'
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`CONSTANT_EFIELD`

Cartesian coordinates of constant electric field vector

Specifies a constant electric field to apply to the system in terms of Cartesian vector components in atomic units Ha/(e a0).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CONSTANT_EFIELD [Text]

   :Example:

   .. code::

      CONSTANT_EFIELD 1.0e-3 0.0 0.0

.. _constrained-dft:

CONSTRAINED_DFT
---------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`CONSTRAINED_DFT`

Constrained_DFT species info [1:symb., 2:l=angul. mom., 3. Ionic_charge, 4: U_occ. (eV), 5:U_q_up (eV), 6:U_q_down (eV), 7:U_spin (eV), 8: Targeted N_up, 9: Targeted N_down, 10:targeted N_up - N_down

Manages constrained-DFT simulations. Provided :ref:`cdft-multi-proj` = F, for species S and subspace of angular momentum channel L (with principal quantum number n=L+1) we apply charge spin-specific [Uq(UP), Uq(DOWN)] or magnetic-moment-specific (Us) constraining potentials (in eV). For :ref:`cdft-atom-charge` = T, N(UP) and N(DOWN) indicate the targeted e-population for spin-channel UP and DOWN, respectively. For :ref:`cdft-atom-spin` = T, [N1(UP)-N1(DOWN)] indicates the targeted e-population difference (i.e. local magnetic moment). Uh indicates the optional Hubbard parameter (U, eV) to be applied for :ref:`cdft-hubbard` = T. An effective nuclear charge Z defines the hydrogenic orbitals spanning the subspace unless a negative value is given, e.g., Z=-10, in which case the NGWFs initial guess orbitals (numerical atomic orbitals) are used. Depending on the activated cDFT-mode, different columns of the block are used. These are: S, L, Z, (Uh), Uq(UP), Uq(DOWN), N(UP), N(DOWN) for :ref:`cdft-atom-charge` = T S, L, Z, (Uh), Us, [N(UP)-N(DOWN)] for :ref:`cdft-atom-spin` = T S, L, Z, (Uh), Uq(UP), Uq(DOWN) for :ref:`cdft-group-charge-acceptor` = T, :ref:`cdft-group-charge-donor` = T, or :ref:`cdft-group-charge-diff` = T. In this case, Uq(UP) must be equal to Uq(DOWN). Acceptor and donor atoms are differentiated by mean of negative [Uq(UP/DOWN)<0] and positive [Uq(UP/DOWN)>0] constraining-potentials, respectively. Setting Uq=0 will result in the given cDFT-atom being excluded from the list of the atoms in a given CDFT_GROUP_CHARGE_DONOR/ACCEPTOR/DIFF group. S, L, Z, (Uh), and Us for :ref:`cdft-group-spin-acceptor` = T, :ref:`cdft-group-spin-donor` = T, or :ref:`cdft-group-spin-diff` = T. In this case, Acceptor and donor atoms are differentiated by mean of negative (Us<0) and positive (Us>0) constraining-potentials, respectively. Setting Us=0 will result in the given cDFT-atom being excluded from the list of the atoms in a given CDFT_GROUP_SPIN_DONOR/ACCEPTOR/DIFF group. For more clarifying information please consult cDFT_keywords.pdf.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK CONSTRAINED_DFT
      S1 L1 Z1 Uh1(UP) Uq1(DOWN) Us1 N1(UP) N1(DOWN) [N1(UP)-N1(DOWN)]
      S2 L2 Z2 Uh2(UP) Uq2(DOWN) Us2 N2(UP) N2(DOWN) [N2(UP)-N2(DOWN)]
       .  .  .  .  .
       .  .  .  .  .
      SM LM ZM UhM(UP) UqM(DOWN) UsM NM(UP) NM(DOWN) [NM(UP)-NM(DOWN)]
      %ENDBLOCK CONSTRAINED_DFT

   :Example:

   .. code::

      %BLOCK CONSTRAINED_DFT
       # L Z Uh Uq(UP) Uq(DOWN) Us N(UP) N(DOWN) [N(UP)-N(DOWN)]
      N1 1 -5. 0.0 11.0 11.0  0.0 2.3 1.3 0.
      N2 1 -5. 0.0 -26.0 -26.0  0.0 2.7 2.7 0.
       %ENDBLOCK CONSTRAINED_DFT

.. _contracoham-radmult:

CONTRACOHAM_RADMULT
-------------------

:Type: Double-Precision
:Default: 1.0
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`CONTRACOHAM_RADMULT`

Sparsity pattern for Contra-Covariant Ham radius multiplier

.. _convolute-func:

CONVOLUTE_FUNC
--------------

:Type: String
:Default: 'erfc'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`CONVOLUTE_FUNC`

Convolute function to use with randomly initialised NGWFs

.. _convolute-rand:

CONVOLUTE_RAND
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`CONVOLUTE_RAND`

If true, convolute randomly initialised NGWFs to smooth edges

.. _conv-region-width:

CONV_REGION_WIDTH
-----------------

:Type: String
:Default: '-1.0'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`CONV_REGION_WIDTH`

Specify width of region (from the sphere edge) in which apply convolution

.. _coreham-denskern-guess:

COREHAM_DENSKERN_GUESS
----------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`COREHAM_DENSKERN_GUESS`

Initial guess for density kernel from core Hamiltonian

Generate an initial guess for the density kernel using a Hamiltonian generated by simple atomic screening of the pseudopotential. The density kernel may be obtained by the Palser-Manolopoulos algorithm or direct diagonalization. If false, a simple diagonal approximation is used for the density kernel.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COREHAM_DENSKERN_GUESS [Logical]

   :Example:

   .. code::

      COREHAM_DENSKERN_GUESS F

.. _coulomb-cutoff-length:

COULOMB_CUTOFF_LENGTH
---------------------

:Type: Physical
:Default: -1.0
:Unit: bohr
:Level: Intermediate
:Group: CHARGE
:Search: :searchlink:`COULOMB_CUTOFF_LENGTH`

Length of cylinder or width of slab for cutoff coulomb interaction

Cutoff Coulomb only. Chooses the length of either (a) the cylinder on which the Coulomb interaction is truncated, in the case of a cylindrical cutoff, or (b) the slab on which the Coulomb interaction is truncated, in the case of a slab cutoff.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COULOMB_CUTOFF_LENGTH [Value] [Unit]

   :Example:

   .. code::

      COULOMB_CUTOFF_LENGTH 100 bohr

.. _coulomb-cutoff-radius:

COULOMB_CUTOFF_RADIUS
---------------------

:Type: Physical
:Default: -1.0
:Unit: bohr
:Level: Intermediate
:Group: CHARGE
:Search: :searchlink:`COULOMB_CUTOFF_RADIUS`

Radius of sphere or cylinder for cutoff coulomb interaction

Cutoff Coulomb only. Chooses the radius of the sphere, cylinder or wire on which the Coulomb interaction is truncated.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COULOMB_CUTOFF_RADIUS [Value] [Unit]

   :Example:

   .. code::

      COULOMB_CUTOFF_RADIUS 100 bohr

.. _coulomb-cutoff-type:

COULOMB_CUTOFF_TYPE
-------------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Intermediate
:Group: CHARGE
:Search: :searchlink:`COULOMB_CUTOFF_TYPE`

Type of cutoff coulomb interaction: NONE, SPHERE, CYLINDER, SLAB, WIRE

Activates Cutoff Coulomb interactions, and chooses which type of cutoff to apply. Allowed values are: NONE, SPHERE, CYLINDER, SLAB, WIRE.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COULOMB_CUTOFF_TYPE [Text]

   :Example:

   .. code::

      COULOMB_CUTOFF_TYPE SPHERE

.. _coulomb-cutoff-write-int:

COULOMB_CUTOFF_WRITE_INT
------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: CHARGE
:Search: :searchlink:`COULOMB_CUTOFF_WRITE_INT`

Write real-space cutoff Coulomb interaction scalarfield

Writes a scalarfield plot of the Cutoff Coulomb interaction for the chosen geometry and cutoff type. Plots .grd or .cube according to the options chosen for :ref:`grd-format` and :ref:`cube-format`

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      COULOMB_CUTOFF_WRITE_INT [Value]

   :Example:

   .. code::

      COULOMB_CUTOFF_WRITE_INT T

.. _couplings-states:

COUPLINGS_STATES
----------------

:Type: Block
:Default: None
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`COUPLINGS_STATES`

Allow the calculation of electronic couplings

.. _cube-format:

CUBE_FORMAT
-----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`CUBE_FORMAT`

Allow .cube format for plot outputs

Output volumetric data (e.g. charge density, potential, NGWFs, canonical orbitals) in cube format . This can be visualized using free software such as gOpenMol , MOLEKEL and XCrySDen .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CUBE_FORMAT [Logical]

   :Example:

   .. code::

      CUBE_FORMAT T

.. _cutoff-energy:

CUTOFF_ENERGY
-------------

:Type: Physical
:Default: -20.0
:Unit: hartree
:Level: Basic
:Group: GENERAL
:Search: :searchlink:`CUTOFF_ENERGY`

Plane wave kinetic energy cutoff

Chooses the psinc basis set to correspond as closely as possible to a plane-wave basis with this cutoff energy. See section 3 of Skylariset al.,J. Phys.: Condens. Matter17, 5757 (2005) for more details.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      CUTOFF_ENERGY [Value] [Unit]

   :Example:

   .. code::

      CUTOFF_ENERGY 500 eV

.. _dbl-grid-scale:

DBL_GRID_SCALE
--------------

:Type: Double-Precision
:Default: 2.0
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`DBL_GRID_SCALE`

Ratio of charge density / potential working grid to standard grid (1 or 2 only)

Ratio of charge density / potential working grid to standard grid (1 or 2 only).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DBL_GRID_SCALE [Real]

   :Example:

   .. code::

      DBL_GRID_SCALE 1.0

.. _ddec-aniso:

DDEC_ANISO
----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: DDEC
:Search: :searchlink:`DDEC_ANISO`

Calculates off center point charges

.. _ddec-aniso-error-reduce:

DDEC_ANISO_ERROR_REDUCE
-----------------------

:Type: Double-Precision
:Default: 0.0625
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_ANISO_ERROR_REDUCE`

Sets the improve in ESP needed before off center charges are added

.. _ddec-aniso-error-thres:

DDEC_ANISO_ERROR_THRES
----------------------

:Type: Double-Precision
:Default: 0.9025
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_ANISO_ERROR_THRES`

Sets the threshold above which off center charges are added

.. _ddec-aniso-max-dis:

DDEC_ANISO_MAX_DIS
------------------

:Type: Double-Precision
:Default: 0.8
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_ANISO_MAX_DIS`

Sets the maximum distance from the atom center

.. _ddec-aniso-max-dis-halogen:

DDEC_ANISO_MAX_DIS_HALOGEN
--------------------------

:Type: Double-Precision
:Default: 1.5
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_ANISO_MAX_DIS_HALOGEN`

Sets the maximum distance from the atom center for the halogens

.. _ddec-avg-rad:

DDEC_AVG_RAD
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Dummy
:Group: DDEC
:Search: :searchlink:`DDEC_AVG_RAD`

Compute expected radius of each atom based on the partitoned density

.. _ddec-c3-refdens:

DDEC_C3_REFDENS
---------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: DDEC
:Search: :searchlink:`DDEC_C3_REFDENS`

Reshape reference densities to produce c3 reference densities

.. _ddec-calculate:

DDEC_CALCULATE
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: DDEC
:Search: :searchlink:`DDEC_CALCULATE`

Performs DDEC charge analysis

Activate Density Derived Electrostatic and Chemical analysis routines.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_CALCULATE [Logical]

   :Example:

   .. code::

      DDEC_CALCULATE T

.. _ddec-classical-hirshfeld:

DDEC_CLASSICAL_HIRSHFELD
------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: DDEC
:Search: :searchlink:`DDEC_CLASSICAL_HIRSHFELD`

DDEC range of IH (+/-) ionic reference states to be generated

Output results from classical Hirshfeld partitioning, which are the atomic charges from the 1st iteration of DDEC. Reference densities must be initialised as neutral atomic densities using the keyword 'ddec_refdens_init: T'

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_CLASSICAL_HIRSHFELD [Logical]

   :Example:

   .. code::

      DDEC_CLASSICAL_HIRSHFELD T

.. _ddec-conv-threshold:

DDEC_CONV_THRESHOLD
-------------------

:Type: Double-Precision
:Default: 1e-05
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_CONV_THRESHOLD`

DDEC charge convergence threshold

.. _ddec-core-correction:

DDEC_CORE_CORRECTION
--------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: DDEC
:Search: :searchlink:`DDEC_CORE_CORRECTION`

Whether to correct the integrated number of core electrons on the Cartesian grid

.. _ddec-core-corr-maxit:

DDEC_CORE_CORR_MAXIT
--------------------

:Type: Integer
:Default: 40
:Unit: None
:Level: Expert
:Group: DDEC
:Search: :searchlink:`DDEC_CORE_CORR_MAXIT`

Number of core correction iterations

.. _ddec-core-maxit:

DDEC_CORE_MAXIT
---------------

:Type: Integer
:Default: 2000
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_CORE_MAXIT`

Maximum number of DDEC core density iterations

Maximum number of DDEC core iterations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_CORE_MAXIT [Value]

   :Example:

   .. code::

      DDEC_CORE_MAXIT 4000

.. _ddec-eff-decay-exp:

DDEC_EFF_DECAY_EXP
------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_EFF_DECAY_EXP`

Calculate AIM effective decay exponents for r > ddec_eff_decay_rmin

.. _ddec-eff-decay-rmin:

DDEC_EFF_DECAY_RMIN
-------------------

:Type: Physical
:Default: Unknown
:Unit: bohr
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_EFF_DECAY_RMIN`

Minumum radius of AIM density to which effective decay exponents are fitted

.. _ddec-format-dens:

DDEC_FORMAT_DENS
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: DDEC
:Search: :searchlink:`DDEC_FORMAT_DENS`

Whether to format the input densities to shave off density spikes

.. _ddec-ih-fraction:

DDEC_IH_FRACTION
----------------

:Type: Double-Precision
:Default: Unknown
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_IH_FRACTION`

DDEC IH fraction

Fraction of reference ion weighting used in DDEC partitioning.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_IH_FRACTION [Value]

   :Example:

   .. code::

      DDEC_IH_FRACTION 0.5

.. _ddec-ih-ionic-range:

DDEC_IH_IONIC_RANGE
-------------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_IH_IONIC_RANGE`

DDEC range of IH (+/-) ionic reference states to be generated

Range of charges (positive or negative with respect to the neutral atom) to be generated for each ionic species as ionic reference densities. DDEC calculation will exit if the charge on any atom exceeds this range.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_IH_IONIC_RANGE [Value]

   :Example:

   .. code::

      DDEC_IH_IONIC_RANGE 4

.. _ddec-interp-rad-dens:

DDEC_INTERP_RAD_DENS
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: DDEC
:Search: :searchlink:`DDEC_INTERP_RAD_DENS`

Interpolate converged radial densities for a smoother profile

Trilinear postprocessing interpolation of converged DDEC AIM densities for a smoother profile. Does not affect calculation results, only the output density profiles.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_INTERP_RAD_DENS [Logical]

   :Example:

   .. code::

      DDEC_INTERP_RAD_DENS T

.. _ddec-maxit:

DDEC_MAXIT
----------

:Type: Integer
:Default: 2000
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_MAXIT`

Maximum number of DDEC iterations

Maximum number of DDEC iterations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_MAXIT [Value] [Unit]

   :Example:

   .. code::

      DDEC_MAXIT 4000

.. _ddec-min-shell-dens:

DDEC_MIN_SHELL_DENS
-------------------

:Type: Double-Precision
:Default: 100.0
:Unit: None
:Level: Expert
:Group: DDEC
:Search: :searchlink:`DDEC_MIN_SHELL_DENS`

Minimum number of points per shell for grid point binning

Minimum number of points lying in each spherical shell. Shells with fewer points than this will be subjected to interpolation if 'ddec_interp_rad_dens: T'.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_MIN_SHELL_DENS [Value]

   :Example:

   .. code::

      DDEC_MIN_SHELL_DENS 50.0

.. _ddec-moment:

DDEC_MOMENT
-----------

:Type: Integer
:Default: -1
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_MOMENT`

Compute DDEC moment

Calculate DDEC AIM moment of order n. Set to positive integer n to turn on calculation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_MOMENT [Value]

   :Example:

   .. code::

      DDEC_MOMENT 5

.. _ddec-multipole:

DDEC_MULTIPOLE
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_MULTIPOLE`

Compute DDEC dipoles and quadrupoles

Calculate DDEC AIM dipoles and quadrupoles.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_MULTIPOLE [Logical]

   :Example:

   .. code::

      DDEC_MULTIPOLE T

.. _ddec-rad-npts:

DDEC_RAD_NPTS
-------------

:Type: Integer
:Default: 100
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`DDEC_RAD_NPTS`

Number of spherical shells per atom

Number of atom-centered shells used for spherical averaging and storing the DDEC AIM density profiles.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_RAD_NPTS [Value]

   :Example:

   .. code::

      DDEC_RAD_NPTS 250

.. _ddec-rad-rcut:

DDEC_RAD_RCUT
-------------

:Type: Physical
:Default: Unknown
:Unit: bohr
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_RAD_RCUT`

Radius of largest spherical shell

Radius of the largest spherical shell for DDEC analysis. Each spherical shell is spaced equally.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_RAD_RCUT [Value] [Unit]

   :Example:

   .. code::

      DDEC_RAD_RCUT 6.0 ang

.. _ddec-rad-shell-mode:

DDEC_RAD_SHELL_MODE
-------------------

:Type: String
:Default: 'MIDDLE'
:Unit: None
:Level: Expert
:Group: DDEC
:Search: :searchlink:`DDEC_RAD_SHELL_MODE`

The effective radius of each shell

.. _ddec-rcomp:

DDEC_RCOMP
----------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: DDEC
:Search: :searchlink:`DDEC_RCOMP`

DDEC rcomp block paramters

.. _ddec-refdens-init:

DDEC_REFDENS_INIT
-----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: DDEC
:Search: :searchlink:`DDEC_REFDENS_INIT`

Initialize ISA guess densities as neutral reference densities

Initialize DDEC AIM densities as neutral atom reference densities. Required for 'ddec_classical_hirshfeld'.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_REFDENS_INIT [Logical]

   :Example:

   .. code::

      DDEC_REFDENS_INIT F

.. _ddec-refdens-path:

DDEC_REFDENS_PATH
-----------------

:Type: String
:Default: ''
:Unit: None
:Level: Basic
:Group: DDEC
:Search: :searchlink:`DDEC_REFDENS_PATH`

Path to DDEC reference densities

.. _ddec-ref-shell-mode:

DDEC_REF_SHELL_MODE
-------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Expert
:Group: DDEC
:Search: :searchlink:`DDEC_REF_SHELL_MODE`

Mode for initializing reference densities from fine radial grid

.. _ddec-renormalize-refdens:

DDEC_RENORMALIZE_REFDENS
------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: DDEC
:Search: :searchlink:`DDEC_RENORMALIZE_REFDENS`

Renormalize reference densities

.. _ddec-reshape-dens:

DDEC_RESHAPE_DENS
-----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: DDEC
:Search: :searchlink:`DDEC_RESHAPE_DENS`

Whether to reshape the partitioned AIM density after each iteration

.. _ddec-use-coredens:

DDEC_USE_COREDENS
-----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_USE_COREDENS`

Whether to include core densities in calculation

.. _ddec-write-rad:

DDEC_WRITE_RAD
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DDEC
:Search: :searchlink:`DDEC_WRITE_RAD`

Write DDEC partial radial density for each atom

Write converged AIM spherically-averaged density profiles for all atoms.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_WRITE_RAD [Logical]

   :Example:

   .. code::

      DDEC_WRITE_RAD T

.. _ddec-zero-threshold:

DDEC_ZERO_THRESHOLD
-------------------

:Type: Double-Precision
:Default: 1e-10
:Unit: None
:Level: Expert
:Group: DDEC
:Search: :searchlink:`DDEC_ZERO_THRESHOLD`

DDEC threshold to neglect 1/density

Threshold for density on grid to be excluded in order to avoid division by zero.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DDEC_ZERO_THRESHOLD [Value]

   :Example:

   .. code::

      DDEC_ZERO_THRESHOLD 1e-8

.. _delta-e-conv:

DELTA_E_CONV
------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`DELTA_E_CONV`

Use consecutive energy gains as a criterion for NGWF convergence

When aggressive density kernel truncation is applied, the energy is not guaranteed to decrease monotonically. When :ref:`delta-e-conv` is true, consecutive energy gains are used as an additional convergence criterion.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DELTA_E_CONV [Logical]

   :Example:

   .. code::

      DELTA_E_CONV F

.. _dense-foe:

DENSE_FOE
---------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: EDFT
:Search: :searchlink:`DENSE_FOE`

Use the dense matrix version of the :ref:`foe`

By default the density kernel is calculated in a sparse format in FOE, even when it has no sparsity. If the user wants to apply :ref:`foe` to systems of less than ~1000 atoms, then using dense matrix algebra may be beneficial.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DENSE_FOE [Logical]

   :Example:

   .. code::

      DENSE_FOE T

.. _dense-threshold:

DENSE_THRESHOLD
---------------

:Type: Double-Precision
:Default: 1e-06
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`DENSE_THRESHOLD`

Threshold for matrix segment filling for segment  to be dense

Sets the filling fraction threshold above which a section of a sparse matrix will be set to dense. Dense matrix algebra is computationally faster above filling fractions of ~10%, but higher communications bandwidth is required so higher values may degrade performance on low-bandwidth parallel architectures. Most users will not need to change this, but in some cases, a higher value than the default can reduce communications bottlenecks during sparse matrix multiplication.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DENSE_THRESHOLD [Value]

   :Example:

   .. code::

      DENSE_THRESHOLD 0.80

.. _density-init-use-omp:

DENSITY_INIT_USE_OMP
--------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`DENSITY_INIT_USE_OMP`

Should density initialisation use OMP?

.. _devel-code:

DEVEL_CODE
----------

:Type: String
:Default: ''
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`DEVEL_CODE`

For development code only

.. _dftb:

DFTB
----

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: DFTB
:Search: :searchlink:`DFTB`

Perform a :ref:`dftb` calculation?

.. _dftb-bc:

DFTB_BC
-------

:Type: String
:Default: ''
:Unit: None
:Level: Expert
:Group: DFTB
:Search: :searchlink:`DFTB_BC`

3 character string defining BCs IN :ref:`dftb` calculations along each lattice vector. 'O' for open, 'P' for periodic.

.. _dftb-broyden-mixing:

DFTB_BROYDEN_MIXING
-------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_BROYDEN_MIXING`

Whether to use broyden mixing in DFTB.

.. _dftb-cartesian-ngwfs:

DFTB_CARTESIAN_NGWFS
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_CARTESIAN_NGWFS`

In DFTB, Use Cartesian basis functions?

.. _dftb-common-param-file:

DFTB_COMMON_PARAM_FILE
----------------------

:Type: String
:Default: Unknown
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_COMMON_PARAM_FILE`

Name of the :ref:`dftb` common parameter definition file

.. _dftb-coord-cutoff:

DFTB_COORD_CUTOFF
-----------------

:Type: Physical
:Default: 40.0
:Unit: bohr
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_COORD_CUTOFF`

distance cutoff for calculation of coordination number.

.. _dftb-dem-sparsity:

DFTB_DEM_SPARSITY
-----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_DEM_SPARSITY`

Whether to use sparsity while calculating DEM matrices in DFTB.

.. _dftb-ewald-parameter:

DFTB_EWALD_PARAMETER
--------------------

:Type: Physical
:Default: -1.0
:Unit: 1/ang
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_EWALD_PARAMETER`

Convergence parameter for the Ewald summation in DFTB.

.. _dftb-ies-charge:

DFTB_IES_CHARGE
---------------

:Type: Physical
:Default: Unknown
:Unit: e
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_IES_CHARGE`

Charge for isotropic electrostatics in DFTB.

.. _dftb-matrix-storage:

DFTB_MATRIX_STORAGE
-------------------

:Type: String
:Default: 'DEM'
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_MATRIX_STORAGE`

Matrix storage format: SPAM3 or DEM.

.. _dftb-method:

DFTB_METHOD
-----------

:Type: String
:Default: 'GFN0'
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_METHOD`

Choice of a method for DFTB

.. _dftb-method-param-file:

DFTB_METHOD_PARAM_FILE
----------------------

:Type: String
:Default: Unknown
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_METHOD_PARAM_FILE`

Name of the :ref:`dftb` method parameter definition file

.. _dftb-neighbour-list:

DFTB_NEIGHBOUR_LIST
-------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_NEIGHBOUR_LIST`

Whether to use neighbour list in :ref:`dftb` when storage scheme is DEM.

.. _dftb-orthogonal-basis:

DFTB_ORTHOGONAL_BASIS
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_ORTHOGONAL_BASIS`

Whether to use orthogonal basis in DFTB.

.. _dftb-overlap-analytical:

DFTB_OVERLAP_ANALYTICAL
-----------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_OVERLAP_ANALYTICAL`

In DFTB, is the overlap matrix to be calculated analytically?

.. _dftb-rep-cutoff:

DFTB_REP_CUTOFF
---------------

:Type: Physical
:Default: 40.0
:Unit: bohr
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_REP_CUTOFF`

distance cutoff for calculation of :ref:`dftb` repulsion term.

.. _dftb-scc-charge-tol:

DFTB_SCC_CHARGE_TOL
-------------------

:Type: Physical
:Default: 2e-05
:Unit: e
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_SCC_CHARGE_TOL`

Tolerance for charge self-consistency in GFN1 DFTB.

.. _dftb-scc-damp:

DFTB_SCC_DAMP
-------------

:Type: Double-Precision
:Default: 0.4
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_SCC_DAMP`

Damping for charge mixing in SCC loop.

.. _dftb-scc-energy-tol:

DFTB_SCC_ENERGY_TOL
-------------------

:Type: Physical
:Default: 1e-06
:Unit: ha
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_SCC_ENERGY_TOL`

Tolerance for energy convergence in GFN1 DFTB.

.. _dftb-scc-maxit:

DFTB_SCC_MAXIT
--------------

:Type: Integer
:Default: 250
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_SCC_MAXIT`

Maximum SCC iterations in DFTB.

.. _dftb-srb-cutoff:

DFTB_SRB_CUTOFF
---------------

:Type: Physical
:Default: Unknown
:Unit: bohr
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_SRB_CUTOFF`

distance cutoff for calculation of :ref:`dftb` SRB term.

.. _dftb-wsc:

DFTB_WSC
--------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_WSC`

Whether to use WSC instead of MIC in :ref:`dftb` electronic calculation.

.. _dftb-wsc-tol:

DFTB_WSC_TOL
------------

:Type: Double-Precision
:Default: 0.01
:Unit: None
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_WSC_TOL`

Tolerance for equivalent images in WSC.

.. _dftb-xb-cutoff:

DFTB_XB_CUTOFF
--------------

:Type: Physical
:Default: 20.0
:Unit: bohr
:Level: Intermediate
:Group: DFTB
:Search: :searchlink:`DFTB_XB_CUTOFF`

Cutoff for length of halogen bonds in DFTB.

.. _dft-nu:

DFT_NU
------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`DFT_NU`

Constrained DFT+nu Species info

.. _dft-nu-continuation:

DFT_NU_CONTINUATION
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DFTNU
:Search: :searchlink:`DFT_NU_CONTINUATION`

Restart U1/2 optimisation from .dft_nu file

.. _dft-nu-opt-u1-only:

DFT_NU_OPT_U1_ONLY
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DFTNU
:Search: :searchlink:`DFT_NU_OPT_U1_ONLY`

Selective optimisazion of U1 potential

.. _dft-nu-opt-u2-only:

DFT_NU_OPT_U2_ONLY
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DFTNU
:Search: :searchlink:`DFT_NU_OPT_U2_ONLY`

Selective optimisazion of U2 potential

.. _dipole-correction:

DIPOLE_CORRECTION
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`DIPOLE_CORRECTION`

Self-consistent dipole correction by external electric field.

.. _dipole-correction-dir:

DIPOLE_CORRECTION_DIR
---------------------

:Type: Integer
:Default: 3
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`DIPOLE_CORRECTION_DIR`

Direction to which the dipole layer is perpendicular to. 1(along X), 2(along Y), 3(along Z)

.. _dispersion:

DISPERSION
----------

:Type: String
:Default: '4'
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`DISPERSION`

Select dispersion correction

Specifies the damping function to be used in the calculation of :ref:`dispersion` corrections: 0 -  No :ref:`dispersion` correction 1 - Damping function from Elstner [J. Chem. Phys. 114(12), 5149-5155] 2 - First damping function from Wu and Yang (I) [J. Chem. Phys. 116(2), 515-524, 2002] 3 - Second damping function from Wu and Yang (II) [J. Chem. Phys. 116(2), 515-524, 2002] 4 - Damping function of D2 correction of Grimme [ S. Grimme, J. Comput. Chem. 27(15), 1787-1799, 2006] See Proceedings of the Royal Society A 465(2103), 669-683 for more details.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DISPERSION [Integer]

   :Example:

   .. code::

      DISPERSION 1

.. _dma-bessel-averaging:

DMA_BESSEL_AVERAGING
--------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: DMA
:Search: :searchlink:`DMA_BESSEL_AVERAGING`

Whether DMA expansion should average over even-odd Bessels

.. _dma-calculate:

DMA_CALCULATE
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: DMA
:Search: :searchlink:`DMA_CALCULATE`

Compute distributed multipole analysis

.. _dma-dipole-scaling:

DMA_DIPOLE_SCALING
------------------

:Type: Double-Precision
:Default: 1.0
:Unit: None
:Level: Intermediate
:Group: DMA
:Search: :searchlink:`DMA_DIPOLE_SCALING`

Scaling factor applied to all DMA dipoles

.. _dma-max-l:

DMA_MAX_L
---------

:Type: Integer
:Default: -1
:Unit: None
:Level: Basic
:Group: DMA
:Search: :searchlink:`DMA_MAX_L`

Maximum order of DMA multipoles for properties

.. _dma-max-q:

DMA_MAX_Q
---------

:Type: Integer
:Default: -1
:Unit: None
:Level: Basic
:Group: DMA
:Search: :searchlink:`DMA_MAX_Q`

Maximum number of Bessel zeros in DMA''s SW expansion

.. _dma-metric:

DMA_METRIC
----------

:Type: String
:Default: 'electrostatic'
:Unit: None
:Level: Intermediate
:Group: DMA
:Search: :searchlink:`DMA_METRIC`

Electrostatic or overlap metric

.. _dma-multipole-scaling:

DMA_MULTIPOLE_SCALING
---------------------

:Type: Double-Precision
:Default: 1.0
:Unit: None
:Level: Intermediate
:Group: DMA
:Search: :searchlink:`DMA_MULTIPOLE_SCALING`

Scaling factor applied to all DMA multipoles

.. _dma-output-potential:

DMA_OUTPUT_POTENTIAL
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: DMA
:Search: :searchlink:`DMA_OUTPUT_POTENTIAL`

Output distributed multipole potential on cell faces

.. _dma-output-potential-reference:

DMA_OUTPUT_POTENTIAL_REFERENCE
------------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: DMA
:Search: :searchlink:`DMA_OUTPUT_POTENTIAL_REFERENCE`

Output reference (pointwise) potential on cell faces

.. _dma-precise-gdma-output:

DMA_PRECISE_GDMA_OUTPUT
-----------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: QMMM
:Search: :searchlink:`DMA_PRECISE_GDMA_OUTPUT`

Extra precision in GDMA output at the cost of breaking format compat

.. _dma-quadrupole-scaling:

DMA_QUADRUPOLE_SCALING
----------------------

:Type: Double-Precision
:Default: 1.0
:Unit: None
:Level: Intermediate
:Group: DMA
:Search: :searchlink:`DMA_QUADRUPOLE_SCALING`

Scaling factor applied to all DMA quadrupoles

.. _dma-scale-charge:

DMA_SCALE_CHARGE
----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: DMA
:Search: :searchlink:`DMA_SCALE_CHARGE`

Scale DMA monopoles?

.. _dma-target-num-val-elec:

DMA_TARGET_NUM_VAL_ELEC
-----------------------

:Type: Double-Precision
:Default: -999999.0
:Unit: None
:Level: Expert
:Group: DMA
:Search: :searchlink:`DMA_TARGET_NUM_VAL_ELEC`

Target number of valence electrons in DMA region (for scaling)

.. _dma-use-ri:

DMA_USE_RI
----------

:Type: String
:Default: '<unset>'
:Unit: None
:Level: Basic
:Group: DMA
:Search: :searchlink:`DMA_USE_RI`

ID of the :ref:`swri` to use for DMA

.. _dmft-complex-freq:

DMFT_COMPLEX_FREQ
-----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_COMPLEX_FREQ`

Perform DMFT using complex frequencies. Real frequencies are required for DOS and optics calculations

.. _dmft-cutoff-small:

DMFT_CUTOFF_SMALL
-----------------

:Type: Physical
:Default: 0.0
:Unit: hartree
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_CUTOFF_SMALL`

Atomic energy threshold for double-precision calculations of the DMFT  Green-function at low frequencies. (Useful for GPU calculations.)

.. _dmft-cutoff-tail:

DMFT_CUTOFF_TAIL
----------------

:Type: Physical
:Default: None
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_CUTOFF_TAIL`

Atomic energy threshold for double-precision calculations of the DMFT  Green-function at high frequencies. (Useful for GPU calculations.)

.. _dmft-dos-max:

DMFT_DOS_MAX
------------

:Type: Physical
:Default: 10.0
:Unit: hartree
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_DOS_MAX`

Maximum of energy window on real axis (Ha) for DMFT DOS calculations

.. _dmft-dos-min:

DMFT_DOS_MIN
------------

:Type: Physical
:Default: -10.0
:Unit: hartree
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_DOS_MIN`

Minimum of energy window on real axis (Ha) for DMFT DOS calculations

.. _dmft-emax:

DMFT_EMAX
---------

:Type: Physical
:Default: 1.0
:Unit: hartree
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_EMAX`

Maximum energy on real axis (Ha) for DFT+DMFT

.. _dmft-emin:

DMFT_EMIN
---------

:Type: Physical
:Default: -1.0
:Unit: hartree
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_EMIN`

Miniumum energy on real axis (Ha) for DFT+DMFT

.. _dmft-fully-sc:

DMFT_FULLY_SC
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_FULLY_SC`

If true uses the self energy in the ONETEP kernel NGWF optimization, in the energy functional

.. _dmft-fully-sc-h:

DMFT_FULLY_SC_H
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_FULLY_SC_H`

If true the H used in the DFT is the KS H built from 1 shot DMFT

.. _dmft-kernel:

DMFT_KERNEL
-----------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_KERNEL`

Writes dmft density kernel, 0:does not calculate it, -1:writes the purified dmft density kernel

.. _dmft-kernel-mix:

DMFT_KERNEL_MIX
---------------

:Type: Double-Precision
:Default: 0.1
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_KERNEL_MIX`

Mixing of DMFT and DFT kernels for DFT+DMFT

.. _dmft-kpoints-sym:

DMFT_KPOINTS_SYM
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_KPOINTS_SYM`

If true and using k points, additional cubic symmetry is used to reduce the number of k points, and not only the k inversion symmetry. Note: this is NOT valid when computing the DMFT density kernel

.. _dmft-ks-shift:

DMFT_KS_SHIFT
-------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_KS_SHIFT`

if true adds the correction to the energy in the SC dmft minimization during kernel optimization where the re-occupation of the energy level by the DMFT density kernel is taken into account

.. _dmft-mu-diff-max:

DMFT_MU_DIFF_MAX
----------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_MU_DIFF_MAX`

The threshold for the difference between the current and target occupancies  when updating the chemical potential in DMFT

.. _dmft-mu-order:

DMFT_MU_ORDER
-------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_MU_ORDER`

Order of the Newton Method used to fix the chemical potential in DMFT (HouseHolder general form)

.. _dmft-nbo:

DMFT_NBO
--------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_NBO`

---Missing description---

.. _dmft-nkpoints:

DMFT_NKPOINTS
-------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_NKPOINTS`

Number of K points for averaging the lattice Green Function

.. _dmft-nmu-loop:

DMFT_NMU_LOOP
-------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_NMU_LOOP`

Number of iterations of the Newtons method for finding the chemical potential

.. _dmft-nval:

DMFT_NVAL
---------

:Type: Integer
:Default: 40
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_NVAL`

Maximum number of eigenstates in this energy window used for the Green's function inversion

.. _dmft-optics:

DMFT_OPTICS
-----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_OPTICS`

Calculate the optical conductivity from the DMFT Green function

.. _dmft-optics-i1:

DMFT_OPTICS_I1
--------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_OPTICS_I1`

First direction for optical conductivity current-current correlator

.. _dmft-optics-i2:

DMFT_OPTICS_I2
--------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_OPTICS_I2`

Second direction for optical conductivity current-current correlator

.. _dmft-optics-window:

DMFT_OPTICS_WINDOW
------------------

:Type: Physical
:Default: 0.1
:Unit: hartree
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_OPTICS_WINDOW`

Window of energy around Fermi energy for optical conductivity

.. _dmft-order-proj:

DMFT_ORDER_PROJ
---------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_ORDER_PROJ`

Small number to enforce the orbital order of the NGWFS when the overlap with projectors are identical

.. _dmft-paramagnetic:

DMFT_PARAMAGNETIC
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_PARAMAGNETIC`

Imposes the paramagnetic state in DFT+DMFT

.. _dmft-plot-real-space:

DMFT_PLOT_REAL_SPACE
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_PLOT_REAL_SPACE`

Write out real space DMFT quantities

.. _dmft-points:

DMFT_POINTS
-----------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_POINTS`

Number of DMFT energy points on real or matsubara axis

.. _dmft-purify-sc:

DMFT_PURIFY_SC
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_PURIFY_SC`

Use the purified kernel for DFT_DMFT in the property module

.. _dmft-read:

DMFT_READ
---------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_READ`

Read DMFT data (Green's functions, Hamiltonians, etc.) if they are present

.. _dmft-rotate-green:

DMFT_ROTATE_GREEN
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_ROTATE_GREEN`

Write out the Green function in the rotated local atomic basis

.. _dmft-sc:

DMFT_SC
-------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SC`

if true will run the self consistent ONETEP+DMFT, if false, one shot ONETEP+DMFT is used

.. _dmft-scaling-cutoff:

DMFT_SCALING_CUTOFF
-------------------

:Type: Double-Precision
:Default: 1e-08
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SCALING_CUTOFF`



.. _dmft-scaling-meth:

DMFT_SCALING_METH
-----------------

:Type: Integer
:Default: 4
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SCALING_METH`



.. _dmft-scaling-nmpi:

DMFT_SCALING_NMPI
-----------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SCALING_NMPI`



.. _dmft-scaling-tail:

DMFT_SCALING_TAIL
-----------------

:Type: Double-Precision
:Default: 10.0
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SCALING_TAIL`



.. _dmft-skip-energy:

DMFT_SKIP_ENERGY
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SKIP_ENERGY`

Do not compute the energy along the Newton steepest descent used to find the chemical potential

.. _dmft-smear:

DMFT_SMEAR
----------

:Type: Physical
:Default: 0.00018
:Unit: hartree
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SMEAR`

Smearing (in Ha) for DFT+DMFT

.. _dmft-smear-eta:

DMFT_SMEAR_ETA
--------------

:Type: Physical
:Default: 0.01
:Unit: hartree
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SMEAR_ETA`

Frequency dependent smearing parameter eta (Ha) for DFT+DMFT. See documentation for details of the smearing

.. _dmft-smear-shift:

DMFT_SMEAR_SHIFT
----------------

:Type: Physical
:Default: 0.0
:Unit: hartree
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SMEAR_SHIFT`

Frequency dependent smearing (Ha) for DFT+DMFT

.. _dmft-smear-t:

DMFT_SMEAR_T
------------

:Type: Physical
:Default: 0.008
:Unit: hartree
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SMEAR_T`

Frequency dependent smearing parameter T (Ha) for DFT+DMFT. See documentation for details of the smearing

.. _dmft-smear-w:

DMFT_SMEAR_W
------------

:Type: Physical
:Default: 0.035
:Unit: hartree
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SMEAR_W`

Frequency dependent smearing parameter w (Ha) for DFT+DMFT. See documentation for details of the smearing

.. _dmft-spoil-kernel:

DMFT_SPOIL_KERNEL
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SPOIL_KERNEL`

If false will NOT update LHXC potential

.. _dmft-switch-off-proj-order:

DMFT_SWITCH_OFF_PROJ_ORDER
--------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_SWITCH_OFF_PROJ_ORDER`

For compatibility with older version of ONETEP-DMFT, if true switchesoff the natural order of the projections

.. _dmft-temp:

DMFT_TEMP
---------

:Type: Physical
:Default: -0.01
:Unit: hartree
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_TEMP`

Temperature (in Hartree) for DFT+DMFT

.. _dmft-win:

DMFT_WIN
--------

:Type: Double-Precision
:Default: 0.3
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_WIN`

Window of energies around the chemical potential considered for the Green's  function inversion in DMFT

.. _dmft-write:

DMFT_WRITE
----------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: DMFT
:Search: :searchlink:`DMFT_WRITE`

Write DMFT data (Green's functions, Hamiltonians, etc.)

.. _dos-smear:

DOS_SMEAR
---------

:Type: Physical
:Default: Unknown
:Unit: hartree
:Level: Intermediate
:Group: None
:Search: :searchlink:`DOS_SMEAR`

Half width of smearing Gaussians for DOS

Specifies the Gaussian smearing for the density of states calculatedif properties are requested. If the smearing width is negative, the density of states is not calculated.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DOS_SMEAR [Value] [Unit]

   :Example:

   .. code::

      DOS_SMEAR 7 mRy

.. _do-fandt:

DO_FANDT
--------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`DO_FANDT`

Perform a freeze-and-thaw optimisation of the NGWFs

.. _do-properties:

DO_PROPERTIES
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`DO_PROPERTIES`

Allow calculation of properties

Enables the calculation of properties including: charge and spin densities, electrostatic potential , Mulliken population analysis , canonical orbitals and energies and density of states.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DO_PROPERTIES [Logical]

   :Example:

   .. code::

      DO_PROPERTIES T

.. _do-tddft:

DO_TDDFT
--------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`DO_TDDFT`

Allow Time-Dependent DFT calculation

.. _dx-format:

DX_FORMAT
---------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`DX_FORMAT`

Allow .dx format for plot outputs

Output volumetric data (e.g. charge density, potential, NGWFs, canonical orbitals) in Open DX format . This can be visualized using free software such as OpenDX or VMD .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DX_FORMAT [Logical]

   :Example:

   .. code::

      DX_FORMAT T

.. _dx-format-coarse:

DX_FORMAT_COARSE
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: IO
:Search: :searchlink:`DX_FORMAT_COARSE`

Output only points on the coarse grid

Makes the .dx files (see :ref:`dx-format` ) smaller by outputting only odd points along every axis, discarding even points. This allows for smaller output files, eliminates Gibbs ringing .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DX_FORMAT_COARSE [Logical]

   :Example:

   .. code::

      DX_FORMAT_COARSE T

.. _dx-format-digits:

DX_FORMAT_DIGITS
----------------

:Type: Integer
:Default: 7
:Unit: None
:Level: Intermediate
:Group: IO
:Search: :searchlink:`DX_FORMAT_DIGITS`

Number of significant digits in .dx output

Selects the number of significant digits in .dx file (see :ref:`dx-format` ) output. This allows for smaller files if some precision can be sacrificed, or to increase output precision of need arises.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      DX_FORMAT_DIGITS [Integer]

   :Example:

   .. code::

      DX_FORMAT_DIGITS 12

.. _eda-continuation:

EDA_CONTINUATION
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_CONTINUATION`

Read information for continuation of a previous EDA calculation

.. _eda-deloc:

EDA_DELOC
---------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_DELOC`

List of fragment pairs to calculate delocalisations for

.. _eda-deltadens:

EDA_DELTADENS
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_DELTADENS`

Write the delta densities (electron density differences) of the EDA energy components

.. _eda-frags:

EDA_FRAGS
---------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_FRAGS`

List of the fragment density kernels and NGWFs prefix (e.g. 'frag1' for frag1.dkn and frag1.tightbox_ngwfs)

.. _eda-frag-atoms:

EDA_FRAG_ATOMS
--------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_FRAG_ATOMS`

(Developmental) Fragment to be split for defining bond-splitted fragments in EDA (frag#, atom#(not in use), NGWF#(not in use))

.. _eda-frag-isol-ct:

EDA_FRAG_ISOL_CT
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_FRAG_ISOL_CT`

Calculate delocalisation energies for each fragment pair (state initialised from the frozen stage). NOTE: This calculation also allows relaxation of the surrounding fragments.

.. _eda-frag-isol-pol:

EDA_FRAG_ISOL_POL
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_FRAG_ISOL_POL`

Enables fragment polarisation calculations to be obtained for each fragment independently.

.. _eda-iatm:

EDA_IATM
--------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_IATM`

List of the number atoms in each monomer. Eg. '3 4' would indicate the first 3 atoms in monomer one, and the final 4 atoms in monomer two.

.. _eda-nodiag:

EDA_NODIAG
----------

:Type: Integer
:Default: 3
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_NODIAG`

Set to avoid the EDA diagonalisation bottlenecks. 0=Off 1=Frozen, 2=Polarisation, 3=Frozen and Polarisation.

.. _eda-read-frags:

EDA_READ_FRAGS
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_READ_FRAGS`

Enables the reading of fragments specified using the :ref:`eda-frags` block.

.. _eda-read-super:

EDA_READ_SUPER
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_READ_SUPER`

Enables the reading of supermolecule dkn and NGWFs using the :ref:`eda-super` block.

.. _eda-reset-ngwfs-ct:

EDA_RESET_NGWFS_CT
------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: None
:Group: EDA
:Search: :searchlink:`EDA_RESET_NGWFS_CT`

Resets the NGWFs for the charge transfer stage of the EDA to the initial guess NGWFs.

.. _eda-reset-ngwfs-pol:

EDA_RESET_NGWFS_POL
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: None
:Group: EDA
:Search: :searchlink:`EDA_RESET_NGWFS_POL`

Resets the NGWFs for the (full) polarisation stage of the EDA to the initial guess NGWFs.

.. _eda-split-atoms:

EDA_SPLIT_ATOMS
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_SPLIT_ATOMS`

Enables partitioning of fragments by atom-splitting

.. _eda-super:

EDA_SUPER
---------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_SUPER`

The supermolecule data filename prefix (e.g. 'super1' for super1.dkn_supermolecule and super1.tightbox_ngwfs_supermolecule)

.. _eda-write:

EDA_WRITE
---------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDA
:Search: :searchlink:`EDA_WRITE`

Write EDA continuation data

.. _edft:

EDFT
----

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDFT
:Search: :searchlink:`EDFT`

Use Ensemble-DFT method to optimise the kernel

Enable finite-temperature DFT calculations with the Ensemble-DFT method. Recommended for calculations on metallic systems.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT [Logical]

   :Example:

   .. code::

      EDFT T

.. _edft-commutator-thres:

EDFT_COMMUTATOR_THRES
---------------------

:Type: Physical
:Default: 1e-05
:Unit: hartree
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_COMMUTATOR_THRES`

Convergence threshold for the RMS commutator in :ref:`edft` calculations

Tolerance threshold for the Hamiltonian-density matrix commutator during the :ref:`edft` inner loop.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_COMMUTATOR_THRES [Value] [Unit]

   :Example:

   .. code::

      EDFT_COMMUTATOR_THRES 1.0e-6

.. _edft-electrode-potential:

EDFT_ELECTRODE_POTENTIAL
------------------------

:Type: Physical
:Default: 0.0
:Unit: ha/e
:Level: Intermediate
:Group: EDFT
:Search: :searchlink:`EDFT_ELECTRODE_POTENTIAL`

electrode potential used to set the Fermi level

.. _edft-energy-thres:

EDFT_ENERGY_THRES
-----------------

:Type: Physical
:Default: 0.0001
:Unit: hartree
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_ENERGY_THRES`

Convergence threshold for the energy in :ref:`edft` calculations

Tolerance threshold for the maximum change of the total energy during two consecutive :ref:`edft` inner loop iteratrions.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_ENERGY_THRES [Value] [Unit]

   :Example:

   .. code::

      EDFT_ENERGY_THRES 1.0e-4 eV

.. _edft-entropy-thres:

EDFT_ENTROPY_THRES
------------------

:Type: Physical
:Default: 0.0001
:Unit: hartree
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_ENTROPY_THRES`

Convergence threshold for the entropy in :ref:`edft` calculations

Tolerance threshold for the maximum change of the total entropy during two consecutive :ref:`edft` inner loop iteratrions.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_ENTROPY_THRES [Value] [Unit]

   :Example:

   .. code::

      EDFT_ENTROPY_THRES 1.0e-5 eV

.. _edft-extra-bands:

EDFT_EXTRA_BANDS
----------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_EXTRA_BANDS`

Number of additional MOs with non-zero occupancy in :ref:`edft`

Extra energy bands in :ref:`edft` calculations. If set to 0 or a negative number, the total number of bands is equal to the total number of NGWFs. Set to a positive integer to add more energy bands.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_EXTRA_BANDS [Integer]

   :Example:

   .. code::

      EDFT_EXTRA_BANDS 16

.. _edft-fermi-thres:

EDFT_FERMI_THRES
----------------

:Type: Physical
:Default: 0.001
:Unit: hartree
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_FERMI_THRES`

Convergence threshold for the Fermi level in :ref:`edft` calculations

Tolerance threshold for the maximum change of the Fermi energy during two consecutive :ref:`edft` inner loop

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_FERMI_THRES [Value] [Unit]

   :Example:

   .. code::

      EDFT_FERMI_THRES 1.0e-4 eV

.. _edft-free-energy-thres:

EDFT_FREE_ENERGY_THRES
----------------------

:Type: Physical
:Default: 1e-06
:Unit: hartree
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_FREE_ENERGY_THRES`

Convergence threshold for the free energy in :ref:`edft` calculations

Tolerance threshold for the maximum change of the Helmholtz free energy during two consecutive :ref:`edft` inner loop iteratrions.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_FREE_ENERGY_THRES [Value] [Unit]

   :Example:

   .. code::

      EDFT_FREE_ENERGY_THRES 1.0e-4 eV

.. _edft-grand-canonical:

EDFT_GRAND_CANONICAL
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDFT
:Search: :searchlink:`EDFT_GRAND_CANONICAL`

use grand canonical ensemble in ensemble DFT

.. _edft-ham-diis-size:

EDFT_HAM_DIIS_SIZE
------------------

:Type: Integer
:Default: 10
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`EDFT_HAM_DIIS_SIZE`

Max number of Hamiltonians saved during :ref:`edft` Pulay DIIS.

.. _edft-init-maxit:

EDFT_INIT_MAXIT
---------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`EDFT_INIT_MAXIT`

Number of iterations of Ensemble DFT (cubic scaling) to run before LNV.

Maximum number of inner loop iterations with the :ref:`edft` method to be performed at the start of the calculation, intended to solve issues with incorrect occupancy schemes after initialisation via Palser Manolopoulos.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_INIT_MAXIT [Integer]

   :Example:

   .. code::

      EDFT_INIT_MAXIT 5

.. _edft-maxit:

EDFT_MAXIT
----------

:Type: Integer
:Default: 10
:Unit: None
:Level: Intermediate
:Group: EDFT
:Search: :searchlink:`EDFT_MAXIT`

Maximum number of :ref:`edft` iterations to optimise the kernel

Maximum number of inner loop iterations in calculations with the :ref:`edft` method.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_MAXIT [Integer]

   :Example:

   .. code::

      EDFT_MAXIT 5

.. _edft-max-step:

EDFT_MAX_STEP
-------------

:Type: Double-Precision
:Default: 1.0
:Unit: None
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_MAX_STEP`

Maximum step during :ref:`edft` line search

Maximum step during the :ref:`edft` inner loop line search.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_MAX_STEP [Value]

   :Example:

   .. code::

      EDFT_MAX_STEP 0.8

.. _edft-nelec-thres:

EDFT_NELEC_THRES
----------------

:Type: Double-Precision
:Default: 1e-06
:Unit: None
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_NELEC_THRES`

Convergence threshold for number of electrons in grand canonical edft

.. _edft-reference-potential:

EDFT_REFERENCE_POTENTIAL
------------------------

:Type: Physical
:Default: Unknown
:Unit: ha
:Level: Intermediate
:Group: EDFT
:Search: :searchlink:`EDFT_REFERENCE_POTENTIAL`

electrochemical potential of reference electrode

.. _edft-rms-gradient-thres:

EDFT_RMS_GRADIENT_THRES
-----------------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_RMS_GRADIENT_THRES`

Convergence threshold for the RMS gradient in :ref:`edft` calculations

Tolerance threshold for the maximum occupancies RMS gradient during the :ref:`edft` inner loop.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_RMS_GRADIENT_THRES [Value]

   :Example:

   .. code::

      EDFT_RMS_GRADIENT_THRES 1.0e-5

.. _edft-round-evals:

EDFT_ROUND_EVALS
----------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_ROUND_EVALS`

Round :ref:`edft` eigenvalues to N decimal figures

Round up the energy eigenvalues to n decimal positions. It helps in calculations where there is a numerical error arising from the grid representation of the NGWFs. If set to a negative number, this directive is ignored.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_ROUND_EVALS [Integer]

   :Example:

   .. code::

      EDFT_ROUND_EVALS 5

.. _edft-smearing-scheme:

EDFT_SMEARING_SCHEME
--------------------

:Type: String
:Default: 'fermidirac'
:Unit: None
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_SMEARING_SCHEME`

Occupancy smearing scheme in :ref:`edft` calculations

.. _edft-smearing-width:

EDFT_SMEARING_WIDTH
-------------------

:Type: Physical
:Default: 0.003166811429
:Unit: hartree
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_SMEARING_WIDTH`

Occupancy smearing width in :ref:`edft` calculations

Occupation smearing width in :ref:`edft` calculations, based on the Fermi-Dirac distribution.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_SMEARING_WIDTH [Value] [Unit]

   :Example:

   .. code::

      EDFT_SMEARING_WIDTH 800 K (sets the electronic temperature to 800 degree Kelvin)

.. _edft-spin-fix:

EDFT_SPIN_FIX
-------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Intermediate
:Group: EDFT
:Search: :searchlink:`EDFT_SPIN_FIX`

Number of iterations to fix the spin, negative is forever

Number of NGWF CG iterations to hold the spin fixed. If negative, hold forever. (Default: -1)

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_SPIN_FIX [Integer]

   :Example:

   .. code::

      EDFT_SPIN_FIX 4

.. _edft-trial-step:

EDFT_TRIAL_STEP
---------------

:Type: Double-Precision
:Default: -1.0
:Unit: None
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_TRIAL_STEP`

User input mixing parameter - replaces default line search.

.. _edft-update-scheme:

EDFT_UPDATE_SCHEME
------------------

:Type: String
:Default: 'DAMP_FIXPOINT'
:Unit: None
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_UPDATE_SCHEME`

Define the update scheme used in the inner loop of EDFT.

.. _edft-write-occ:

EDFT_WRITE_OCC
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: EDFT
:Search: :searchlink:`EDFT_WRITE_OCC`

Generate file with smeared occupancies

Write the occupancies and the energy levels on disk. If set to true, this directive will generate a .occ file.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EDFT_WRITE_OCC [Logical]

   :Example:

   .. code::

      EDFT_WRITE_OCC T

.. _efield-calculate:

EFIELD_CALCULATE
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`EFIELD_CALCULATE`

Calculate and output electric field during properties

.. _efield-origin:

EFIELD_ORIGIN
-------------

:Type: String
:Default: '0.0 0.0 0.0'
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`EFIELD_ORIGIN`

Cartesian coordinates of the origin of the sawtooth potential

.. _eigensolver-abstol:

EIGENSOLVER_ABSTOL
------------------

:Type: Double-Precision
:Default: 1e-13
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`EIGENSOLVER_ABSTOL`

Precision to which the parallel eigensolver will calculate the eigenvalues

Indicates the precision to which the ScaLapack PDSYGVX eigensolver will resolve the eigenvalues of a matrix. Active only if ONETEP is compiled against ScaLapack. Set to a negative number to use ScaLAPACK default.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EIGENSOLVER_ABSTOL [Value]

   :Example:

   .. code::

      EIGENSOLVER_ABSTOL 1.0e-5

.. _eigensolver-orfac:

EIGENSOLVER_ORFAC
-----------------

:Type: Double-Precision
:Default: 1e-08
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`EIGENSOLVER_ORFAC`

Precision to which the parallel eigensolver will orthogonalise evecs

Indicates the precision to which the ScaLapack PDSYGVX eigensolver will reorthonormalise the eigenvectors of a matrix. Active only if ONETEP is compiled against ScaLapack. Set to a negative number to tell ScaLAPACK to not to perform any kind of orthonormalisation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EIGENSOLVER_ORFAC [Value]

   :Example:

   .. code::

      eigensolver_abstol 1.0e-3

.. _eld-calculate:

ELD_CALCULATE
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: ELD
:Search: :searchlink:`ELD_CALCULATE`

Calculate electron localisation descriptors

Calculate electron localisation descriptors.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ELD_CALCULATE [Logical]

   :Example:

   .. code::

      ELD_CALCULATE T

.. _eld-function:

ELD_FUNCTION
------------

:Type: String
:Default: 'ELF'
:Unit: None
:Level: Basic
:Group: ELD
:Search: :searchlink:`ELD_FUNCTION`

Choose which electron localisation descriptor to use during the properties calculation: ELF, LOL or DORI

Choose which electron localisation descriptor to use during the properties calculation, either ELF or LOL.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ELD_FUNCTION [Text]

   :Example:

   .. code::

      ELD_FUNCTION ELF

.. _elec-cg-max:

ELEC_CG_MAX
-----------

:Type: Integer
:Default: 5
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`ELEC_CG_MAX`

Number of NGWF iterations to reset CG

Specifies the maximum number of NGWF conjugate gradients iterations between resets.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ELEC_CG_MAX [Integer]

   :Example:

   .. code::

      ELEC_CG_MAX 0 ; steepest descents

.. _elec-energy-tol:

ELEC_ENERGY_TOL
---------------

:Type: Physical
:Default: -0.001
:Unit: hartree
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`ELEC_ENERGY_TOL`

Tolerance on total energy change during NGWF optimisation

Convergence criterion for minimisation of electronic energy: Energy change per NGWF optimisation iteration must be less than this amount PER ATOM before the calculation is regarded as converged. Ignored if negative.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ELEC_ENERGY_TOL [Value] [Unit]

   :Example:

   .. code::

      ELEC_ENERGY_TOL 0.00001 eV

.. _elec-force-tol:

ELEC_FORCE_TOL
--------------

:Type: Physical
:Default: -0.001
:Unit: ha/bohr
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`ELEC_FORCE_TOL`

Tolerance on max force change during NGWF optimisation

Convergence criterion for minimisation of electronic energy: Maximum change in any component of the forces from NGWF optimisation iteration to the next must be less than this amount before the calculation is regarded as converged. Ignored if negative.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ELEC_FORCE_TOL [Value] [Unit]

   :Example:

   .. code::

      ELEC_FORCE_TOL 0.01 "eV/ang"

.. _embed-debug:

EMBED_DEBUG
-----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: I
:Search: :searchlink:`EMBED_DEBUG`

Verbose printing for embedding if debugging

.. _emft-lnv-steps:

EMFT_LNV_STEPS
--------------

:Type: Integer
:Default: 10
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`EMFT_LNV_STEPS`

Number of LNV iterations during EMFT kernel optimisation

.. _energy-components-interval:

ENERGY_COMPONENTS_INTERVAL
--------------------------

:Type: Integer
:Default: 5
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`ENERGY_COMPONENTS_INTERVAL`

How often to print out energy components

.. _esdf-dump:

ESDF_DUMP
---------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: IO
:Search: :searchlink:`ESDF_DUMP`

Dump all runtime parameters at startup

.. _etrans-bulk:

ETRANS_BULK
-----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: ETRANS
:Search: :searchlink:`ETRANS_BULK`

Compute electronic transport coefficients (Bulk config)

Compute the bulk transmission coefficients of the individual leads defined in ETRANS_LEADS.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_BULK [Logical]

   :Example:

   .. code::

      ETRANS_BULK T

.. _etrans-calculate-lead-mu:

ETRANS_CALCULATE_LEAD_MU
------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: ETRANS
:Search: :searchlink:`ETRANS_CALCULATE_LEAD_MU`

Calculate the lead chemical potentials

Calculate the lead chemical potentials via a non-self consistent band structure calculation. The band structure for each lead is written to a .bands file. Defaults to TRUE is :ref:`etrans-eref-method` = LEADS.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_CALCULATE_LEAD_MU [Logical]

   :Example:

   .. code::

      ETRANS_CALCULATE_LEAD_MU T

.. _etrans-ecmplx:

ETRANS_ECMPLX
-------------

:Type: Physical
:Default: 1e-06
:Unit: hartree
:Level: Intermediate
:Group: ETRANS
:Search: :searchlink:`ETRANS_ECMPLX`

Imaginary part of the energy

Small imaginary part added to the energy in order to impose the appropriate boundary condition to the computed retarded Green's function. This parameter should theoretically tends toward zero. If set too small, instabilities may occur and the calculation of the Green's function may fail.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_ECMPLX [Value] [Unit]

   :Example:

   .. code::

      ETRANS_ECMPLX 0.00001 hartree

.. _etrans-emax:

ETRANS_EMAX
-----------

:Type: Physical
:Default: 0.2
:Unit: hartree
:Level: Intermediate
:Group: ETRANS
:Search: :searchlink:`ETRANS_EMAX`

Highest energy for the calculation of transmission coefficients

Highest energy for the calculation of the transmission coefficients (defined with respect to the reference level). Transmission coefficients are calculated in the range ETRANS_MIN <= E - :ref:`etrans-eref` <= ETRANS_MAX .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_EMAX [Value] [Unit]

   :Example:

   .. code::

      ETRANS_EMAX 0.2 hartree

.. _etrans-emin:

ETRANS_EMIN
-----------

:Type: Physical
:Default: -0.2
:Unit: hartree
:Level: Intermediate
:Group: ETRANS
:Search: :searchlink:`ETRANS_EMIN`

Lowest energy for the calculation of transmission coefficients

Lowest energy for the calculation of the transmission coefficients (defined with respect to the reference level). Transmission coefficients are calculated in the range ETRANS_MIN <= E - :ref:`etrans-eref` <= ETRANS_MAX .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_EMIN [Value] [Unit]

   :Example:

   .. code::

      ETRANS_EMIN -0.2 hartree

.. _etrans-enum:

ETRANS_ENUM
-----------

:Type: Integer
:Default: 50
:Unit: None
:Level: Intermediate
:Group: ETRANS
:Search: :searchlink:`ETRANS_ENUM`

Number of energy points for the calculation of transmission coefficients

Number of energy points equally spaced between :ref:`etrans-emin` and :ref:`etrans-emax` for the calculation of the electronic transmission coefficients as a function of the energy.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_ENUM [Integer]

   :Example:

   .. code::

      ETRANS_ENUM 100

.. _etrans-eref:

ETRANS_EREF
-----------

:Type: Physical
:Default: 0.0
:Unit: hartree
:Level: Basic
:Group: ETRANS
:Search: :searchlink:`ETRANS_EREF`

Reference energy for electronic transport calculation

If :ref:`etrans-eref-method` = REFERENCE, this defines the reference energy about which transmission is calculated. Transmission coefficients are calculated in the range ETRANS_MIN <= E - :ref:`etrans-eref` <= ETRANS_MAX . If any other :ref:`etrans-eref-method` is chosen, this energy is determined automatically according to that method.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_EREF [Value] [Unit]

   :Example:

   .. code::

      ETRANS_EREF 0.0 hartree

.. _etrans-eref-method:

ETRANS_EREF_METHOD
------------------

:Type: String
:Default: 'LEADS'
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`ETRANS_EREF_METHOD`

The method used to determine the reference energy for electronic transport

The method to determine the reference energy for the calculation of transmission coefficients. Options are: LEADS (take the average chemical potential of the leads), REFERENCE (explicitly set the reference energy using :ref:`etrans-eref` ), DIAG (use the mid-gap level of the entire system). LEADS and REFERENCE are independent of system size. DIAG scales cubically with system size, and will be unsuitable for very large systems. (Calculating the Green's function currently scales cubically also, however a linear-scaling recursive algorithm is in development.)

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_EREF_METHOD [Text]

   :Example:

   .. code::

      ETRANS_EREF_METHOD REFERENCE

.. _etrans-lcr:

ETRANS_LCR
----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: ETRANS
:Search: :searchlink:`ETRANS_LCR`

Compute electronic transport coefficients (LCR config)

Compute the 'Left-Centre-Right' transmission coefficients between all leads defined in :ref:`etrans-leads` . Transmission occurs through the device region defined in :ref:`etrans-bulk` .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_LCR [Logical]

   :Example:

   .. code::

      ETRANS_LCR T

.. _etrans-leads:

ETRANS_LEADS
------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: ETRANS
:Search: :searchlink:`ETRANS_LEADS`

Define the transport leads

Defines the atoms that form the leads for the calculation of the transport coefficients. Each line of the block defines a lead, consisting of four numbers. The first two numbers define the first and last atom contained within the lead; the second two numbers define the first and last atom that form the principle layer for that lead. The leads should form a bulk periodic unit cell. The atoms in the principle layer should be a periodic repeat, in the same atomic ordering, as the lead atoms. How strictly this is enforced is controlled by :ref:`etrans-lead-disp-tol` . The principle layer should define the the only set of atoms that the lead interacts with; the lead interacts with the central region through the principle layer. A lead should not directly interact with any other lead. The atoms are ordered by their order in the input file. This block is mandatory when :ref:`etrans-lcr` and/or :ref:`etrans-bulk` is set to true.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK ETRANS_LEADS
      lead_start lead_end principle_layer_start principle_layer_end
       lead_start lead_end principle_layer_start principle_layer_end
       ...
       %ENDBLOCK ETRANS_LEADS

   :Example:

   .. code::

      In this example, three leads are defined containing 36, 60 and 20 atoms.
      
      
      
      %BLOCK ETRANS_LEADS
        037 072 073 108
       241 300 301 360
       601 640 561 600
       %ENDBLOCK ETRANS_LEADS

.. _etrans-lead-disp-tol:

ETRANS_LEAD_DISP_TOL
--------------------

:Type: Physical
:Default: 1.0
:Unit: bohr
:Level: Expert
:Group: ETRANS
:Search: :searchlink:`ETRANS_LEAD_DISP_TOL`

The maximum acceptable difference in atomic positions between a lead and its first principle layer

The maximum acceptable difference in the translation vectors between the atoms in a lead, and the corresponding atoms in the lead principle layer. If the principle layer geometry is an exact repeat of the lead geometry, the translation vectors will all be identical. This parameter allows for this criterion to be relaxed.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_LEAD_DISP_TOL [Value] [Unit]

   :Example:

   .. code::

      ETRANS_LEAD_DISP_TOL 1.0 bohr

.. _etrans-lead-nkpoints:

ETRANS_LEAD_NKPOINTS
--------------------

:Type: Integer
:Default: 32
:Unit: None
:Level: Intermediate
:Group: ETRANS
:Search: :searchlink:`ETRANS_LEAD_NKPOINTS`

Number of kpoints to use to determine lead chemical potential

The number of kpoints the lead band structure is calculated for. The kpoints are equally spaced between [0,pi/a].

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_LEAD_NKPOINTS [Integer]

   :Example:

   .. code::

      ETRANS_LEAD_NKPOINTS 100

.. _etrans-lead-size-check:

ETRANS_LEAD_SIZE_CHECK
----------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: ETRANS
:Search: :searchlink:`ETRANS_LEAD_SIZE_CHECK`

Check if leads define a full principle layer

.. _etrans-num-eigchan:

ETRANS_NUM_EIGCHAN
------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Basic
:Group: ETRANS
:Search: :searchlink:`ETRANS_NUM_EIGCHAN`

The number of transmission eigenchannels to calculate

.. _etrans-plot-eigchan:

ETRANS_PLOT_EIGCHAN
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: ETRANS
:Search: :searchlink:`ETRANS_PLOT_EIGCHAN`

Plot the transmission eigenchannels defined in etrans_eigenchannel_energies block

.. _etrans-plot-eigchan-energies:

ETRANS_PLOT_EIGCHAN_ENERGIES
----------------------------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: ETRANS
:Search: :searchlink:`ETRANS_PLOT_EIGCHAN_ENERGIES`

The energies at which the transmission eigenchannels are to be plotted

.. _etrans-same-leads:

ETRANS_SAME_LEADS
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: ETRANS
:Search: :searchlink:`ETRANS_SAME_LEADS`

Use same description for all leads

Use the same self energy for all leads. If all leads are identical, this may give a very small computational saving. Warning: this may still be a bad approximation for leads with the same geometry.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_SAME_LEADS [Logical]

   :Example:

   .. code::

      ETRANS_SAME_LEADS T

.. _etrans-seed-lead:

ETRANS_SEED_LEAD
----------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Expert
:Group: ETRANS
:Search: :searchlink:`ETRANS_SEED_LEAD`

The seed lead for determining the tri-diagonal partitioning

.. _etrans-setup:

ETRANS_SETUP
------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: ETRANS
:Search: :searchlink:`ETRANS_SETUP`

Transport setup description

Defines the atoms used for the calculation of the transport coefficients. The block should contain a single line giving the index of the first and last atom contained within the transport calculation. All atoms between these indices (inclusive) are included, with all other atoms considered as buffer and ignored. These indices must contain all the leads, and the central scattering region. The atoms are ordered by their order in the input file. This block is mandatory when :ref:`etrans-lcr` is set to true.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK ETRANS_SETUP
      atom_start atom_stop
      %ENDBLOCK ETRANS_SETUP

   :Example:

   .. code::

      In this example, all atoms between 37 and 640 will be used.
      All other atoms are considered as buffer atoms.
      Note: This syntax is not compatible with versions earlier than ONETEP 3.3.4
      
      
      
      %BLOCK ETRANS_SETUP
        037 640
       %ENDBLOCK ETRANS_SETUP

.. _etrans-write-hs:

ETRANS_WRITE_HS
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: ETRANS
:Search: :searchlink:`ETRANS_WRITE_HS`

Write hamiltonian corresponding to transport setup

Write the lead and LCR Hamiltonian and Overlap matrices to disk for further analysis. The binary file format description is given in etrans_mod.F90. Warning: these matrices can be very large.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ETRANS_WRITE_HS [Logical]

   :Example:

   .. code::

      ETRANS_WRITE_HS T

.. _etrans-write-xyz:

ETRANS_WRITE_XYZ
----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: ETRANS
:Search: :searchlink:`ETRANS_WRITE_XYZ`

Write the lead and device co-ordinates to .xyz files

.. _even-psinc-grid:

EVEN_PSINC_GRID
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`EVEN_PSINC_GRID`

Force even number of points in simcell psinc grid

Force even number of points in the simulation-cell psinc grid.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EVEN_PSINC_GRID [Logical]

   :Example:

   .. code::

      EVEN_PSINC_GRID T

.. _exact-lnv:

EXACT_LNV
---------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`EXACT_LNV`

Use original LNV algorithm

Specifies that the normalization constraint on the density matrix should be imposed exactly, using the purified density kernel (as in the original Li-Nunes-Vanderbilt algorithm [Phys. Rev. B47, 10891 (1993)]) rather than the auxiliary kernel (as in the Millam-Scuseria variant [J. Chem. Phys.106, 5569 (1997)]).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EXACT_LNV [Logical]

   :Example:

   .. code::

      EXACT_LNV F

.. _extend-ngwf:

EXTEND_NGWF
-----------

:Type: String
:Default: 'F F F'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`EXTEND_NGWF`

directions along which NGWFs are extended

.. _external-bc-from-cube:

EXTERNAL_BC_FROM_CUBE
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`EXTERNAL_BC_FROM_CUBE`

Read external potential for boundary conditions from cube file

If this flag is True, external boundary conditions for the electrostatic potential are imposed according to the contents of the cube file rootname_POT_EXT_BC.cube. This cube file needs to match the dimensions of the FD multigrid (see the implicit solvation documentation for more details).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EXTERNAL_BC_FROM_CUBE [Logical]

   :Example:

   .. code::

      EXTERNAL_BC_FROM_CUBE : T

.. _external-pressure:

EXTERNAL_PRESSURE
-----------------

:Type: Physical
:Default: 0.0
:Unit: ha/bohr**3
:Level: Basic
:Group: None
:Search: :searchlink:`EXTERNAL_PRESSURE`

External applied pressure

Value of the input pressure Pin in the electronic enthalpy functional H=U+PV where U is the total Kohn-Sham internal energy of the system and V is a volume definition based on an electronic-density isosurface (determined by the :ref:`smoothing-factor` and :ref:`isosurface-cutoff` keywords). The electronic enthalpy can be minimized self-consistently during geometry relaxation or MD runs and allows for constant pressure simulation of finite systems [Cococcioni et al,  Phys. Rev. Lett.94, 145501 (2005)]. The implementation is described in more detail in [Corsini et al, J. Chem. Phys. 2013, 139, 084117].

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EXTERNAL_PRESSURE [Physical]

   :Example:

   .. code::

      EXTERNAL_PRESSURE 1.0 gpa

.. _extra-n-sw:

EXTRA_N_SW
----------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`EXTRA_N_SW`

Maximum number of zeros of the sph Bessel function for the SW

Generates extra spherical waves for the NGWFs representation. The extra SW will suffer of aliasing as their frequency is higher than the maximum plane waves basis set given by the kinetic cut-off.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      EXTRA_N_SW [Integer]

   :Example:

   .. code::

      EXTRA_N_SW -5

.. _faster-ewald:

FASTER_EWALD
------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FASTER_EWALD`

Toggle between original O(N^2) and faster O(N) recip space Ewald sum.

.. _fast-dense-to-sparse:

FAST_DENSE_TO_SPARSE
--------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_DENSE_TO_SPARSE`

Use newer, better-scaling dense to sparse conversions?

.. _fast-density:

FAST_DENSITY
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_DENSITY`

Use newer, faster method for calculating density?

.. _fast-density-batch-size:

FAST_DENSITY_BATCH_SIZE
-----------------------

:Type: Integer
:Default: 64
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_DENSITY_BATCH_SIZE`

Batch size in fast density. Lower conserves CPU & GPU RAM.

.. _fast-density-elec-energy-tol:

FAST_DENSITY_ELEC_ENERGY_TOL
----------------------------

:Type: Double-Precision
:Default: 1e-50
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_DENSITY_ELEC_ENERGY_TOL`

Energy per atom threshold for turning off fast density.

.. _fast-density-fast-ngwfs:

FAST_DENSITY_FAST_NGWFS
-----------------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_DENSITY_FAST_NGWFS`

Use faster (rod) NGWF representation in fast density?

.. _fast-density-flatten-method:

FAST_DENSITY_FLATTEN_METHOD
---------------------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_DENSITY_FLATTEN_METHOD`

MPI flattening method to use for fast density

.. _fast-density-gpu-copy-ahead:

FAST_DENSITY_GPU_COPY_AHEAD
---------------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_DENSITY_GPU_COPY_AHEAD`

Copy stuff to the GPU ahead of time for performance?

.. _fast-density-method:

FAST_DENSITY_METHOD
-------------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_DENSITY_METHOD`

Which of the two methods to use for fast density?

.. _fast-density-off-for-last:

FAST_DENSITY_OFF_FOR_LAST
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_DENSITY_OFF_FOR_LAST`

Switch to old density method for last energy eval?

.. _fast-locpot-int:

FAST_LOCPOT_INT
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_LOCPOT_INT`

Use newer, faster method for calc. locpot integrals?

.. _fast-locpot-int-fast-ngwfs:

FAST_LOCPOT_INT_FAST_NGWFS
--------------------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_LOCPOT_INT_FAST_NGWFS`

Use faster (rod) NGWF representation in fast locpot int?

.. _fast-ngwfs:

FAST_NGWFS
----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_NGWFS`

Use faster (rod) NGWF representation wherever possible?

.. _fast-ngwf-gradient:

FAST_NGWF_GRADIENT
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_NGWF_GRADIENT`

Use newer, faster method for calculating NGWF gradient?

.. _fast-ngwf-gradient-fast-ngwfs:

FAST_NGWF_GRADIENT_FAST_NGWFS
-----------------------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_NGWF_GRADIENT_FAST_NGWFS`

Use faster (rod) NGWF representation in fast NGWF grad?

.. _fast-sparse-to-dense:

FAST_SPARSE_TO_DENSE
--------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FAST_SPARSE_TO_DENSE`

Use newer, better-scaling sparse to dense conversions?

.. _ff:

FF
--

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: FORCE_FIELD
:Search: :searchlink:`FF`

Perform a Force Field calculation?

.. _fftbox-batch-size:

FFTBOX_BATCH_SIZE
-----------------

:Type: Integer
:Default: 16
:Unit: None
:Level: Expert
:Group: THREADS
:Search: :searchlink:`FFTBOX_BATCH_SIZE`

Number of NGWFs in fftbox batches

Number of NGWFs in each batch of fftboxes.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      FFTBOX_BATCH_SIZE [Int]

   :Example:

   .. code::

      FFTBOX_BATCH_SIZE 8

.. _fftbox-pref:

FFTBOX_PREF
-----------

:Type: String
:Default: '0 0 0'
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`FFTBOX_PREF`

Preferred FFT box dimensions

Specifies a size for the FFT-box that is preferable to the smallest possible size that would normally be chosen (e.g. if the FFT library on a particular machine favours certain sizes). The FFT-box is specified by three integers (which must all be odd) that give the number of coarse grid points in thea1,a2anda3directions respectively.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      FFTBOX_PREF [Text]

   :Example:

   .. code::

      FFTBOX_PREF 65 65 65

.. _ff-model:

FF_MODEL
--------

:Type: String
:Default: ''
:Unit: None
:Level: Expert
:Group: FORCE_FIELD
:Search: :searchlink:`FF_MODEL`

FF model type  options: QUIP

.. _fine-grid-scale:

FINE_GRID_SCALE
---------------

:Type: Double-Precision
:Default: 2.0
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`FINE_GRID_SCALE`

Ratio of size of fine grid to standard grid

Specifies the spacing of the fine grid as a multiple of the spacing of the standard grid (which is determined by psinc_spacing or by cutoff_energy).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      FINE_GRID_SCALE [Real]

   :Example:

   .. code::

      FINE_GRID_SCALE 4.0

.. _finite-difference-order:

FINITE_DIFFERENCE_ORDER
-----------------------

:Type: Integer
:Default: Unknown
:Unit: None
:Level: Intermediate
:Group:  FD
:Search: :searchlink:`FINITE_DIFFERENCE_ORDER`

Order of finite differences to use outside of high-order defect correction, e.g. for computing the electric field in open boundary conditions.

.. _foe:

FOE
---

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDFT
:Search: :searchlink:`FOE`

Use the Fermi Operator expansion to evaluate density kernels

Enable calculation of the density kernel with a Fermi Operator Expansion approach in finite-temperature DFT calculations with the Ensemble-DFT method. This method is recommended when the calculation contains more than ~1000 atoms. :ref:`edft` should also be enabled.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      FOE [Logical]

   :Example:

   .. code::

      FOE T

.. _foe-avoid-inversions:

FOE_AVOID_INVERSIONS
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`FOE_AVOID_INVERSIONS`

Avoid performing any inversions or using any inverses in the :ref:`foe`

In the :ref:`foe` method, several matrix inversions are necessary to calculate the finite temperature density kernel. If this parameter is enabled, the matrix solves are instead approximated by Chebyshev expansions. This may be more accurate with a given sparsity pattern, but is likely to be slightly slower than calculating the inverses iteratively.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      FOE_AVOID_INVERSIONS [Logical]

   :Example:

   .. code::

      FOE_AVOID_INVERSIONS T

.. _foe-cheby-thres:

FOE_CHEBY_THRES
---------------

:Type: Double-Precision
:Default: 1e-09
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`FOE_CHEBY_THRES`

The maximum error threshold on the Chebyshev expansions in the :ref:`foe`

When the :ref:`foe` method builds up an approximation for the density kernel in powers of the Hamiltonian matrix, the maximum term in the Chebyshev expansion is determined by this parameter.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      FOE_CHEBY_THRES [Real]

   :Example:

   .. code::

      FOE_CHEBY_THRES 1.0e-10

.. _foe-check-entropy:

FOE_CHECK_ENTROPY
-----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`FOE_CHECK_ENTROPY`

Validate the :ref:`foe` entropy approximation against a simple  quadratic form

In the :ref:`foe` method, the entropy matrix is also calculated as an expansion (in powers of the density kernel) to calculate the entropy itself. This expansion is prone to divergence, so to check for this, and to correct it if it happens, the result is checked against a simple quadratic approximation to the entropy matrix which cannot diverge.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      FOE_CHECK_ENTROPY [Logical]

   :Example:

   .. code::

      FOE_CHECK_ENTROPY T

.. _foe-entropy-approx:

FOE_ENTROPY_APPROX
------------------

:Type: String
:Default: 'REFINED'
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`FOE_ENTROPY_APPROX`

FOE entropy approximation. REFINED=default. Options: NONE QUAD GOOD or REFINED .

.. _foe-mu-tol:

FOE_MU_TOL
----------

:Type: Physical
:Default: 1e-07
:Unit: hartree
:Level: Expert
:Group: None
:Search: :searchlink:`FOE_MU_TOL`

Tolerance for stopping in :ref:`foe` chemical potential search.

The performance of the :ref:`foe` method is affected strongly by how accurately the chemical potential is determined. This parameter should be tuned by the user to find an accurate energy, while minimising the number of iterations in FOE.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      FOE_MU_TOL [Value] [Unit]

   :Example:

   .. code::

      FOE_MU_TOL 1.0e-9 hartree

.. _foe-test-sparsity:

FOE_TEST_SPARSITY
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDFT
:Search: :searchlink:`FOE_TEST_SPARSITY`

Test the quality of the H^2 sparsity pattern for K in :ref:`foe`

If using the AQuA-FOE method, the sparsity pattern is mainly determined by the NGWF radii. To determine the accuracy of this approximation, this parameter can be enabled to print out an estimate.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      FOE_TEST_SPARSITY [Value]

   :Example:

   .. code::

      FOE_TEST_SPARSITY F hartree

.. _forces-output-detail:

FORCES_OUTPUT_DETAIL
--------------------

:Type: String
:Default: 'DEFAULT'
:Unit: None
:Level: Basic
:Group: GENERAL
:Search: :searchlink:`FORCES_OUTPUT_DETAIL`

Level of output detail for forces: BRIEF, NORMAL, VERBOSE, PROLIX

.. _freeze-envir-ngwfs:

FREEZE_ENVIR_NGWFS
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FREEZE_ENVIR_NGWFS`

Never optimise the environment NGWFs

.. _freeze-switch-steps:

FREEZE_SWITCH_STEPS
-------------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`FREEZE_SWITCH_STEPS`

No. of CG steps to perform before switching F+T

.. _full-rand-ngwf:

FULL_RAND_NGWF
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`FULL_RAND_NGWF`

request NGWFs initialised with random values

.. _geometry:

GEOMETRY
--------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: CELLDATA
:Search: :searchlink:`GEOMETRY`

input geometry

.. _geom-backup-iter:

GEOM_BACKUP_ITER
----------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Intermediate
:Group: GEOM
:Search: :searchlink:`GEOM_BACKUP_ITER`

Number of geometry optimisation iterations between backups of all data for continuation

Specifies the backup frequency for geometry optimisation. If the input filename is rootname.dat then the backup filename is rootname.continuation .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_BACKUP_ITER [Integer]

   :Example:

   .. code::

      GEOM_BACKUP_ITER 5

.. _geom-continuation:

GEOM_CONTINUATION
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: GEOM
:Search: :searchlink:`GEOM_CONTINUATION`

Read information for continuation of a previous geometry optimisation

Continue a geometry optimization from a previous run using the .continuation backup file.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_CONTINUATION [Logical]

   :Example:

   .. code::

      GEOM_CONTINUATION T

.. _geom-convergence-win:

GEOM_CONVERGENCE_WIN
--------------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Intermediate
:Group: GEOM
:Search: :searchlink:`GEOM_CONVERGENCE_WIN`

Geometry optimization convergence tolerance window. The geometry optimization convergence criteria must all be met for geom_convergence_win iterations before acceptance

Specifies the number of consecutive iterations during which the convergence criteria must be met.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_CONVERGENCE_WIN [Integer]

   :Example:

   .. code::

      GEOM_CONVERGENCE_WIN 3

.. _geom-disp-tol:

GEOM_DISP_TOL
-------------

:Type: Physical
:Default: 0.005
:Unit: bohr
:Level: Intermediate
:Group: GEOM
:Search: :searchlink:`GEOM_DISP_TOL`

Geometry optimization displacement convergence tolerance

Specifies atomic displacement tolerance used as one of the criteria for convergence of geometry optimization. The positions of all atoms must change by less than this tolerance to satisfy this criterion.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_DISP_TOL [Value] [Unit]

   :Example:

   .. code::

      GEOM_DISP_TOL 1.0e-4 nm

.. _geom-energy-tol:

GEOM_ENERGY_TOL
---------------

:Type: Physical
:Default: 1e-06
:Unit: hartree
:Level: Intermediate
:Group: GEOM
:Search: :searchlink:`GEOM_ENERGY_TOL`

Geometry optimization energy convergence tolerance. The difference between max and min energies over geom_convergence_win iterations must be less than this

Specifies the tolerance for enthalpy per atom over the convergence window as a criterion for geometry optimization convergence.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_ENERGY_TOL [Value] [Unit]

   :Example:

   .. code::

      GEOM_ENERGY_TOL 0.2 meV

.. _geom-force-tol:

GEOM_FORCE_TOL
--------------

:Type: Physical
:Default: 0.002
:Unit: ha/bohr
:Level: Intermediate
:Group: GEOM
:Search: :searchlink:`GEOM_FORCE_TOL`

Geometry optimization force convergence tolerance

Specifies the tolerance for maximum atomic force as a criterion for geometry optimization convergence. Note that units involving a forward slash (/) must be quoted as in the example below.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_FORCE_TOL [Value] [Unit]

   :Example:

   .. code::

      GEOM_FORCE_TOL 0.1 "ev/ang"

.. _geom-frequency-est:

GEOM_FREQUENCY_EST
------------------

:Type: Physical
:Default: 0.0076
:Unit: hartree
:Level: Intermediate
:Group: GEOM
:Search: :searchlink:`GEOM_FREQUENCY_EST`

The estimated average phonon frequency at the gamma point

Specifies the estimated average phonon frequency (as an energy) used to initialize the inverse Hessian matrix for geometry optimization.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_FREQUENCY_EST [Value] [Unit]

   :Example:

   .. code::

      GEOM_FREQUENCY_EST 0.2 eV

.. _geom-lbfgs:

GEOM_LBFGS
----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_LBFGS`

Whether to perform LBFGS rather than BFGS in a Geometry Optimization

If the history length (GEOM_LBFGS_MAX_UPDATES) is set to 0 then LBFGS will perform a geometry optimisation equivalent to the BFGS method. If combined with a limited history length, however, it will store only the latest number of history vectors of length nDOF (number of degrees of freedom) rather than nDOF^2 of them. This potentially allows for larger calculations, where storage of the full Hessian matrix is impossible.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_LBFGS [Logical]

   :Example:

   .. code::

      GEOM_LBFGS F

.. _geom-lbfgs-block-length:

GEOM_LBFGS_BLOCK_LENGTH
-----------------------

:Type: Integer
:Default: 30
:Unit: None
:Level: Expert
:Group: GEOM
:Search: :searchlink:`GEOM_LBFGS_BLOCK_LENGTH`

How many updates to store before reallocation in an unbounded LBFGS calculation

If LBFGS is performed in unbounded mode, then the geometry optimiser should perform identically to BFGS, however, to avoid using as much memory as BFGS, the number of history vectors which are stored is increased in increments of GEOM_LBFGS_BLOCK_LENGTH. So, provided that the number of iterations of the geometry optimiser does not reach ~1/2 * number of degrees of freedom, then it will use less memory than a standard BFGS calculation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_LBFGS_BLOCK_LENGTH [Integer]

   :Example:

   .. code::

      GEOM_LBFGS_BLOCK_LENGTH 30

.. _geom-lbfgs-max-updates:

GEOM_LBFGS_MAX_UPDATES
----------------------

:Type: Integer
:Default: 30
:Unit: None
:Level: Intermediate
:Group: GEOM
:Search: :searchlink:`GEOM_LBFGS_MAX_UPDATES`

Number of LBFGS update vectors to store

The LBFGS method can optionally limit the number of history vectors which it uses to build an approximation to he inverse Hessian to the latest N. This can vastly reduce the memory requirements if N is small, but the user should ensure that N is large enough that the approximation is sufficient. If N is set to 0 then LBFGS keeps an unlimited history, which is equivalent to BFGS.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_LBFGS_MAX_UPDATES [Integer]

   :Example:

   .. code::

      GEOM_LBFGS_MAX_UPDATES 30

.. _geom-max-iter:

GEOM_MAX_ITER
-------------

:Type: Integer
:Default: 50
:Unit: None
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_MAX_ITER`

Maximum number of geometry optimization iterations

Specifies the maximum number of iterations for geometry optimisation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_MAX_ITER [Integer]

   :Example:

   .. code::

      GEOM_MAX_ITER 30

.. _geom-method:

GEOM_METHOD
-----------

:Type: String
:Default: 'CARTESIAN'
:Unit: None
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_METHOD`

Method for geometry optimization  CARTESIAN = BFGS from CASTEP; or  BFGS = BFGS from CASTEP;  LBFGS = limited memory BFGS;  TPSD = two-point steepest descent;  DELOCALIZED = DELOCALIZED INTERNALS from CASTEP.

Specifies the method for geometry optimisation, currently either CARTESIAN for the BFGS algorithm based on Cartesian atomic coordinates [e.g. Pfrommeret al.,J. Comp. Phys.131, 233 (1997)] or DELOCALIZED for delocalized internal coordinates [Andzelm et al., Chem. Phys. Lett., 335, 321, (2001)].

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_METHOD [Text]

   :Example:

   .. code::

      GEOM_METHOD DELOCALIZED

.. _geom-modulus-est:

GEOM_MODULUS_EST
----------------

:Type: Physical
:Default: 0.017
:Unit: ha/bohr**3
:Level: Intermediate
:Group: GEOM
:Search: :searchlink:`GEOM_MODULUS_EST`

The estimated bulk modulus

Specifies the estimated bulk modulus used to initialize the inverse Hessian matrix for geometry optimization.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_MODULUS_EST [Value] [Unit]

   :Example:

   .. code::

      GEOM_MODULUS_EST 100 GPa

.. _geom-output-detail:

GEOM_OUTPUT_DETAIL
------------------

:Type: String
:Default: 'DEFAULT'
:Unit: None
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_OUTPUT_DETAIL`

Level of output detail for GEOM: BRIEF, NORMAL, VERBOSE, PROLIX

.. _geom-precond-exp-a:

GEOM_PRECOND_EXP_A
------------------

:Type: Double-Precision
:Default: 3.0
:Unit: None
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_PRECOND_EXP_A`

A value of EXP preconditioner

This is a parameter in the EXP geometry optimisation pre-conditioning scheme explained in: Packwood, David, et al. "A universal preconditioner for simulating condensed phase materials." The Journal of Chemical Physics 144.16 (2016): 164109. The convergence of the geometry optimisation is "relatively insensitive" to this parameter, but it can be tweaked to obtain slightly faster convergence if desired.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_PRECOND_EXP_A [Real]

   :Example:

   .. code::

      GEOM_PRECOND_EXP_A 3.0

.. _geom-precond-exp-c-stab:

GEOM_PRECOND_EXP_C_STAB
-----------------------

:Type: Double-Precision
:Default: 0.1
:Unit: None
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_PRECOND_EXP_C_STAB`

stabilization constant of EXP preconditioner

Specifies a diagonal contribution to add onto the ionic part of the Hessian pre-conditioning matrix in LBFGS / EXP pre-conditioning. This can improve stability if increased in magnitude, but should be left alone if the geometry optimisation is converging.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_PRECOND_EXP_C_STAB [Value] [Unit]

   :Example:

   .. code::

      GEOM_PRECOND_EXP_C_STAB 0.15 ha/bohr**2

.. _geom-precond-exp-mu:

GEOM_PRECOND_EXP_MU
-------------------

:Type: Physical
:Default: 0.0
:Unit: ha/bohr**2
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_PRECOND_EXP_MU`

mu value for EXP preconditioner

This pre-conditioner scaling parameter is calculated automatically if set to the default value of 0. The value found automatically is not guaranteed to give the best convergence, but has performed well empirically. The user may experiment with values to give faster convergence.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_PRECOND_EXP_MU [Value] [Unit]

   :Example:

   .. code::

      GEOM_PRECOND_EXP_MU 0.1 ha/bohr**2

.. _geom-precond-exp-r-cut:

GEOM_PRECOND_EXP_R_CUT
----------------------

:Type: Physical
:Default: 0.0
:Unit: bohr
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_PRECOND_EXP_R_CUT`

cutoff distance for EXP preconditioner

Specifies an upper limit in atomic separation to consider when calculating terms in the preconditioning matrix, with LBFGS / EXP pre-conditioning. A lower value is faster, but a larger value will give a potentially better pre-conditioning matrix. This is calculated from the nearest neighbour distance :ref:`geom-precond-exp-r-nn` by default.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_PRECOND_EXP_R_CUT [Value] [Unit]

   :Example:

   .. code::

      GEOM_PRECOND_EXP_R_CUT 4.0 bohr

.. _geom-precond-exp-r-nn:

GEOM_PRECOND_EXP_R_NN
---------------------

:Type: Physical
:Default: 0.0
:Unit: bohr
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_PRECOND_EXP_R_NN`

nearest neighbor distance for EXP preconditioner

If set to 0.0, as it is by default, the nearest neighbour distance is calculated automatically. This is used to calculate the distance cutoff in the EXP LBFGS pre-conditioner.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_PRECOND_EXP_R_NN [Value] [Unit]

   :Example:

   .. code::

      GEOM_PRECOND_EXP_R_NN 4.0 bohr

.. _geom-precond-ff-c-stab:

GEOM_PRECOND_FF_C_STAB
----------------------

:Type: Physical
:Default: 0.1
:Unit: ha/bohr**2
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_PRECOND_FF_C_STAB`

stabilization constant of :ref:`ff` preconditioner

Specifies a diagonal contribution to add onto the ionic part of the Hessian pre-conditioning matrix in LBFGS / :ref:`ff` pre-conditioning. This can improve stability if increased in magnitude, but should be left alone if the geometry optimisation is converging.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_PRECOND_FF_C_STAB [Value] [Unit]

   :Example:

   .. code::

      GEOM_PRECOND_FF_C_STAB 0.15 ha/bohr**2

.. _geom-precond-ff-r-cut:

GEOM_PRECOND_FF_R_CUT
---------------------

:Type: Physical
:Default: 3.8
:Unit: bohr
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_PRECOND_FF_R_CUT`

cutoff distance for :ref:`ff` preconditioner

Specifies an upper limit in atomic separation to consider when calculating terms in the preconditioning matrix, with LBFGS / :ref:`ff` pre-conditioning. A lower value is faster, but a larger value will give a potentially better pre-conditioning matrix.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_PRECOND_FF_R_CUT [Value] [Unit]

   :Example:

   .. code::

      GEOM_PRECOND_FF_R_CUT 4.0 bohr

.. _geom-precond-scale-cell:

GEOM_PRECOND_SCALE_CELL
-----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_PRECOND_SCALE_CELL`

Scaling cell in variable cell optimisation.

.. _geom-precond-type:

GEOM_PRECOND_TYPE
-----------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Basic
:Group: GEOM
:Search: :searchlink:`GEOM_PRECOND_TYPE`

type of preconditioner  NONE = LBFGS from CASTEP;  ID = ID/LBFGS should be identical to NONE;  EXP = EXP/LBFGS.

If this is set to NONE, then LBFGS will use the Pfrommer pre-conditioner as normal. If it is set to ID, then a scaled identity matrix will be used as the pre-conditioning matrix. If set to EXP, then an exponential pre-conditioner will be used which can reduce the number of geometry iterations in inorganic calculations to less than half. For organic calculations, the FF, forcefield pre-conditioning method is recommended which can reduce the number of geometry iterations to about a third of the number with :ref:`geom-precond-type` : F. The :ref:`ff` method does not support atomic species beneath row 3 in the periodic table. More information on these methods may be found in : Packwood, David, et al. "A universal preconditioner for simulating condensed phase materials." The Journal of Chemical Physics 144.16 (2016): 164109.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_PRECOND_TYPE [Text]

   :Example:

   .. code::

      GEOM_PRECOND_TYPE EXP

.. _geom-print-inv-hessian:

GEOM_PRINT_INV_HESSIAN
----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: GEOM
:Search: :searchlink:`GEOM_PRINT_INV_HESSIAN`

Write inverse Hessian to standard output

Include information about the inverse Hessian matrix in the ouput of a geometry optimization.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_PRINT_INV_HESSIAN [Logical]

   :Example:

   .. code::

      GEOM_PRINT_INV_HESSIAN T

.. _geom-reset-dk-ngwfs-iter:

GEOM_RESET_DK_NGWFS_ITER
------------------------

:Type: Integer
:Default: 6
:Unit: None
:Level: Intermediate
:Group: GEOM
:Search: :searchlink:`GEOM_RESET_DK_NGWFS_ITER`

Number of geom iterations between resets of kernel and NGWFs

Number of geom iterations between resets of kernel and NGWFs

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_RESET_DK_NGWFS_ITER [Integer]

   :Example:

   .. code::

      GEOM_RESET_DK_NGWFS_ITER 20

.. _geom-reuse-dk-ngwfs:

GEOM_REUSE_DK_NGWFS
-------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`GEOM_REUSE_DK_NGWFS`

Re-use density kernel and NGWFs during geometry optimisation steps

Re-use density kernel and NGWFs during geometry optimisation steps

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GEOM_REUSE_DK_NGWFS [Logical]

   :Example:

   .. code::

      GEOM_REUSE_DK_NGWFS F

.. _gpu-fft-scheme:

GPU_FFT_SCHEME
--------------

:Type: String
:Default: 'THREADED'
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`GPU_FFT_SCHEME`

Are GPU FFTs done THREADED or BATCHED?

.. _gpu-group-size:

GPU_GROUP_SIZE
--------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`GPU_GROUP_SIZE`

Number of procs in a GPU group

.. _grd-format:

GRD_FORMAT
----------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`GRD_FORMAT`

Allow .grd format for plot outputs

Output volumetric data (e.g. charge density, potential, NGWFs, canonical orbitals) in .grd format used by Accelrys Materials Studio .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      GRD_FORMAT [Logical]

   :Example:

   .. code::

      GRD_FORMAT F

.. _h2denskern-sparsity:

H2DENSKERN_SPARSITY
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: EDFT
:Search: :searchlink:`H2DENSKERN_SPARSITY`

Use the H^2 sparsity pattern for K in :ref:`foe`

Enable the AQuA-FOE method when :ref:`foe` and :ref:`edft` are both enabled. This allows the sparsity of the density kernel to be adjusted by the NGWF radii. This approach should be faster for calculations with > 1000 atoms, and explicitly allows sparsity in the density kernel.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      H2DENSKERN_SPARSITY [Logical]

   :Example:

   .. code::

      H2DENSKERN_SPARSITY T

.. _hfx-bc:

HFX_BC
------

:Type: String
:Default: ''
:Unit: None
:Level: Expert
:Group: VDW
:Search: :searchlink:`HFX_BC`

3 character string defining BCs for HFx along each lattice vector. 'O' for open, 'P' for periodic.

.. _hfx-bessel-rad-nptsx:

HFX_BESSEL_RAD_NPTSX
--------------------

:Type: Integer
:Default: 100000
:Unit: None
:Level: Expert
:Group: HFX
:Search: :searchlink:`HFX_BESSEL_RAD_NPTSX`

HFx: Number of points in Bessel radial interpolation

.. _hfx-cutoff:

HFX_CUTOFF
----------

:Type: Physical
:Default: 1000.0
:Unit: bohr
:Level: Basic
:Group: HFX
:Search: :searchlink:`HFX_CUTOFF`

HFx cutoff radius

.. _hfx-debug:

HFX_DEBUG
---------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: HFX
:Search: :searchlink:`HFX_DEBUG`

Perform extra sanity checks for HFx?

.. _hfx-max-l:

HFX_MAX_L
---------

:Type: Integer
:Default: -1
:Unit: None
:Level: Basic
:Group: HFX
:Search: :searchlink:`HFX_MAX_L`

Maximum order of HFx expansion into SWs

.. _hfx-max-q:

HFX_MAX_Q
---------

:Type: Integer
:Default: -1
:Unit: None
:Level: Basic
:Group: HFX
:Search: :searchlink:`HFX_MAX_Q`

Maximum number of Bessel zeros in HFx''s SW expansion

.. _hfx-memory-limit:

HFX_MEMORY_LIMIT
----------------

:Type: Integer
:Default: 4096
:Unit: None
:Level: Expert
:Group: HFX
:Search: :searchlink:`HFX_MEMORY_LIMIT`

Max cache size (per MPI rank) for all of HFx (in MiB)

.. _hfx-memory-weights:

HFX_MEMORY_WEIGHTS
------------------

:Type: String
:Default: '-1.0 -1.0 -1.0'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`HFX_MEMORY_WEIGHTS`

Three weights for HFx memory use (SWOP, EXPA, PROD).

.. _hfx-metric:

HFX_METRIC
----------

:Type: String
:Default: 'electrostatic'
:Unit: None
:Level: Intermediate
:Group: HFX
:Search: :searchlink:`HFX_METRIC`

Electrostatic or overlap metric

.. _hfx-nlpp-for-exchange:

HFX_NLPP_FOR_EXCHANGE
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: HFX
:Search: :searchlink:`HFX_NLPP_FOR_EXCHANGE`

Give exchange matrix same sparsity as non-local pseudopotential matrix

.. _hfx-output-detail:

HFX_OUTPUT_DETAIL
-----------------

:Type: String
:Default: 'DEFAULT'
:Unit: None
:Level: Basic
:Group: HFX
:Search: :searchlink:`HFX_OUTPUT_DETAIL`

Level of output detail for HFx: BRIEF, NORMAL, VERBOSE, PROLIX

.. _hfx-read-xmatrix:

HFX_READ_XMATRIX
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: HFX
:Search: :searchlink:`HFX_READ_XMATRIX`

Read restart information for the X matrix

.. _hfx-symm-thresh:

HFX_SYMM_THRESH
---------------

:Type: Double-Precision
:Default: 3.4
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`HFX_SYMM_THRESH`

Symmetry threshold for HFx exchange matrix (minimum no. of correct decimals)

.. _hfx-use-ri:

HFX_USE_RI
----------

:Type: String
:Default: '<unset>'
:Unit: None
:Level: Basic
:Group: HFX
:Search: :searchlink:`HFX_USE_RI`

ID of the :ref:`swri` to use for HFx

.. _hfx-write-xmatrix:

HFX_WRITE_XMATRIX
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: HFX
:Search: :searchlink:`HFX_WRITE_XMATRIX`

Write restart information for the X matrix

.. _hhf-nstates:

HHF_NSTATES
-----------

:Type: Integer
:Default: 0
:Unit: None
:Level: Basic
:Group: HHF
:Search: :searchlink:`HHF_NSTATES`

Number of extra occupied states for HHF calculation

.. _histonum:

HISTONUM
--------

:Type: Integer
:Default: 2001
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`HISTONUM`

Number of grid points used for plotting DoS, LDoS, or spectra

.. _homo-dens-plot:

HOMO_DENS_PLOT
--------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`HOMO_DENS_PLOT`

Number of squared MOs to plot from HOMO and lower

Specifies the number of canonical orbitals below the HOMO to plot, if :ref:`do-properties` is set to true. Thus a value of zero plots only the HOMO, a negative value disables plotting and a positive value of N plots the N+1 highest occupied canonical orbitals.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      HOMO_DENS_PLOT [Integer]

   :Example:

   .. code::

      HOMO_DENS_PLOT 0

.. _homo-plot:

HOMO_PLOT
---------

:Type: Integer
:Default: 5
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`HOMO_PLOT`

Number of MOs to plot from HOMO and lower

Specifies the number of canonical orbitals below the HOMO to plot, if :ref:`do-properties` is set to true. Thus a value of zero plots only the HOMO, a negative value disables plotting and a positive value of N plots the N+1 highest occupied canonical orbitals.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      HOMO_PLOT [Integer]

   :Example:

   .. code::

      HOMO_PLOT 0

.. _ht-stash-size:

HT_STASH_SIZE
-------------

:Type: Integer
:Default: 256
:Unit: None
:Level: Expert
:Group: HT
:Search: :searchlink:`HT_STASH_SIZE`

OMP stash size for hash tables (in MiB)

.. _hubbard:

HUBBARD
-------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD`

Hubbard species info (symb., ang. mom., U parameter (eV), effective charge, alpha parameter (eV))

Applies the DFT+U, also known as LDA+U, correction for strongly correlated materials. For species S and correlated subspace of angular momentum channel L (with principal quantum number n=L+1 ) we apply a DFT+U correction with :ref:`hubbard` parameter U (eV) and exchange parameter J (eV). Standard DFT+U functionality can be obtained by setting J=0 . The effective nuclear charge Z determines how the projectors defining the correlated subspace are generated. If any negative value is given, e.g., Z=-10 , the NGWF initial guess orbitals (numerical atomic orbitals) are used. Alternatively, a positive value of Z causes the code to generate hydrogenic orbitals spanning this space with effective nuclear charge Z . The a and s parameters (eV) are a rigid potential shift and a spin-splitting, respectively, applied to the subspaces. For more information, please read the file in the documentation section.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK HUBBARD
      S1 L1 U1 J1 Z1 a1 s1
      S2 L2 U2 J2 Z2 a2 s2
       .   .   .   .       .
       .   .   .   .       .
      SN LN UN JN ZN aN sN
      %ENDBLOCK HUBBARD

   :Example:

   .. code::

      %BLOCK HUBBARD
      O  1 0.0 0.0 -4.5 0.0 0.0
      Fe 2 3.0 0.0 -9.5 0.0 0.0
      %ENDBLOCK HUBBARD

.. _hubbardscf-on-the-fly:

HUBBARDSCF_ON_THE_FLY
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARDSCF_ON_THE_FLY`

Carry out on-the-fly HUBBARDSCF with new projectors for new NGWFs

Activate a non-variational on-the-fly form of projector self-consistency in DFT+U or cDFT, in which the projectors are updated whenever the NGWFs are. task : HUBBARDSCF is then not needed.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      HUBBARDSCF_ON_THE_FLY [Logical]

   :Example:

   .. code::

      HUBBARDSCF_ON_THE_FLY T

.. _hubbard-calculating-u:

HUBBARD_CALCULATING_U
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_CALCULATING_U`

Calculate subspace-projected potentials for calculating U and J

.. _hubbard-compute-u-or-j:

HUBBARD_COMPUTE_U_OR_J
----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_COMPUTE_U_OR_J`

Compute U or J correction - not recommended method for now

.. _hubbard-conv-win:

HUBBARD_CONV_WIN
----------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_CONV_WIN`

Energy convergence window when using DFT+U projector optimisation

The minimum number of Hubbard projector update steps satisfying the incremental energy tolerance :ref:`hubbard-energy-tol` required for convergence in task : HUBBARDSCF.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      HUBBARD_CONV_WIN [Integer]

   :Example:

   .. code::

      HUBBARD_CONV_WIN 4

.. _hubbard-energy-tol:

HUBBARD_ENERGY_TOL
------------------

:Type: Physical
:Default: 1e-08
:Unit: hartree
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_ENERGY_TOL`

Energy tolerance when using DFT+U projector optimisation

The maximum incremental energy change between Hubbard projector update steps allowed for converge in task : HUBBARDSCF.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      HUBBARD_ENERGY_TOL [Value] [Unit]

   :Example:

   .. code::

      HUBBARD_ENERGY_TOL 1.0E-4 eV

.. _hubbard-functional:

HUBBARD_FUNCTIONAL
------------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_FUNCTIONAL`

DFT+U energy functional to use

The form of DFT+U energy term used. Contact developers if you need to try something beyond the default.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      HUBBARD_FUNCTIONAL [Real]

   :Example:

   .. code::

      HUBBARD_FUNCTIONAL 1

.. _hubbard-j-minority-term:

HUBBARD_J_MINORITY_TERM
-----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_J_MINORITY_TERM`

Include minority-only energy term in DFT+U+J

.. _hubbard-max-iter:

HUBBARD_MAX_ITER
----------------

:Type: Integer
:Default: 10
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_MAX_ITER`

Maximum number of DFT+U projector optimisation steps, 0 for none

The maximum allowed number of Hubbard projector update steps taken in a projector self-consistent DFT+U or cDFT calculation in task : HUBBARDSCF.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      HUBBARD_MAX_ITER [Integer]

   :Example:

   .. code::

      HUBBARD_MAX_ITER 6

.. _hubbard-ngwf-spin-threshold:

HUBBARD_NGWF_SPIN_THRESHOLD
---------------------------

:Type: Double-Precision
:Default: 2e-05
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_NGWF_SPIN_THRESHOLD`

NGWF RMS  gradient threshold at which to switch off DFT+U spin-splitting

The incremental change in energy, in total-energy minimisation, at which any spin-splitting (Zeeman) type term in DFT+U is switched off, and the minimisation history reset. Useful for breaking open-shell, antiferromagnetic, or charge-density wave symmetries.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      HUBBARD_NGWF_SPIN_THRESHOLD [Value] [Unit]

   :Example:

   .. code::

      HUBBARD_NGWF_SPIN_THRESHOLD 1.0E-3 eV

.. _hubbard-proj-mixing:

HUBBARD_PROJ_MIXING
-------------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_PROJ_MIXING`

Proportion of old Hubbard projector to mix with new

The fraction of previous Hubbard projector to mix with new for projector self-consistent DFT+U or cDFT in task : HUBBARDSCF. Not found to be necessary.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      HUBBARD_PROJ_MIXING [Real]

   :Example:

   .. code::

      HUBBARD_PROJ_MIXING 0.2

.. _hubbard-proj-read-only:

HUBBARD_PROJ_READ_ONLY
----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_PROJ_READ_ONLY`

Read, but do not write hubbard projectors

.. _hubbard-read-projectors:

HUBBARD_READ_PROJECTORS
-----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_READ_PROJECTORS`

Logical to read Hubbard-projectors from file

Read Hubbard projectors from .tightbox_hub_projs file in restart calculations involving DFT+U.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      HUBBARD_READ_PROJECTORS [Logical]

   :Example:

   .. code::

      HUBBARD_READ_PROJECTORS T

.. _hubbard-tensor-corr:

HUBBARD_TENSOR_CORR
-------------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_TENSOR_CORR`

DFT+U projector tensorial correction to use

The form of correction used to correct for any nonorthogonality between Hubbard projectors. Contact developers if you need to try something other than the default "tensorial" correction.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      HUBBARD_TENSOR_CORR [Integer]

   :Example:

   .. code::

      HUBBARD_TENSOR_CORR 1

.. _hubbard-tensor-forces:

HUBBARD_TENSOR_FORCES
---------------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Intermediate
:Group: HUBBARD
:Search: :searchlink:`HUBBARD_TENSOR_FORCES`

Calculate force contributions due to Hubbard metric tensor

.. _hubbard-unify-sites:

HUBBARD_UNIFY_SITES
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`HUBBARD_UNIFY_SITES`

Combine all projectors into one Hubbard site

.. _image-sizes:

IMAGE_SIZES
-----------

:Type: String
:Default: 'DEFAULT'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`IMAGE_SIZES`

MPI Process size of each ONETEP image separated by pipes |

If specified in the input file, a string of the format ‘i|j|k|l|m|...’ can be used to individually size the images in an image-parallel run. The number of sections specified should be equal the number of images in the run and the sum of the image sizes should be equal the number of MPI processes specified at runtime.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IMAGE_SIZES [Text]

   :Example:

   .. code::

      IMAGE_SIZES 3|3|5|4

.. _imag-thr:

IMAG_THR
--------

:Type: Double-Precision
:Default: 1e-06
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`IMAG_THR`

Threshold to accept value of imaginary part of a quantity

.. _initial-dens-realspace:

INITIAL_DENS_REALSPACE
----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`INITIAL_DENS_REALSPACE`

Construct initial density in real space from atomsolver density

Specifies whether to construct the initial density passed to Palser-Manolopoulos (or diagonalisation) in real-space, from the sum of the atom-solver densities (if true), or the default of a superposition of gaussians (if false).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      INITIAL_DENS_REALSPACE [Logical]

   :Example:

   .. code::

      INITIAL_DENS_REALSPACE T

.. _ion-ion-bc:

ION_ION_BC
----------

:Type: String
:Default: ''
:Unit: None
:Level: Intermediate
:Group: BC
:Search: :searchlink:`ION_ION_BC`

3 character string defining BCs for ion-ion interaction along each lattice vector. 'O' for open, 'P' for periodic.

.. _isosurface-cutoff:

ISOSURFACE_CUTOFF
-----------------

:Type: Double-Precision
:Default: 0.0005
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`ISOSURFACE_CUTOFF`

Isosurface cutoff in volume term

Determines the cutoff density alpha of the electronic density isosurface defining the volume Ve used in the electronic enthalpy method. Care must be taken to calibrate its value, along with SMOOTHING_FACTOR, for the system of interest as described in [Corsini et al, J. Chem. Phys. 2013, 139, 084117]

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ISOSURFACE_CUTOFF [Value]

   :Example:

   .. code::

      ISOSURFACE_CUTOFF 0.0003

.. _is-apolar-method:

IS_APOLAR_METHOD
----------------

:Type: String
:Default: 'SASA'
:Unit: None
:Level: Basic
:Group: SOLVATION
:Search: :searchlink:`IS_APOLAR_METHOD`

Implicit solvent: the method by which the apolar contribution is calculated

.. _is-apolar-sasa-definition:

IS_APOLAR_SASA_DEFINITION
-------------------------

:Type: String
:Default: 'DENSITY'
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_APOLAR_SASA_DEFINITION`

Implicit solvent: sets the method used to define the surface area for the nonpolar term

.. _is-apolar-scaling-factor:

IS_APOLAR_SCALING_FACTOR
------------------------

:Type: Double-Precision
:Default: 0.281075
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_APOLAR_SCALING_FACTOR`

Implicit solvent: Scaling factor for apolar term

Controls the scaling of the apolar term with the aim of taking solute-solvent dispersion-repulsion into account. This is only relevant in implicit solvent calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_APOLAR_SCALING_FACTOR [Value]

   :Example:

   .. code::

      IS_APOLAR_SCALING_FACTOR 1.0

.. _is-auto-solvation:

IS_AUTO_SOLVATION
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_AUTO_SOLVATION`

If true, vacuum calculation will automatically precede solvated calculation

Specifies that a calculation in vacuum should be automatically performed before any calculation that employs implicit solvent.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_AUTO_SOLVATION [Logical]

   :Example:

   .. code::

      IS_AUTO_SOLVATION T

.. _is-bc-allow-frac-charge:

IS_BC_ALLOW_FRAC_CHARGE
-----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_BC_ALLOW_FRAC_CHARGE`

Implicit solvent: Don't check for total charge being an integer in MG BCs.

.. _is-bc-coarseness:

IS_BC_COARSENESS
----------------

:Type: Integer
:Default: 5
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_BC_COARSENESS`

Open BCs: controls boundary condition coarse-graining

Specifies the edge length of the cubic block, in units of fine grid delta, over which charge will be coarse-grained in the calculation of open boundary conditions. This is only relevant in implicit solvent calculations and in calculations with open boundary conditions (such as calculations with smeared ions).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_BC_COARSENESS [Integer]

   :Example:

   .. code::

      IS_BC_COARSENESS 7 ; Use blocks 7x7x7

.. _is-bc-surface-coarseness:

IS_BC_SURFACE_COARSENESS
------------------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_BC_SURFACE_COARSENESS`

Open BCs: controls boundary condition coarse-graining

Specifies the edge length of the square block, in units of fine grid delta, over which the potential will be bilinearly interpolated in the calculation of open boundary conditions. This is only relevant in implicit solvent calculations and in calculations with open boundary conditions (such as calculations with smeared ions). Values larger than 1 will speed up the calculation but can impact accuracy for charged systems -- use with care.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_BC_SURFACE_COARSENESS [Integer]

   :Example:

   .. code::

      IS_BC_SURFACE_COARSENESS 3 ; Use surface blocks of 3x3

.. _is-bc-threshold:

IS_BC_THRESHOLD
---------------

:Type: Double-Precision
:Default: 1e-09
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_BC_THRESHOLD`

Open BCs: controls boundary condition coarse-graining

Specifies the charge density threshold used for coarse-graining in the calculation of open boundary conditions. Fine grid points with charge magnitudes below this threshold will be ignored during the coarse-graining procedure. This serves to eliminate the unnecessary integration of noise and ringing. Decreasing this threshold (to, say, 1E-10) might be necessary in rare situations, such as in runs using simulation cells with inadequate padding and fine_grid_scale > 2.0, which may lead to more severe ringing. Increasing this threshold mainly serves to increase performance, however, accuracy will be impacted if this threshold is set too high (higher than, say, 5E-8). This is only relevant in implicit solvent calculations and in calculations with open boundary conditions (such as calculations with smeared ions).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_BC_THRESHOLD [Real]

   :Example:

   .. code::

      IS_BC_THRESHOLD 1E-10 ; Be extra accurate

.. _is-bulk-permittivity:

IS_BULK_PERMITTIVITY
--------------------

:Type: Double-Precision
:Default: Unknown
:Unit: None
:Level: Basic
:Group: SOLVATION
:Search: :searchlink:`IS_BULK_PERMITTIVITY`

Implicit solvent: eps_inf parameter(relative permittivity) in Fattebert-Gygi functional

Sets the relative dielectric permittivity of the solvent.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_BULK_PERMITTIVITY [Value]

   :Example:

   .. code::

      IS_BULK_PERMITTIVITY 14.2 ; ethanediamine as solvent

.. _is-check-solv-energy-grad:

IS_CHECK_SOLV_ENERGY_GRAD
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_CHECK_SOLV_ENERGY_GRAD`

Implicit solvent: sanity check the energy gradient

Checks the gradient of solvation energy with finite differences. This is only relevant in implicit solvent calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_CHECK_SOLV_ENERGY_GRAD [Logical]

   :Example:

   .. code::

      IS_CHECK_SOLV_ENERGY_GRAD T

.. _is-core-width:

IS_CORE_WIDTH
-------------

:Type: Physical
:Default: 1.2
:Unit: bohr
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_CORE_WIDTH`

Implicit solvent: Radius where eps is set to unity

Only used in implicit solvent calculations. In the IS model used in ONETEP the dielectric permittivity is a function of electronic density. For certain atoms (e.g. Pt) the use of pseudopotentials may cause the electronic density in the immediate vicinity of an atom to be so low as to produce permittivities that non-negligibly differ from 1. By using this directive you can specify a radius around each core where the permittivity is set to unity regardless of the usual definition of eps=eps(rho). We've not yet seen a case where the default would be unsuitable.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_CORE_WIDTH [Physical]

   :Example:

   .. code::

      IS_CORE_WIDTH 1.4 bohr

.. _is-density-max-threshold:

IS_DENSITY_MAX_THRESHOLD
------------------------

:Type: Double-Precision
:Default: 0.005
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_DENSITY_MAX_THRESHOLD`

Implicit solvent: parameter in Andreussi functional

.. _is-density-min-threshold:

IS_DENSITY_MIN_THRESHOLD
------------------------

:Type: Double-Precision
:Default: 0.0001
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_DENSITY_MIN_THRESHOLD`

Implicit solvent: parameter in Andreussi functional

.. _is-density-threshold:

IS_DENSITY_THRESHOLD
--------------------

:Type: Double-Precision
:Default: 0.00035
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_DENSITY_THRESHOLD`

Implicit solvent: rho_0 parameter in Fattebert-Gygi functional

Sets the value of the rho_0 parameter (in atomic units) in the definition of the dielectric cavity as described in DA Scherlis, J-L Fattebert, F Gygi, M Cococcioni, and N Marzari, Journal of Chemical Physics 124, 074103 (2006). This is only relevant in implicit solvent calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_DENSITY_THRESHOLD [Value]

   :Example:

   .. code::

      IS_DENSITY_THRESHOLD 0.00035

.. _is-dielectric-exclusions:

IS_DIELECTRIC_EXCLUSIONS
------------------------

:Type: Block
:Default: None
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_DIELECTRIC_EXCLUSIONS`

Dielectric exclusion regions

In typical applications this block can be absent. If not absent, it is used to determine which additional parts of the system are inaccessible to the implicit solvent.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK IS_DIELECTRIC_EXCLUSIONS
      sphere x y z r OR box xmin xmax ymin ymax zmin zmax
      ... ... ...
      %ENDBLOCK IS_DIELECTRIC_EXCLUSIONS

   :Example:

   .. code::

      %BLOCK IS_DIELECTRIC_EXCLUSIONS
       sphere 20.0 15.0 22.0  4.0    ; x, y, z and radius, all in bohr
       box 13.0 15.0  10.0 14.5  22.5 29.0 ; xmin xmax  ymin ymax zmin zmax, all in bohr
       xcyl 17.0 45.0  7.0 ; y, z and radius, all in bohr
      %ENDBLOCK IS_DIELECTRIC_EXCLUSIONS

.. _is-dielectric-exclusions-smear:

IS_DIELECTRIC_EXCLUSIONS_SMEAR
------------------------------

:Type: Physical
:Default: 0.0
:Unit: bohr
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_DIELECTRIC_EXCLUSIONS_SMEAR`

Implicit solvent: smoothing on boundaries of dielectric exclusion regions defined in the :ref:`is-dielectric-exclusions` block.  This is a smearing distance.

Length scale that defines the extent of the smearing of dielectric exclusion region boundaries. For more details, see the implicit solvation documentation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_DIELECTRIC_EXCLUSIONS_SMEAR [Value] [Unit]

   :Example:

   .. code::

      IS_DIELECTRIC_EXCLUSIONS_SMEAR 0.5 Bohr

.. _is-dielectric-function:

IS_DIELECTRIC_FUNCTION
----------------------

:Type: String
:Default: 'fgf'
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_DIELECTRIC_FUNCTION`

Implicit solvent: how the cavity is determined

Chooses the function used to generate the dielectric cavity from the electronic density. FGF uses the one described in DA Scherlis, J-L Fattebert, F Gygi, M Cococcioni, and N Marzari, Journal of Chemical Physics 124, 074103 (2006). GAUSSIAN uses the core density to generate the cavity, this is not currently supported. This is only relevant in implicit solvent calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_DIELECTRIC_FUNCTION [FGF | GAUSSIAN]

   :Example:

   .. code::

      IS_DIELECTRIC_FUNCTION FGF

.. _is-dielectric-model:

IS_DIELECTRIC_MODEL
-------------------

:Type: String
:Default: 'fix_initial'
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_DIELECTRIC_MODEL`

Implicit solvent: how the cavity is determined

Chooses how the dielectric cavity responds to changes in the electronic density. With FIX_INITIAL the cavity remains fixed (and the calculation is still self-consistent). With SELF_CONSISTENT , the cavity self-consistently reacts to changes in the density. With GAUSSIAN_IONS the core density is used to generate the cavity, so it remains fixed as well. GAUSSIAN_IONS is not currently supported. FIX_INITIAL is strongly recommended. SELF_CONSISTENT offers slightly improved accuracy, but requires very fine grids to converge (such as :ref:`fine-grid-scale` 4.0 ), which translates into extremely high memory requirements -- thus it is not recommended, unless for very small molecules. This keyword is only relevant in implicit solvent calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_DIELECTRIC_MODEL [FIX_INITIAL | SELF_CONSISTENT | GAUSSIAN_IONS]

   :Example:

   .. code::

      IS_DIELECTRIC_MODEL SELF_CONSISTENT

.. _is-discretization-order:

IS_DISCRETIZATION_ORDER
-----------------------

:Type: Integer
:Default: Unknown
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_DISCRETIZATION_ORDER`

[OBSOLETE] Implicit solvent: discretization order (2nd, 4th, ...) for the PB solver

Sets the discretization order used for finite-differences. The available orders are: 2, 4, 6, 8, 10 and 12. Recommended is 8 or 10. Currently this keyword is only relevant in multigrid calculations (which are those using implicit solvent or open boundary conditions), where it controls the discretization order used for defect-correcting the multigrid solution and for calculating gradients and laplacians.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_DISCRETIZATION_ORDER [Integer]

   :Example:

   .. code::

      IS_DISCRETIZATION_ORDER 10

.. _is-emft-cavity:

IS_EMFT_CAVITY
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_EMFT_CAVITY`

Decides whether the IS cavity is determined using the EMFT-optimised kernel or the normal kernel

.. _is-hc-steric-dens-isovalue:

IS_HC_STERIC_DENS_ISOVALUE
--------------------------

:Type: Double-Precision
:Default: 0.003
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_HC_STERIC_DENS_ISOVALUE`

Implicit solvent: n_0 parameter in electrolyte accessibility

.. _is-hc-steric-smearing:

IS_HC_STERIC_SMEARING
---------------------

:Type: Physical
:Default: 0.4
:Unit: bohr
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_HC_STERIC_SMEARING`

Implicit solvent: smearing distance for smoothed hard-core potential

.. _is-implicit-solvent:

IS_IMPLICIT_SOLVENT
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: SOLVATION
:Search: :searchlink:`IS_IMPLICIT_SOLVENT`

Use implicit solvent?

Turns the implicit solvent on or off. As the implicit solvent requires the smeared ion representation, it also sets :ref:`is-smeared-ion-rep` to T . When on, open boundary conditions are used for the calculation of ion-ion, Hartree and local pseudopotential terms.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_IMPLICIT_SOLVENT [Logical]

   :Example:

   .. code::

      IS_IMPLICIT_SOLVENT T

.. _is-include-apolar:

IS_INCLUDE_APOLAR
-----------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Basic
:Group: SOLVATION
:Search: :searchlink:`IS_INCLUDE_APOLAR`

Implicit solvent: include apolar terms in solvation energy

When T , includes the apolar term in an implicit solvent calculation. Can only be used with :ref:`is-implicit-solvent` T .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_INCLUDE_APOLAR [Logical]

   :Example:

   .. code::

      IS_INCLUDE_APOLAR F

.. _is-include-cavitation:

IS_INCLUDE_CAVITATION
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: SOLVATION
:Search: :searchlink:`IS_INCLUDE_CAVITATION`

[OBSOLETE] Use is_include_apolar instead

When T , includes the cavitation term in an implicit solvent calculation. Can only be used with :ref:`is-implicit-solvent` T .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_INCLUDE_CAVITATION [Logical]

   :Example:

   .. code::

      IS_INCLUDE_CAVITATION F

.. _is-multigrid-defect-error-tol:

IS_MULTIGRID_DEFECT_ERROR_TOL
-----------------------------

:Type: Double-Precision
:Default: Unknown
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_MULTIGRID_DEFECT_ERROR_TOL`

[OBSOLETE] Implicit solvent: stop criterion for defect correction

Sets the error tolerance for the defect-correction algorithm in a multigrid calculation. This controls the maximum error when solving the defect equation in every defect-correction iteration and is *not* directly related to the magnitude of the error in the final solution. This keyword is only relevant in multigrid calculations (which are those using implicit solvent or open boundary conditions).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_MULTIGRID_DEFECT_ERROR_TOL [Value]

   :Example:

   .. code::

      IS_MULTIGRID_DEFECT_ERROR_TOL 1E-4 ; Try a stricter tolerance in case defect-correction diverges

.. _is-multigrid-error-damping:

IS_MULTIGRID_ERROR_DAMPING
--------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_MULTIGRID_ERROR_DAMPING`

[OBSOLETE] Implicit solvent: error damping in defect correction?

Turns on error damping in the multigrid defect-correction procedure. This is useful for solving the full (non-linearised) Poisson-Boltzmann equation, but will likely not do much for the linearised PBE or for the Poisson equation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_MULTIGRID_ERROR_DAMPING [Boolean]

   :Example:

   .. code::

      IS_MULTIGRID_ERROR_DAMPING T

.. _is-multigrid-error-tol:

IS_MULTIGRID_ERROR_TOL
----------------------

:Type: Double-Precision
:Default: Unknown
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_MULTIGRID_ERROR_TOL`

[OBSOLETE] Implicit solvent: stop criterion for the multigrid solver

Sets the error tolerance for the solution obtained through multigrid. If :ref:`is-discretization-order` is larger than 2, this is the final error obtained after defect correction, otherwise this is the error of the uncorrected multigrid solution. This keyword is only relevant in multigrid calculations (which are those using implicit solvent or open boundary conditions).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_MULTIGRID_ERROR_TOL [Value]

   :Example:

   .. code::

      IS_MULTIGRID_ERROR_TOL 1E-4 ; Try a relaxed tolerance to speed calculation up

.. _is-multigrid-max-iters:

IS_MULTIGRID_MAX_ITERS
----------------------

:Type: Integer
:Default: Unknown
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_MULTIGRID_MAX_ITERS`

[OBSOLETE] Implicit solvent: max number of iterations in multigrid solver

Sets the maximum number of iterations for the multigrid calculation. This controls both the maximum number of defect-correction steps and the maximum number of iterations of the multigrid process in each defect-correction step (and in the first solution with 2nd order, prior to defect correction). This value is best left at its default. This keyword is only relevant in multigrid calculations (which are those using implicit solvent or open boundary conditions).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_MULTIGRID_MAX_ITERS [Integer]

   :Example:

   .. code::

      IS_MULTIGRID_MAX_ITERS 200 ; purposefully waste time

.. _is-multigrid-nlevels:

IS_MULTIGRID_NLEVELS
--------------------

:Type: Integer
:Default: Unknown
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_MULTIGRID_NLEVELS`

[OBSOLETE] Implicit solvent: number of levels in multigrid solver

Sets the number of multigrid levels for a multigrid calculation. This keyword is only relevant in multigrid calculations (which are those using implicit solvent or open boundary conditions).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_MULTIGRID_NLEVELS [Integer]

   :Example:

   .. code::

      IS_MULTIGRID_NLEVELS 3

.. _is-multigrid-verbose:

IS_MULTIGRID_VERBOSE
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_MULTIGRID_VERBOSE`

Implicit solvent: verbose multigrid output?

Output cross-setions of quantities that are of interest during multigrid calculations to text files. For instance it might be desirable to examine the permittivity to verify whether a pocket in a molecule is solvent-acessible or not. The cross sections are always performed along the X direction, for a given value of Y and Z.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_MULTIGRID_VERBOSE [Logical]

   :Example:

   .. code::

      IS_MULTIGRID_VERBOSE T

.. _is-multigrid-verbose-y:

IS_MULTIGRID_VERBOSE_Y
----------------------

:Type: Physical
:Default: 0.0
:Unit: bohr
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_MULTIGRID_VERBOSE_Y`

Implicit solvent: x-section Y for verbose output

Specifies the offset along the Y axis for cross-sections performed with :ref:`is-multigrid-verbose` . Make sure you provide units. Compare :ref:`is-multigrid-verbose-z`

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_MULTIGRID_VERBOSE_Y [physical]

   :Example:

   .. code::

      IS_MULTIGRID_VERBOSE_Y 14.5 bohr

.. _is-multigrid-verbose-z:

IS_MULTIGRID_VERBOSE_Z
----------------------

:Type: Physical
:Default: 0.0
:Unit: bohr
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_MULTIGRID_VERBOSE_Z`

Implicit solvent: x-section Z for verbose output

Specifies the offset along the Z axis for cross-sections performed with :ref:`is-multigrid-verbose` . Make sure you provide units. Compare :ref:`is-multigrid-verbose-y`

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_MULTIGRID_VERBOSE_Y [physical]

   :Example:

   .. code::

      IS_MULTIGRID_VERBOSE_Y 14.5 bohr

.. _is-pbe:

IS_PBE
------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_PBE`

Implicit solvent: include ionic strengths?

Chooses the equation to be solved in implicit solvation. NONE chooses the nonomogeneous Poisson equation (NPE), LINEARISED chooses the linearised Poisson-Boltzmann equation, FULL chooses the full (non-linearised) Poisson-Boltzmann equation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_PBE [NONE|LINEARISED|FULL]

   :Example:

   .. code::

      IS_PBE FULL

.. _is-pbe-bc-debye-screening:

IS_PBE_BC_DEBYE_SCREENING
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_PBE_BC_DEBYE_SCREENING`

Should solvated BCs use Debye lambda exp() factor

Specifies whether boundary conditions in implicit solvation should use Debye screening (lambda*exp) factor. This is only relevant for implicit solvation calculations using the Poisson-Boltzmann formulation. This screening is exact in the linearised formulation, and an approximation in the full formulation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_PBE_BC_DEBYE_SCREENING [Boolean]

   :Example:

   .. code::

      IS_PBE_BC_DEBYE_SCREENING F

.. _is-pbe-energy-tolerance:

IS_PBE_ENERGY_TOLERANCE
-----------------------

:Type: Physical
:Default: 1.5936e-05
:Unit: hartree
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_PBE_ENERGY_TOLERANCE`

Absolute tolerance for difference between energy expressions in Boltzmann solvation

.. _is-pbe-exp-cap:

IS_PBE_EXP_CAP
--------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_PBE_EXP_CAP`

Cap of exponential argument in Boltzmann term

Sets a numerical cap at the arguments in the exp() in Poisson-Boltzmann terms in implicit solvation. If this keyword is specified, and uses a value different from 0.0, every argument of an exp() function in Poisson-Boltzmann implicit solvation will be checked against the cap and replaced with the value of the cap if it exceeds the cap. This is a crude way of preventing runaway nonlinearities. Note that DL_MG internally caps the cap (!) at max_expcap =50.0, while on the ONETEP side any positive value can be used for the cap. Thus, using values larger that 50.0 will lead to an inconsistency. Anyway, exp(50.0) > 5E21, so tread carefully.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_PBE_EXP_CAP [Double]

   :Example:

   .. code::

      IS_PBE_EXP_CAP 20.0

.. _is-pbe-neutralisation-scheme:

IS_PBE_NEUTRALISATION_SCHEME
----------------------------

:Type: String
:Default: '*undefined*'
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_PBE_NEUTRALISATION_SCHEME`

Neutralisation scheme for PBE solvation in PBCs

.. _is-pbe-temperature:

IS_PBE_TEMPERATURE
------------------

:Type: Double-Precision
:Default: -1.0
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_PBE_TEMPERATURE`

Implicit solvent: temperature for Boltzmann term

Sets the temperature for the Boltzmann term in implicit solvation. Has no effect if :ref:`is-pbe` is set to NONE or if implicit solvation is not in use.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_PBE_TEMPERATURE [Double]

   :Example:

   .. code::

      IS_PBE_TEMPERATURE 300.0

.. _is-pbe-use-fas:

IS_PBE_USE_FAS
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_PBE_USE_FAS`

[OBSOLETE] Should FAS be used for non-linear PBE

Specifies whether the full aproximation scheme (FAS) should be used for the solution of the Poisson-Boltzmann equation in implicit solvation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_PBE_USE_FAS [Boolean]

   :Example:

   .. code::

      IS_PBE_USE_FAS T

.. _is-restart-vac-from-vac:

IS_RESTART_VAC_FROM_VAC
-----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_RESTART_VAC_FROM_VAC`

Decides whether the vacuum calculation in an IS autosolvation calculation should be restarted from vacuum_* files or not

.. _is-sc-steric-cutoff:

IS_SC_STERIC_CUTOFF
-------------------

:Type: Physical
:Default: -1.0
:Unit: bohr
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_SC_STERIC_CUTOFF`

Implicit solvent: cutoff rad for softcore steric pot

Specifies the cutoff radius for the soft-core steric potential in implicit solvation with Boltzmann ions. Only relevant for implicit solvation calculations with non-zero salt concentrations. This works vastly differently than the hard-core steric potential (compare IS_HC_STERIC_CUTOFF ) -- here this parameter controls mostly computational efficiency, as the soft-core steric potential is only generated within :ref:`is-sc-steric-cutoff` from each physical ion core, and assumed to be zero elsewhere. This ensures linear scaling behaviour. The actual values of the steric potentials are controlled via :ref:`is-sc-steric-magnitude` and :ref:`is-sc-steric-smoothing-alpha` . The potential is shifted down by the value at IS_STERIC_CUTOFF to avoid discontinuities.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_SC_STERIC_CUTOFF [Physical]

   :Example:

   .. code::

      IS_SC_STERIC_CUTOFF 12.0 bohr

.. _is-sc-steric-magnitude:

IS_SC_STERIC_MAGNITUDE
----------------------

:Type: Physical
:Default: -1.0
:Unit: ha*bohr**12
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_SC_STERIC_MAGNITUDE`

Implicit solvent: softcore steric potential prefactor

Prefactor A in soft-core steric potential in implicit solvation with Boltzmann ions. The soft-core potential is the repulsive part of the LJ potential, i.e. A/r^12 centred around each ion, smoothed by multiplying by erf( :ref:`is-sc-steric-smoothing-alpha` *r)^12, then truncated at a truncation radius of :ref:`is-sc-steric-cutoff` , and shifted by a tiny amount to be zero at the truncation radius, to avoid a discontinuity.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_SC_STERIC_MAGNITUDE [Physical]

   :Example:

   .. code::

      IS_SC_STERIC_MAGNITUDE 2000 Ha*bohr^12

.. _is-sc-steric-smoothing-alpha:

IS_SC_STERIC_SMOOTHING_ALPHA
----------------------------

:Type: Physical
:Default: 1.5
:Unit: 1/bohr
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_SC_STERIC_SMOOTHING_ALPHA`

Implicit solvent: softcore steric pot erf parameter

Smoothing factor alpha in soft-core steric potential in implicit solvation with Boltzmann ions. The soft-core potential is the repulsive part of the LJ potential, i.e. IS_STERIC_MAGNITUDE /r^12 centred around each ion, smoothed by multiplying by erf(alpha*r)^12, then truncated at a truncation radius of IS_STERIC_CUTOFF , and shifted by a tiny amount to be zero at the truncation radius, to avoid a discontinuity.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_SC_STERIC_SMOOTHING_ALPHA [Physical]

   :Example:

   .. code::

      IS_SC_STERIC_SMOOTHING_ALPHA 1.2 bohr^-1

.. _is-separate-restart-files:

IS_SEPARATE_RESTART_FILES
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_SEPARATE_RESTART_FILES`

If true, dielectric cavity will be constructed from a second set of restart files

Causes the solute cavity used in implicit solvation calculations to be constructed from a separate set of restart files (.vacuum_dkn, .vacuum_tightbox_ngwfs) from those that are used to restart the calculation itself (.dkn, .tightbox_ngwfs).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_SEPARATE_RESTART_FILES [Logical]

   :Example:

   .. code::

      IS_SEPARATE_RESTART FILES T

.. _is-smeared-ion-rep:

IS_SMEARED_ION_REP
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_SMEARED_ION_REP`

Implicit solvent: use smeared ions for electrostatics

Turns the smeared ion representation on or off. All smeared ion calculations are performed in open boundary conditions. Turning on the smeared ion representation is a necessary condition for performing implicit solvent calculations. Calculations in vacuum that will serve as reference calculations for calculations in solvent should also used smeared ions. Smeared ions are not compatible with cutoff Coulomb ( :ref:`coulomb-cutoff-type` ) or Martyna-Tuckerman ( :ref:`pbc-correction-cutoff` ), which are other ways of realizing open boundary conditions.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_SMEARED_ION_REP [Logical]

   :Example:

   .. code::

      IS_SMEARED_ION_REP T

.. _is-smeared-ion-width:

IS_SMEARED_ION_WIDTH
--------------------

:Type: Physical
:Default: 0.8
:Unit: bohr
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_SMEARED_ION_WIDTH`

Implicit solvent: Width of Gaussian smearing

Sets the smearing width for smeared ions. This is only relevant when :ref:`is-smeared-ion-rep` is @T@. Values larger than default, especially larger than 1.0 bohr, are likely to lead to non-physical results in implicit solvent calculations. Values smaller than default, especially smaller than 0.6 bohr will negatively impact the convergence of the multigrid.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_SMEARED_ION_WIDTH [Value] [Unit]

   :Example:

   .. code::

      IS_SMEARED_ION_WIDTH 0.6 bohr

.. _is-soft-sphere-delta:

IS_SOFT_SPHERE_DELTA
--------------------

:Type: Double-Precision
:Default: 0.5
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_SOFT_SPHERE_DELTA`

Implicit solvent: Value delta used to define the smoothing function of the soft spheres.

.. _is-soft-sphere-radii:

IS_SOFT_SPHERE_RADII
--------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_SOFT_SPHERE_RADII`

Implicit solvent: Block of Van der Waals radii used to define the cavity size of elements in the soft sphere continuum model.

.. _is-soft-sphere-scale:

IS_SOFT_SPHERE_SCALE
--------------------

:Type: Double-Precision
:Default: 1.33
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_SOFT_SPHERE_SCALE`

Implicit solvent: Value used to parametrise the library of solvation radii.

.. _is-solvation-beta:

IS_SOLVATION_BETA
-----------------

:Type: Double-Precision
:Default: 1.3
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_SOLVATION_BETA`

Implicit solvent: beta parameter in Fattebert-Gygi functional

Sets the value of the beta parameter (unitless) in the definition of the dielectric cavity as described in DA Scherlis, J-L Fattebert, F Gygi, M Cococcioni, and N Marzari, Journal of Chemical Physics 124, 074103 (2006). This is only relevant in implicit solvent calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_SOLVATION_BETA [Value]

   :Example:

   .. code::

      IS_SOLVATION_BETA 1.6

.. _is-solvation-method:

IS_SOLVATION_METHOD
-------------------

:Type: String
:Default: 'direct'
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_SOLVATION_METHOD`

Implicit solvent: direct or corrective method

Chooses either the direct approach or a corrective approach to solving the Poisson equation in solvent. This keyword is reserved for future development, CORRECTIVE is not currently implemented. This is only relevant in implicit solvent calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_SOLVATION_METHOD [DIRECT | CORRECTIVE]

   :Example:

   .. code::

      IS_SOLVATION_METHOD DIRECT

.. _is-solvation-output-detail:

IS_SOLVATION_OUTPUT_DETAIL
--------------------------

:Type: String
:Default: 'none'
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_SOLVATION_OUTPUT_DETAIL`

Implicit solvent: controls extra output

With the sensible default of NONE no additional information is produced. With any other value, regardless of what it is, relevant solvation data, such as densities, potentials, dielectric permittivities, gradient terms are produced in 3D grid formats (cube, dx, grd -- depending on :ref:`cube-format` , :ref:`dx-format` and :ref:`grd-format` ) in every step. These consume a lot of disk space and should only be used for debugging.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_SOLVATION_OUTPUT_DETAIL [Text]

   :Example:

   .. code::

      IS_SOLVATION_OUTPUT_DETAIL SOME

.. _is-solvation-properties:

IS_SOLVATION_PROPERTIES
-----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`IS_SOLVATION_PROPERTIES`

Produce scalarfields of solvation inputs and outputs in properties?

.. _is-solvent-pressure:

IS_SOLVENT_PRESSURE
-------------------

:Type: Physical
:Default: -1.1896e-05
:Unit: ha/bohr**3
:Level: Basic
:Group: SOLVATION
:Search: :searchlink:`IS_SOLVENT_PRESSURE`

Adjust the pressure used for the SAV apolar model

.. _is-solvent-surface-tension:

IS_SOLVENT_SURFACE_TENSION
--------------------------

:Type: Physical
:Default: Unknown
:Unit: ha/bohr**2
:Level: Basic
:Group: SOLVATION
:Search: :searchlink:`IS_SOLVENT_SURFACE_TENSION`

[OBSOLETE] Use is_solvent_surf_tension_instead, specify unscaled value

Sets the surface tension of the solvent. This is only relevant in implicit solvent calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_SOLVENT_SURFACE_TENSION [Value] [Unit]

   :Example:

   .. code::

      IS_SOLVENT_SURFACE_TENSION 1.33859E-5 ha/bohr**2 ; corresponds to H2O with approximate inclusion of dispersion-repulsion

.. _is-solvent-surf-tension:

IS_SOLVENT_SURF_TENSION
-----------------------

:Type: Physical
:Default: 4.7624e-05
:Unit: ha/bohr**2
:Level: Basic
:Group: SOLVATION
:Search: :searchlink:`IS_SOLVENT_SURF_TENSION`

[OBSOLETE] Use is_solvent_surf_tension_instead, specify unscaled value

Sets the surface tension of the solvent. This is only relevant in implicit solvent calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_SOLVENT_SURF_TENSION [Value] [Unit]

   :Example:

   .. code::

      IS_SOLVENT_SURF_TENSION 4.7624E-5 ha/bohr**2 ; suitable for H2O, corresponds to 0.07415 N/m

.. _is-steric-pot-type:

IS_STERIC_POT_TYPE
------------------

:Type: String
:Default: 'X'
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_STERIC_POT_TYPE`

Implicit solvent: steric potential type

.. _is-steric-write:

IS_STERIC_WRITE
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_STERIC_WRITE`

Implicit solvent: write steric pot to file?

Specifies whether the steric potential (used in implicit solvation with Boltzmann ions) is to be written to a (dx/cube/grd) file.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_STERIC_WRITE [Boolean]

   :Example:

   .. code::

      IS_STERIC_WRITE T

.. _is-surface-thickness:

IS_SURFACE_THICKNESS
--------------------

:Type: Double-Precision
:Default: 0.0002
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`IS_SURFACE_THICKNESS`

Implicit solvent: thickness used for SA calculation

Sets the electronic iso-surface thickness (in atomic units of charge density) used to calculate the surface area of the dielectric cavity. This is only relevant in implicit solvent calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      IS_SURFACE_THICKNESS [Value]

   :Example:

   .. code::

      IS_SURFACE_THICKNESS 0.0003

.. _is-vac-ngwf-iter:

IS_VAC_NGWF_ITER
----------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Basic
:Group: SOLVATION
:Search: :searchlink:`IS_VAC_NGWF_ITER`

Allows users to specify number of vacuum NGWF iterations in autosolvation

.. _kerfix:

KERFIX
------

:Type: Integer
:Default: 1
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`KERFIX`

Density kernel fixing approach

.. _kernel-check-all:

KERNEL_CHECK_ALL
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`KERNEL_CHECK_ALL`

Turn on all kernel checking parameters

.. _kernel-christoffel-update:

KERNEL_CHRISTOFFEL_UPDATE
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`KERNEL_CHRISTOFFEL_UPDATE`

Update density kernel during NGWF line search

Preserve the density-matrix (idempotency, norm) to first order when the NGWFs change. Only implemented for zero-temperature ground-state calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KERNEL_CHRISTOFFEL_UPDATE [Logical]

   :Example:

   .. code::

      KERNEL_CHRISTOFFEL_UPDATE T

.. _kernel-cutoff:

KERNEL_CUTOFF
-------------

:Type: Physical
:Default: Unknown
:Unit: bohr
:Level: Basic
:Group: GENERAL
:Search: :searchlink:`KERNEL_CUTOFF`

Density kernel radius

Specifies the density kernel spatial cutoff. Matrix elements are only included if the corresponding NGWF centres are closer than this distance.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KERNEL_CUTOFF [Value] [Unit]

   :Example:

   .. code::

      KERNEL_CUTOFF 25.0 bohr

.. _kernel-diis-coeff:

KERNEL_DIIS_COEFF
-----------------

:Type: Double-Precision
:Default: 0.1
:Unit: None
:Level: None
:Group: CONV
:Search: :searchlink:`KERNEL_DIIS_COEFF`

Coefficient for the input kernel in linear mixing DIIS

Fraction of the output density kernel or Hamiltonian matrix in the inner loop DIIS. Its value must be in the range [0,1]. Set to a negative number to enable the ODA method for calculating the optimum mixing parameter. References: E. Cancès, and C. Le Bris, Int. J. Quantum Chem. 79(2):82, 2000. E. Cancès, J. Chem. Phys. 114(24):10616, 2001.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KERNEL_DIIS_COEFF [Real]

   :Example:

   .. code::

      KERNEL_DIIS_COEFF 0.2500

.. _kernel-diis-conv-criteria:

KERNEL_DIIS_CONV_CRITERIA
-------------------------

:Type: String
:Default: '1000'
:Unit: None
:Level: None
:Group: CONV
:Search: :searchlink:`KERNEL_DIIS_CONV_CRITERIA`

Density mixing convergence criteria

Set convergence criteria for inner loop diis. This input flag acts as a logical switch whose terms can only have the values 0 for false and 1 for true. Written as kernel_diis_criteria = wxyz, each component refers to: w : residual: sqrt[sum(K_{out} - K_{in})^2] x : [HKS,SKH] commutator y : delta energy gap (in Hartree) z : delta energy: E(n+1)-E(n) (in Hartree) Two or more elements activated means that the two criteria have to be true at the same time to achieve convergence (i.e. they have to be lower than kernel_diis_threshold).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KERNEL_DIIS_CRITERIA [Text]

   :Example:

   .. code::

      KERNEL_DIIS_CONV_CRITERIA 0110 (activates x and y but not w or z)

.. _kernel-diis-linear-iter:

KERNEL_DIIS_LINEAR_ITER
-----------------------

:Type: Integer
:Default: 5
:Unit: None
:Level: None
:Group: CONV
:Search: :searchlink:`KERNEL_DIIS_LINEAR_ITER`

Number of linear mixing iterations

Set the number of linear mixing iterations before activating Pulay, LiSTi or LiSTb mixing. The aim of these iterations is to generate a history of accurate density kernels to be used with the Pulay, LiSTi or LiSTb methods.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KERNEL_DIIS_LINEAR_ITER [Integer]

   :Example:

   .. code::

      KERNEL_DIIS_LINEAR_ITER 10

.. _kernel-diis-lshift:

KERNEL_DIIS_LSHIFT
------------------

:Type: Physical
:Default: 1.0
:Unit: hartree
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`KERNEL_DIIS_LSHIFT`

The initial value of Beta in the level shifting matrix

Value of the shift in energy of the conduction bands with the level-shifting technique during the inner loop DIIS. Reference: V. R. Saunders, and I. H. Hillier, Int. J. Quantum Chem. 7(4):699, 1973.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KERNEL_DIIS_LSHIFT [Value] [Units]

   :Example:

   .. code::

      KERNEL_DIIS_LSHIFT: 1 eV

.. _kernel-diis-ls-iter:

KERNEL_DIIS_LS_ITER
-------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`KERNEL_DIIS_LS_ITER`

Maximum Level shifting iteration

Number of iterations of the inner loop DIIS method with level-shifting enabled.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KERNEL_DIIS_LS_ITER [Integer]

   :Example:

   .. code::

      KERNEL_DIIS_LS_ITER: 5

.. _kernel-diis-maxit:

KERNEL_DIIS_MAXIT
-----------------

:Type: Integer
:Default: 25
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`KERNEL_DIIS_MAXIT`

Max number of kernel DIIS iterations

Maximum number of inner loop DIIS iterations

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KERNEL_DIIS_MAXIT [Integer]

   :Example:

   .. code::

      KERNEL_DIIS_MAXIT 40

.. _kernel-diis-scheme:

KERNEL_DIIS_SCHEME
------------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`KERNEL_DIIS_SCHEME`

Select scheme for kernel-diis

Enable self-consistent density kernel or Hamiltonian mixing during the inner loop. Possible options: NONE - no mixing - use LNV optimisation method instead. DKN_LINEAR - linear mixing of density kernels. HAM_LINEAR - linear mixing of Hamiltonians. DKN_PULAY - Pulay mixing of density kernels. HAM_PULAY - Pulay mixing of Hamiltonians. DKN_LISTI - LiSTi mixing of density kernels. HAM_LISTI - LiSTi mixing of Hamiltonians. DKN_LISTB - LiSTb mixing of density kernels. HAM_LISTB - LiSTb mixing of Hamiltonians. DIAG - no mixing, only Hamiltonian diagonalisation. Not recommended. References: P. Pulay, Chem. Phys. Lett. 73(2):393, 1980. Y. A. Wang, C. Y. Yam, Y. K. Chen, and G. Chen, J. Chem. Phys. 134(24):241103, 2011 Y. K. Chen, and Y. A. Wang, J. Chem. Theory Comput. 7(10):3045, 2011.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KERNEL_DIIS_SCHEME [Text]

   :Example:

   .. code::

      KERNEL_DIIS_SCHEME DKN_PULAY

.. _kernel-diis-size:

KERNEL_DIIS_SIZE
----------------

:Type: Integer
:Default: 10
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`KERNEL_DIIS_SIZE`

Max number of kernels saved during kernel DIIS

Maximum number of density kernel or Hamiltonian matrices that will be stored in memory. These kernels are then used with the Pulay, LiSTi or LiSTb schemes to generate the next input matrix. Warning: the more matrices are stored, the better the convergence will be, but also the more memory resources will be needed.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KERNEL_DIIS_SIZE [Integer]

   :Example:

   .. code::

      KERNEL_DIIS_SIZE 25

.. _kernel-diis-threshold:

KERNEL_DIIS_THRESHOLD
---------------------

:Type: Double-Precision
:Default: 1e-09
:Unit: None
:Level: None
:Group: CONV
:Search: :searchlink:`KERNEL_DIIS_THRESHOLD`

Density mixing convergence threshold

Convergence threshold for the inner loop self-consistent optimisation. It acts for all active values of kernel_diis_conv_criteria.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KERNEL_DIIS_THRESHOLD [Real]

   :Example:

   .. code::

      kernel_diis_thres 1.0e-7

.. _kernel-force-conv:

KERNEL_FORCE_CONV
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`KERNEL_FORCE_CONV`

Force density kernel convergence on last NGWFs optimization step

.. _kernel-track-mid-occ:

KERNEL_TRACK_MID_OCC
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`KERNEL_TRACK_MID_OCC`

Print middle occupancy after LNV convergence

.. _kernel-update:

KERNEL_UPDATE
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`KERNEL_UPDATE`

Update density kernel during NGWF line search

Update the density kernel when taking a trial step for NGWF optimization.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KERNEL_UPDATE [Logical]

   :Example:

   .. code::

      KERNEL_UPDATE T

.. _ke-density-calculate:

KE_DENSITY_CALCULATE
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: ELD
:Search: :searchlink:`KE_DENSITY_CALCULATE`

Calculate kinetic energy density

Calculate kinetic energy density.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KE_DENSITY_CALCULATE [Logical]

   :Example:

   .. code::

      KE_DENSITY_CALCULATE T

.. _ke-density-init:

KE_DENSITY_INIT
---------------

:Type: String
:Default: 'GGA'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`KE_DENSITY_INIT`

How the KE density should be initialised.

.. _kpoints-list:

KPOINTS_LIST
------------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`KPOINTS_LIST`

K-point list to be used for BZ sampling in scf calculation

K-point list for SCF calculation

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK KPOINTS_LIST
      k1x k1y k1z w1
      k2x k2y k2z w2
       .   .   .
      kNx kNy kNz wN
      %ENDBLOCK KPOINTS_LIST

   :Example:

   .. code::

      %BLOCK KPOINTS_LIST
      0.0 0.0 0.0 0.5
      0.0 0.0 0.5 0.5
      %ENDBLOCK KPOINTS_LIST

.. _kpoint-gamma-centred:

KPOINT_GAMMA_CENTRED
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`KPOINT_GAMMA_CENTRED`

force the k-point grid to be gamma centred. If false, whether gamma point is included depends on kpoint_grid_size and kpoint_grid_shift. Does not affect user defined k-grid

.. _kpoint-grid-shift:

KPOINT_GRID_SHIFT
-----------------

:Type: String
:Default: '0 0 0'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`KPOINT_GRID_SHIFT`

shift of the k-point grid

K-point grid shift for SCF calculation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KPOINT_GRID_SHIFT [Text]

   :Example:

   .. code::

      KPOINT_GRID_SHIFT 1 1 1

.. _kpoint-grid-size:

KPOINT_GRID_SIZE
----------------

:Type: String
:Default: '1 1 1'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`KPOINT_GRID_SIZE`

size of the k-point grid

K-point grid for SCF calculation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KPOINT_GRID_SIZE [Text]

   :Example:

   .. code::

      KPOINT_GRID_SIZE 3 3 3

.. _kpoint-method:

KPOINT_METHOD
-------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`KPOINT_METHOD`

Method for sampling of BZ

K-point method for SCF calculation: "Plane-Wave" (PW) or "Tight-binding" (TB)

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      KPOINT_METHOD [Text]

   :Example:

   .. code::

      KPOINT_METHOD TB

.. _kpoint-mp-spacing:

KPOINT_MP_SPACING
-----------------

:Type: Physical
:Default: 0.0
:Unit: 1/bohr
:Level: Intermediate
:Group: None
:Search: :searchlink:`KPOINT_MP_SPACING`

minimum spacing of the k-point grid

.. _k-smooth:

K_SMOOTH
--------

:Type: Physical
:Default: 5.0
:Unit: 1/bohr
:Level: Expert
:Group: None
:Search: :searchlink:`K_SMOOTH`

Characteristic wavevector of the smoothing function(NGWF gradient in reciprocal space

.. _k-zero:

K_ZERO
------

:Type: Physical
:Default: 3.0
:Unit: 1/bohr
:Level: Expert
:Group: CONV
:Search: :searchlink:`K_ZERO`

KE preconditioning parameter

Specifies the kinetic energy preconditioning parameter. See Mostofi et al.,J. Chem. Phys.119, 8842 (2003) for further details.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      K_ZERO [Value] [Unit]

   :Example:

   .. code::

      K_ZERO 4.0 bohr

.. _lattice-abc:

LATTICE_ABC
-----------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: CELLDATA
:Search: :searchlink:`LATTICE_ABC`

The simulation cell vectors

.. _lattice-cart:

LATTICE_CART
------------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: CELLDATA
:Search: :searchlink:`LATTICE_CART`

The simulation cell lattice vectors

Specifies the lattice vectors a1 , a2 and a3 for the simulation cell as Cartesian coordinates. By default, these will be interpreted as being in atomic units (a0), but they will be interpreted as being Angstroms if "ang" is on the first line of the block.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK LATTICE_CART
      a1x a1y a1z
      a2x a2y a2z
      a3x a3y a3z
      %ENDBLOCK LATTICE_CART

   :Example:

   .. code::

      %BLOCK LATTICE_CART
       7.500000 0.000000 0.000000 ; hexagonal unit cell with
      -3.750000 6.495191 0.000000 ;   a = 7.5 a0
       0.000000 0.000000 9.000000 ;   c = 9.0 a0
      %ENDBLOCK LATTICE_CART
      or
      %BLOCK LATTICE_CART
      ang
       50.000000  0.000000  0.000000 ; large cubic cell
        0.000000 50.000000  0.000000 ;
        0.000000  0.000000 50.000000 ;
      %ENDBLOCK LATTICE_CART

.. _libxc-c-func-id:

LIBXC_C_FUNC_ID
---------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: XC
:Search: :searchlink:`LIBXC_C_FUNC_ID`

Functional identifier for which correlation functional to use with LIBXC - see LIBXC documentation

Functional ID for the correlation functional (used in calculations employing the LIBXC library). The value of FUNCTIONAL must be set to LIBXC for this value to be accessed

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LIBXC_C_FUNC_ID [Integer]

   :Example:

   .. code::

      LIBXC_C_FUNC_ID 13

.. _libxc-x-func-id:

LIBXC_X_FUNC_ID
---------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: XC
:Search: :searchlink:`LIBXC_X_FUNC_ID`

Functional identifier for which exchange functional to use with LIBXC - see LIBXC documentation

Functional ID for the exchange functional (used in calculations employing the LIBXC library). The value of FUNCTIONAL must be set to LIBXC for this value to be accessed

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LIBXC_X_FUNC_ID [Integer]

   :Example:

   .. code::

      LIBXC_X_FUNC_ID 13

.. _lnv-cg-max-step:

LNV_CG_MAX_STEP
---------------

:Type: Double-Precision
:Default: 3.0
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`LNV_CG_MAX_STEP`

Maximum length of trial step for kernel optimisation line search

Maximum length of trial step for kernel optimisation line search

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LNV_CG_MAX_STEP [Value]

   :Example:

   .. code::

      LNV_CG_MAX_STEP 10.0

.. _lnv-cg-type:

LNV_CG_TYPE
-----------

:Type: String
:Default: 'LNV_FLETCHER'
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`LNV_CG_TYPE`

Type of CG coefficient for LNV denskern optimisation  LNV_POLAK = Polak-Ribbiere formula;  LNV_FLETCHER = Fletcher-Reeves formula.

Specifies the variant of the conjugate gradients algorithm used for the optimization of the density kernel, currently either LNV_FLETCHER for Fletcher-Reeves or LNV_POLAK for Polak-Ribiere.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LNV_CG_TYPE [Text]

   :Example:

   .. code::

      LNV_CG_TYPE LNV_POLAK

.. _lnv-check-trial-steps:

LNV_CHECK_TRIAL_STEPS
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`LNV_CHECK_TRIAL_STEPS`

Check stability of kernel at each trial step during LNV

Activate checks on the stability of kernel at each trial step during LNV line search. Checks occupancy bounds and RMS occupancy error

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LNV_CHECK_TRIAL_STEPS [Logical]

   :Example:

   .. code::

      LNV_CHECK_TRIAL_STEPS T

.. _lnv-threshold-orig:

LNV_THRESHOLD_ORIG
------------------

:Type: Double-Precision
:Default: 1e-09
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`LNV_THRESHOLD_ORIG`

LNV convergence threshold

Specifies the convergence threshold for the RMS gradient of the density kernel.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LNV_THRESHOLD_ORIG [Real]

   :Example:

   .. code::

      LNV_THRESHOLD_ORIG 1.0e-8

.. _locpot-scheme:

LOCPOT_SCHEME
-------------

:Type: String
:Default: 'FULL'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`LOCPOT_SCHEME`

Scheme for evaluating local potential matrix elements  FULL = Calculate matrix and symmetrize; LOWER = Calculate lower triangle only and expand; ALTERNATE = Calculate alternating elements from both triangles and expand

Scheme for evaluating local potential matrix elements. Possible values: FULL = Calculate matrix and symmetrize explicitly; LOWER = Calculate lower triangle elements only and infer upper triangle; ALTERNATE = Calculate alternating elements from both triangles and expand (fastest).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LOCPOT_SCHEME [Text]

   :Example:

   .. code::

      LOCPOT_SCHEME ALTERNATE

.. _lowdin-popn-calculate:

LOWDIN_POPN_CALCULATE
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`LOWDIN_POPN_CALCULATE`

Allow Lowdin population analysis

.. _lr-optical-permittivity:

LR_OPTICAL_PERMITTIVITY
-----------------------

:Type: Double-Precision
:Default: Unknown
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_OPTICAL_PERMITTIVITY`

Optical permittivity of solvent used in SCF response in TDDFT

.. _lr-phonons-calculate:

LR_PHONONS_CALCULATE
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRPHONONS
:Search: :searchlink:`LR_PHONONS_CALCULATE`

enables LR-PHONONS calculation

.. _lr-phonons-kernel-cutoff:

LR_PHONONS_KERNEL_CUTOFF
------------------------

:Type: Physical
:Default: 1000.0
:Unit: bohr
:Level: Expert
:Group: None
:Search: :searchlink:`LR_PHONONS_KERNEL_CUTOFF`

sets cutoff on the effective response density kernel

.. _lr-phonons-restart:

LR_PHONONS_RESTART
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`LR_PHONONS_RESTART`

Restart from previously written force constants

.. _lr-phonons-zero-dim:

LR_PHONONS_ZERO_DIM
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`LR_PHONONS_ZERO_DIM`

Ensure correction of dynamical matrix for molecules

.. _lr-tddft-analysis:

LR_TDDFT_ANALYSIS
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_ANALYSIS`

Do a full O(N^3) analysis of TDDFT transitions

If the flag is set to True, a full cubic-scalling analysis of each TDDFT excitation is performed in which the response density is decomposed into dominant Kohn-Sham transitions.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_ANALYSIS [Logical]

   :Example:

   .. code::

      LR_TDDFT_ANALYSIS True

.. _lr-tddft-calculate:

LR_TDDFT_CALCULATE
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_CALCULATE`

enables LR-TDDFT calculation

.. _lr-tddft-cg-threshold:

LR_TDDFT_CG_THRESHOLD
---------------------

:Type: Double-Precision
:Default: 1e-06
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_CG_THRESHOLD`

sets convergence tolerance for CG routine

The keyword specifies the convergence tolerance on the sum of the n TDDFT excitation energies. If the sum of excitation energies changes by less than :ref:`lr-tddft-cg-threshold` in two consecutive iterations, the calculation is taken to be converged.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_CG_THRESHOLD [Real]

   :Example:

   .. code::

      LR_TDDFT_CG_THRESHOLD 5.0E-7

.. _lr-tddft-check-conv-iter:

LR_TDDFT_CHECK_CONV_ITER
------------------------

:Type: Integer
:Default: 5
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_CHECK_CONV_ITER`

Num of iterations at which conv of states is checked

.. _lr-tddft-ct-length:

LR_TDDFT_CT_LENGTH
------------------

:Type: Physical
:Default: 20.0
:Unit: bohr
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_CT_LENGTH`

Charge-tranfer length for definition of the TDDFTresponse matrix

.. _lr-tddft-homo-num:

LR_TDDFT_HOMO_NUM
-----------------

:Type: Integer
:Default: 20
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_HOMO_NUM`

Defines number of occ KS transitions considered in TDDFT analysis.

.. _lr-tddft-init-max-overlap:

LR_TDDFT_INIT_MAX_OVERLAP
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_INIT_MAX_OVERLAP`

If set to T, initialise to KS transitions that maximise the elec-hole overlap, ie. not charge transfer states

.. _lr-tddft-init-random:

LR_TDDFT_INIT_RANDOM
--------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_INIT_RANDOM`

Set whether initial TDDFT vectors are set to random matrices or pure KS transitions with minimum energies

.. _lr-tddft-joint-set:

LR_TDDFT_JOINT_SET
------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_JOINT_SET`

Use joint set to represent cond states

If the flag is set to T, the joint NGWF set is used to represent the conduction space in the LR-TDDFT calculation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_JOINT_SET [Logical]

   :Example:

   .. code::

      LR_TDDFT_JOINT_SET False

.. _lr-tddft-kernel-cutoff:

LR_TDDFT_KERNEL_CUTOFF
----------------------

:Type: Physical
:Default: 1000.0
:Unit: bohr
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_KERNEL_CUTOFF`

sets cutoff on the effective response density kernel

Keyword sets a truncation radius on all response density kernels in order to achieve linear scaling computational effort with system size.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_KERNEL_CUTOFF [Value] [Unit]

   :Example:

   .. code::

      LR_TDDFT_KERNEL_CUTOFF 30.0 bohr

.. _lr-tddft-lumo-num:

LR_TDDFT_LUMO_NUM
-----------------

:Type: Integer
:Default: 20
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_LUMO_NUM`

Defines number of unocc KS transitions considered in TDDFT analysis.

.. _lr-tddft-maxit-cg:

LR_TDDFT_MAXIT_CG
-----------------

:Type: Integer
:Default: 60
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_MAXIT_CG`

sets the maximum number of iterations for CG routine

.. _lr-tddft-maxit-pen:

LR_TDDFT_MAXIT_PEN
------------------

:Type: Integer
:Default: 20
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_MAXIT_PEN`

sets the maximum number of iterations for penalty functional routine

The maximum number purification iterations performed per conjugate gradient step.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_MAXIT_PEN [Integer]

   :Example:

   .. code::

      LR_TDDFT_MAXIT_PEN 50

.. _lr-tddft-mgga-gauge-corr:

LR_TDDFT_MGGA_GAUGE_CORR
------------------------

:Type: Boolean
:Default: None
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`LR_TDDFT_MGGA_GAUGE_CORR`

Whether to include the gauge correction term in LR-TDDFT calculations with mGGAs

.. _lr-tddft-mlwf-analysis:

LR_TDDFT_MLWF_ANALYSIS
----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_MLWF_ANALYSIS`

If set to T, a maximally localised wannier function analysis of the converged TDDFT evecs is performed

.. _lr-tddft-mom-mat-els:

LR_TDDFT_MOM_MAT_ELS
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_MOM_MAT_ELS`

Compute oscillator strengths in momentum rather than position space

.. _lr-tddft-num-conv-states:

LR_TDDFT_NUM_CONV_STATES
------------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_NUM_CONV_STATES`

Sets the number of already converged states.

.. _lr-tddft-num-states:

LR_TDDFT_NUM_STATES
-------------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_NUM_STATES`

Sets the number of excitation energies we want to solve for

The keyword specifies how many excitations we want to converge. If set to a positive integer n, the TDDFT algorithm will converge the n lowest excitations of the system.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_NUM_STATES [Integer]

   :Example:

   .. code::

      LR_TDDFT_NUM_STATES 10

.. _lr-tddft-penalty-func:

LR_TDDFT_PENALTY_FUNC
---------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_PENALTY_FUNC`

If set to F, the idempotency violation through a penalty functional is not computed, and no iterative improvements are performed

.. _lr-tddft-penalty-tol:

LR_TDDFT_PENALTY_TOL
--------------------

:Type: Double-Precision
:Default: 1e-08
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_PENALTY_TOL`

sets the convergence tolerance for the Penalty functional routine

Keyword sets a tolerance for the penalty functional. If the penalty functional is larger than LR_TDDFT_PENALTY_TOL, the algorithm will perform purification iterations in order to decrease the penalty value and force towards the correct idempotency behaviour.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_PENALTY_TOL [Real]

   :Example:

   .. code::

      LR_TDDFT_PENALTY_TOL 5.0E-9

.. _lr-tddft-precond:

LR_TDDFT_PRECOND
----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_PRECOND`

If set to T, TDDFT search direction gets preconditioned

.. _lr-tddft-precond-iter:

LR_TDDFT_PRECOND_ITER
---------------------

:Type: Integer
:Default: 20
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_PRECOND_ITER`

Max number of iterations in applying the preconditioner

.. _lr-tddft-precond-tol:

LR_TDDFT_PRECOND_TOL
--------------------

:Type: Double-Precision
:Default: 1e-06
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_PRECOND_TOL`

Convergence tolerance in applying the preconditioner

.. _lr-tddft-preopt:

LR_TDDFT_PREOPT
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_PREOPT`

Refine starting guess in preoptimisation routine

.. _lr-tddft-preopt-iter:

LR_TDDFT_PREOPT_ITER
--------------------

:Type: Integer
:Default: 20
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_PREOPT_ITER`

Number of preoptimisation iterations

.. _lr-tddft-projector:

LR_TDDFT_PROJECTOR
------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_PROJECTOR`

Use projector onto unoccupied subspace

If the flag is set to True, the conduction density matrix is redefined to be a projector onto the entire unoccupied subspace.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_PROJECTOR [Logical]

   :Example:

   .. code::

      LR_TDDFT_PROJECTOR False

.. _lr-tddft-reset-cg:

LR_TDDFT_RESET_CG
-----------------

:Type: Integer
:Default: 100
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_RESET_CG`

sets the number of iterations after which the search direction gets reset

.. _lr-tddft-restart:

LR_TDDFT_RESTART
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_RESTART`

Restart flag for the LR_TDDFT option

If the flag is set to True, the algorithm reads in :ref:`lr-tddft-num-states` response density kernels in .dkn format and uses them as initial trial vectors for a restarted LR-TDDFT calculation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_RESTART [Logical]

   :Example:

   .. code::

      LR_TDDFT_RESTART True

.. _lr-tddft-restart-from-tda:

LR_TDDFT_RESTART_FROM_TDA
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_RESTART_FROM_TDA`

Option to restart RPA calculation from Tamm-Dancoff response kernels

.. _lr-tddft-rpa:

LR_TDDFT_RPA
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_RPA`

If true, perform a full LR_TDDFT calculation rather than the Tamm-Dancoff approx.

If the flag is set to True, a full TDDFT calculation in the so-called "Random Phase Approximation" will be performed, rather than invoking the Tamm-Dancoff approximation

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_RPA [Logical]

   :Example:

   .. code::

      LR_TDDFT_RPA True

.. _lr-tddft-spectrum-smear:

LR_TDDFT_SPECTRUM_SMEAR
-----------------------

:Type: Physical
:Default: Unknown
:Unit: hartree
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_SPECTRUM_SMEAR`

Gaussian smearing half-width for LR-TDDFT spectrum

.. _lr-tddft-subsystem-coupling:

LR_TDDFT_SUBSYSTEM_COUPLING
---------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_SUBSYSTEM_COUPLING`

Compute coupling between subsystems in LRTDDFT

.. _lr-tddft-triplet:

LR_TDDFT_TRIPLET
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_TRIPLET`

DEtermines if triplet states are calculated or singlets

Flag that decides whether the :ref:`lr-tddft-num-states` states to be converged are singlet or triplet states.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_TRIPLET [Logical]

   :Example:

   .. code::

      lt_tddft_triplet T

.. _lr-tddft-write-densities:

LR_TDDFT_WRITE_DENSITIES
------------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_WRITE_DENSITIES`

Determines whether to write out TDDFT response densities

If the flag is set to True, the response density, electron density and hole density for each excitation is computed and written into a .cube file.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_WRITE_DENSITIES [Logical]

   :Example:

   .. code::

      LR_TDDFT_WRITE_DENSITIES False

.. _lr-tddft-write-kernels:

LR_TDDFT_WRITE_KERNELS
----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_WRITE_KERNELS`

writes out response kernels after each iteration

If the flag is set to T, the TDDFT response density kernels are printed out at every conjugate gradient iteration. These files are necessary to restart a LR-TDDFT calculation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LR_TDDFT_WRITE_KERNELS [Logical]

   :Example:

   .. code::

      LR_TDDFT_WRITE_KERNELS False

.. _lr-tddft-xc-finite-diff:

LR_TDDFT_XC_FINITE_DIFF
-----------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`LR_TDDFT_XC_FINITE_DIFF`

Evaluate fxc using finite difference technique.

.. _lumo-dens-plot:

LUMO_DENS_PLOT
--------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`LUMO_DENS_PLOT`

Number of squared MOs to plot from LUMO and higher

Specifies the number of canonical orbitals above the LUMO to plot, if :ref:`do-properties` is set to true. Thus a value of zero plots only the LUMO, a negative value disables plotting and a positive value of N plots the N+1 lowest unoccupied canonical orbitals.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LUMO_DENS_PLOT [Integer]

   :Example:

   .. code::

      LUMO_DENS_PLOT 0

.. _lumo-plot:

LUMO_PLOT
---------

:Type: Integer
:Default: 5
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`LUMO_PLOT`

Number of MOs to plot from LUMO and higher

Specifies the number of canonical orbitals above the LUMO to plot, if :ref:`do-properties` is set to true. Thus a value of zero plots only the LUMO, a negative value disables plotting and a positive value of N plots the N+1 lowest unoccupied canonical orbitals.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      LUMO_PLOT [Integer]

   :Example:

   .. code::

      LUMO_PLOT 0

.. _maxit-cdft-u-cg:

MAXIT_CDFT_U_CG
---------------

:Type: Integer
:Default: 60
:Unit: None
:Level: Intermediate
:Group: CDFT
:Search: :searchlink:`MAXIT_CDFT_U_CG`

Max number of cdFT-U conjugate gradients (CG) iterations

Specifies the maximum number of iterations for the constraining potentials (Uq/s) conjugate gradients optimisation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MAXIT_CDFT_U_CG [Integer]

   :Example:

   .. code::

      MAXIT_CDFT_U_CG 1

.. _maxit-hotelling:

MAXIT_HOTELLING
---------------

:Type: Integer
:Default: 50
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`MAXIT_HOTELLING`

Number of Hotelling iteration per NGWF change

Specifies the maximum number of iterations in the Hotelling algorithm used to invert the overlap matrix. See Ozaki,Phys. Rev. B.64, 195110 (2001) for more details. If :ref:`maxit-hotelling` is zero, then the inverse is computed using a traditional O(N^3) method.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MAXIT_HOTELLING [Integer]

   :Example:

   .. code::

      MAXIT_HOTELLING 100

.. _maxit-kernel-fix:

MAXIT_KERNEL_FIX
----------------

:Type: Integer
:Default: 3
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`MAXIT_KERNEL_FIX`

Maximum # iterations of Penalty Functional idempotency correction per LNV step

.. _maxit-kernel-occ-check:

MAXIT_KERNEL_OCC_CHECK
----------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`MAXIT_KERNEL_OCC_CHECK`

Maximum number of kernel resets after occupancy checks

.. _maxit-lnv:

MAXIT_LNV
---------

:Type: Integer
:Default: 8
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`MAXIT_LNV`

Max number of LNV iterations

Specifies the maximum number of iterations for the density kernel optimization.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MAXIT_LNV [Integer]

   :Example:

   .. code::

      MAXIT_LNV 3

.. _maxit-ngwf-cg:

MAXIT_NGWF_CG
-------------

:Type: Integer
:Default: 60
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`MAXIT_NGWF_CG`

Max number of NGWF conjugate gradients (CG) iterations

Specifies the maximum number of iterations for the NGWF conjugate gradients optimization.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MAXIT_NGWF_CG [Integer]

   :Example:

   .. code::

      MAXIT_NGWF_CG 25

.. _maxit-ngwf-cg-confined:

MAXIT_NGWF_CG_CONFINED
----------------------

:Type: Integer
:Default: 5
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`MAXIT_NGWF_CG_CONFINED`

Number of iterations for which the NGWFs are explicitly confined

.. _maxit-palser-mano:

MAXIT_PALSER_MANO
-----------------

:Type: Integer
:Default: 200
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`MAXIT_PALSER_MANO`

Maximum number of iterations for Palser-Manolopoulos scheme

Specifies the maximum number of iterations for the Palser-Manolopoulos algorithm [Phys. Rev. B.58, 12704 (1998)] used to initialize the density kernel before the main optimization begins (when :ref:`coreham-denskern-guess` is true, the default). If :ref:`maxit-palser-mano` is negative then a traditionalO(N3) diagonalization is used.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MAXIT_PALSER_MANO [Integer]

   :Example:

   .. code::

      MAXIT_PALSER_MANO 30

.. _maxit-pen:

MAXIT_PEN
---------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`MAXIT_PEN`

Max number of penalty functional iterations

Specifies the maximum number of iterations for the penalty-functional algorithm [ Hayneset al.,Phys. Rev. B.59, 12173 (1999) ] used to refine the density kernel intialization before the main optimization begins. When reading the density kernel from disk this should normally be set to zero.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MAXIT_PEN [Integer]

   :Example:

   .. code::

      MAXIT_PEN 5

.. _max-resid-hotelling:

MAX_RESID_HOTELLING
-------------------

:Type: Double-Precision
:Default: 1e-12
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`MAX_RESID_HOTELLING`

Max allowed value in Hotelling residual

Specifies the maximum residual allowed when inverting the overlap matrix by the Hotelling method. See Ozaki,Phys. Rev. B.64, 195110 (2001) for more details.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MAX_RESID_HOTELLING [Real]

   :Example:

   .. code::

      MAX_RESID_HOTELLING 1.0e-10

.. _md-autocorr:

MD_AUTOCORR
-----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: MD
:Search: :searchlink:`MD_AUTOCORR`

Keyword to output real and auxiliary kernels to external files during Niklasson/Berendsen propagation

.. _md-aux-beren-tc:

MD_AUX_BEREN_TC
---------------

:Type: Physical
:Default: 413.41105
:Unit: aut
:Level: Intermediate
:Group: MD
:Search: :searchlink:`MD_AUX_BEREN_TC`

Set the value for the relaxation time in the Berendsen coupling

.. _md-aux-dkn-t:

MD_AUX_DKN_T
------------

:Type: Physical
:Default: 100.0
:Unit: 1/aut**2
:Level: Intermediate
:Group: MD
:Search: :searchlink:`MD_AUX_DKN_T`

Target temperature of the auxiliary density kernel

.. _md-aux-rep:

MD_AUX_REP
----------

:Type: String
:Default: 'ASYM'
:Unit: None
:Level: Expert
:Group: MD
:Search: :searchlink:`MD_AUX_REP`

Specify the representation of the auxiliary density matrix  for the XLBOMD

.. _md-delta-t:

MD_DELTA_T
----------

:Type: Physical
:Default: 40.0
:Unit: aut
:Level: Basic
:Group: MD
:Search: :searchlink:`MD_DELTA_T`

Molecular dynamics time step

Specifies the time step for molecular dynamics.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MD_DELTA_T [Value] [Unit]

   :Example:

   .. code::

      MD_DELTA_T 1.0 fs

.. _md-global-restart:

MD_GLOBAL_RESTART
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: MD
:Search: :searchlink:`MD_GLOBAL_RESTART`

Option to restart the md calculation with electronic history

.. _md-lnv-threshold:

MD_LNV_THRESHOLD
----------------

:Type: Double-Precision
:Default: 1e-09
:Unit: None
:Level: Expert
:Group: MD
:Search: :searchlink:`MD_LNV_THRESHOLD`

Threshold for the lnv loop when doing extrapolation

.. _md-ngwf-threshold:

MD_NGWF_THRESHOLD
-----------------

:Type: Double-Precision
:Default: 2e-06
:Unit: None
:Level: Expert
:Group: MD
:Search: :searchlink:`MD_NGWF_THRESHOLD`

Threshold for the outer loop when doing extrapolation

.. _md-num-iter:

MD_NUM_ITER
-----------

:Type: Integer
:Default: 100
:Unit: None
:Level: Basic
:Group: MD
:Search: :searchlink:`MD_NUM_ITER`

Maximum number of molecular dynamics iterations

Specifies the number of molecular dynamics steps.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MD_NUM_ITER [Integer]

   :Example:

   .. code::

      MD_NUM_ITER 1000

.. _md-output-detail:

MD_OUTPUT_DETAIL
----------------

:Type: String
:Default: 'DEFAULT'
:Unit: None
:Level: Basic
:Group: MD
:Search: :searchlink:`MD_OUTPUT_DETAIL`

Level of output detail for MD: BRIEF, NORMAL or VERBOSE

.. _md-properties:

MD_PROPERTIES
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: MD
:Search: :searchlink:`MD_PROPERTIES`

Compute vibrational and IR spectra from MD

.. _md-reset-history:

MD_RESET_HISTORY
----------------

:Type: Integer
:Default: 100
:Unit: None
:Level: Intermediate
:Group: MD
:Search: :searchlink:`MD_RESET_HISTORY`

Reset mixing scheme for initial guess of NGWFs and density kernel

By default, in a molecular dynamics calculation, the initial guess for the electronic degrees of freedom is provided by the optimized NGWFs and density kernel from the previous time step. :ref:`md-reset-history` specifies the number of MD steps to be performed before the generation of new initial guesses for the NGWFs and density kernel. See :ref:`mix-dkn-type` and :ref:`mix-ngwfs-type` for more advanced mixing options.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MD_RESET_HISTORY [Integer]

   :Example:

   .. code::

      MD_RESET_HISTORY 1000

.. _md-restart:

MD_RESTART
----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: MD
:Search: :searchlink:`MD_RESTART`

Restart MD from backup files

Restart the molecular dynamics calculation from previously generated backup files (i.e. *.md.restart and *.thermo.restart files).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MD_RESTART [Logical]

   :Example:

   .. code::

      MD_RESTART T

.. _md-restart-thermo:

MD_RESTART_THERMO
-----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: MD
:Search: :searchlink:`MD_RESTART_THERMO`

Restart MD from .thermo.restart file

.. _md-write-history:

MD_WRITE_HISTORY
----------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Intermediate
:Group: MD
:Search: :searchlink:`MD_WRITE_HISTORY`

Write mixing scheme for initial guess of NGWFs and density kernel

.. _md-write-out:

MD_WRITE_OUT
------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: MD
:Search: :searchlink:`MD_WRITE_OUT`

Makes MD restart output cleaner

.. _mermin:

MERMIN
------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: MERMIN
:Search: :searchlink:`MERMIN`

Use mermin method to optimise the kernel

.. _mermin-cg-max-step:

MERMIN_CG_MAX_STEP
------------------

:Type: Double-Precision
:Default: 3.0
:Unit: None
:Level: Expert
:Group: MERMIN
:Search: :searchlink:`MERMIN_CG_MAX_STEP`

Maximum length of trial step for kernel optimisation  line search

.. _mermin-cg-type:

MERMIN_CG_TYPE
--------------

:Type: String
:Default: 'MERMIN_FLETCHER'
:Unit: None
:Level: Expert
:Group: MERMIN
:Search: :searchlink:`MERMIN_CG_TYPE`

Type of CG coefficient for :ref:`mermin` denskern optimisation  MERMIN_POLAK = Polak-Ribbiere formula;  MERMIN_FLETCHER = Fletcher-Reeves formula.

.. _mermin-cheb:

MERMIN_CHEB
-----------

:Type: Integer
:Default: 11
:Unit: None
:Level: Intermediate
:Group: MERMIN
:Search: :searchlink:`MERMIN_CHEB`

Chebyshev expansion to be used in mermin mod

.. _mermin-check:

MERMIN_CHECK
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: MERMIN
:Search: :searchlink:`MERMIN_CHECK`

Check kernel search direction during mermin optimisation

.. _mermin-check-trial-steps:

MERMIN_CHECK_TRIAL_STEPS
------------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: MERMIN
:Search: :searchlink:`MERMIN_CHECK_TRIAL_STEPS`

Check stability of kernel at each trial step during LNV

.. _mermin-free-energy-thres:

MERMIN_FREE_ENERGY_THRES
------------------------

:Type: Physical
:Default: 1e-06
:Unit: hartree
:Level: Expert
:Group: MERMIN
:Search: :searchlink:`MERMIN_FREE_ENERGY_THRES`

Convergence threshold for the free energy  in :ref:`mermin` calculations

.. _mermin-inv-init:

MERMIN_INV_INIT
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: MERMIN
:Search: :searchlink:`MERMIN_INV_INIT`

Initialise the kernel as normalised S^-1 (identical occupation for all NGWFs)

.. _mermin-maxit:

MERMIN_MAXIT
------------

:Type: Integer
:Default: 10
:Unit: None
:Level: Intermediate
:Group: MERMIN
:Search: :searchlink:`MERMIN_MAXIT`

Maxit Mermin cycle iterations

.. _mermin-mu-sq:

MERMIN_MU_SQ
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: MERMIN
:Search: :searchlink:`MERMIN_MU_SQ`

Use the quadratic approximation to calculate mu in the outer loop

.. _mermin-round-evals:

MERMIN_ROUND_EVALS
------------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Expert
:Group: MERMIN
:Search: :searchlink:`MERMIN_ROUND_EVALS`

Round :ref:`mermin` eigenvalues to N decimal figures

.. _mermin-smearing-width:

MERMIN_SMEARING_WIDTH
---------------------

:Type: Physical
:Default: 0.003166811429
:Unit: hartree
:Level: Expert
:Group: MERMIN
:Search: :searchlink:`MERMIN_SMEARING_WIDTH`

Occupancy smearing width in :ref:`mermin` calculations

.. _mermin-temp:

MERMIN_TEMP
-----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: MERMIN
:Search: :searchlink:`MERMIN_TEMP`

Use easy annealing during mermin

.. _mermin-threshold-orig:

MERMIN_THRESHOLD_ORIG
---------------------

:Type: Double-Precision
:Default: 1e-09
:Unit: None
:Level: Expert
:Group: MERMIN
:Search: :searchlink:`MERMIN_THRESHOLD_ORIG`

Threshold for the lnv loop when doing extrapolation

.. _mg-continue-on-error:

MG_CONTINUE_ON_ERROR
--------------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Expert
:Group: MULTIGRID
:Search: :searchlink:`MG_CONTINUE_ON_ERROR`

If true, solutions DL_MG will not abort on errors

.. _mg-defco-fd-order:

MG_DEFCO_FD_ORDER
-----------------

:Type: Integer
:Default: 8
:Unit: None
:Level: Basic
:Group: MULTIGRID
:Search: :searchlink:`MG_DEFCO_FD_ORDER`

Order of finite differences to use in the high-order defect correction component of the multigrid solver.

Order of finite differences to use in the high-order defect correction component of the multigrid solver. :ref:`mg-defco-fd-order` must be positive and even

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MG_DEFCO_FD_ORDER [Integer]

   :Example:

   .. code::

      MG_DEFCO_FD_ORDER  3

.. _mg-granularity-power:

MG_GRANULARITY_POWER
--------------------

:Type: Integer
:Default: 3
:Unit: None
:Level: Expert
:Group: MULTIGRID
:Search: :searchlink:`MG_GRANULARITY_POWER`

Power of 2 which gives multigrid granularity, i.e. granularity = 2**N where N is MG_GRANULARITY_POWER.

Power of 2 which gives multigrid granularity, i.e. granularity = 2**N where N is MG_GRANULARITY_POWER. :ref:`mg-granularity-power` must be > 0.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MG_GRANULARITY_POWER [Integer]

   :Example:

   .. code::

      MG_GRANULARITY_POWER 5

.. _mg-max-iters-cg:

MG_MAX_ITERS_CG
---------------

:Type: Integer
:Default: 50
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_MAX_ITERS_CG`

Maximum number of iterations for conjugate gradients in the multigrid solver.

.. _mg-max-iters-defco:

MG_MAX_ITERS_DEFCO
------------------

:Type: Integer
:Default: 30
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_MAX_ITERS_DEFCO`

Maximum number of iterations for the high-order defect correction procedure in the multigrid solver.

.. _mg-max-iters-newton:

MG_MAX_ITERS_NEWTON
-------------------

:Type: Integer
:Default: 30
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_MAX_ITERS_NEWTON`

Maximum number of iterations for the Newton method in the multigrid solver.

.. _mg-max-iters-vcycle:

MG_MAX_ITERS_VCYCLE
-------------------

:Type: Integer
:Default: 200
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_MAX_ITERS_VCYCLE`

Maximum number of multigrid V-cycle iterations.

.. _mg-max-res-ratio:

MG_MAX_RES_RATIO
----------------

:Type: Double-Precision
:Default: 0.999
:Unit: None
:Level: Expert
:Group: MULTIGRID
:Search: :searchlink:`MG_MAX_RES_RATIO`

Residual ratio threshold for giving up on MG convergence: passed to DL_MG

.. _mg-tol-cg-res-abs:

MG_TOL_CG_RES_ABS
-----------------

:Type: Double-Precision
:Default: 0.05
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_TOL_CG_RES_ABS`

Absolute tolerance in norm of residual for defect correction procedure in multigrid solver for CG.

.. _mg-tol-cg-res-rel:

MG_TOL_CG_RES_REL
-----------------

:Type: Double-Precision
:Default: 0.01
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_TOL_CG_RES_REL`

Relative tolerance in norm of residual for defect correction procedure in multigrid solver for CG.

.. _mg-tol-mu-abs:

MG_TOL_MU_ABS
-------------

:Type: Double-Precision
:Default: 0.001
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_TOL_MU_ABS`

Absolute tolerance for chemical potential in multigrid calculations in PBC with Boltzmann ions.

.. _mg-tol-mu-rel:

MG_TOL_MU_REL
-------------

:Type: Double-Precision
:Default: 0.001
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_TOL_MU_REL`

Relative tolerance for chemical potential in multigrid calculations in PBC with Boltzmann ions.

.. _mg-tol-newton-abs:

MG_TOL_NEWTON_ABS
-----------------

:Type: Double-Precision
:Default: 1e-05
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_TOL_NEWTON_ABS`

Absolute tolerance for norm of residual in Newton method iterations in multigrid solver.

.. _mg-tol-newton-rel:

MG_TOL_NEWTON_REL
-----------------

:Type: Double-Precision
:Default: 1e-08
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_TOL_NEWTON_REL`

Relative tolerance for norm of residual in Newton method iterations in multigrid solver.

.. _mg-tol-pot-abs:

MG_TOL_POT_ABS
--------------

:Type: Double-Precision
:Default: 1e-06
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_TOL_POT_ABS`

Absolute tolerance in norm of potential for defect correction procedure in multigrid solver.

.. _mg-tol-pot-rel:

MG_TOL_POT_REL
--------------

:Type: Double-Precision
:Default: 1e-06
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_TOL_POT_REL`

Relative tolerance in norm of potential for defect correction procedure in multigrid solver.

.. _mg-tol-res-abs:

MG_TOL_RES_ABS
--------------

:Type: Double-Precision
:Default: 0.05
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_TOL_RES_ABS`

Absolute tolerance in norm of residual for defect correction procedure in multigrid solver.

.. _mg-tol-res-rel:

MG_TOL_RES_REL
--------------

:Type: Double-Precision
:Default: 0.01
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_TOL_RES_REL`

Relative tolerance in norm of residual for defect correction procedure in multigrid solver.

Relative tolerance in norm of residual for defect correction procedure in multigrid solver.  :ref:`mg-tol-res-rel` must be >= 0.0.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MG_TOL_RES_REL

   :Example:

   .. code::

      MG_TOL_RES_REL 1.0e-1

.. _mg-tol-vcyc-abs:

MG_TOL_VCYC_ABS
---------------

:Type: Double-Precision
:Default: 1e-05
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_TOL_VCYC_ABS`

Absolute tolerance for norm of residual in multigrid V-cycle iterations.

.. _mg-tol-vcyc-rel:

MG_TOL_VCYC_REL
---------------

:Type: Double-Precision
:Default: 1e-08
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_TOL_VCYC_REL`

Relative tolerance for norm of residual in multigrid V-cycle iterations.

.. _mg-use-cg:

MG_USE_CG
---------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: MULTIGRID
:Search: :searchlink:`MG_USE_CG`

Implicit solvent: Use conjugate gradients in DL_MG.

.. _mg-use-error-damping:

MG_USE_ERROR_DAMPING
--------------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Expert
:Group:  MULTIGRID
:Search: :searchlink:`MG_USE_ERROR_DAMPING`

Should we use error damping in the high-order defect correction procedure of the multigrid solver?

.. _mg-use-fas:

MG_USE_FAS
----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group:  MULTIGRID
:Search: :searchlink:`MG_USE_FAS`

Should FAS be used for non-linear PB equation in the multigrid solver (instead of Newton method)?

.. _mg-vcyc-smoother-iter-post:

MG_VCYC_SMOOTHER_ITER_POST
--------------------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Expert
:Group: MULTIGRID
:Search: :searchlink:`MG_VCYC_SMOOTHER_ITER_POST`

V cycle smoother iterations post-smoothing: passed to DL_MG

.. _mg-vcyc-smoother-iter-pre:

MG_VCYC_SMOOTHER_ITER_PRE
-------------------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Expert
:Group: MULTIGRID
:Search: :searchlink:`MG_VCYC_SMOOTHER_ITER_PRE`

V cycle smoother iterations pre-smoothing: passed to DL_MG

.. _minit-lnv:

MINIT_LNV
---------

:Type: Integer
:Default: 3
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`MINIT_LNV`

Min number of LNV iterations

Specifies the minimum number of iterations for the density kernel optimization.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MINIT_LNV [Integer]

   :Example:

   .. code::

      MINIT_LNV 1

.. _mix-dkn-init-num:

MIX_DKN_INIT_NUM
----------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`MIX_DKN_INIT_NUM`

Number of steps before extrapolation of the desity kernel

Length of the initialization phase for the density kernel. Number of MD steps before the activation of the extrapolation/propagation scheme for building density kernel initial guesses.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MIX_DKN_INIT_NUM [Integer]

   :Example:

   .. code::

      MIX_DKN_INIT_NUM 2

.. _mix-dkn-init-type:

MIX_DKN_INIT_TYPE
-----------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`MIX_DKN_INIT_TYPE`

Type of initialization before :ref:`mix-dkn-type`

Specifies the mixing scheme used during the initialisation phase for the density kernel. NONE : During the initialization phase, the initial density kernel is built according to :ref:`coreham-denskern-guess` block. REUSE : During the initialization phase, the density kernel from the last MD step is used as initial guess.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MIX_DKN_INIT_TYPE [Text]

   :Example:

   .. code::

      MIX_DKN_INIT_TYPE REUSE

.. _mix-dkn-num:

MIX_DKN_NUM
-----------

:Type: Integer
:Default: 0
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`MIX_DKN_NUM`

Number of coefficients used to build new guess for dkn

Number of density kernels required by the density kernel mixing scheme in order to generate the new initial guesses for the density kernel SCF process. See :ref:`mix-dkn-type` for a description of the available mixing schemes. The default depends on :ref:`mix-dkn-type` .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MIX_DKN_NUM [Integer]

   :Example:

   .. code::

      MIX_DKN_NUM 2

.. _mix-dkn-reset:

MIX_DKN_RESET
-------------

:Type: Integer
:Default: 50
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`MIX_DKN_RESET`

Number of extrapolation steps between two resets of the density kernel

:ref:`mix-dkn-reset` specifies the number of MD steps to be performed before the generation of a new initial guess for the density kernel. See :ref:`mix-dkn-type` for more advanced mixing options.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MIX_DKN_RESET [Integer]

   :Example:

   .. code::

      MIX_DKN_RESET 100

.. _mix-dkn-type:

MIX_DKN_TYPE
------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`MIX_DKN_TYPE`

Type of mixing used to build new guess for dkn

Specifies the mixing scheme used to generate new initial guesses for the density kernel from the density kernels optimized at previous MD steps. NONE : No use of MD history, initial density kernel is built according to :ref:`coreham-denskern-guess` parameter. REUSE :  No kernel mixing. SCF density kernel at previous MD step is used as initial guess. LINEAR : One dimensional linear extrapolation from density kernel at two previous MD steps. MULTID : Multi-dimensional linear extrapolation from density kernel at previous MD steps. The dimension of the extrapolation space is determined by :ref:`mix-dkn-num` . POLY : One-dimensional polynomial extrapolation from density kernel at previous steps. The degree of the extrapolation polynom is determined by :ref:`mix-dkn-num` . PROJ : Projection of the previous SCF density kernel onto the set of extrapolated NGWFs. This option requires that :ref:`mix-ngwfs-type` is different than NONE. TENSOR : Correction of the previous SCF density kernel in order to preserve tensorial integrity. This option requires that :ref:`mix-ngwfs-type` is different than NONE. TRPROP : Time-reversible propagation of auxiliary density kernel. DISSIP :  Dissipative propagation of auxiliary density kernel. The number of previous MD steps used for the derivation of the dissipative force is determined by :ref:`mix-dkn-num`

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MIX_DKN_TYPE [Text]

   :Example:

   .. code::

      MIX_DKN_TYPE REUSE

.. _mix-local-length:

MIX_LOCAL_LENGTH
----------------

:Type: Physical
:Default: 10.0
:Unit: bohr
:Level: Expert
:Group: CONV
:Search: :searchlink:`MIX_LOCAL_LENGTH`

Max radius for local mixing of NGWFs

Specifies the localization length required by :ref:`mix-ngwfs-type` =3.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MIX_LOCAL_LENGTH [Value] [Unit]

   :Example:

   .. code::

      MIX_LOCAL_LENGTH 15.0 bohr

.. _mix-local-smear:

MIX_LOCAL_SMEAR
---------------

:Type: Physical
:Default: 5.0
:Unit: bohr
:Level: Expert
:Group: CONV
:Search: :searchlink:`MIX_LOCAL_SMEAR`

Radial smearing for local mixing of NGWFs

Allows to smear out the localization sphere used when :ref:`mix-ngwfs-type` =3.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MIX_LOCAL_SMEAR [Value] [Unit]

   :Example:

   .. code::

      mix_local_length 3.0 bohr

.. _mix-ngwfs-coeff:

MIX_NGWFS_COEFF
---------------

:Type: Double-Precision
:Default: 0.1
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`MIX_NGWFS_COEFF`

Mix the propagated NGWFs with the new NGWFs

.. _mix-ngwfs-init-num:

MIX_NGWFS_INIT_NUM
------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`MIX_NGWFS_INIT_NUM`

Number of steps before extrapolation of the NGWFs

Length of the initialization phase for NGWFs. Number of MD steps before the activation of the extrapolation/propagation scheme for building density kernel initial guesses.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MIX_NGWFS_INIT_NUM [Integer]

   :Example:

   .. code::

      MIX_NGWFS_INIT_NUM 2

.. _mix-ngwfs-init-type:

MIX_NGWFS_INIT_TYPE
-------------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`MIX_NGWFS_INIT_TYPE`

Type of initialization before :ref:`mix-dkn-type`

Specifies the mixing scheme used during the initialisation phase for the NGWFs. NONE : During the initialization phase, initial NGWFs are built according to :ref:`species-atomic-set` block. REUSE : During the initialization phase, NGWFs from the last MD step are used as initial guess.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MIX_NGWFS_INIT_TYPE [Text]

   :Example:

   .. code::

      MIX_NGWFS_INIT_TYPE REUSE

.. _mix-ngwfs-num:

MIX_NGWFS_NUM
-------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`MIX_NGWFS_NUM`

Number of coefficients used to build new guess for NGWFS

Number of NGWFs sets required by the NGWFs mixing scheme in order to generate the new initial guesses for the NGWFs optimization process. See :ref:`mix-ngwfs-type` for a description of the available mixing schemes. Default depends on :ref:`mix-ngwfs-type` .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MIX_NGWFS_NUM [Integer]

   :Example:

   .. code::

      MIX_NGWFS_NUM 2

.. _mix-ngwfs-reset:

MIX_NGWFS_RESET
---------------

:Type: Integer
:Default: 50
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`MIX_NGWFS_RESET`

Number of extrapolation steps between two resets of the NGWFs

:ref:`mix-ngwfs-reset` specifies the number of MD steps to be performed before the generation of new initial guesses for the NGWFs. See :ref:`mix-ngwfs-type` for more advanced mixing options.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MIX_NGWFS_RESET [Integer]

   :Example:

   .. code::

      MIX_NGWFS_RESET 100

.. _mix-ngwfs-type:

MIX_NGWFS_TYPE
--------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`MIX_NGWFS_TYPE`

Type of mixing used to build new guess for NGWFS

Specifies the mixing scheme used to generate new initial guesses for the NGWFs from the NGWFs optimized at previous MD steps. NONE : No use of MD history, initial NGWFs are built according to the :ref:`species-atomic-set` block. REUSE :  No mixing of NGWFs. NGWFs from previous MD step are used as initial guess. LINEAR : One dimensional linear extrapolation from NGWFs at two previous MD steps. MULTID : Multi-dimensional linear extrapolation from NGWFs at previous MD steps. The dimension of the extrapolation space is determined by :ref:`mix-ngwfs-num` . POLY : One-dimensional polynomial extrapolation from NGWFs at previous steps. The degree of the extrapolation polynom is determined by :ref:`mix-ngwfs-num` . LOCAL :  Generalized multi-dimensional linear extrapolation from NGWFs at previous steps. The dimension of the extrapolation space is determined by input parameter :ref:`mix-ngwfs-num` . The localization radius is determine by input parameter :ref:`mix-local-length` . Optionnally, the localization radius can be smeared out by using non-zero values for :ref:`mix-local-smear` . TRPROP : Time-reversible propagation of auxiliary NGWFs. DISSIP :  Dissipative propagation of auxiliary NGWFs. The number of previous MD steps used for the derivation of the dissipative force is determined by :ref:`mix-ngwfs-num`

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      MIX_NGWFS_TYPE [Text]

   :Example:

   .. code::

      MIX_NGWFS_TYPE REUSE

.. _mm-rep-params:

MM_REP_PARAMS
-------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: QMMM
:Search: :searchlink:`MM_REP_PARAMS`

Repulsive MM potential params of all MM species

.. _mts-elec-energy-tol:

MTS_ELEC_ENERGY_TOL
-------------------

:Type: Physical
:Default: -0.001
:Unit: hartree
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`MTS_ELEC_ENERGY_TOL`

Tolerance on total energy change during NGWF optimisation

.. _mts-elec-force-tol:

MTS_ELEC_FORCE_TOL
------------------

:Type: Physical
:Default: -0.001
:Unit: ha/bohr
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`MTS_ELEC_FORCE_TOL`

Tolerance on max force change during NGWF optimisation

.. _mts-lnv-threshold:

MTS_LNV_THRESHOLD
-----------------

:Type: Double-Precision
:Default: 5e-06
:Unit: None
:Level: Expert
:Group: MD
:Search: :searchlink:`MTS_LNV_THRESHOLD`

LNV convergence threshold for the mts correction

.. _mts-maxit-lnv:

MTS_MAXIT_LNV
-------------

:Type: Integer
:Default: 5
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`MTS_MAXIT_LNV`

Max number of LNV iterations

.. _mts-maxit-ngwf-cg:

MTS_MAXIT_NGWF_CG
-----------------

:Type: Integer
:Default: 50
:Unit: None
:Level: Intermediate
:Group: MD
:Search: :searchlink:`MTS_MAXIT_NGWF_CG`

Max number of conjugate gradients iterations

.. _mts-maxit-pen:

MTS_MAXIT_PEN
-------------

:Type: Integer
:Default: 3
:Unit: None
:Level: Intermediate
:Group: MD
:Search: :searchlink:`MTS_MAXIT_PEN`

Max number of penalty iterations

.. _mts-minit-lnv:

MTS_MINIT_LNV
-------------

:Type: Integer
:Default: 5
:Unit: None
:Level: Intermediate
:Group: MD
:Search: :searchlink:`MTS_MINIT_LNV`

Min number of LNV iterations

.. _mts-mix-inc:

MTS_MIX_INC
-----------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`MTS_MIX_INC`

Include the mts correction step in the NGWFs and dkn mixing scheme

.. _mts-ngwf-max-grad:

MTS_NGWF_MAX_GRAD
-----------------

:Type: Double-Precision
:Default: -2e-05
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`MTS_NGWF_MAX_GRAD`

Maximum permissible value of NGWF Gradient for convergence

.. _mts-ngwf-threshold:

MTS_NGWF_THRESHOLD
------------------

:Type: Double-Precision
:Default: 0.0005
:Unit: None
:Level: Expert
:Group: MD
:Search: :searchlink:`MTS_NGWF_THRESHOLD`

NGWF convergence threshold for the mts correction

.. _mts-nstep:

MTS_NSTEP
---------

:Type: Integer
:Default: 1
:Unit: None
:Level: Expert
:Group: MD
:Search: :searchlink:`MTS_NSTEP`

Number of time steps in the multiple time-step scheme

.. _mts-xi:

MTS_XI
------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: MD
:Search: :searchlink:`MTS_XI`

Internal thermostat in the multiple time-step scheme

.. _multigrid-bc:

MULTIGRID_BC
------------

:Type: String
:Default: ''
:Unit: None
:Level: Intermediate
:Group: BC
:Search: :searchlink:`MULTIGRID_BC`

3 character string defining BCs for multigrid solver along each lattice vector. 'O' for open, 'P' for periodic, 'Z' for zero (i.e. open, but with the potential assumed to be zero on cell boundaries).

.. _mult-ngwf-by-phase:

MULT_NGWF_BY_PHASE
------------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`MULT_NGWF_BY_PHASE`

Phase theta added to initial complex NGWFs

.. _mult-ngwf-by-random-phase:

MULT_NGWF_BY_RANDOM_PHASE
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`MULT_NGWF_BY_RANDOM_PHASE`

If true, random phase in [0,2PI] is added to initial complex NGWFs

.. _mw-total-force:

MW_TOTAL_FORCE
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: GENERAL
:Search: :searchlink:`MW_TOTAL_FORCE`

Subtract mass-weighted average force to ensure Newton's 3rd law holds

.. _nbo-aopnao-scheme:

NBO_AOPNAO_SCHEME
-----------------

:Type: String
:Default: 'ORIGINAL'
:Unit: None
:Level: Expert
:Group: NBO
:Search: :searchlink:`NBO_AOPNAO_SCHEME`

AO to PNAO scheme to use in generating NAOs (for testing purposes).

Thee AO to PNAO scheme to use. Affects the lm-averaging and diagonalisation steps in the initial AO to PNAO, NRB lm-averaging, and rediagonalisation transformations. For testing purposes only - so far none of the other schemes apart from ORIGINAL works. Possbile values are: ORIGINAL - default, with lm-averaging DIAGONALIZATION - Diagonalises entire atom-centred sub-block without lm-averaging or splitting between different angular channels. NONE - Skips all rediagonalisation transformations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NBO_AOPNAO_SCHEME [Text]

   :Example:

   .. code::

      NBO_AOPNAO_SCHEME DIAGONALIZATION

.. _nbo-init-lclowdin:

NBO_INIT_LCLOWDIN
-----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: NBO
:Search: :searchlink:`NBO_INIT_LCLOWDIN`

Performs atom-centered Lowdin symmetric orthogonalization in generating the NAOs.

Performs atom-local Lowdin orthogonalisation on NGWFs as the first step before constructing NAOs.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NBO_INIT_LCLOWDIN [Logical]

   :Example:

   .. code::

      NBO_INIT_LCLOWDIN T

.. _nbo-list-plotnbo:

NBO_LIST_PLOTNBO
----------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: NBO
:Search: :searchlink:`NBO_LIST_PLOTNBO`

List of NBOs to be plotted according to GENNBO output indices.

The list of :ref:`nbo-plot-orbtype` orbitals to be plotted, identified by their indices as in the gennbo output. Specify each index on a new line.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK NBO_LIST_PLOTNBO
      GENNBO_orbital_index1
      GENNBO_orbital_index2
      ...
      GENNBO_orbital_indexN
      %ENDBLOCK NBO_LIST_PLOTNBO

   :Example:

   .. code::

      GENNBO output indices specified on separate lines:
      
      
      
      %BLOCK NBO_LIST_PLOTNBO
      
       8
      
       10
      
      %ENDBLOCK NBO_LIST_PLOTNBO

.. _nbo-plot-orbtype:

NBO_PLOT_ORBTYPE
----------------

:Type: String
:Default: ''
:Unit: None
:Level: Intermediate
:Group: NBO
:Search: :searchlink:`NBO_PLOT_ORBTYPE`

Type of GENNBO-generated orbital to plot.

The type of gennbo-generated orbitals to read and plot. Possible values and their associated gennbo transformation files must be present, as follows: NAO - seedname_nao.33 NHO - seedname_nao.35 NBO - seedname_nao.37 NLMO - seedname_nao.39 ; NLMO is only defined for the full system i.e. partitioned FILE.47 will give meaningless NLMOs. Except for NLMO, adding a "P" prefix e.g. "PNAO" to the value of :ref:`nbo-plot-orbtype` causes the non-orthogonalised PNAOs to be used in plotting instead of NAOs. PNAOs are of the normal type, i.e. when RPNAO = F in gennbo (default).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NBO_PLOT_ORBTYPE [Text]

   :Example:

   .. code::

      NBO_PLOT_ORBTYPE NAO

.. _nbo-pnao-analysis:

NBO_PNAO_ANALYSIS
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: NBO
:Search: :searchlink:`NBO_PNAO_ANALYSIS`

S/P/D/F CHARACTER ANALYSIS ON PNAO.

Perform s/p/d/f analysis on the PNAOs (analogous to :ref:`ngwf-analysis` ).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NBO_PNAO_ANALYSIS [Logical]

   :Example:

   .. code::

      NBO_PNAO_ANALYSIS T

.. _nbo-scale-dm:

NBO_SCALE_DM
------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: NBO
:Search: :searchlink:`NBO_SCALE_DM`

Scales density matrix in the FILE.47 output to achieve charge integrality (Required for proper GENNBO functionality).

Scales partial density matrix output to seedname_nao_nbo.47 in order to achieve charge integrality.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NBO_SCALE_DM [Logical]

   :Example:

   .. code::

      NBO_SCALE_DM F

.. _nbo-scale-spin:

NBO_SCALE_SPIN
--------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: NBO
:Search: :searchlink:`NBO_SCALE_SPIN`

Whether or not partial density matrices for different spins are scaled independently

Scales alpha and beta spins independently to integral charge when partial matrices are printed and :ref:`nbo-scale-dm` = T. Inevitably means spin density values from gennbo are invalid and one should calculate them manually from the NPA populations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NBO_SCALE_SPIN [Logical]

   :Example:

   .. code::

      NBO_SCALE_SPIN F

.. _nbo-species-ngwflabel:

NBO_SPECIES_NGWFLABEL
---------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: NBO
:Search: :searchlink:`NBO_SPECIES_NGWFLABEL`

User-specified NGWF (false) lm-label and NMB/NRBs for GENNBO

Optional user-defined (false) lm-label for NGWFs according to gennbo convention. "N" suffix denotes NMB orbital. If "SOLVE" orbitals are used, this block should be present, as "AUTO" initialisation assumes orbitals were also initialised as "AUTO".

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK NBO_SPECIES_NGWFLABEL
      sub_region_atoms_1 "lm-label1"
      sub_region_atoms_2 "lm-label2"
      ...
      sub_region_atoms_N "lm-labelN"
      %ENDBLOCK NBO_SPECIES_NGWFLABEL

   :Example:

   .. code::

      Species not specified will default to AUTO:
      
      
      
      %BLOCK NBO_SPECIES_NGWFLABEL
      
       C1 "1N 151N 152N 153N"
      
       H1 "AUTO"
      
      %ENDBLOCK NBO_SPECIES_NGWFLABEL

.. _nbo-write-dipole:

NBO_WRITE_DIPOLE
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`NBO_WRITE_DIPOLE`

Writes dipole matrix to FILE.47

Computes and writes dipole matrix to FILE.47

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NBO_WRITE_DIPOLE [Logical]

   :Example:

   .. code::

      NBO_WRITE_DIPOLE T

.. _nbo-write-lclowdin:

NBO_WRITE_LCLOWDIN
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: NBO
:Search: :searchlink:`NBO_WRITE_LCLOWDIN`

Write a GENNBO FILE.47 containing all the atoms in the atom-centered Lowdin basis to satisfy the strict lm-orthogonality requirement in GENNBO

Writes full matrices (all atoms) in the atom-local Lowdin-orthogonalized basis to FILE.47 (For reference/testing/comparison purposes). Output will be seedname_lclowdin_nbo.47

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NBO_WRITE_LCLOWDIN [Logical]

   :Example:

   .. code::

      NBO_WRITE_LCLOWDIN T

.. _nbo-write-npacomp:

NBO_WRITE_NPACOMP
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: NBO
:Search: :searchlink:`NBO_WRITE_NPACOMP`

Writes individual NAO population into the standard output.

Writes NAO charges for all orbitals to standard output.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NBO_WRITE_NPACOMP [Logical]

   :Example:

   .. code::

      NBO_WRITE_NPACOMP T

.. _nbo-write-species:

NBO_WRITE_SPECIES
-----------------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: NBO
:Search: :searchlink:`NBO_WRITE_SPECIES`

List of atoms to be included in the output to GENNBO FILE.47

Block of lists of species to be included in the partial matrix output of seedname_nao_nbo.47. If not present all atoms will be included.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK NBO_WRITE_SPECIES
      sub_region_atoms_1
      sub_region_atoms_2
      ...
      sub_region_atoms_N
      %ENDBLOCK NBO_WRITE_SPECIES

   :Example:

   .. code::

      If specified will default to AUTO:
      
      
      
      %BLOCK NBO_WRITE_SPECIES
      
       C1
      
       H1
      
      %ENDBLOCK NBO_WRITE_SPECIES

.. _neb-ci-delay:

NEB_CI_DELAY
------------

:Type: Integer
:Default: -2
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`NEB_CI_DELAY`

Number of NEB chain LBFGS steps before climging image kicks in.  Negative number for no climbing image (default).

Defines the number of BFGS steps the chain should take before enabling a climbing image. Negative numbers disable the climbing image entirely.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NEB_CI_DELAY [Integer]

   :Example:

   .. code::

      NEB_CI_DELAY 5

.. _neb-continuation:

NEB_CONTINUATION
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`NEB_CONTINUATION`

Continue NEB run from .neb_cont files

Continue NEB run from .neb_cont files.

.. note::
   :collapsible: closed

   :Example:

   .. code::

      NEB_CONTINUATION T

.. _neb-converge-all:

NEB_CONVERGE_ALL
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: TS
:Search: :searchlink:`NEB_CONVERGE_ALL`

Use energy and displacement convergence criteria for NEB as well as forces.

.. _neb-glbfgs-history-size:

NEB_GLBFGS_HISTORY_SIZE
-----------------------

:Type: Integer
:Default: 10
:Unit: None
:Level: Expert
:Group: TS
:Search: :searchlink:`NEB_GLBFGS_HISTORY_SIZE`

History size of GLBFGS for NEB.

.. _neb-max-iter:

NEB_MAX_ITER
------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`NEB_MAX_ITER`

Maximum number of NEB iterations.

.. _neb-print-summary:

NEB_PRINT_SUMMARY
-----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`NEB_PRINT_SUMMARY`

Flag to print NEB pathway and convergence information to stdout

If True, ONETEP will print NEB convergence information as well as a summary of the reduced reaction coordinate and relative energy of each bead after each NEB step to the original stdout.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NEB_PRINT_SUMMARY [Boolean]

   :Example:

   .. code::

      NEB_PRINT_SUMMARY F

.. _neb-read-xyz:

NEB_READ_XYZ
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: TS
:Search: :searchlink:`NEB_READ_XYZ`

Read XYZ file for each image.

.. _neb-spring-constant:

NEB_SPRING_CONSTANT
-------------------

:Type: Physical
:Default: 0.02
:Unit: ha/bohr**2
:Level: Intermediate
:Group: TS
:Search: :searchlink:`NEB_SPRING_CONSTANT`

Spring constant for the NEB chain.

.. _neb-update-method:

NEB_UPDATE_METHOD
-----------------

:Type: String
:Default: 'GLBFGS'
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`NEB_UPDATE_METHOD`

Update method for NEB. Currently supported: FIRE (default), GLBFGS.

.. _ngwfs-init-recip:

NGWFS_INIT_RECIP
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`NGWFS_INIT_RECIP`

request NGWFs initialised in reciprocal space

.. _ngwfs-spin-polarised:

NGWFS_SPIN_POLARISED
--------------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Basic
:Group: SPIN
:Search: :searchlink:`NGWFS_SPIN_POLARISED`

Switch for spin polarized NGWFs

.. _ngwfs-spin-polarized:

NGWFS_SPIN_POLARIZED
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: SPIN
:Search: :searchlink:`NGWFS_SPIN_POLARIZED`

Switch for spin polarized NGWFs

Specifies that in the event that a spin-polarized calculation is being performed, the NGWFs themselves (as opposed to just the kernel and hamiltonian matrices) will be treated as having separate components for up and down spins.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NGWFS_SPIN_POLARIZED [Logical]

   :Example:

   .. code::

      NGWFS_SPIN_POLARIZED T

.. _ngwf-analysis:

NGWF_ANALYSIS
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`NGWF_ANALYSIS`

Perform NGWF analysis

.. _ngwf-cg-max-step:

NGWF_CG_MAX_STEP
----------------

:Type: Double-Precision
:Default: -8.0
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`NGWF_CG_MAX_STEP`

Maximum length of trial step for NGWF optimisation line search

Maximum length of trial step for NGWF optimisation line search. If NGWFS_CG_MAX_STEP is set to be negative, then NGWFS_CG_MAX_STEP = -NGWFS_CG_MAX_STEP * ( :ref:`cutoff-energy` / 22.04959837). For positive values, it is left unchanged.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NGWF_CG_MAX_STEP [Value]

   :Example:

   .. code::

      NGWF_CG_MAX_STEP 10.0

.. _ngwf-cg-rotate:

NGWF_CG_ROTATE
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`NGWF_CG_ROTATE`

Rotate density kernel during NGWF optimization

Rotate the density kernel to the new NGWF representation after CG update. In :ref:`edft` calculations, it also rotates the eigenvectors.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NGWF_CG_ROTATE [Logical]

   :Example:

   .. code::

      NGWF_CG_ROTATE T

.. _ngwf-cg-type:

NGWF_CG_TYPE
------------

:Type: String
:Default: 'NGWF_FLETCHER'
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`NGWF_CG_TYPE`

Type of CG coefficient for NGWF optimisation  NGWF_POLAK = Polak-Ribbiere formula;  NGWF_FLETCHER = Fletcher-Reeves formula;  NGWF_LBFGS = limited-memory BFGS with a trust-region step.

Specifies the variant of the conjugate gradients algorithm used for the optimization of the NGWFs, currently either NGWF_FLETCHER for Fletcher-Reeves or NGWF_POLAK for Polak-Ribiere.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NGWF_CG_TYPE [Text]

   :Example:

   .. code::

      NGWF_CG_TYPE NGWF_POLAK

.. _ngwf-halo:

NGWF_HALO
---------

:Type: Physical
:Default: -1.0
:Unit: bohr
:Level: Expert
:Group: BASIS
:Search: :searchlink:`NGWF_HALO`

Halo extension to NGWF radii

Specifies a halo size for the NGWFs to include matrix elements between NGWFs which do not directly overlap. In atomic units (a0). A negative value indicates that no halo should be used.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NGWF_HALO [Real]

   :Example:

   .. code::

      NGWF_HALO 1.0

.. _ngwf-max-grad:

NGWF_MAX_GRAD
-------------

:Type: Double-Precision
:Default: -2e-05
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`NGWF_MAX_GRAD`

Maximum permissible value of NGWF Gradient for convergence

Specifies the convergence threshold for the maximum value of the NGWF gradient at any psinc grid point. Ignored if negative.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NGWF_MAX_GRAD [Real]

   :Example:

   .. code::

      NGWF_MAX_GRAD 1.0e-4

.. _ngwf-threshold-orig:

NGWF_THRESHOLD_ORIG
-------------------

:Type: Double-Precision
:Default: 2e-06
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`NGWF_THRESHOLD_ORIG`

NGWF convergence threshold

Specifies the convergence threshold for the RMS gradient of the NGWFs.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NGWF_THRESHOLD_ORIG [Real]

   :Example:

   .. code::

      NGWF_THRESHOLD_ORIG 1.0e-5

.. _nlpp-for-exchange:

NLPP_FOR_EXCHANGE
-----------------

:Type: Boolean
:Default: None
:Unit: None
:Level: Expert
:Group: HFX
:Search: :searchlink:`NLPP_FOR_EXCHANGE`

Give exchange matrix same sparsity as non-local pseudopotential matrix

.. _nnho:

NNHO
----

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: BASIS
:Search: :searchlink:`NNHO`

Initialise NGWFs to nonorthogonal natural hybrid orbitals

Generate non-orthogonal natural hybrid orbitals from the NGWFs. See Fosteret al.,J. Am. Chem. Soc.102, 7211 (1980) for more details.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NNHO [Logical]

   :Example:

   .. code::

      NNHO T

.. _nonsc-forces:

NONSC_FORCES
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: None
:Group: None
:Search: :searchlink:`NONSC_FORCES`

Include non self-consistent forces due to NGWF optimisation

Calculates the residual non self-consistent forces due to the NGWF gradient.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NONSC_FORCES [Logical]

   :Example:

   .. code::

      NONSC_FORCES true

.. _num-acc-queues:

NUM_ACC_QUEUES
--------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Expert
:Group: THREADS
:Search: :searchlink:`NUM_ACC_QUEUES`

Number of OpenACC queues / CUDA streams for the GPU

.. _num-eigenvalues:

NUM_EIGENVALUES
---------------

:Type: Integer
:Default: 10
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`NUM_EIGENVALUES`

Number of energy and occupancy eigenvalues to print below and above the Fermi level

Specifies the number of canonical orbital eigenvalues above and below the Fermi level to print when properties are required.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NUM_EIGENVALUES [Integer]

   :Example:

   .. code::

      NUM_EIGENVALUES 5

.. _num-images:

NUM_IMAGES
----------

:Type: Integer
:Default: 1
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`NUM_IMAGES`

Control the number of ONETEP images

Defines the number of ONETEP instances that should run in parallel in the simulation and enables image-parallel mode. ONETEP must be run with MPI and the number of MPI processes must be divisible by the number of ONETEP images unless advanced specification is used. (see: image_sizes) In NEB, this is also the number of beads in the chain.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      NUM_IMAGES [Integer]

   :Example:

   .. code::

      NUM_IMAGES 5

.. _num-kpars:

NUM_KPARS
---------

:Type: Integer
:Default: 1
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`NUM_KPARS`

Control the number of ONETEP kpars

.. _occ-mix:

OCC_MIX
-------

:Type: Double-Precision
:Default: 0.25
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`OCC_MIX`

Mix fraction of occupancy preconditioned NGWF cov grad

Specifies the fraction of the NGWF gradient to which occupancy preconditioning is applied.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      OCC_MIX [Real]

   :Example:

   .. code::

      OCC_MIX 1.0 ; fully preconditioned gradient

.. _odd-psinc-grid:

ODD_PSINC_GRID
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`ODD_PSINC_GRID`

Force odd number of points in simcell psinc grid

Forces the simulation cell psinc grid to contain an odd number of points in each direction.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ODD_PSINC_GRID [Logical]

   :Example:

   .. code::

      odd_osinc_grid T

.. _old-lnv:

OLD_LNV
-------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`OLD_LNV`

Use LNV algorithm backwards compatible pre Dec 2004

Enables backwards compatibility with legacy code.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      OLD_LNV [Logical]

   :Example:

   .. code::

      OLD_LNV T

.. _openbc-hartree:

OPENBC_HARTREE
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`OPENBC_HARTREE`

Force open BCs in Hartree potential

Forces open boundary conditions in the calculation of the Hartree energy. These are automatically used whenever smeared ions ( :ref:`is-smeared-ion-rep` ) are in use. This keyword can be used to force them in other (extremely rare) situations. It cannot be used to force them off.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      OPENBC_HARTREE [Logical]

   :Example:

   .. code::

      OPENBC_HARTREE T

.. _openbc-ion-ion:

OPENBC_ION_ION
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`OPENBC_ION_ION`

Force open BCs in ion-ion energy

Forces open boundary conditions in the calculation of the ion-ion energy. These are automatically used whenever Martyna-Tuckerman ( :ref:`pbc-correction-cutoff` ), cutoff Coulomb ( :ref:`coulomb-cutoff-type` ) or smeared ions ( :ref:`is-smeared-ion-rep` ) are in use. This keyword can be used to force them in other (extremely rare) situations. It cannot be used to force them off.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      OPENBC_ION ION [Logical]

   :Example:

   .. code::

      OPENBC_ION_ION T

.. _openbc-pspot:

OPENBC_PSPOT
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: PSEUDO
:Search: :searchlink:`OPENBC_PSPOT`

Force open BCs in local pseudopotential

Forces open boundary conditions in the calculation of the local pseudopotential energy. These are automatically used whenever smeared ions ( :ref:`is-smeared-ion-rep` ) are in use. This keyword can be used to force them in other (extremely rare) situations. It cannot be used to force them off.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      OPENBC_PSPOT [Logical]

   :Example:

   .. code::

      OPENBC_PSPOT T

.. _openbc-pspot-finetune-alpha:

OPENBC_PSPOT_FINETUNE_ALPHA
---------------------------

:Type: Double-Precision
:Default: 0.3
:Unit: None
:Level: Expert
:Group: PSEUDO
:Search: :searchlink:`OPENBC_PSPOT_FINETUNE_ALPHA`

Open BCs in local pseudo, alpha parameter

Sets the value of a numerical parameter (alpha) used in the calculation of the local pseudopotential in open boundary conditions. This parameter controls the transition between the short-range and long-range parts of the pseudopotential. Its impact on the total energy is negligible, provided it stays within reasonable bounds. Units of 1/bohr are implicitly assumed. This keyword is only relevant for calculations with open boundary conditions.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      OPENBC_PSPOT_FINETUNE_ALPHA [Value]

   :Example:

   .. code::

      OPENBC_PSPOT_FINETUNE_ALPHA 0.5

.. _openbc-pspot-finetune-f:

OPENBC_PSPOT_FINETUNE_F
-----------------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Expert
:Group: PSEUDO
:Search: :searchlink:`OPENBC_PSPOT_FINETUNE_F`

Open BCs in local pseudo, fineness parameter

Sets the value of a unitless numerical parameter (grid fineness factor, f ) used in the calculation of the local pseudopotential in open boundary conditions. This parameter controls the fineness of the reciprocal space radial grid used in the calculation. Its impact on the total energy is negligible, provided it stays within reasonable bounds. The default value of -1 causes f to be determined automatically -- this will generate a 'safe' value, making the grid as fine as necessary to have at least 50 sample g-points in any period of sin(gx) for the largest x in use in the calculation (the diagonal of the simulation cell). Thus, the automatically generated value depends on the cell size. Increasing this value makes little sense. Decreasing this value allows calculations to start faster, but decreases accuracy. This keyword is only relevant for calculations with open boundary conditions.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      OPENBC_PSPOT_FINETUNE_F [INTEGER]

   :Example:

   .. code::

      OPENBC_PSPOT_FINETUNE_F 6

.. _openbc-pspot-finetune-nptsx:

OPENBC_PSPOT_FINETUNE_NPTSX
---------------------------

:Type: Integer
:Default: 100000
:Unit: None
:Level: Expert
:Group: PSEUDO
:Search: :searchlink:`OPENBC_PSPOT_FINETUNE_NPTSX`

Open BCs in local pseudo, npts_x parameter

Sets the value of a unitless numerical parameter npts_x used in the calculation of the local pseudopotential in open boundary conditions. This parameter controls the number of points in the radial real-space grid on which the local pseudopotential is evaluated before interpolation to the 3D grid takes place. Increasing this value will offer marginal increase in accuracy at the expense of calculation wall time. This keyword is only relevant for calculations with open boundary conditions.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      OPENBC_PSPOT_FINETUNE_NPTS_X [INTEGER]

   :Example:

   .. code::

      OPENBC_PSPOT_FINETUNE_NPTS_X 500000

.. _output-detail:

OUTPUT_DETAIL
-------------

:Type: String
:Default: 'NORMAL'
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`OUTPUT_DETAIL`

Level of output detail BRIEF, NORMAL or VERBOSE

Specifies the level of detail in ONETEP's output: either BRIEF , NORMAL or VERBOSE .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      OUTPUT_DETAIL [Text]

   :Example:

   .. code::

      OUTPUT_DETAIL VERBOSE

.. _ovlp-for-nonlocal:

OVLP_FOR_NONLOCAL
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`OVLP_FOR_NONLOCAL`

Overlap sparsity for nonlocal

Forces the nonlocal pseudopotential matrix and hence the Hamiltonian to have the sparsity pattern of the overlap matrix.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      OVLP_FOR_NONLOCAL [Logical]

   :Example:

   .. code::

      OVLP_FOR_NONLOCAL T

.. _padded-lattice-abc:

PADDED_LATTICE_ABC
------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: CELLDATA
:Search: :searchlink:`PADDED_LATTICE_ABC`

The simulation cell lattice vectors for the padded cell

.. _padded-lattice-cart:

PADDED_LATTICE_CART
-------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`PADDED_LATTICE_CART`

The simulation cell lattice vectors for the padded cell

Cutoff Coulomb only. Specifies the padded lattice vectors a1 , a2 and a3 for the 'padded' simulation cell as Cartesian coordinates. By default, these will be interpreted as being in atomic units (a0), but they will be interpreted as being Angstroms if "ang" is on the first line of the block.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK PADDED_LATTICE_CART
      a1x a1y a1z
      a2x a2y a2z
      a3x a3y a3z
      %ENDBLOCK PADDED_LATTICE_CART

   :Example:

   .. code::

      %BLOCK PADDED_LATTICE_CART
       100.00000   0.00000    0.00000 ; cubic unit cell
         0.00000 100.00000    0.00000 ; side length 100 bohr
         0.00000   0.000000 100.00000 ;
      %ENDBLOCK PADDED_LATTICE_CART

.. _parallel-scheme:

PARALLEL_SCHEME
---------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`PARALLEL_SCHEME`

Types of parallel strategies that can be used in subsystem calculations

.. _paw:

PAW
---

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: PAW
:Search: :searchlink:`PAW`

Uses a :ref:`paw` construction to find correct core densities/wavefunctions

Activates the Projector Augmented Wave Formalism: :ref:`paw` potentials must then be supplied in the species_pot block.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PAW [Logical]

   :Example:

   .. code::

      PAW : T

.. _paw-output-detail:

PAW_OUTPUT_DETAIL
-----------------

:Type: String
:Default: 'DEFAULT'
:Unit: None
:Level: Basic
:Group: PAW
:Search: :searchlink:`PAW_OUTPUT_DETAIL`

Level of output detail for PAW: BRIEF, NORMAL or VERBOSE

.. _pbc-correction-cutoff:

PBC_CORRECTION_CUTOFF
---------------------

:Type: Physical
:Default: 0.0
:Unit: bohr
:Level: Expert
:Group: None
:Search: :searchlink:`PBC_CORRECTION_CUTOFF`

alpha*L cutoff parameter for Martyna-Tuckerman PBC correction

Turns on the Martyna-Tuckerman correction to the effects of periodic boundary conditions (PBCs), specifies the dimensionless cutoff parameter. A value of 7.0 is recommended by the authors in Martyna GJ and Tuckerman ME, J. Chem. Phys. 110, 2810 (1999), DOI:10.1063/1.477923 .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PBC_CORRECTION_CUTOFF [Value] [Unit]

   :Example:

   .. code::

      PBC_CORRECTION_CUTOFF 7.0 bohr

.. _pdos-construct-basis:

PDOS_CONSTRUCT_BASIS
--------------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PDOS_CONSTRUCT_BASIS`

Compute PDOS using a SW fit to NGWFs

.. _pdos-d-band-threshold:

PDOS_D_BAND_THRESHOLD
---------------------

:Type: Physical
:Default: -0.5512
:Unit: hartree
:Level: Intermediate
:Group: None
:Search: :searchlink:`PDOS_D_BAND_THRESHOLD`

The minimum energy from which the d band centre is calculated

.. _pdos-lcao-optimize:

PDOS_LCAO_OPTIMIZE
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PDOS_LCAO_OPTIMIZE`

Compute PDOS by solving Kohn-Sham equations with an LCAO basis

.. _pdos-lowdin:

PDOS_LOWDIN
-----------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PDOS_LOWDIN`

Compute PDOS by taking the Lowdin factorization of the SW overlap

.. _pdos-max-l:

PDOS_MAX_L
----------

:Type: Integer
:Default: -1
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`PDOS_MAX_L`

The maximum azimuthal angular momentum channel to project on to in a pDOS calculation

.. _pdos-max-n:

PDOS_MAX_N
----------

:Type: Integer
:Default: -1
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PDOS_MAX_N`

The maximum number of Bessels to use in SW expansion in a pDOS calc

.. _pdos-optados-output:

PDOS_OPTADOS_OUTPUT
-------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`PDOS_OPTADOS_OUTPUT`

Output angular momentum projected density of states weights for input into OptaDOS

.. _pdos-orth-atom-blocks:

PDOS_ORTH_ATOM_BLOCKS
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PDOS_ORTH_ATOM_BLOCKS`

Orthogonalize the LCAOs on same centres in PDOS

.. _pdos-output-basis:

PDOS_OUTPUT_BASIS
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PDOS_OUTPUT_BASIS`

Write the pDOS SW basis to disk in tightbox_ngwf format

.. _pdos-output-swopt-kernham:

PDOS_OUTPUT_SWOPT_KERNHAM
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PDOS_OUTPUT_SWOPT_KERNHAM`

Write the kernel / Hamiltonian in a SW optimized pDOS

.. _pdos-pseudoatomic:

PDOS_PSEUDOATOMIC
-----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`PDOS_PSEUDOATOMIC`

Use pseudoatomic functions as the PDOS AM resolved basis

.. _pdos-reduce-sws:

PDOS_REDUCE_SWS
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PDOS_REDUCE_SWS`

Reduce bessel functions in pDOS before projection

.. _pdos-sum-mag:

PDOS_SUM_MAG
------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PDOS_SUM_MAG`

Sum over magnetic quantum number in PDOS (true by default)

.. _pen-param:

PEN_PARAM
---------

:Type: Double-Precision
:Default: 4.0
:Unit: None
:Level: Intermediate
:Group: CONV
:Search: :searchlink:`PEN_PARAM`

Penalty functional parameter

Specifies the energy parameter in hartrees for the penalty-functional algorithm [ Hayneset al.,Phys. Rev. B.59, 12173 (1999) ] used to refine the density kernel intialization before the main optimization begins.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PEN_PARAM [Real]

   :Example:

   .. code::

      PEN_PARAM 5.0

.. _permit-unusual-ngwf-count:

PERMIT_UNUSUAL_NGWF_COUNT
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PERMIT_UNUSUAL_NGWF_COUNT`

Allows continuing the calc with suspect number of NGWFs.

.. _phonon-animate-list:

PHONON_ANIMATE_LIST
-------------------

:Type: Block
:Default: None
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_ANIMATE_LIST`

List of phonon modes to write as xyz animations

List of Gamma-point modes (where 1 is the lowest) for which to write xyz animation files.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK PHONON_ANIMATE_LIST
      mode_1
      mode_2
      ...
      mode_N
      %ENDBLOCK PHONON_ANIMATE_LIST

   :Example:

   .. code::

      %BLOCK PHONON_ANIMATE_LIST
      
      2
      
      6
      
      33
      
      34
      
      %ENDBLOCK PHONON_ANIMATE_LIST

.. _phonon-animate-scale:

PHONON_ANIMATE_SCALE
--------------------

:Type: Double-Precision
:Default: 1.0
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_ANIMATE_SCALE`

Scaling factor for phonon mode animations

Relative scale of the amplitude of the vibration in the xyz animation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_ANIMATE_SCALE [Real]

   :Example:

   .. code::

      PHONON_ANIMATE_SCALE 2.0

.. _phonon-deltat:

PHONON_DELTAT
-------------

:Type: Physical
:Default: 1.5e-05
:Unit: hartree
:Level: Basic
:Group: None
:Search: :searchlink:`PHONON_DELTAT`

Temperature step for computation of vibrational thermodynamic quantities

Temperature step for the computation of thermodynamic quantities.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_DELTAT [Value] [Unit]

   :Example:

   .. code::

      PHONON_DELTAT 0.5E-5 Ha

.. _phonon-disp-list:

PHONON_DISP_LIST
----------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`PHONON_DISP_LIST`

List of displacements to perform for phonon calculation

List of force constant calculations to perform for Stage 2 in phonon calculations (i.e. in the case of phonon_farming_task 2 or 0). Note that the total number of force constant calculations is given in the main output file in the line 'Number of force constants'; this will be less than or equal to 3N. The numbers listed in the :ref:`phonon-disp-list` block should go from 1 to this number; they can only be equated to the label 'i' if all 3N force constants are calculated. If unspecified, all displacements are performed.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK PHONON_DISP_LIST
      i_1
      i_2
      ...
      i_M (M smaller than/ equal to 3N)
      %ENDBLOCK PHONON_DISP_LIST

   :Example:

   .. code::

      %BLOCK PHONON_DISP_LIST
      
      1
      
      3
      
      5
      
      %ENDBLOCK PHONON_DISP_LIST

.. _phonon-dos:

PHONON_DOS
----------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_DOS`

Calculate phonon DOS from MP grid and write to file

Calculate the phonon DOS and write to file.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_DOS [Logical]

   :Example:

   .. code::

      PHONON_DOS F

.. _phonon-dos-delta:

PHONON_DOS_DELTA
----------------

:Type: Double-Precision
:Default: 10.0
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_DOS_DELTA`

Frequency step (in cm^-1) for phonon DOS calculation

Frequency step for the phonon DOS calculation (in 1/cm).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_DOS_DELTA [Real]

   :Example:

   .. code::

      PHONON_DOS_DELTA 5.0

.. _phonon-dos-max:

PHONON_DOS_MAX
--------------

:Type: Double-Precision
:Default: 1000.0
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_DOS_MAX`

Upper bound of frequency range (in cm^-1) for phonon DOS calculation

Upper bound of the phonon DOS range (in 1/cm).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_DOS_MAX [Real]

   :Example:

   .. code::

      PHONON_DOS_MAX 1500.0

.. _phonon-dos-min:

PHONON_DOS_MIN
--------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_DOS_MIN`

Lower bound of frequency range (in cm^-1) for phonon DOS calculation

Lower bound of the phonon DOS range (in 1/cm).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_DOS_MIN [Real]

   :Example:

   .. code::

      PHONON_DOS_MIN 2.0

.. _phonon-energy-check:

PHONON_ENERGY_CHECK
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_ENERGY_CHECK`

Check total energy of system doesn't decrease upon ionic displacement

Perform a sanity check that the total energy does not decrease upon ionic displacement.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_ENERGY_CHECK [Logical]

   :Example:

   .. code::

      PHONON_ENERGY_CHECK T

.. _phonon-exception-list:

PHONON_EXCEPTION_LIST
---------------------

:Type: Block
:Default: None
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_EXCEPTION_LIST`

List of ionic degrees of freedom with modified properties

This is a block in which the user can list specific ion-coordinate pairs with options differing from the global defaults defined by :ref:`phonon-vib-free` , :ref:`phonon-sampling` , and :ref:`phonon-finite-disp` .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK PHONON_EXCEPTION_LIST
      ion1 direction1 displacement_switch1 phonon_sampling1 factor_phonon_finite_disp1
      ion2 direction2 displacement_switch2 phonon_sampling2 factor_phonon_finite_disp2
      ...
      ionN directionN displacement_switchN phonon_samplingN factor_phonon_finite_dispN
      %ENDBLOCK PHONON_EXCEPTION_LIST

   :Example:

   .. code::

      In this example, we are overwriting the default
      PHONON_VIB_FREE
      ,
      PHONON_SAMPLING
      , and
      PHONON_FINITE_DISP
      
       as such: the displacement of ion 10 in the z-direction (3) is switched
      on (1), with a value of phonon_sampling of 2, and a value of
      phonon_finite_disp of 0.9 times the global value; displacement of ion 15
       in the x-direction (1) is switched off (0), with the last two
      parameters not being read; displacement of ion 36 in the y-direction (2)
       is switched off (0), with the last two parameters not being read.
      
      
      
      %BLOCK PHONON_EXCEPTION_LIST
      
      10 3 1 2 0.9
      
      15 1 0 1 1.0
      
      36 2 0 1 1.0
      
      %ENDBLOCK PHONON_EXCEPTION_LIST

.. _phonon-farming-task:

PHONON_FARMING_TASK
-------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`PHONON_FARMING_TASK`

Operation to perform for phonon calc (for task farming or post-proc. of dynamical matrix)

The most efficient way of performing a phonon calculation is by task farming, as the full force constants matrix is built up from many perturbed-structure calculations, each of which is completely independent. This can be done with the following steps: Run :ref:`phonon-farming-task` 1 as a single job: this is essentially a standard single-point energy-and-force ONETEP calculation. Find the line in the main output file which gives the number of force constants needed for the phonon calculation you have specified (this will be between 1 and 3N) Divide the total number of force constants that need to be calculated between the desired number of jobs. Prepare the ONETEP input file for each job specifying :ref:`phonon-farming-task` 2 and a subset of the force constant calculations in the :ref:`phonon-disp-list` block. Make sure every job has access to the files filename.dkn and filename.tightbox_ngwfs obtained from the unperturbed calculation in the previous step. Collect all the filename.force_consts_i files and place them in the same directory. Finally, run :ref:`phonon-farming-task` 3 as a single job, to construct the full force constants matrix and perform the post-processing calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_FARMING_TASK [Integer]

   :Example:

   .. code::

      PHONON_FARMING_TASK 1

.. _phonon-finite-disp:

PHONON_FINITE_DISP
------------------

:Type: Physical
:Default: 0.1
:Unit: bohr
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_FINITE_DISP`

Amplitude of the ionic perturbation to be used in a finite displacement phonon calculation

Ionic displacement distance used in the finite-difference formula.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_FINITE_DISP [VALUE] [Unit]

   :Example:

   .. code::

      PHONON_FINITE_DISP 5.0E-2 bohr

.. _phonon-fmax:

PHONON_FMAX
-----------

:Type: Physical
:Default: 0.005
:Unit: ha/bohr
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_FMAX`

Maximum force allowed on the unperturbed system for a phonon calculation

Maximum ionic force allowed in the unperturbed system.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_FMAX [Value] [Unit]

   :Example:

   .. code::

      PHONON_FMAX 2.5E-3 'ha/bohr'

.. _phonon-grid:

PHONON_GRID
-----------

:Type: Block
:Default: None
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_GRID`

Regular grid of q points used for calculating vibrational thermodynamic quantities

Definition of the regular grid of q-points used in phonon calculations for the computation of thermodynamic quantities and the phonon DOS. Default is 1 1 1 (i.e. Gamma point only).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK PHONON_GRID
      factor_b1 factor_b2 factor_b3
      %ENDBLOCK PHONON_GRID

   :Example:

   .. code::

      In this example, we define a 10x10x10 sampling grid (over b1, b2 and b3 respectively), instead of the 1x1x1 default grid.
      
      
      
      %BLOCK PHONON_GRID
      
      10 10 10
      
      %ENDBLOCK PHONON_GRID

.. _phonon-min-freq:

PHONON_MIN_FREQ
---------------

:Type: Physical
:Default: 3.6e-06
:Unit: hartree
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_MIN_FREQ`

Discard phonon frequencies smaller than this value for computation of vibrational thermodynamic quantities

Minimum phonon frequency for the computation of thermodynamic quantities, expressed as an energy; frequencies lower than this are discarded.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_MIN_FREQ [Value] [Unit]

   :Example:

   .. code::

      PHONON_MIN_FREQ 2.0E-6 Ha

.. _phonon-qpoints:

PHONON_QPOINTS
--------------

:Type: Block
:Default: None
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_QPOINTS`

List of additional q points to calculate

List of additional q-points for which to calculate the phonon frequencies, in fractional coordinates of the reciprocal unit cell vectors. For non-supercell calculations only the Gamma point can be specified.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK PHONON_QPOINTS
      frac-b1_1 frac-b2_1 frac-b3_1
      frac-b1_2 frac-b2_2 frac-b3_2
      ...
      frac-b1_N frac-b2_N frac-b3_N
      %ENDBLOCK PHONON_QPOINTS

   :Example:

   .. code::

      %BLOCK PHONON_QPOINTS
      
      0.0 0.0 0.0
      
      0.0 0.0 0.1
      
      0.0 0.0 0.2
      
      0.0 0.0 0.3
      
      0.0 0.0 0.4
      
      0.0 0.0 0.5
      
      %ENDBLOCK PHONON_QPOINTS

.. _phonon-sampling:

PHONON_SAMPLING
---------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_SAMPLING`

Default number of sampling points for finite difference calculation (1 or 2)

Selects which finite-difference formula to use. The elements of the force constants matrix are calculated by a central-difference formula, using either 2 (the default :ref:`phonon-sampling` 1) or 4 displacements (PHONON_SAMPLING 2). See documentation file for more information.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_SAMPLING [Integer]

   :Example:

   .. code::

      PHONON_SAMPLING 2

.. _phonon-sk:

PHONON_SK
---------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_SK`

Use Slater-Koster style interpolation for q points instead of real-space cutoff

Use a Slater-Koster style interpolation for q-points instead of a real-space cutoff of the force constants matrix elements.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_SK [Logical]

   :Example:

   .. code::

      PHONON_SK T

.. _phonon-tmax:

PHONON_TMAX
-----------

:Type: Physical
:Default: 0.002
:Unit: hartree
:Level: Basic
:Group: None
:Search: :searchlink:`PHONON_TMAX`

Upper bound of temperature range for computation of vibrational thermodynamic quantities

Upper bound of the temperature range for the computation of thermodynamic quantities.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_TMAX [Value] [Unit]

   :Example:

   .. code::

      PHONON_TMAX 3.0E-3 Ha

.. _phonon-tmin:

PHONON_TMIN
-----------

:Type: Physical
:Default: 0.0
:Unit: hartree
:Level: Basic
:Group: None
:Search: :searchlink:`PHONON_TMIN`

Lower bound of temperature range for computation of vibrational thermodynamic quantities

Lower bound of the temperature range for the computation of thermodynamic quantities, expressed as an energy (k_B T).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_TMIN [Value] [Unit]

   :Example:

   .. code::

      PHONON_TMIN 0.001 Ha

.. _phonon-vib-free:

PHONON_VIB_FREE
---------------

:Type: Integer
:Default: 7
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_VIB_FREE`

Default allowed vibrational degrees of freedom for all ions

This integer parameter controls the global default of which Cartesian directions are switched on for all ions. The options are: 0 (x=F y=F z=F), 1 (x=T y=F z=F), 2 (x=F y=T z=F), 3 (x=T y=T z=F), 4 (x=F y=F z=T), 5 (x=T y=F z=T), 6 (x=F y=T z=T) and 7 (x=T y=T z=T). The values in parenthesis explain which Cartesian direction (i.e. vibrational degree of freedom) is allowed.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_VIB_FREE [Integer]

   :Example:

   .. code::

      PHONON_VIB_FREE 9

.. _phonon-write-eigenvecs:

PHONON_WRITE_EIGENVECS
----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PHONON_WRITE_EIGENVECS`

Write phonon mode eigenvectors to file

Write the eigenvectors as well as the phonon frequencies to file for the additional q-points.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PHONON_WRITE_EIGENVECS [Logical]

   :Example:

   .. code::

      PHONON_WRITE_EIGENVECS T

.. _plot-nbo:

PLOT_NBO
--------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: NBO
:Search: :searchlink:`PLOT_NBO`

Plot NBO's orbitals from FILE.xx as defined by nbo_plot_orbtype.

Instructs ONETEP to read the relevant orbital transformation output from gennbo, determined by the flag :ref:`nbo-plot-orbtype` and plots the orbitals specified in the :ref:`nbo-list-plotnbo` block. :ref:`write-nbo` and :ref:`plot-nbo` are mutually exclusive. Scalar field plotting must be enabled (e.g. :ref:`cube-format` = T).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PLOT_NBO [Logical]

   :Example:

   .. code::

      PLOT_NBO T

.. _polarisation-berry:

POLARISATION_BERRY
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`POLARISATION_BERRY`

Allow calculation of polarisation using Berry phase

.. _polarisation-calculate:

POLARISATION_CALCULATE
----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`POLARISATION_CALCULATE`

Allow calculation of polarisation

Activates the calculation of polarisation

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      POLARISATION_CALCULATE [Logical]

   :Example:

   .. code::

      POLARISATION_CALCULATE T

.. _polarisation-local:

POLARISATION_LOCAL
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`POLARISATION_LOCAL`

Allow the calculation of local polarisation

.. _polarisation-simcell-calculate:

POLARISATION_SIMCELL_CALCULATE
------------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`POLARISATION_SIMCELL_CALCULATE`

Calculate simcell polarisation (also, quadrupoles)

Turns on the calculation of polarisation in a properties calculation. Dipole moments and quadrupole moments are calculated for the entire system using the "simcell" approach (i.e. directly from integrals over real space). Both are calculated relative to a point defined by :ref:`polarisation-simcell-refpt` (default: 0.0 0.0 0.0).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      POLARISATION_SIMCELL_CALCULATE [Boolean]

   :Example:

   .. code::

      POLARISATION_SIMCELL_CALCULATE T

.. _polarisation-simcell-refpt:

POLARISATION_SIMCELL_REFPT
--------------------------

:Type: String
:Default: '0.0 0.0 0.0'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`POLARISATION_SIMCELL_REFPT`

Reference point for simcell dipoles, quadrupoles

.. _pol-emb-dbl-grid:

POL_EMB_DBL_GRID
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: QMMM
:Search: :searchlink:`POL_EMB_DBL_GRID`

Should polarisable embedding do gradients on double grid?

.. _pol-emb-dma-max-l:

POL_EMB_DMA_MAX_L
-----------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Basic
:Group: DMA
:Search: :searchlink:`POL_EMB_DMA_MAX_L`

Maximum order of DMA multipoles for polarisable embedding

.. _pol-emb-dma-min-l:

POL_EMB_DMA_MIN_L
-----------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Basic
:Group: DMA
:Search: :searchlink:`POL_EMB_DMA_MIN_L`

Minimum order of DMA multipoles for polarisable embedding

.. _pol-emb-fixed-charge:

POL_EMB_FIXED_CHARGE
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: QMMM
:Search: :searchlink:`POL_EMB_FIXED_CHARGE`

Is the embedding a fixed-charge (non-polarisable) FF?

.. _pol-emb-mpole-exclusion-radius:

POL_EMB_MPOLE_EXCLUSION_RADIUS
------------------------------

:Type: Physical
:Default: 0.25
:Unit: bohr
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_MPOLE_EXCLUSION_RADIUS`

Exclusion radius for point multipole singularities

.. _pol-emb-pairwise-polarisability:

POL_EMB_PAIRWISE_POLARISABILITY
-------------------------------

:Type: Physical
:Default: 1.92618
:Unit: bohr
:Level: Intermediate
:Group: QMMM
:Search: :searchlink:`POL_EMB_PAIRWISE_POLARISABILITY`

Pairwise polarisability for emulating Thole damping

.. _pol-emb-perm-scaling:

POL_EMB_PERM_SCALING
--------------------

:Type: Double-Precision
:Default: 1.0
:Unit: None
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_PERM_SCALING`

Scaling factor applied to interactions with MM perm. mpoles

.. _pol-emb-polscal:

POL_EMB_POLSCAL
---------------

:Type: Double-Precision
:Default: 1.0
:Unit: None
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_POLSCAL`

Pol-emb: QM polarisability scaling factor

.. _pol-emb-pot-filename:

POL_EMB_POT_FILENAME
--------------------

:Type: String
:Default: '*undefined*'
:Unit: None
:Level: Intermediate
:Group: QMMM
:Search: :searchlink:`POL_EMB_POT_FILENAME`

File with multipoles and energy terms for polarisable embedding potential

.. _pol-emb-qmstar:

POL_EMB_QMSTAR
--------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Intermediate
:Group: QMMM
:Search: :searchlink:`POL_EMB_QMSTAR`

Should the QM* rep be used for any QM/MM interaction

.. _pol-emb-repulsive-mm-pot-a:

POL_EMB_REPULSIVE_MM_POT_A
--------------------------

:Type: Double-Precision
:Default: 6.97
:Unit: None
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_REPULSIVE_MM_POT_A`

OBSOLETE Pol-emb repulsive MM pot: a parameter

.. _pol-emb-repulsive-mm-pot-alpha:

POL_EMB_REPULSIVE_MM_POT_ALPHA
------------------------------

:Type: Double-Precision
:Default: 146869.0
:Unit: None
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_REPULSIVE_MM_POT_ALPHA`

OBSOLETE Pol-emb repulsive MM pot: alpha parameter

.. _pol-emb-repulsive-mm-pot-b:

POL_EMB_REPULSIVE_MM_POT_B
--------------------------

:Type: Double-Precision
:Default: -11.87
:Unit: None
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_REPULSIVE_MM_POT_B`

OBSOLETE Pol-emb repulsive MM pot: b parameter

.. _pol-emb-repulsive-mm-pot-beta:

POL_EMB_REPULSIVE_MM_POT_BETA
-----------------------------

:Type: Double-Precision
:Default: 8.897
:Unit: None
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_REPULSIVE_MM_POT_BETA`

OBSOLETE Pol-emb repulsive MM pot: beta parameter

.. _pol-emb-repulsive-mm-pot-c:

POL_EMB_REPULSIVE_MM_POT_C
--------------------------

:Type: Double-Precision
:Default: 5.64
:Unit: None
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_REPULSIVE_MM_POT_C`

OBSOLETE Pol-emb repulsive MM pot: c parameter

.. _pol-emb-repulsive-mm-pot-cutoff:

POL_EMB_REPULSIVE_MM_POT_CUTOFF
-------------------------------

:Type: Physical
:Default: 10.0
:Unit: bohr
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_REPULSIVE_MM_POT_CUTOFF`

Pol-emb repulsive MM pot: cutoff rad around MM atom

.. _pol-emb-repulsive-mm-pot-r0:

POL_EMB_REPULSIVE_MM_POT_R0
---------------------------

:Type: Physical
:Default: 7.804568
:Unit: bohr
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_REPULSIVE_MM_POT_R0`

Pol-emb repulsive MM pot: R0 parameter

.. _pol-emb-repulsive-mm-pot-verbose:

POL_EMB_REPULSIVE_MM_POT_VERBOSE
--------------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_REPULSIVE_MM_POT_VERBOSE`

Pol-emb repulsive MM pot: verbose output?

.. _pol-emb-repulsive-mm-pot-write:

POL_EMB_REPULSIVE_MM_POT_WRITE
------------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_REPULSIVE_MM_POT_WRITE`

Pol-emb repulsive MM pot: write to file?

.. _pol-emb-smearing-a:

POL_EMB_SMEARING_A
------------------

:Type: Physical
:Default: 0.2
:Unit: bohr
:Level: Intermediate
:Group: QMMM
:Search: :searchlink:`POL_EMB_SMEARING_A`

Thole big A for short-range smearing of undamped

.. _pol-emb-thole-a:

POL_EMB_THOLE_A
---------------

:Type: Double-Precision
:Default: 0.39
:Unit: None
:Level: Expert
:Group: QMMM
:Search: :searchlink:`POL_EMB_THOLE_A`

Thole constant (a) for emulating Thole damping

.. _pol-emb-vacuum-dma-max-l:

POL_EMB_VACUUM_DMA_MAX_L
------------------------

:Type: Integer
:Default: -1
:Unit: None
:Level: Basic
:Group: QMMM
:Search: :searchlink:`POL_EMB_VACUUM_DMA_MAX_L`

Maximum order of DMA multipoles for polarisable embedding (vacuum calc)

.. _pol-emb-vacuum-dma-min-l:

POL_EMB_VACUUM_DMA_MIN_L
------------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Basic
:Group: QMMM
:Search: :searchlink:`POL_EMB_VACUUM_DMA_MIN_L`

Minimum order of DMA multipoles for polarisable embedding (vacuum calc)

.. _pol-emb-vacuum-qmstar:

POL_EMB_VACUUM_QMSTAR
---------------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Intermediate
:Group: QMMM
:Search: :searchlink:`POL_EMB_VACUUM_QMSTAR`

Should the QM* rep be used for any QM/MM interaction

.. _pol-emb-write-vacuum-restart:

POL_EMB_WRITE_VACUUM_RESTART
----------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: QMMM
:Search: :searchlink:`POL_EMB_WRITE_VACUUM_RESTART`

Should QM/MM restart files be written out

.. _popn-bond-cutoff:

POPN_BOND_CUTOFF
----------------

:Type: Physical
:Default: Unknown
:Unit: bohr
:Level: Basic
:Group: None
:Search: :searchlink:`POPN_BOND_CUTOFF`

Bond length cutoff for population analysis

Specifies the bond length cutoff to use when performing Mulliken population analysis.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      POPN_BOND_CUTOFF [Value] [Unit]

   :Example:

   .. code::

      POPN_BOND_CUTOFF 5.0 ang

.. _popn-calculate:

POPN_CALCULATE
--------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`POPN_CALCULATE`

Allow population analysis

Perform Mulliken population analysis.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      POPN_CALCULATE [Logical]

   :Example:

   .. code::

      POPN_CALCULATE F

.. _popn-mulliken-partial:

POPN_MULLIKEN_PARTIAL
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`POPN_MULLIKEN_PARTIAL`

Enable Mulliken partial charge analysis

.. _positions-abs:

POSITIONS_ABS
-------------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: GENERAL
:Search: :searchlink:`POSITIONS_ABS`

Cartesian positions for each atom

Specifies the atomic positions as Cartesian coordinates). In the above syntax, Si denotes the species of atomi(max 4 characters) and Ri its position vector. Note that all atoms are currently required to be positioned within the simulation cell.  By default, these will be interpreted as being in atomic units (a0), but they will be interpreted as being Angstroms if "ang" is on the first line of the block.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK POSITIONS_ABS
      S1 R1x R1y R1z
      S2 R2x R2y R2z
       .   .   .   .
       .   .   .   .
      SN RNx RNy RNz
      %ENDBLOCK POSITIONS_ABS

   :Example:

   .. code::

      %BLOCK POSITIONS_ABS
      C  5.0 5.0 5.0 ; CO2 molecule
      O  2.7 5.0 5.0 ; centred in a cubic simulation cell
      O  7.3 5.0 5.0 ; with sides of 10 a0
      %ENDBLOCK POSITIONS_ABS

.. _positions-abs-intermediate:

POSITIONS_ABS_INTERMEDIATE
--------------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`POSITIONS_ABS_INTERMEDIATE`

Cartesian positions for each atom in the intermediate structure (TS search)

.. _positions-abs-product:

POSITIONS_ABS_PRODUCT
---------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`POSITIONS_ABS_PRODUCT`

Cartesian positions for each atom in the product (TS search)

.. _positions-frac:

POSITIONS_FRAC
--------------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`POSITIONS_FRAC`

Fractional positions of atomic species

.. _positions-frac-intermediate:

POSITIONS_FRAC_INTERMEDIATE
---------------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`POSITIONS_FRAC_INTERMEDIATE`

Fractional positions for each atom in the intermediate structure (TS search)

.. _positions-frac-product:

POSITIONS_FRAC_PRODUCT
----------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`POSITIONS_FRAC_PRODUCT`

Fractional positions for each atom in the product (TS search)

.. _positions-intermediate-xyz-file:

POSITIONS_INTERMEDIATE_XYZ_FILE
-------------------------------

:Type: String
:Default: ''
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`POSITIONS_INTERMEDIATE_XYZ_FILE`

.xyz file to read positional data for intermediate structure (TS search)

.. _positions-product-xyz-file:

POSITIONS_PRODUCT_XYZ_FILE
--------------------------

:Type: String
:Default: ''
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`POSITIONS_PRODUCT_XYZ_FILE`

.xyz file to read positional data for product structure (TS search)

.. _positions-xyz-file:

POSITIONS_XYZ_FILE
------------------

:Type: String
:Default: ''
:Unit: None
:Level: Basic
:Group: CELLDATA
:Search: :searchlink:`POSITIONS_XYZ_FILE`

.xyz file to read positional data from

.. _ppd-npoints:

PPD_NPOINTS
-----------

:Type: String
:Default: '0 0 1'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PPD_NPOINTS`

PPD edge length in grid points for each lattice direction

Specifies the size of the parallelepipeds (PPDs) used to group the simulation cell psinc grid points for efficiency. The size of the PPD is given by three integers corresponding to the number of grid points in the a1, a2 and a3 directions respectively. These integers must all be factors of the simulation cell psinc grid size in the relevant direction.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PPD_NPOINTS [Text]

   :Example:

   .. code::

      PPD_NPOINTS 5 7 6

.. _precond-array:

PRECOND_ARRAY
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`PRECOND_ARRAY`

NGWF-specific recip-space KE preconditioning

.. _precond-array-type:

PRECOND_ARRAY_TYPE
------------------

:Type: String
:Default: 'KT'
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`PRECOND_ARRAY_TYPE`

NGWF-specific recip-space KE preconditioning scheme

.. _precond-real:

PRECOND_REAL
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`PRECOND_REAL`

Real-space KE preconditioning

Apply kinetic energy preconditioning by a convolution in real-space. See Mostofiet al.,J. Chem. Phys.119, 8842 (2003) for further details.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PRECOND_REAL [Logical]

   :Example:

   .. code::

      PRECOND_REAL T

.. _precond-recip:

PRECOND_RECIP
-------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`PRECOND_RECIP`

Recip-space KE preconditioning

Apply kinetic energy preconditioning by a multiplication in reciprocal-space. See Mostofiet al.,J. Chem. Phys.119, 8842 (2003) for further details.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PRECOND_RECIP [Logical]

   :Example:

   .. code::

      PRECOND_RECIP F

.. _precond-scheme:

PRECOND_SCHEME
--------------

:Type: String
:Default: 'TETER'
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`PRECOND_SCHEME`

Recip-space preconditioning scheme  BG = Bowler-Gillan method; MAURI = Mauri method; TETER = Teter-Allen-Payne method

Specifies the form of the kinetic energy preconditioner used, currently one of: BG - Bowler-Gillan scheme:Comput. Phys. Commun.112, 103 (1998) MAURI - Mauri scheme TETER - Teter-Payne-Allan scheme:Phys. Rev. B40, 12255 (1989) NONE - no kinetic energy preconditioning

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PRECOND_SCHEME [Text]

   :Example:

   .. code::

      PRECOND_SCHEME MAURI

.. _print-internal-order:

PRINT_INTERNAL_ORDER
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`PRINT_INTERNAL_ORDER`

Print atom indices in internal order.

.. _print-potential-noxc:

PRINT_POTENTIAL_NOXC
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`PRINT_POTENTIAL_NOXC`

Print Local potential withouth XC (only Hartree+Ion)

.. _print-qc:

PRINT_QC
--------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: IO
:Search: :searchlink:`PRINT_QC`

Print Quality Control information

Include a summary of the calculation in the output for the purposes of "quality control" on code modifications.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PRINT_QC [Text]

   :Example:

   .. code::

      PRINT_QC T

.. _product-energy:

PRODUCT_ENERGY
--------------

:Type: Physical
:Default: 100.0
:Unit: hartree
:Level: Intermediate
:Group: TS
:Search: :searchlink:`PRODUCT_ENERGY`

Direct specification of product energy.

Both the reactant and product energies must be known at the start of a NEB calculation. The energy can be specified either as a raw total energy or as a rootname from which ONETEP can read the tightbox NGWF and density kernel (and, in EDFT, Hamiltonian) files from a previous calculation, or they can be calculated from scratch if neither is specified. The reactant and product energies needn’t be specified in the same way. This keyword specifies the total energy of the product.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PRODUCT_ENERGY [Physical]

   :Example:

   .. code::

      PRODUCT_ENERGY -21102.843530 Ha

.. _product-rootname:

PRODUCT_ROOTNAME
----------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`PRODUCT_ROOTNAME`

Specification of product rootname for energy calculation.  User must also include .tightbox_ngwf and .dkn files in this directory.

Both the reactant and product energies must be known at the start of a NEB calculation. The energy can be specified either as a raw total energy or as a rootname from which ONETEP can read the tightbox NGWF and density kernel (and, in EDFT, Hamiltonian) files from a previous calculation, or they can be calculated from scratch if neither is specified. The reactant and product energies needn’t be specified in the same way. This keyword specifies the rootname of the .tightbox_ngwf, .dkn, and/or .ham files that ONETEP can read the product from.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PRODUCT_ROOTNAME [Text]

   :Example:

   .. code::

      PRODUCT_ROOTNAME my_prod_calculation

.. _projectors-precalculate:

PROJECTORS_PRECALCULATE
-----------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PROJECTORS_PRECALCULATE`

Whether to pre-calculate the nonlocal projectors in FFTboxes rather than on-the-fly

Controls whether the projectors are all evaluated in FFTboxes simultaneously, whenever the projector-NGWF overlap or projector gradient is required. If true, all projectors are evaluated at once (requiring many FFTboxes and significant memory usage if many projectors are present). If false, only one projector is evaluated at a time (which is slower, as new projectors must be re-evaluated many times over, but uses minimal memory).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PROJECTORS_PRECALCULATE [Text]

   :Example:

   .. code::

      PROJECTORS_PRECALCULATE F

.. _project-embed:

PROJECT_EMBED
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`PROJECT_EMBED`

Do an embedding calculation using the projector method

.. _pseudo-path:

PSEUDO_PATH
-----------

:Type: String
:Default: Unknown
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`PSEUDO_PATH`

Path to pseudopotentials

.. _psinc-spacing:

PSINC_SPACING
-------------

:Type: String
:Default: '0.0 0.0 0.0'
:Unit: None
:Level: Expert
:Group: CELLDATA
:Search: :searchlink:`PSINC_SPACING`

PSINC grid spacing in atomic units

Specifies the spacing between psinc grid points in the simulation cell by three real values (in atomic units a0) in the a1,a2 and a3directions respectively. These spacings must all be factors of the simulation cell lengths in the relevant directions.  By default, these will be interpreted as being in atomic units (a0), but any recognised unit symbol can be used after the third value to override to a specific choice of units.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      PSINC_SPACING [Text]

   :Example:

   .. code::

      PSINC_SPACING 0.4 0.5 0.5
      or
      
      PSINC_SPACING 0.25 0.25 0.25 ang

.. _pspot-bc:

PSPOT_BC
--------

:Type: String
:Default: ''
:Unit: None
:Level: Intermediate
:Group: BC
:Search: :searchlink:`PSPOT_BC`

3 character string defining BCs for local pseudopotential along each lattice vector. 'O' for open, 'P' for periodic.

.. _qnto-analysis:

QNTO_ANALYSIS
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: LRTDDFT
:Search: :searchlink:`QNTO_ANALYSIS`

Runs QNTO analysis

.. _qnto-nbo-proj:

QNTO_NBO_PROJ
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`QNTO_NBO_PROJ`

Enables projection to NBOs

.. _qnto-num-core-atoms:

QNTO_NUM_CORE_ATOMS
-------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`QNTO_NUM_CORE_ATOMS`

Sets the number of atoms for projection

.. _qnto-num-ref-states:

QNTO_NUM_REF_STATES
-------------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`QNTO_NUM_REF_STATES`

Sets the number of states to reference

.. _qnto-num-transition:

QNTO_NUM_TRANSITION
-------------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`QNTO_NUM_TRANSITION`

Sets the number of NTO pairs to output or compare

.. _qnto-ref-dir:

QNTO_REF_DIR
------------

:Type: String
:Default: ''
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`QNTO_REF_DIR`

Sets the reference directory for NTO projection

.. _qnto-svd-method:

QNTO_SVD_METHOD
---------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Expert
:Group: LRTDDFT
:Search: :searchlink:`QNTO_SVD_METHOD`

Sets the SVD method

.. _qnto-write-orbitals:

QNTO_WRITE_ORBITALS
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: LRTDDFT
:Search: :searchlink:`QNTO_WRITE_ORBITALS`

Enables plotting NTOs

.. _quip-calc-args:

QUIP_CALC_ARGS
--------------

:Type: String
:Default: ''
:Unit: None
:Level: Expert
:Group: FORCE_FIELD
:Search: :searchlink:`QUIP_CALC_ARGS`

QUIP calculation-time arguments string arguments for potential calculation

.. _quip-init-args:

QUIP_INIT_ARGS
--------------

:Type: String
:Default: ''
:Unit: None
:Level: Expert
:Group: FORCE_FIELD
:Search: :searchlink:`QUIP_INIT_ARGS`

QUIP Initialisation arguments string arguments for initializing potential

.. _quip-param-file:

QUIP_PARAM_FILE
---------------

:Type: String
:Default: ''
:Unit: None
:Level: Expert
:Group: FORCE_FIELD
:Search: :searchlink:`QUIP_PARAM_FILE`

QUIP parameter filename

.. _rand-normal-sigma:

RAND_NORMAL_SIGMA
-----------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`RAND_NORMAL_SIGMA`

User specified sigma for normal distributed random numbers

.. _rand-seed:

RAND_SEED
---------

:Type: Integer
:Default: -1
:Unit: None
:Level: Basic
:Group: MD
:Search: :searchlink:`RAND_SEED`

Seed for generating velocities in MD from Maxwell-Boltzmann distribution

.. _rand-seed-ngwf-dynamic:

RAND_SEED_NGWF_DYNAMIC
----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`RAND_SEED_NGWF_DYNAMIC`

To use datetime dependent seed for pseudo-random generator

.. _reactant-energy:

REACTANT_ENERGY
---------------

:Type: Physical
:Default: 100.0
:Unit: hartree
:Level: Intermediate
:Group: TS
:Search: :searchlink:`REACTANT_ENERGY`

Direct specification of reactant energy.

Both the reactant and product energies must be known at the start of a NEB calculation. The energy can be specified either as a raw total energy or as a rootname from which ONETEP can read the tightbox NGWF and density kernel (and, in EDFT, Hamiltonian) files from a previous calculation, or they can be calculated from scratch if neither is specified. The reactant and product energies needn’t be specified in the same way. This keyword specifies the total energy of the reactant.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      REACTANT_ENERGY [Physical]

   :Example:

   .. code::

      neb_REACTANT_ENERGY -21102.843530 Ha

.. _reactant-rootname:

REACTANT_ROOTNAME
-----------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`REACTANT_ROOTNAME`

Specification of reactant rootname for energy calculation.  User must also include .tightbox_ngwf and .dkn files in this directory.

Both the reactant and product energies must be known at the start of a NEB calculation. The energy can be specified either as a raw total energy or as a rootname from which ONETEP can read the tightbox NGWF and density kernel (and, in EDFT, Hamiltonian) files from a previous calculation, or they can be calculated from scratch if neither is specified. The reactant and product energies needn’t be specified in the same way. This keyword specifies the rootname of the .tightbox_ngwf, .dkn, and/or .ham files that ONETEP can read the reactant from.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      REACTANT_ROOTNAME [Text]

   :Example:

   .. code::

      REACTANT_ROOTNAME my_reac_calculation

.. _read-denskern:

READ_DENSKERN
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`READ_DENSKERN`

Read density kernel restart information

Read in the density kernel from disk. If the input filename is rootname.dat then the density kernel filename is rootname.denskern .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      READ_DENSKERN [Logical]

   :Example:

   .. code::

      READ_DENSKERN T

.. _read-hamiltonian:

READ_HAMILTONIAN
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: IO
:Search: :searchlink:`READ_HAMILTONIAN`

Read current Hamiltonian matrix from a file

Read the Hamiltonian matrix from a .ham file. Currently, only used for restarting :ref:`edft` calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      READ_HAMILTONIAN [Logical]

   :Example:

   .. code::

      READ_HAMILTONIAN F

.. _read-max-l:

READ_MAX_L
----------

:Type: Integer
:Default: 3
:Unit: None
:Level: Intermediate
:Group: IO
:Search: :searchlink:`READ_MAX_L`

Maximum angular momentum number when reading in SW representation

Specifies the maximum angular momentum of the spherical waves (l number) when reading from file.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      READ_MAX_L [Integer]

   :Example:

   .. code::

      READ_MAX_L 5

.. _read-real-ngwfs:

READ_REAL_NGWFS
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`READ_REAL_NGWFS`

Read real NGWFs from file into complex NGWFs

.. _read-sub-denskern:

READ_SUB_DENSKERN
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`READ_SUB_DENSKERN`

Read density kernel restart information from subsystem kernels.

.. _read-sw-ngwfs:

READ_SW_NGWFS
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`READ_SW_NGWFS`

Read NGWFs restart information in spherical waves representation

Read in the NGWFs from disk in spherical waves format and generates a linear combination of SW to restart the NGWFs. If the input filename is rootname.dat then the NGWFs filename is rootname.sw_ngwfs .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      READ_SW_NGWFS [Logical]

   :Example:

   .. code::

      READ_SW_NGWFS T

.. _read-tightbox-ngwfs:

READ_TIGHTBOX_NGWFS
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`READ_TIGHTBOX_NGWFS`

Read in universal tightbox NGWFs restart information

Read in the NGWFs from disk. If the input filename is rootname.dat then the NGWFs filename is rootname.tightbox_ngwfs .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      READ_TIGHTBOX_NGWFS [Logical]

   :Example:

   .. code::

      READ_TIGHTBOX_NGWFS T

.. _realspace-projectors:

REALSPACE_PROJECTORS
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`REALSPACE_PROJECTORS`

Whether to evaluate and store projectors in real space

.. _rms-kernel-measure:

RMS_KERNEL_MEASURE
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: CONV
:Search: :searchlink:`RMS_KERNEL_MEASURE`

Use root mean squared measure of [K,H] commutator and delta K

Use a legacy measure of the commutator of the density-matrix and Hamiltonian, given by the root mean squared value of the doubly-covariant NGWF representation of their commutator.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      RMS_KERNEL_MEASURE [Logical]

   :Example:

   .. code::

      RMS_KERNEL_MEASURE T

.. _run-time:

RUN_TIME
--------

:Type: Double-Precision
:Default: -1.0
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`RUN_TIME`

The maximum allocated run time for this job (in seconds)

The maximum allocated run time for this job (in seconds). Certain iterative processes (NGWF CG, electronic transport etc) are timed on a per-iteration basis: if the timer detects that there is not enough time left before the total elapsed wall time reaches the value of RUN_TIME, then the iterative process will be halted to allow the code to exit gracefully.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      RUN_TIME [Real]

   :Example:

   .. code::

      RUN_TIME 43000

.. _r-precond:

R_PRECOND
---------

:Type: Physical
:Default: 2.0
:Unit: bohr
:Level: Expert
:Group: CONV
:Search: :searchlink:`R_PRECOND`

Radial cut-off for real-space preconditioner

Specifies the radius in atomic units (a0) of the real-space kinetic energy preconditioner (used to accelerate the convolution).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      R_PRECOND [Value] [Unit]

   :Example:

   .. code::

      R_PRECOND 1.5 bohr

.. _r-smooth:

R_SMOOTH
--------

:Type: Physical
:Default: 1.5
:Unit: bohr
:Level: Expert
:Group: None
:Search: :searchlink:`R_SMOOTH`

Radius of the unshaved NGWF gradients

.. _show-overlap:

SHOW_OVERLAP
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`SHOW_OVERLAP`

Save to file overlap matrix at the end of the calculation

.. _simulationbox-pref:

SIMULATIONBOX_PREF
------------------

:Type: String
:Default: '0 0 0'
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`SIMULATIONBOX_PREF`

Preferred simulation box dimensions

.. _smeared-ion-bc:

SMEARED_ION_BC
--------------

:Type: String
:Default: ''
:Unit: None
:Level: Intermediate
:Group: BC
:Search: :searchlink:`SMEARED_ION_BC`

3 character string defining BCs for smeared ion representation along each lattice vector. 'O' for open, 'P' for periodic.

.. _smoothing-factor:

SMOOTHING_FACTOR
----------------

:Type: Double-Precision
:Default: 5.0
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`SMOOTHING_FACTOR`

Smoothing factor in volume term

The electronic volume Ve used in the electronic enthalpy method is obtained by using a Heaviside step function smeared by a smoothing factor [ corresponding to alpha/sigma in Corsini et al, J. Chem. Phys. 2013, 139, 084117] for numerical reasons.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      SMOOTHING_FACTOR [Value]

   :Example:

   .. code::

      SMOOTHING_FACTOR 6.0

.. _smooth-loc-pspot:

SMOOTH_LOC_PSPOT
----------------

:Type: Double-Precision
:Default: -0.4
:Unit: None
:Level: Expert
:Group: PSEUDO
:Search: :searchlink:`SMOOTH_LOC_PSPOT`

Halfwidth of Gaussian filter for local pseudopotential

.. _smooth-projectors:

SMOOTH_PROJECTORS
-----------------

:Type: Double-Precision
:Default: -0.4
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`SMOOTH_PROJECTORS`

Halfwidth of Gaussian filter for nonlocal projectors

Specifies the half-width in atomic units (a0) of a Gaussian filter used to smooth the nonlocal projectors. A negative value indicates that no smoothing should be applied.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      SMOOTH_PROJECTORS [Real]

   :Example:

   .. code::

      SMOOTH_PROJECTORS 0.5

.. _smooth-scheme:

SMOOTH_SCHEME
-------------

:Type: String
:Default: 'NONE'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`SMOOTH_SCHEME`

Smoothing scheme for the NGWF gradients at the edges

.. _sol-ions:

SOL_IONS
--------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: SOLVATION
:Search: :searchlink:`SOL_IONS`

Ions in solvent: name, charge, concentration

Describes the kinds of Boltzmann ions in implicit solvent. Only relevant when solving the Poisson-Boltzmann equation in implicit solvent. Each entry specifies a name (species), charge and concentration (in mol/L).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK SOL_IONS
      species1 charge1 conc1
      species2 charge2 conc2
      ... ... ...
      speciesn chargen concn
      %ENDBLOCK SOL_IONS

   :Example:

   .. code::

      %BLOCK SOL_IONS
       Mg +2 0.1    ; MgCl2 @ 0.1 mol/L
       Cl -1 0.2
      %ENDBLOCK SOL_IONS

.. _sparse-debug-comms:

SPARSE_DEBUG_COMMS
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`SPARSE_DEBUG_COMMS`

Print debug information for comms in sparse product

.. _sparse-num-comms-buffers:

SPARSE_NUM_COMMS_BUFFERS
------------------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`SPARSE_NUM_COMMS_BUFFERS`

How many buffers to allocate at once in sparse product

.. _sparse-preshared-comms:

SPARSE_PRESHARED_COMMS
----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`SPARSE_PRESHARED_COMMS`

Pre-communicate all matrix data before calculation

.. _sparse-shared-comms:

SPARSE_SHARED_COMMS
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`SPARSE_SHARED_COMMS`

Use MPI windows for shared comms in sparse product

.. _sparse-shared-data:

SPARSE_SHARED_DATA
------------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`SPARSE_SHARED_DATA`

Use MPI windows for shared data over comms groups in sparse

.. _species:

SPECIES
-------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: GENERAL
:Search: :searchlink:`SPECIES`

Species information (symbol, atomic number, number of NGWFs, NGWF radius)

Defines the atomic SPECIES. In the above syntax, Si denotes the :ref:`species` of atom i(max 4 characters), corresponding to the element with symbol Xi and atomic number ZN , and with which are associated ni NGWFs of radius RN . More than one atomic :ref:`species` may refer to the same element, e.g. so that different ionic constraints may be applied to them.  By default, the radii will be interpreted as being in atomic units (a0), but they will be interpreted as being Angstroms if "ang" is on the first line of the block.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK SPECIES
      S1 X1 Z1 n1 R1
      S2 X2 Z2 n2 R2
       .  .  .  .  .
       .  .  .  .  .
      SN XN ZN nN RN
      %ENDBLOCK SPECIES

   :Example:

   .. code::

      %BLOCK SPECIES
      C1  C  6  4  6.0 ; SPECIES C1 is carbon with 4 NGWFs of radius 6.0 a0
      C2  C  6  4  7.0 ; SPECIES C2 is also carbon but has 7.0 a0 NGWF radii
      H   H  1  1  5.0 ; SPECIES H is hydrogen with 1 NGWF of radius 5.0 a0
      %ENDBLOCK SPECIES

.. _species-atomic-set:

SPECIES_ATOMIC_SET
------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`SPECIES_ATOMIC_SET`

Atomic set name for each species

Specifies the set of initial atomic or pseudoatomic orbitals which will be used to initialise the NGWFs. One can either specify "fireball" (truncated pseudoatomic orbital) files,or use AUTO to generate STO-3G and 6-31G* basis functions, or one can use the built-in pseudoatomic solver, using "SOLVE". With "SOLVE", a configuration for the neutral pseudoatom is guessed on the basis of the ion charge and the atomic number, but this can be overridden. See the help file "pseudoatomic_solver.pdf" in the documentation folder (/doc in the distribution) for more information on how to use the pseudoatomic solver In the above syntax, Si denotes atomic species i(max 4 characters). automatically as required.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK SPECIES_ATOMIC_SET
      S1 <Fireball filename 1> | AUTO | SOLVE
      S2 <Fireball filename 2> | AUTO | SOLVE
      .         ..                .
      %ENDBLOCK SPECIES_ATOMIC_SET

   :Example:

   .. code::

      %BLOCK SPECIES_ATOMIC_SET
      C1  C_01.fbl
      H   SOLVE
      %ENDBLOCK SPECIES_ATOMIC_SET

.. _species-atomic-set-aux:

SPECIES_ATOMIC_SET_AUX
----------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`SPECIES_ATOMIC_SET_AUX`

Atomic set description for each species, for initialising Auxiliary NGWFs

.. _species-atomic-set-cond:

SPECIES_ATOMIC_SET_COND
-----------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: COND
:Search: :searchlink:`SPECIES_ATOMIC_SET_COND`

Atomic set description for each species, for initialising Conduction NGWFs

.. _species-aux:

SPECIES_AUX
-----------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`SPECIES_AUX`

Species information for Auxiliary NGWFs (symbol, atomic number, number of NGWFs, NGWF radius)

.. _species-bsunfld-groups:

SPECIES_BSUNFLD_GROUPS
----------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: BS_UNFOLDING
:Search: :searchlink:`SPECIES_BSUNFLD_GROUPS`

Species groups for spectral function unfolding calculation

.. _species-bsunfld-projatoms:

SPECIES_BSUNFLD_PROJATOMS
-------------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: BS_UNFOLDING
:Search: :searchlink:`SPECIES_BSUNFLD_PROJATOMS`

Species projected atoms for spectral function unfolding calculation

.. _species-cond:

SPECIES_COND
------------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: COND
:Search: :searchlink:`SPECIES_COND`

Species information for Conduction NGWFs (symbol, atomic number, number of NGWFs, NGWF radius)

Defines the atomic species used for conduction optimisation. The atomic species details must match those given in the :ref:`species` block, and the same guidelines apply.  By default, the radii will be interpreted as being in atomic units (a0), but they will be interpreted as being Angstroms if "ang" is on the first line of the block.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK SPECIES_COND
      S1 X1 Z1 n1 R1
      S2 X2 Z2 n2 R2
       .  .  .  .  .
       .  .  .  .  .
      SN XN ZN nN RN
      %ENDBLOCK SPECIES

   :Example:

   .. code::

      %BLOCK species
      C1  C  6  9 12.0 ; species C1 is carbon with 9 NGWFs of radius 12.0 a0
      C2  C  6  9 12.0 ; species C2 is also carbon but has 12.0 a0 NGWF radii
      H   H  1  4 10.0 ; species H is hydrogen with 4 NGWFs of radius 10.0 a0
      %ENDBLOCK species

.. _species-constraints:

SPECIES_CONSTRAINTS
-------------------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`SPECIES_CONSTRAINTS`

Ionic constraints for each species

Defines the constraints for the atomic species for use during geometry optimization. In the above syntax, Si denotes atomic speciesi(max 4 characters). The constraint type is one of NONE (no constraint), FIXED (atom is constrained to remain fixed), LINE (atom is constrained to a line) or PLANE (atom is constrained to a plane). In the case of LINE and PLANE , three further real values are required, to specify the direction vector of the line or the normal vector to the plane (in Cartesian coordinates) respectively.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK SPECIES_CONSTRAINTS
      S1 NONE | FIXED | LINE | PLANE  [C1x C1y C1z]
      .               .                 .   .   .
      %ENDBLOCK SPECIES_CONSTRAINTS

   :Example:

   .. code::

      %BLOCK SPECIES_CONSTRAINTS
      C1  FIXED             ; atoms of species C1 are fixed
      C2  LINE  1.0 0.0 0.0 ; atoms of species C2 can only move parallel to thex-axis
      H   PLANE 0.0 0.0 1.0 ; atoms of species H can only move in thexy-plane
      %ENDBLOCK SPECIES_CONSTRAINTS

.. _species-core-wf:

SPECIES_CORE_WF
---------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`SPECIES_CORE_WF`

Core Wavefunction filename for each species

.. _species-ldos-groups:

SPECIES_LDOS_GROUPS
-------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: GENERAL
:Search: :searchlink:`SPECIES_LDOS_GROUPS`

Species groups for Local density of states calculation

Defines the groups of species identifiers for which the groups of an LDOS plot are defined. Each line defines a group with any number of entries allowed on the line. Species identifier labels must correspond to those defined in %BLOCK species .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK SPECIES_LDOS_GROUPS
      S1 S2 S3
      .  .  .
      %ENDBLOCK SPECIES_LDOS_GROUPS

   :Example:

   .. code::

      %BLOCK SPECIES_LDOS_GROUPS
      C1 H1 ; atoms of species C1 and H1 are in first group
      C2 H2 ; atoms of species C1 and H1 are in second group
      %ENDBLOCK SPECIES_LDOS_GROUPS

.. _species-locdipole-groups:

SPECIES_LOCDIPOLE_GROUPS
------------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: GENERAL
:Search: :searchlink:`SPECIES_LOCDIPOLE_GROUPS`

Species groups for calculation of dipole moments of subsystems

.. _species-ngwf-plot:

SPECIES_NGWF_PLOT
-----------------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`SPECIES_NGWF_PLOT`

Species whose NGWFs to plot

Defines the atomic species whose NGWFs are to be plotted during the calculation. In the above syntax, Si denotes atomic species i to plot.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK SPECIES_NGWF_PLOT
      S1
      S2
      .
      %ENDBLOCK SPECIES_NGWF_PLOT

   :Example:

   .. code::

      %BLOCK SPECIES_NGWF_PLOT
      C1
      C2
      H
      %ENDBLOCK SPECIES_NGWF_PLOT

.. _species-ngwf-regions:

SPECIES_NGWF_REGIONS
--------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: GENERAL
:Search: :searchlink:`SPECIES_NGWF_REGIONS`

Regions that each atom is allocated to

.. _species-pdos-groups:

SPECIES_PDOS_GROUPS
-------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: GENERAL
:Search: :searchlink:`SPECIES_PDOS_GROUPS`

Species groups for Local, angular momentum projected density of states calculation

.. _species-pot:

SPECIES_POT
-----------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: PSEUDO
:Search: :searchlink:`SPECIES_POT`

Pseudopotential name for each species

Specifies the pseudopotential files for the atomic species in a norm-conserving pseudopotential calculation, or the :ref:`paw` potentials in a :ref:`paw` Calculation. In the above syntax, Si denotes atomic species i (max 4 characters). Pseudopotential files can be in the CASTEP .recpot format or .usp format and must define norm-conserving pseudopotentials. :ref:`paw` Potentials can be in the ABINIT .paw format.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK SPECIES_POT
      S1 <Pseudopotential filename 1>
      S2 <Pseudopotential filename 2>
      .                ..
      %ENDBLOCK SPECIES_POT

   :Example:

   .. code::

      %BLOCK SPECIES_POT
      C1  C_01.recpot
      C2  C_00.recpot
      H   H_01.recpot
      %ENDBLOCK SPECIES_POT

.. _species-scissor:

SPECIES_SCISSOR
---------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`SPECIES_SCISSOR`

Apply energy shift to species hamiltonian eigenvalues

.. _species-solvent-radius:

SPECIES_SOLVENT_RADIUS
----------------------

:Type: Block
:Default: None
:Unit: None
:Level: Expert
:Group: SOLVATION
:Search: :searchlink:`SPECIES_SOLVENT_RADIUS`

Implicit solvent: solvent radius around ions

.. _species-tddft-ct:

SPECIES_TDDFT_CT
----------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: GENERAL
:Search: :searchlink:`SPECIES_TDDFT_CT`

Species groups defining the region in which the TDDFTct is defined

.. _species-tddft-kernel:

SPECIES_TDDFT_KERNEL
--------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: GENERAL
:Search: :searchlink:`SPECIES_TDDFT_KERNEL`

Species groups defining the region in which the TDDFT kernel is defined

.. _spin:

SPIN
----

:Type: Double-Precision
:Default: Unknown
:Unit: None
:Level: Basic
:Group: SPIN
:Search: :searchlink:`SPIN`

Total spin of system

Specifies the total :ref:`spin` of the system in units of 1/2;h/(2pi). If the total :ref:`spin` is non-zero, a SPIN-polarized calculation will automatically be selected. Can be specified as a non-integer number in :ref:`edft` calculations.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      SPIN [Integer]

   :Example:

   .. code::

      SPIN 1

.. _spin-polarised:

SPIN_POLARISED
--------------

:Type: Boolean
:Default: Unknown
:Unit: None
:Level: Basic
:Group: SPIN
:Search: :searchlink:`SPIN_POLARISED`

Switch for spin polarisation

.. _spin-polarized:

SPIN_POLARIZED
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: SPIN
:Search: :searchlink:`SPIN_POLARIZED`

Switch for spin polarisation

Specifies that a spin-polarized calculation should be performed.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      SPIN_POLARIZED [Logical]

   :Example:

   .. code::

      SPIN_POLARIZED T

.. _spread-calculate:

SPREAD_CALCULATE
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`SPREAD_CALCULATE`

Calculate spread of NGWFs

Activates the Calculation of NGWF spreads

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      SPREAD_CALCULATE [Text]

   :Example:

   .. code::

      SPREAD_CALCULATE T

.. _stress-assumed-symmetry:

STRESS_ASSUMED_SYMMETRY
-----------------------

:Type: String
:Default: 'nosymm'
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_ASSUMED_SYMMETRY`

Use assumed symmetry to minimise calculations. Values are: 'nosymm'; 3D: 'cubic', 'ortho', 'tetra1', 'tetra2', 'hexa3d', 'rhomb1', 'rhomb2'; 2D: recta, squar1, squar2, hexa2d.

.. _stress-components:

STRESS_COMPONENTS
-----------------

:Type: String
:Default: 'T T T'
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_COMPONENTS`

Which rows/columns of the stress tensor to compute. The flags match X Y Z. Overrides stress_assumed_summetry.

.. _stress-deformation-step:

STRESS_DEFORMATION_STEP
-----------------------

:Type: Double-Precision
:Default: 0.002
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_DEFORMATION_STEP`

Unitless strain parameter in finite differences. It controls how different the deformation matrix is from the identity.

.. _stress-elasticity:

STRESS_ELASTICITY
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_ELASTICITY`

Enable the calculation of elastic constants.

.. _stress-maxit-ngwf-cg:

STRESS_MAXIT_NGWF_CG
--------------------

:Type: Integer
:Default: 10
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_MAXIT_NGWF_CG`

Maximum number of NGWF CG iterations for total energy calculations of distorted cells needed for the stress tensor.

.. _stress-relax:

STRESS_RELAX
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_RELAX`

Use the stress tensor to optimise the cell parameters.

.. _stress-relax-atoms:

STRESS_RELAX_ATOMS
------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_RELAX_ATOMS`

Atomic positions are relaxed together with cell parameters.

.. _stress-relax-cell-diis:

STRESS_RELAX_CELL_DIIS
----------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_RELAX_CELL_DIIS`

The cell parameters are optimised using DIIS and the history of previous calculations.

.. _stress-relax-cell-rtol:

STRESS_RELAX_CELL_RTOL
----------------------

:Type: Double-Precision
:Default: 0.001
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_RELAX_CELL_RTOL`

Convergence criterion for relative change of cell parameters in cell relaxation.

.. _stress-relax-diis-mem:

STRESS_RELAX_DIIS_MEM
---------------------

:Type: Integer
:Default: 2
:Unit: None
:Level: Intermediate
:Group: STRESS
:Search: :searchlink:`STRESS_RELAX_DIIS_MEM`

How many previous calculations to keep in memory for cell relaxation using DIIS.

.. _stress-relax-energy-tol:

STRESS_RELAX_ENERGY_TOL
-----------------------

:Type: Physical
:Default: 0.0001
:Unit: hartree
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_RELAX_ENERGY_TOL`

Convergence criterion for absolute change of total energy per atom in cell relaxation.

.. _stress-relax-max-iter:

STRESS_RELAX_MAX_ITER
---------------------

:Type: Integer
:Default: 10
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_RELAX_MAX_ITER`

Maximum number of iterations in cell relaxation.

.. _stress-relax-max-step:

STRESS_RELAX_MAX_STEP
---------------------

:Type: Double-Precision
:Default: 0.01
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_RELAX_MAX_STEP`

Maximum step size for distortion in cell relaxation.

.. _stress-relax-out-angstrom:

STRESS_RELAX_OUT_ANGSTROM
-------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_RELAX_OUT_ANGSTROM`

The cell parameters and atomic positions are written to the .cell file in angstrom.

.. _stress-relax-pressure:

STRESS_RELAX_PRESSURE
---------------------

:Type: Physical
:Default: 0.0
:Unit: ha/bohr**3
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_RELAX_PRESSURE`

External pressure applied during cell relaxation.

.. _stress-relax-pressure-tol:

STRESS_RELAX_PRESSURE_TOL
-------------------------

:Type: Physical
:Default: 1e-05
:Unit: ha/bohr**3
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_RELAX_PRESSURE_TOL`

Convergence criterion for absolute change of pressure in cell relaxation.

.. _stress-rescale-volume:

STRESS_RESCALE_VOLUME
---------------------

:Type: Double-Precision
:Default: 1.0
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_RESCALE_VOLUME`

Rescaling for cell volume. Use for 1D or 2D systems.

.. _stress-tensor:

STRESS_TENSOR
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: STRESS
:Search: :searchlink:`STRESS_TENSOR`

Enable the calculation of the stress tensor.

.. _supercell:

SUPERCELL
---------

:Type: Block
:Default: None
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`SUPERCELL`

Definition of supercell

Within this block, the first line gives the shape of the :ref:`supercell` (2x2x2), and subsequent lines list the ions in the positions_abs_block that belong to the 'base' unit cell. When a :ref:`supercell` calculation is specified, only the ions within the unit cell are displaced, although the forces on all ions in the system are used to calculate the elements of the dynamical matrix. It is also possible to specify :ref:`phonon-vib-free` and :ref:`phonon-exception-list` in a :ref:`supercell` calculation, although only the ions listed in the :ref:`supercell` block can be included in the a href="#phonon_exception_list"> :ref:`phonon-exception-list` block.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK SUPERCELL
      factor_a1 factor_a2 factor_a3
      ion1_base
      ...
      ionN_base
      %ENDBLOCK SUPERCELL

   :Example:

   .. code::

      In this example, we are defining a 2x2x2 SUPERCELL (for example for
      Si), with the ions of index 1 and 9 defining the "base" unit cell.
      Of course, a small SUPERCELL will not give sensible results for a phonon calculation.
      However, a good example would be a 1000-atom cubic SUPERCELL of Si, which gives excellent results.
      
      
      %BLOCK SUPERCELL
      
      2 2 2
      
      1
      
      9
      
      %ENDBLOCK SUPERCELL

.. _swri:

SWRI
----

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: SWRI
:Search: :searchlink:`SWRI`

Defines spherical-wave resolutions of identity

.. _swri-assembly-prefix:

SWRI_ASSEMBLY_PREFIX
--------------------

:Type: String
:Default: Unknown
:Unit: None
:Level: Expert
:Group: SWRI
:Search: :searchlink:`SWRI_ASSEMBLY_PREFIX`

Directory+rootname for assembling [VO]matrix blocks

.. _swri-cheb-batchsize:

SWRI_CHEB_BATCHSIZE
-------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Expert
:Group: SWRI
:Search: :searchlink:`SWRI_CHEB_BATCHSIZE`

Number of SW pot expansions buffered

.. _swri-improve-inverse:

SWRI_IMPROVE_INVERSE
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SWRI
:Search: :searchlink:`SWRI_IMPROVE_INVERSE`

Use Hotelling improvement when calculating inverses

.. _swri-overlap-indirect:

SWRI_OVERLAP_INDIRECT
---------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SWRI
:Search: :searchlink:`SWRI_OVERLAP_INDIRECT`

Inversions done for overlap metric

.. _swri-print-eigenvalues:

SWRI_PRINT_EIGENVALUES
----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SWRI
:Search: :searchlink:`SWRI_PRINT_EIGENVALUES`

Print debugging SW metric matrix eigenvalue info?

.. _swri-proximity-sort-point:

SWRI_PROXIMITY_SORT_POINT
-------------------------

:Type: String
:Default: '0.0 0.0 0.0'
:Unit: None
:Level: Intermediate
:Group: SWRI
:Search: :searchlink:`SWRI_PROXIMITY_SORT_POINT`

SWRI atomblocks will be processed closest-first to this point

.. _swri-swop-smoothing:

SWRI_SWOP_SMOOTHING
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SWRI
:Search: :searchlink:`SWRI_SWOP_SMOOTHING`

Apply SW/SWpot smoothing for more accurate overlaps?

.. _swri-verbose:

SWRI_VERBOSE
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: SWRI
:Search: :searchlink:`SWRI_VERBOSE`

Verbose output for spherical wave resolution of identity?

.. _swx-c-threshold:

SWX_C_THRESHOLD
---------------

:Type: Double-Precision
:Default: 0.0
:Unit: None
:Level: Expert
:Group: SWX
:Search: :searchlink:`SWX_C_THRESHOLD`

Absolute magnitude below which expansion coefficients will be zeroed

.. _swx-dbl-grid:

SWX_DBL_GRID
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: SWX
:Search: :searchlink:`SWX_DBL_GRID`

Should spherical-wave expansion use double grid?

.. _swx-output-detail:

SWX_OUTPUT_DETAIL
-----------------

:Type: String
:Default: 'DEFAULT'
:Unit: None
:Level: Basic
:Group: SWX
:Search: :searchlink:`SWX_OUTPUT_DETAIL`

Level of output detail for SWX: BRIEF, NORMAL or VERBOSE

.. _symmetry-tol:

SYMMETRY_TOL
------------

:Type: Physical
:Default: 0.001889726
:Unit: bohr
:Level: Expert
:Group: None
:Search: :searchlink:`SYMMETRY_TOL`

Tolerance to use when searching for symmetry operations

.. _task:

TASK
----

:Type: String
:Default: 'SINGLEPOINT'
:Unit: None
:Level: Basic
:Group: GENERAL
:Search: :searchlink:`TASK`

Type of calculation

Specifies the :ref:`task` to be carried out, currently one of: SINGLEPOINT - single point energy calculation COND - Conduction NGWF optimisation calculation PROPERTIES - properties using results from a previous calculation of the ground state. PROPERTIES_COND - properties using results from a previous calculation of the conduction NGWFs. GEOMETRYOPTIMIZATION - geometry optimization using Cartesian or delocalized internal coordinates. MOLECULARDYNAMICS - molecular dynamics simulation. TRANSITIONSTATESEARCH - transition state search PHONON - a phonon frequencies and thermodynamics calculation. HUBBARDSCF - a projector-self-consistent DFT+U calculation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      TASK [Text]

   :Example:

   .. code::

      TASK GEOMETRYOPTIMIZATION

.. _tddft-damping:

TDDFT_DAMPING
-------------

:Type: Physical
:Default: 0.0
:Unit: hartree
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_DAMPING`

Energy smearing when Fourier transforming for frequency-dependent dipole moment

.. _tddft-dipole-kick-strength:

TDDFT_DIPOLE_KICK_STRENGTH
--------------------------

:Type: String
:Default: '0.0 0.0 0.0'
:Unit: None
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_DIPOLE_KICK_STRENGTH`

Maximum allowed phase shift in TDDFT delta-kick, units of PI

.. _tddft-enforced-idempotency:

TDDFT_ENFORCED_IDEMPOTENCY
--------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_ENFORCED_IDEMPOTENCY`

Project out at each timestep that part of change to denskern not respecting idempotency to 1st order

.. _tddft-hamiltonian-mixing:

TDDFT_HAMILTONIAN_MIXING
------------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_HAMILTONIAN_MIXING`

Order of polynomial extrapolation to H(t + half Delta t) 0,1,2

.. _tddft-inv-overlap-exact:

TDDFT_INV_OVERLAP_EXACT
-----------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_INV_OVERLAP_EXACT`

Renew inverse overlap with O N^3 algorithm before beginning TDDFT

.. _tddft-maximum-energy:

TDDFT_MAXIMUM_ENERGY
--------------------

:Type: Physical
:Default: 1.0
:Unit: hartree
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_MAXIMUM_ENERGY`

Desired maximum of spectrum from TDDFT

.. _tddft-maxit-hotelling:

TDDFT_MAXIT_HOTELLING
---------------------

:Type: Integer
:Default: 50
:Unit: None
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_MAXIT_HOTELLING`

Number of Hotelling iteration per propagation step in Crank-Nicholson propagator

.. _tddft-max-resid-hotelling:

TDDFT_MAX_RESID_HOTELLING
-------------------------

:Type: Double-Precision
:Default: 1e-18
:Unit: None
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_MAX_RESID_HOTELLING`

Max allowed value in Hotelling residual for Crank-Nicholson propagator

.. _tddft-propagation-method:

TDDFT_PROPAGATION_METHOD
------------------------

:Type: String
:Default: 'CRANKNICHOLSON'
:Unit: None
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_PROPAGATION_METHOD`

Method used to integrate von Neumann equation eg. RUNGEKUTTA or CRANKNICHOLSON

.. _tddft-resolution:

TDDFT_RESOLUTION
----------------

:Type: Physical
:Default: 0.001
:Unit: hartree
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_RESOLUTION`

Desired resolution of spectrum from TDDFT (in Hartree)

.. _tddft-sparsity-level:

TDDFT_SPARSITY_LEVEL
--------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_SPARSITY_LEVEL`

Matrix sparsity when computing propagators e.g. 0(recommended),1,2,3

.. _tddft-tammdancoff:

TDDFT_TAMMDANCOFF
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_TAMMDANCOFF`

Invoke Tamm-Dancoff decoupling approximation

.. _tddft-xc-functional:

TDDFT_XC_FUNCTIONAL
-------------------

:Type: String
:Default: 'LDA'
:Unit: None
:Level: Expert
:Group: TDDFT
:Search: :searchlink:`TDDFT_XC_FUNCTIONAL`

Exchange-correlation functional for TDDFT  LDA = Adiabatic Perdew-Zunger LDA; NONE = Random Phase Approximation.

.. _thermostat:

THERMOSTAT
----------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`THERMOSTAT`

Thermostat for MD in NVT ensemble

Defines the molecular dynamics THERMOSTAT. For each THERMOSTAT, the first line should contain the following mandatory parameters, time_start (integer): the time step at which the :ref:`thermostat` is initialized; time_stop (integer): the time step at which the :ref:`thermostat` is closed; thermo_type (text): the kind of :ref:`thermostat` to be used, currently NONE, ANDERSEN, LANGEVIN, or NOSEHOOVER; thermo_temp (physical): the :ref:`thermostat` temperature in physical units. Each :ref:`thermostat` may also be tuned using the options, tgrad (physical)(Default = 0 K): Discrete variation of temperature T per MD step. group (integer)(Default = 0): Index of the group of atoms (as defined in POSITION_ABS ) to which the :ref:`thermostat` is coupled. If no group of atoms is specfied, the :ref:`thermostat` is applied to the full system (i.e. group index 0). tau (Physical)(Default = 10.0* :ref:`md-delta-t` ): Characteristic time scale of the THERMOSTAT. Depending on the type of THERMOSTAT, it may relate either to the average collision frequency or the :ref:`thermostat` fluctuation frequency or to the coupling with the heat bath; damp (real)(Default = 0.2): Langevin damping parameter. mix (real)(Default = 1.0): Collision amplitude of the Andersen THERMOSTAT. nchain (integer)(Default = 0): Number of THERMOSTATs in the Nose-Hoover chain. nstep (integer)(Default = 20): Number of substeps used to integrate the equation of motion of the Nose-Hoover coordinates. update (logical)(Default = False): Impose to update the effective masses of the Nose-Hoover coordinates when the temperature is modified.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK THERMOSTAT
      time_start1 time_stop1 thermo_type1 thermo_temp1
      option1 = value1 (optional)
      time_start2 time_stop2 thermo_type2 thermo_temp2
      option2 = value2 (optional)
      %ENDBLOCK THERMOSTAT

   :Example:

   .. code::

      Let us set an NVT calculation at 300K with Langevin THERMOSTAT for
      the equilibration (3000 steps) and Nose-Hoover THERMOSTAT for the
      thermodynamical sampling (10000 steps).
      The input parameters could look like.
      
      
      
      %BLOCK THERMOSTAT
      
      1 3000 langevin 300.0 K
      
         damp = 0.2
      
      3001 13000 nosehoover 300.0 K
      
         nchain = 4
      
         tau = 800 aut
      
      %ENDBLOCK THERMOSTAT

.. _thole-polarisabilities:

THOLE_POLARISABILITIES
----------------------

:Type: Block
:Default: None
:Unit: None
:Level: Intermediate
:Group: QMMM
:Search: :searchlink:`THOLE_POLARISABILITIES`

Thole polarisabilities of all QM atoms

.. _threads-gpu:

THREADS_GPU
-----------

:Type: Integer
:Default: Unknown
:Unit: None
:Level: Expert
:Group: THREADS
:Search: :searchlink:`THREADS_GPU`

Number of threads for FFTs on the GPU

.. _threads-max:

THREADS_MAX
-----------

:Type: Integer
:Default: Unknown
:Unit: None
:Level: Expert
:Group: THREADS
:Search: :searchlink:`THREADS_MAX`

Number of threads in outer loops

Number of OpenMP threads in outer loops.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      THREADS_MAX [INTEGER]

   :Example:

   .. code::

      THREADS_MAX 4

.. _threads-num-fftboxes:

THREADS_NUM_FFTBOXES
--------------------

:Type: Integer
:Default: Unknown
:Unit: None
:Level: Expert
:Group: THREADS
:Search: :searchlink:`THREADS_NUM_FFTBOXES`

Number of threads to use in OpenMP-parallel FFTs

Number of threads to use in OpenMP-parallel FFTs.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      THREADS_NUM_FFTBOXES [INTEGER]

   :Example:

   .. code::

      THREADS_NUM_FFTBOXES 4

.. _threads-num-mkl:

THREADS_NUM_MKL
---------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Expert
:Group: THREADS
:Search: :searchlink:`THREADS_NUM_MKL`

Number of threads to use in OpenMP-parallel MKL operations

The number of threads to use in MKL routines (matrix-matrix multiplications, inverses, diagonalisations etc.). ONETEP must be compiled against Intel's MKL library with the compile flag -DMKLOMP. Currently only used in the calculation of electron transmission.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      THREADS_NUM_MKL [INTEGER]

   :Example:

   .. code::

      THREADS_NUM_MKL 2

.. _threads-per-cellfft:

THREADS_PER_CELLFFT
-------------------

:Type: Integer
:Default: Unknown
:Unit: None
:Level: Expert
:Group: THREADS
:Search: :searchlink:`THREADS_PER_CELLFFT`

Number of threads to use in OpenMP-parallel FFTs on simulation cell

Number of threads to use in OpenMP-parallel FFTs on simulation cell.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      THREADS_PER_CELLFFT [INTEGER]

   :Example:

   .. code::

      THREADS_PER_CELLFFT 4

.. _threads-per-fftbox:

THREADS_PER_FFTBOX
------------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Expert
:Group: THREADS
:Search: :searchlink:`THREADS_PER_FFTBOX`

Number of nested threads used for FFT box operations.

Number of nested threads used for FFT box operations. This kind of threading requires an OpenMP-enabled version of the FFTW library.  Otherwise, this functionality should be disabled via the FFTW3_NO_OMP compilation flag.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      THREADS_PER_FFTBOX [INTEGER]

   :Example:

   .. code::

      THREADS_PER_FFTBOX 2

.. _threads-precond:

THREADS_PRECOND
---------------

:Type: Integer
:Default: Unknown
:Unit: None
:Level: Expert
:Group: THREADS
:Search: :searchlink:`THREADS_PRECOND`

Number of threads to use in preconditioning

.. _timings-level:

TIMINGS_LEVEL
-------------

:Type: Integer
:Default: 1
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`TIMINGS_LEVEL`

Level of timings output: 0(none) 1(procs summary), 2(proc details)

Specifies the amount of detail in the timing information collected:0 - total time only reported1 - timings for routines averaged across all processors2 - timings for routines on all processors individually

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      TIMINGS_LEVEL [Integer]

   :Example:

   .. code::

      TIMINGS_LEVEL 0

.. _timings-order:

TIMINGS_ORDER
-------------

:Type: String
:Default: 'TIME'
:Unit: None
:Level: Intermediate
:Group: None
:Search: :searchlink:`TIMINGS_ORDER`

Sorting order of timings

.. _trimmed-boxes-output-detail:

TRIMMED_BOXES_OUTPUT_DETAIL
---------------------------

:Type: String
:Default: 'DEFAULT'
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`TRIMMED_BOXES_OUTPUT_DETAIL`

Output detail for trimmed boxes.

.. _trimmed-boxes-threshold:

TRIMMED_BOXES_THRESHOLD
-----------------------

:Type: Double-Precision
:Default: Unknown
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`TRIMMED_BOXES_THRESHOLD`

Threshold for trimming in fast density and locpot ints.

.. _tssearch-cg-max-iter:

TSSEARCH_CG_MAX_ITER
--------------------

:Type: Integer
:Default: 20
:Unit: None
:Level: Expert
:Group: TS
:Search: :searchlink:`TSSEARCH_CG_MAX_ITER`

Specifies maximum number of CG steps

Specifies the maximum number of conjugate gradients iterations for the transition state search.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      TSSEARCH_CG_MAX_ITER [Integer]

   :Example:

   .. code::

      TSSEARCH_CG_MAX_ITER 30

.. _tssearch-disp-tol:

TSSEARCH_DISP_TOL
-----------------

:Type: Physical
:Default: 0.01
:Unit: bohr
:Level: Intermediate
:Group: TS
:Search: :searchlink:`TSSEARCH_DISP_TOL`

Displacement tolerance for TS search

Specifies atomic displacement tolerance used as one of the criteria for convergence of a transition state search. The positions of all atoms must change by less than this tolerance to satisfy this criterion.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      TSSEARCH_DISP_TOL [Value] [Unit]

   :Example:

   .. code::

      TSSEARCH_DISP_TOL 1.0e-3 nm

.. _tssearch-energy-tol:

TSSEARCH_ENERGY_TOL
-------------------

:Type: Physical
:Default: 1e-05
:Unit: hartree
:Level: Intermediate
:Group: TS
:Search: :searchlink:`TSSEARCH_ENERGY_TOL`

Energy tolerance for TS search

Specifies the tolerance for enthalpy per atom over one NEB step for convergence.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      TSSEARCH_ENERGY_TOL [Value] [Unit]

   :Example:

   .. code::

      TSSEARCH_ENERGY_TOL 0.2 meV

.. _tssearch-force-tol:

TSSEARCH_FORCE_TOL
------------------

:Type: Physical
:Default: 0.005
:Unit: ha/bohr
:Level: Intermediate
:Group: TS
:Search: :searchlink:`TSSEARCH_FORCE_TOL`

Force tolerance for TS search

Specifies the tolerance for maximum atomic force as a criterion for transition state search convergence. Note that units involving a forward slash (/) must be quoted as in the example below.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      TSSEARCH_FORCE_TOL [Value] [Unit]

   :Example:

   .. code::

      TSSEARCH_FORCE_TOL 0.05 'ev/ang'

.. _tssearch-lstqst-protocol:

TSSEARCH_LSTQST_PROTOCOL
------------------------

:Type: String
:Default: 'LSTMAXIMUM'
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`TSSEARCH_LSTQST_PROTOCOL`

Specifies LSTQST protocol

Specifies the protocol for transition state search with the LSTQST method, currently one of LSTMAXIMUM , HALGREN-LIPSCOMB , LST/OPTIMIZATION , COMPLETELSTQST or QST/OPTIMIZATION .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      TSSEARCH_LSTQST_PROTOCOL [Text]

   :Example:

   .. code::

      TSSEARCH_LSTQST_PROTOCOL LST/OPTIMIZATION

.. _tssearch-method:

TSSEARCH_METHOD
---------------

:Type: String
:Default: 'LSTQST'
:Unit: None
:Level: Intermediate
:Group: TS
:Search: :searchlink:`TSSEARCH_METHOD`

Specifies method to be used for TS search (e.g., LSTQST

Specifies the method for transition state search, LSTQST or NEB . If NEB is used, :ref:`num-images` should also be specified to set the number of NEB beads.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      TSSEARCH_METHOD [Text]

   :Example:

   .. code::

      TSSEARCH_METHOD NEB

.. _tssearch-qst-max-iter:

TSSEARCH_QST_MAX_ITER
---------------------

:Type: Integer
:Default: 5
:Unit: None
:Level: Expert
:Group: TS
:Search: :searchlink:`TSSEARCH_QST_MAX_ITER`

Specifies maximum number of QST steps

Specifies the maximum number of QST iterations for the transition state search.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      TSSEARCH_QST_MAX_ITER [Integer]

   :Example:

   .. code::

      TSSEARCH_QST_MAX_ITER 10

.. _turn-off-ewald:

TURN_OFF_EWALD
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`TURN_OFF_EWALD`

Omit Ewald term from energies and forces

Elides the calculation of Ewald energy and force terms in the calculation. This is potentially useful in properties calculations, where the Ewald terms are known already from the singlepoint calculation and you don't want to spend time to recalculate them again.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      TURN_OFF_EWALD [Boolean]

   :Example:

   .. code::

      TURN_OFF_EWALD T

.. _turn-off-hartree:

TURN_OFF_HARTREE
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`TURN_OFF_HARTREE`

Omit Hartree terms

.. _upf-key-debug:

UPF_KEY_DEBUG
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: UPF_HANDLER
:Search: :searchlink:`UPF_KEY_DEBUG`

Print info used to search for data in UPF PP file.

.. _upf-print-values:

UPF_PRINT_VALUES
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: UPF_HANDLER
:Search: :searchlink:`UPF_PRINT_VALUES`

Print values read from a UPF PP file.

.. _use-cmplx-ngwfs:

USE_CMPLX_NGWFS
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: GENERAL
:Search: :searchlink:`USE_CMPLX_NGWFS`

specify to use complex valued NGWFs

.. _use-core-ke-density:

USE_CORE_KE_DENSITY
-------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`USE_CORE_KE_DENSITY`

Are pseudopotentials including KE core density present?

.. _use-emft:

USE_EMFT
--------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`USE_EMFT`

Do an embedding mean field theory calculation

.. _use-emft-follow:

USE_EMFT_FOLLOW
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`USE_EMFT_FOLLOW`

Do an EMFT calculation after a regular NGWF optimisation

.. _use-emft-lnv-only:

USE_EMFT_LNV_ONLY
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`USE_EMFT_LNV_ONLY`

Do an LNV only EMFT calculation

.. _use-space-filling-curve:

USE_SPACE_FILLING_CURVE
-----------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`USE_SPACE_FILLING_CURVE`

Re-arrange atoms according to space-filling curve

Use a Hilbert space-filling curve to distribute the atoms among processors in a parallel calculation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      USE_SPACE_FILLING_CURVE [Logical]

   :Example:

   .. code::

      USE_SPACE_FILLING_CURVE F

.. _use-sph-harm-rot:

USE_SPH_HARM_ROT
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: SPH_HARM_ROT
:Search: :searchlink:`USE_SPH_HARM_ROT`

Initialize spherical harmonic rotation module. Not needed in normal use, as this should be done automatically.

When True, manually activate the sph_harm_rotation (spherical harmonic rotation) module (used to evaluate the metric matrix in the 2Dn-1Da scheme for spherical wave metric matrix evaluation). In normal operation this is not necessary, since the module will be activated if it is detected that spherical harmonic rotation is required. Setting this to False has no effect, since the option will be overridden if ONETEP detects that the module is needed, anyway.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      USE_SPH_HARM_ROT [Boolean]

   :Example:

   .. code::

      USE_SPH_HARM_ROT T

.. _use-symmetry:

USE_SYMMETRY
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`USE_SYMMETRY`

Turn on symmetry or not

.. _use-time-reversal:

USE_TIME_REVERSAL
-----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`USE_TIME_REVERSAL`

Use TRS to reduce k-points or not

.. _vdw-bc:

VDW_BC
------

:Type: String
:Default: ''
:Unit: None
:Level: Expert
:Group: VDW
:Search: :searchlink:`VDW_BC`

3 character string defining BCs for van der Waals interactions along each lattice vector. 'O' for open, 'P' for periodic.

.. _vdw-dcoeff:

VDW_DCOEFF
----------

:Type: Double-Precision
:Default: -1.0
:Unit: None
:Level: Expert
:Group: VDW
:Search: :searchlink:`VDW_DCOEFF`

Replacement VDW damping coefficient

Overrides the damping constant associated with a damping function.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      VDW_DCOEFF [Real]

   :Example:

   .. code::

      VDW_DCOEFF 11

.. _vdw-params:

VDW_PARAMS
----------

:Type: Block
:Default: None
:Unit: None
:Level: Expert
:Group: VDW
:Search: :searchlink:`VDW_PARAMS`

Replacement VDW parameters (atomic number, c6coeff, radzero, neff)

This option allows the user to specify parameters for elements and functionals for which values are not given. The atom-dependent variables C6_i (used to calculate C6_ij),R0_i (related to the atomic vdW radius of an atom i), and n_eff (used in the calculation of C6_ij for all damping functions excluding the D2 correction of Grimme) are modified using the :ref:`vdw-params` block. This override block applies the parameter changes to atoms by their atomic number (nzatom).

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      %BLOCK VDW_PARAMS
       nzatom_1 c6coeff_1 radzero_1 neff_1
       nzatom_2 c6coeff_2 radzero_2 neff_2
       ......
      %ENDBLOCK VDW_PARAMS

   :Example:

   .. code::

      For example, to override the disp ersion parameters asso ciated with nitrogen:
      
      
      
      %BLOCK VDW_PARAMS
      
      ! nzatom, c6coeff, radzero, neff
      
      7 21.1200 2.6200 2.51
      
      %ENDBLOCK VDW_PARAMS

.. _vdw-radial-cutoff:

VDW_RADIAL_CUTOFF
-----------------

:Type: Physical
:Default: 100.0
:Unit: bohr
:Level: Intermediate
:Group: VDW
:Search: :searchlink:`VDW_RADIAL_CUTOFF`

Radial cutoff for van der Waals interactions

.. _velocities:

VELOCITIES
----------

:Type: Block
:Default: None
:Unit: None
:Level: Basic
:Group: None
:Search: :searchlink:`VELOCITIES`

Initial velocities for each atom

.. _write-converged-dk-ngwfs:

WRITE_CONVERGED_DK_NGWFS
------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: IO
:Search: :searchlink:`WRITE_CONVERGED_DK_NGWFS`

Only write Density Kernel and NGWFs upon convergence of NGWF optimisation

Specifies that the density kernel and NGWF output files should only be written at the end of a converged calculation, rather than after every iteration.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      WRITE_CONVERGED_DKNGWFS [Logical]

   :Example:

   .. code::

      write_converged_dkngwfs T

.. _write-density-plot:

WRITE_DENSITY_PLOT
------------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_DENSITY_PLOT`

Write the charge density in plotting format

Specifies that the charge density, electrostatic potential and spin density (if appropriate) be written out for plottingif properties are requested.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      WRITE_DENSITY_PLOT [Logical]

   :Example:

   .. code::

      WRITE_DENSITY_PLOT F

.. _write-denskern:

WRITE_DENSKERN
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_DENSKERN`

Write density kernel restart information

Write the density kernel to disk. If the input filename is rootname.dat then the density kernel filename is rootname.denskern .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      WRITE_DENSKERN [Logical]

   :Example:

   .. code::

      WRITE_DENSKERN F

.. _write-forces:

WRITE_FORCES
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_FORCES`

Write ionic forces

Include the forces in the output of a single point energy calculation.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      WRITE_FORCES [Logical]

   :Example:

   .. code::

      WRITE_FORCES T

.. _write-hamiltonian:

WRITE_HAMILTONIAN
-----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: IO
:Search: :searchlink:`WRITE_HAMILTONIAN`

Save current Hamiltonian matrix in a file

Write the Hamiltonian matrix on a .ham file. Currently, only used in :ref:`edft` calculations. Set to true if a calculation is intended to be restarted at some point in the future.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      WRITE_HAMILTONIAN [Logical]

   :Example:

   .. code::

      WRITE_HAMILTONIAN T

.. _write-initial-radial-ngwfs:

WRITE_INITIAL_RADIAL_NGWFS
--------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: None
:Search: :searchlink:`WRITE_INITIAL_RADIAL_NGWFS`

Controls output of radial NGWF plots from atomsolver

Whether to write a file for each species that contains the initial NGWFs as output from the atomsolver. Format is column 1 is position (in bohr), columns 2-N_shells+1 are the PAO wavefunctions for each of the N_shells, that will be used to initialise the NGWFs

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      WRITE_INITIAL_RADIAL_NGWFS [Logical]

   :Example:

   .. code::

      write_initial_ngwfs T

.. _write-max-l:

WRITE_MAX_L
-----------

:Type: Integer
:Default: 3
:Unit: None
:Level: Intermediate
:Group: IO
:Search: :searchlink:`WRITE_MAX_L`

Maximum angular momentum number when writing in SW representation

Specifies the maximum angular momentum of the spherical waves (l number) when writing to file.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      WRITE_MAX_L [Integer]

   :Example:

   .. code::

      WRITE_MAX_L 2

.. _write-nbo:

WRITE_NBO
---------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: NBO
:Search: :searchlink:`WRITE_NBO`

Performs Natural Population Analysis and writes a FILE.47 input for GENNBO

Enables Natural Population Analysis (NPA) and writing of gennbo input file seedname_nao_nbo.47

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      WRITE_NBO [Logical]

   :Example:

   .. code::

      WRITE_NBO T

.. _write-ngwf-grad-plot:

WRITE_NGWF_GRAD_PLOT
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_NGWF_GRAD_PLOT`

Write NGWF Gradients in plotting format

.. _write-ngwf-grad-radial:

WRITE_NGWF_GRAD_RADIAL
----------------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_NGWF_GRAD_RADIAL`

Write NGWFs gradients radial distributions

.. _write-ngwf-plot:

WRITE_NGWF_PLOT
---------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_NGWF_PLOT`

Write NGWFs in plotting format

Write out NGWFs for species listed in the :ref:`species-ngwf-plot` to disk for plotting during a single point energy calculation, in the cube and/or .grd formats as requested.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      WRITE_NGWF_PLOT [Logical]

   :Example:

   .. code::

      WRITE_NGWF_PLOT T

.. _write-ngwf-plot-every-it:

WRITE_NGWF_PLOT_EVERY_IT
------------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_NGWF_PLOT_EVERY_IT`

Write NGWFs in plotting format at every iteration

.. _write-ngwf-radial:

WRITE_NGWF_RADIAL
-----------------

:Type: Integer
:Default: 0
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_NGWF_RADIAL`

Write NGWFs radial distributions

.. _write-overlap:

WRITE_OVERLAP
-------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Expert
:Group: IO
:Search: :searchlink:`WRITE_OVERLAP`

Save current Overlap matrix in a file

.. _write-params:

WRITE_PARAMS
------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_PARAMS`

Output runtime parameters at startup

.. _write-polarisation-plot:

WRITE_POLARISATION_PLOT
-----------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Intermediate
:Group: IO
:Search: :searchlink:`WRITE_POLARISATION_PLOT`

Write the polarisation density in plotting format

.. _write-positions:

WRITE_POSITIONS
---------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_POSITIONS`

Write ionic positions each geometry or MD step

.. _write-radial-smear:

WRITE_RADIAL_SMEAR
------------------

:Type: Physical
:Default: 0.01
:Unit: bohr
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_RADIAL_SMEAR`

Define the gaussian smearing used for writing radial distributions

.. _write-radial-step:

WRITE_RADIAL_STEP
-----------------

:Type: Physical
:Default: 0.005
:Unit: bohr
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_RADIAL_STEP`

Define the grid step used for writing radial distributions

.. _write-sw-ngwfs:

WRITE_SW_NGWFS
--------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_SW_NGWFS`

Write NGWFs restart information in spherical waves representation

Write the NGWFs to disk in spherical waves decomposition. If the input filename is rootname.dat then the NGWFs filename is rootname.sw_ngwfs .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      WRITE_SW_NGWFS [Logical]

   :Example:

   .. code::

      WRITE_SW_NGWFS T

.. _write-tightbox-ngwfs:

WRITE_TIGHTBOX_NGWFS
--------------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_TIGHTBOX_NGWFS`

Write in universal tightbox NGWFs restart information

Write the NGWFs to disk. If the input filename is rootname.dat then the NGWFs filename is rootname.tightbox_ngwfs .

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      WRITE_TIGHTBOX_NGWFS [Logical]

   :Example:

   .. code::

      WRITE_TIGHTBOX_NGWFS F

.. _write-velocities:

WRITE_VELOCITIES
----------------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_VELOCITIES`

Write ionic velocities each MD step

.. _write-xyz:

WRITE_XYZ
---------

:Type: Boolean
:Default: FALSE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_XYZ`

Output coordinates in .xyz file

Write the atom coordinates to disk as an .xyz file

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      WRITE_XYZ [Logical]

   :Example:

   .. code::

      WRITE_XYZ T

.. _write-xyz-lattice:

WRITE_XYZ_LATTICE
-----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Basic
:Group: IO
:Search: :searchlink:`WRITE_XYZ_LATTICE`

If .xyz files are produce, output cell lattice in comment

.. _xc-functional:

XC_FUNCTIONAL
-------------

:Type: String
:Default: 'LDA'
:Unit: None
:Level: Basic
:Group: XC
:Search: :searchlink:`XC_FUNCTIONAL`

Exchange-correlation functional

Specifies the exchange-correlation functional to use, currently one of: LDA - default local (spin) density approximation, currently CAPZ GGA - default generalized gradient approximation, currently RPBE CAPZ - Perdew-Zunger parameterization [Phys. Rev. B 23, 5048 (1981)] of the Ceperley-Alder Monte Carlo data [Phys. Rev. Lett. 45, 566 (1980)] and Gell-Mann-Brueckner expansion [Phys. Rev. 106, 364 (1957)] PW92 - Perdew and Wang 1992 LDA [Phys. Rev. B 45, 13244 (1992)] VWN - Vosko, Wilk and Nusair parameterization [Phys. Rev. B 22, 3812 (1980)] of the LDA PW91 - Perdew and Wang GGA [Phys. Rev. B 45, 13244 (1992)] PBE - Perdew, Burke and Ernzerhof GGA [Phys. Rev. Lett. 77, 3865 (1996) and Erratum] REVPBE - revised PBE by Zhang and Yang [Phys. Rev. Lett. 80, 890 (1998)] RPBE - revised PBE by Hammer, Hansen and Norskov [Phys. Rev. B 59, 7413 (1999)] PBESOL - revised PBE for solids by Perdew et al. [Phys. Rev. Lett. 100, 136406 (2008)] BLYP -Becke 88 + LYP (Lee, Yang, Parr) GGA [Phys. Rev. A 38, 3098 (1988); Phys. Rev. B 37, 785 (1988)] XLYP - Xu and Goddard GGA [PNAS 101, 2673 (2004)] OPTB88 - X (OPTB88), C (LDA), vdW (vdW-DF 1) - J. Klimes et al. [J. Phys. Cond. Mat. 22 (2010)] OPTPBE - X (OPTPBE), C (LDA), vdW (vdW-DF 1) - J. Klimes et al. [J. Phys. Cond. Mat. 22 (2010)] VDWDF - X (revPBE), C (LDA), vdW (vdW-DF 1) - M. Dion et al. [Phys. Rev. Lett. (2004)] VDWDF2 - X (rPW86), C (LDA), vdW (vdW-DF 2) - K. Lee et al. [Phys. Rev. B (2010)] VV10 - X (rPW86), C (PBE), vdW (rVV10) - O. A. Vydrov et al. [J. Chem. Phys. (2010)]; R. Sabatini et al. [Phys. Rev. B (2013)] AVV10S - X (AM05), C (AM05), vdW (rVV10-sol) - T. Bjorkman [Phys. Rev. B (2012)]

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      XC_FUNCTIONAL [Text]

   :Example:

   .. code::

      XC_FUNCTIONAL PBE

.. _xc-initial-functional:

XC_INITIAL_FUNCTIONAL
---------------------

:Type: String
:Default: 'PBE'
:Unit: None
:Level: Expert
:Group: XC
:Search: :searchlink:`XC_INITIAL_FUNCTIONAL`

Use an alternative XC functional when calculating XC energy for initial guess. Only available when :ref:`xc-functional` is a meta-GGA. Default: 'PBE'. To omit XC when computing initial guess set to 'NONE'.

.. _xc-mintau:

XC_MINTAU
---------

:Type: Double-Precision
:Default: None
:Unit: None
:Level: Expert
:Group: XC
:Search: :searchlink:`XC_MINTAU`

The minimum threshold for tau (the kinetic energy density): this is typically used to determine the cutoff where expressions containing 1/tau in the XC energy and potential functions are set to zero, to avoid numerical issues

.. _zero-total-force:

ZERO_TOTAL_FORCE
----------------

:Type: Boolean
:Default: TRUE
:Unit: None
:Level: Expert
:Group: GENERAL
:Search: :searchlink:`ZERO_TOTAL_FORCE`

Subtract avg force to ensure Newton's 3rd law holds

Forces the total ionic force to be zero by subtracting the average ionic force from all ionic forces.

.. note::
   :collapsible: closed

   :Syntax:

   .. code::

      ZERO_TOTAL_FORCE [Logical]

   :Example:

   .. code::

      ZERO_TOTAL_FORCE F