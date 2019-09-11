""" k path generator 

This script allows the user to generate the k-path in the BZ for bandstructure calculations

This script requires as input the k_points dictionary containing:

    * high-symmetry points
    * the path sequence
    * total number of high-symmetry points: n_sym_pts
    * number of k-points along one symmetry line: n_line_pts
    
It saves the "k_path.npy" file to disc with the array of k-points
"""

import numpy as np

k_points = {'K': [1/3, 1/3, 0],
            'G': [0, 0, 0],
            'M': [1/2, 0, 0],
            'path': ['K', 'G', 'M', 'K'],
            'n_sym_pts': 4,
            'n_line_pts': 30
           }

####################################################
#### no need to change anything below this line ####
####################################################

nkpts = k_points['n_sym_pts']
npts = k_points['n_line_pts']
path = k_points['path']

kxlist=[]
kylist=[]
kzlist=[]
for i in range(nkpts-1):
    
    kx = np.linspace(k_points[path[i]][0], k_points[path[i+1]][0], npts)
    ky = np.linspace(k_points[path[i]][1], k_points[path[i+1]][1], npts)
    kz = np.linspace(k_points[path[i]][2], k_points[path[i+1]][2], npts)
    
    # remove points that repeat
    if i != (nkpts-2):
        kx = np.delete(kx, -1)
        ky = np.delete(ky, -1)
        kz = np.delete(kz, -1)
        
    kxlist = np.hstack((kxlist, kx))
    kylist = np.hstack((kylist, ky))
    kzlist = np.hstack((kzlist, kz))

klist = np.vstack((kxlist, kylist, kzlist))
np.save('k_path', klist)