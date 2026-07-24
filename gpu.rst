=================
ONETEP using GPUs
=================

:Author: Jacek Dziedzic, University of Southampton
:Author: Gianluca Seaford, University of Warwick

Introduction
============

Starting from v7.3, an OpenACC-based GPU port of ONETEP is available. Starting
from v8.1, the implementation is sufficiently mature to be enjoyed by users,
even if development continues.

At this moment, the following key algorithms have been GPU ported:
 - fast density (see :ref:`user_fast_density`),
 - fast local potential integrals (see :ref:`user_fast_locpot_int`),
 - fast NGWF gradient (see :ref:`user_fast_ngwf_gradient`),
 - Hartree-Fock exchange (not completely),
 - sparse matrix products (work is very much in progress).
 - dense linear algebra (via ELSI interface, optimisation is in progress).

Note that the usual ("slow") calculation of density, local potential integrals,
and NGWF gradient are not GPU-capable. You will not get any improvement from
using GPUs unless you switch to, respectively, fast density, fast local
potential integrals, and fast NGWF gradient, except if you use
use Hartree-Fock exchange, as this does not require any extra keywords.
The improvement in sparse matrix products is currently modest and only if you
have many (hundreds) of atoms per MPI rank. This does not require any extra
keywords, either. Similarly, the improvement to the dense linear algebra routines
via the ELSI interface is system dependent, and typically requires large numbers 
of atoms per GPU.

Implementation
==============

ONETEP uses OpenACC for offloading compute-intensive parts of the calculation
to GPUs. You will need an OpenACC-capable Fortran compiler to be able to use
that. At the time this document is written (2026.06), there are three options:

1. nvfortran (versions 24.x, 25.x, or 26.x are recommended),
2. Cray Fortran,
3. gfortran (suitably compiled).

Only option 1. has been tested thoroughly. Cray Fortran can be used on Archer2,
but you are likely to run into problems due to lack of testing of this configuration.
Option 3. has not been tested at all, and obtaining an OpenACC-capable gfortran
compiler is in itself a daunting task. We recommend, and support, only option 1.

CUDA Fortran is not required for ONETEP, although CUDA libraries (cuFFT, cuBLAS) are.
These will be provided with your nvfortran (``nvhpc``) installation.

Compilation and linking
=======================

A number of flags must be passed to the compiler to enable GPU support. We highly
recommend using one of the config files provided in ``config`` as a template.

Good choices are:
 - ``conf.iridisx.nvfortran.omp.scalapack.acc``,
 - ``conf.jureca.nvfortran.omp.scalapack.acc``,
 - ``conf.isambardai.nvfortran.acc``,
 - ``conf.RH9.nvfortran.acc``.

The first two use MKL for FFTW, BLAS, LAPACK and ScaLAPACK. The third one uses
NVPL. The last one uses system-wide FFTW, and the BLAS, LAPACK and ScaLAPACK
shipped with ``nvhpc``.

If you prefer to build your own compilation line from scratch (not recommended),
here are some required flags:

 - ``-acc`` to enable OpenACC in nvfortran,
 - ``-cudalibs`` to link against CUDA libraries,
 - ``-lcufft -lcublas`` to link against cuFFT and cuBLAS,
 - ``-DGPU_ACC`` to tell ONETEP to use GPU acceleration.

The following is highly recommended:

 - ``-DGPU_FFT_CUFFT_ACC`` to use GPU-accelerated FFTs via cuFFT.

The following is recommended if you have an A100 card:

 - ``-DGPU_A100`` to use an alternative approach in HFx on A100 cards.

The following is recommended if you have much more GPU power than CPU power.
For instance, with 4 H100 cards on a 64-core node you would definitely want that,
but with 4 A100 cards on a 128-core node you wouldn't. Differences will not be
substantial, so do not worry.

 - ``-DGPU_DGEMM`` to use GPUs for sparse matrix products.

For calculations involving dense linear algebra, theere may be an advantage to using
the ELPA routines via the ELSI interface. Please note that these routines require 
both ELPA and ELSI to be compiled with an appropriate compiler, ELSI to be linked to 
ELPA at compile time (guidance can be found in the ELSI documentation), and ONETEP
needs to be linked to both libraries and passed the ``-DELSI`` flag at compile time. 
An example of configuring ONETEP with ELSI and ELPA can be found in 
``config/conf.isambardai_elsi.nvfortran.acc``.

 - ``-DGPU_ELPA`` to use ELPA GPU routines via the ELSI interface.

All the options are described in detail later in this document.

Once again, it's much easier to start off with one of the provided config files.
Take care to adjust the paths (``MKLMODPATH``, ``LIBCUFFTPATH``, ``LIBCUDAPATH``,
``LIBNVSHMEMPATH`` -- if present).

Running jobs
============

