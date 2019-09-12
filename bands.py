""" Bandstructure calculator 

This script allows the user to do bandstructure calculations

This script requires as input the lattice parameters information

    * alat: lattice constant
    * a1, a2, a3: lattice vectors (in terms of alat)

Also it requires prior Wannier90 post-processing from "helper.py" library
and the k-path from "k_path.npy"

It saves the array of bands to "bands.npy"
"""

import numpy as np

alat = 12.0616
a1 = np.array([   1.000000,   0.000000,   0.000000 ]) * alat
a2 = np.array([   0.000000,   0.540617,   0.000000 ]) * alat
a3 = np.array([   0.000000,   0.000000,   3.158529 ]) * alat

####################################################
#### no need to change anything below this line ####
####################################################

vol = np.absolute(np.dot(np.cross(a1,a2),a3));
b1 = 2 * np.pi * np.cross(a2,a3) / vol;
b2 = 2 * np.pi * np.cross(a3,a1) / vol;
b3 = 2 * np.pi * np.cross(a1,a2) / vol;

degen = np.load('degeneracy.npy')
disp = np.load('displacement.npy')
matrices = np.load('matrix.npy')
kpoints = np.load('k_path.npy')

nrpts, dim, dim = np.shape(matrices)
eigen = []

for kc in range(np.shape(kpoints)[1]):
    k1, k2, k3 = kpoints[:, kc]
    k = k1*b1 + k2*b2 + k3*b3
    ham = np.zeros((dim, dim), dtype = complex)
    
    for count in range(nrpts):
        d1, d2, d3 = disp[count, :]
        r = d1*a1 + d2*a2 + d3*a3
        matrix = matrices[count, :, :]
        ham += matrix * np.exp(1j * np.dot(k, r)) * degen[count]
        
    ham = (ham + ham.conj().T) / 2
    ek = np.real(np.linalg.eigvals(ham))
    eigen.append(ek)

np.save('bands', eigen)