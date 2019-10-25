# Electronic Structure Project

This project consists of a set of tools to post-process the DFT (from Quantum Espresso) and Wannier (from Wannier90) results, and to further perform quantum transport calculations.

Current capabilities

- Generate (fractional) Monkhorst-Pack k-point grids for Brillouin zone sampling
- Read data from the Wannier90 output file `seedname_hr.dat` and save it in `.npy` format for further use
- Perform Wannier interpolation of the Hamiltonian in the reciprocal space
- Calculate bandstructures