Easy-peasy! ``onetep_launcher`` now supports GPUs and will happily set everything
up for you. Just make sure to follow the documentation of your HPC system to
ensure you ask for GPUs in your submission script. This is typically realised
by passing ``-gres=gpu:n`` to ask for *n* GPUs on each node. Some HPC systems
(*cough*, JURECA, *cough*) instead prefer you don't this. You might also want
to ensure you get exclusive access to the nodes. This may happen automatically
or not, depending on your HPC system.

Then, pass the options ``-G -g n`` to ``onetep_launcher``, where *n* is the
number of GPUs on a node. The option ``-g n`` tells ``onetep_launcher`` that
you would like to use *n* GPUs on each node. The option ``-G`` tells it to
start MPS (multi-process service) for you. This saves you a lot of hassle --
a *single* instance of MPS needs to be started on each node, and ``onetep_launcher``
knows how to do this. It will also ensure this worked and abort if it didn't.
If, for some reason, you prefer not to use MPS, do not pass ``-G``. In typical
scenarios using MPS gives a modest (10-20%) boost to GPU performance, but
your mileage may vary. In particular, if you have a 1:1 mapping between MPI
ranks and GPUs, you might want not to use MPS. To start and stop MPS, ``onetep_launcher``
uses an auxiliary script called ``gpu_mps_control``. It's provided in the
``utils`` directory.

Starting from v7.3.68, ``onetep_launcher``'s ``resmon`` also supports GPUs.
That is, if you pass the ``-r k`` option to ``onetep_launcher`` to ask for
monitoring resources every *k* seconds, in addition to running ``top``,
``onetep_launcher`` will also run ``gpu_top`` (provided in the ``utils`` directory).
Results will go into a directory called ``resmon``. This lets you easily
monitor the utilisation of the GPU(s) and GPU memory use. GPU OOM scenarios
are difficult to debug, and this can help.

Control over GPU acceleration
=============================

The following compile-time options are recognized by the GPU port.

+--------------------------+-----------------------------------------------------------+
| Option                   | Effect                                                    |
+==========================+===========================================================+
| ``-DGPU_ACC``            | Enables OpenACC, and thus the GPU port. Required.         |
+--------------------------+-----------------------------------------------------------+
| ``-DGPU_FFT_CUFFT_ACC``  | Uses GPUs (via cuFFT, controlled via OpenACC) for Fourier |
|                          |                                                           |
|                          | interpolation and Fourier filtering in fast density and   |
|                          |                                                           |
|                          | fast local potential integrals. Does not affect the rest  |
|                          |                                                           |
|                          | of ONETEP. By moving adjacent operations to the GPU,      |
|                          |                                                           |
|                          | host to device copyin, and device to host copyout can be  |
|                          |                                                           |
|                          | avoided. Highly recommended.                              |
+--------------------------+-----------------------------------------------------------+
| ``-DGPU_FFT_CUFFT_CUDA`` | An alternative to ``-DGPU_FFT_CUFFT_ACC`` which uses a    |
|                          |                                                           |
|                          | CUDA (rather than an OpenACC) backend to cuFFT.           |
|                          |                                                           |
|                          | In some scenarios it can offer a modest advantage over    |
|                          |                                                           |
|                          | ``-DGPU_FFT_CUFFT_ACC``, but it has not been tested as    |
|                          |                                                           |
|                          | thoroughly. Requires CUDA Fortran. Starting in v8.0, this |
|                          |                                                           |
|                          | option has been _deprecated_. Use ``-DGPU_FFT_CUFFT_ACC`` |
|                          | instead.                                                  |
+--------------------------+-----------------------------------------------------------+
| ``-DGPU_DGEMM``          | Moves ``DGEMM()`` operations in ``sparse_product()`` to   |
|                          |                                                           |
|                          | cuBLAS. Reduces the default value of ``dense_threshold``  |
|                          |                                                           |
|                          | from 0.10 to 0.05.                                        |
|                          |                                                           |
|                          | This is a naive approach to porting sparse matrix         |
|                          |                                                           |
|                          | multiplications to GPUs. Anytime dense blocks that are    |
|                          |                                                           |
|                          | larger than 256x256 are multiplied, the multiplication is |
|                          |                                                           |
|                          | offloaded to the GPU(s). This is only modestly faster than|
|                          |                                                           |
|                          | CPU BLAS because of copyin and copyout. The associated    |
|                          |                                                           |
|                          | reduction in ``dense_threshold`` helps move more matmuls  |
|                          |                                                           |
|                          | to the GPU.                                               |
|                          |                                                           |
|                          | If your nodes have a lot of CPU power compared to GPU     |
|                          |                                                           |
|                          | power, this might not be advantageous at all. However,    |
|                          |                                                           |
|                          | if you have a lot of GPU power, this can speed sparse     |
|                          |                                                           |
|                          | algebra substantially.                                    |
|                          |                                                           |
|                          | For instance, with H100 cards it's likely to help.        |
|                          |                                                           |
|                          | With A100 cards it may help if you don't have very many   |
|                          |                                                           |
|                          | cores on a node (e.g. 64 or 48). On a desktop machine     |
|                          |                                                           |
|                          | with ~10 cores, it's likely to help even with a less      |
|                          |                                                           |
|                          | powerful GPU. You might want to measure with and without  |
|                          |                                                           |
|                          | this setting to see if it helps with performance on your  |
|                          |                                                           |
|                          | machine. If you find good speed-ups, you may consider     |
|                          |                                                           |
|                          | reducing ``dense_threshold`` further, even to 0.0.        |
+--------------------------+-----------------------------------------------------------+
| ``-DGPU_ELPA             | Moves dense linear algebra operations to the GPU in the   |
|                          |                                                           |
|                          | ``dense_eigensolve`` routine. Please note, this option    |
|                          |                                                           |
|                          | requires ONETEP to be compiled using the ``-DELSI`` flag  |
|                          |                                                           |
|                          | and linked to suitable ELSI and ELPA libraries.           |
|                          |                                                           |
|                          | These routines are still a work in progress, and thus may |
|                          |                                                           |
|                          | not yield any speed-up for small systems.                 |
+--------------------------+-----------------------------------------------------------+
| ``-DGPU_A100``           | Forces the GPU port of Hartree-Fock exchange to use an    |
|                          |                                                           |
|                          | alternative parallelisation scheme, suitable for A100     |
|                          |                                                           |
|                          | cards. Use this if you have A100 GPUs or if you experience|
|                          |                                                           |
|                          | deadlocks when using HFx on GPUs.                         |
|                          |                                                           |
|                          | Otherwise, you probably do not need this, although it     |
|                          |                                                           |
|                          | may be beneficial to check if it improves performance.    |
|                          |                                                           |
|                          | Ignored outside of Hartree-Fock exchange.                 |
+--------------------------+-----------------------------------------------------------+

There is also one runtime option (specified in the input file) that controls
the GPU port:

 - ``threads_gpu`` -- can be used to adjust the number of OpenMP threads in loops
   involving FFTs on the GPU(s). This defaults to ``threads_max`` (which is the
   number of OpenMP threads for most of ONETEP -- set with ``onetep_launcher``'s
   ``-t`` option or via ``OMP_NUM_THREADS``). However, if this value is large
   (e.g. 16 or more), it can put a lot of strain on GPU memory. If you find that
   you run out of GPU memory, reduce this value (e.g. to 4, or as a last resort, to 1).
   This will vastly reduce the requirement on GPU memory while the reduction in
   performance should not be dramatic -- FFTs are expensive, and even with fewer
   threads it is often possible to saturate the GPU.


Hartree-Fock exchange
=====================

This has been ported only partially. Work is in progress to complete that. You
will notice most speed-ups for relatively small systems (under 200 atoms).
For best speed-up set:

- ``hfx_memory_limit -1`` to turn off automatic memory management

- ``cache_limit_for_swops 0`` to not waste memory on caching spherical wave potentials ("SWOPs"),
  as they will be recalculated efficiently on the GPU(s),

- ``cache_limit_for_expansions n`` to instead use *n* MB of RAM per MPI rank for caching
  expansions (of NGWF pairs in spherical waves), where you should choose *n*
  to be as large as possible without exceeding your RAM allowance.

All the usual guidelines in :ref:`hfx_advanced` still apply.


Dense Linear Algebra
====================

ONETEP utilises the ELSI interface to perform dense linear algebra operations on GPUs.
Currently, only ELPA routines are supported on GPUs. This is expected to be expanded 
to incorporate additional solvers in the future. This option is enabled using the 
``-DGPU_ELSI`` and ``-DGPU_ELPA`` compile-time flags. This approach does require the
ELPA and ELSI libraries to be correctly cross compiled using an appropriate compiler
and linked to ONETEP. Although not a difficult task, it is recommended to build ELPA 
and ELSI with the relevant Fortran test suites to catch any issues early. Instructions
for building and linking the ELPA and ELSI libraries can be found in the respective
documentation. An example of modifying a configuration file to support ELPA calculations 
the ELSI interface on GH200 nodes can be found in ``config/conf.isambardai_elsi.nvfortran.acc``.

In addition, a debugging option is also available for ELPA GPU runs via the ``-DGPU_ELPA_DEBUG`` 
flag. This enables additional sanity checks aro routines and can help diagnose any issues.
This option may reduce performace, so should only be used for troubleshooting.

State of the art
================

This is work in progress. You can expect speed-ups of about 4-6x (GPU-equipped
node vs. CPU-only node) provided you have GPUs that have decent FP64 performance.
For instance, A100 and GH200 definitely work very well.
Single-node performance should be very good. With more nodes performance will be
good if your system is big enough (roughly, if you do not drop below 100 atoms
per GPU). Work is in progress to address scaling to large number of GPUs
(hundreds). Much of the time is still spent on CPUs. We are working on that too.
