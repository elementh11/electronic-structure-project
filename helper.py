import numpy as np


class Kpoints:
    """
    A class used to generate and save uniform grids of k-points

    ...

    Attributes
    ----------
    nk1 : int
        number of k-points along x-direction
    nk2 : int
        number of k-points along y-direction
    nk3 : int
        number of k-points along z-direction
    name : str
        name of file to save the k-mesh (default "kpts.csv")

    Methods
    -------
    gen_kpts()
        Returns the array of k-points
    save_kpts(listname)
        Saves the `listname` array of k-points to file `name`
    """ 

    def __init__(self, nk1, nk2, nk3, name="kpts.csv"):
        self.nk1 = nk1
        self.nk2 = nk2
        self.nk3 = nk3
        self.name = name
        
    def gen_kpts(self):
        kx = np.linspace(0, 1, self.nk1)
        ky = np.linspace(0, 1, self.nk2)
        kz = np.linspace(0, 1, self.nk3)
        weightlist = np.ones((self.nk1 * self.nk2 * self.nk3, 1)) / (self.nk1 * self.nk2 * self.nk3)
        klist = np.empty([0,3])

        for k1 in kx:
            k1val = np.array([k1, 0, 0]) if self.nk1 > 1 else np.array([0, 0, 0])
            for k2 in ky:
                k2val = np.array([0, k2, 0]) if self.nk2 > 1 else np.array([0, 0, 0])
                for k3 in kz:
                    k3val = np.array([0, 0, k3]) if self.nk3 > 1 else np.array([0, 0, 0])
                    kval = k1val + k2val + k3val
                    klist = np.vstack((klist, kval))
        list = np.hstack((klist, weightlist))

        return list
    
    def save_kpts(self,listname):
        np.savetxt(self.name, listname, fmt="%10.6f", delimiter=",")


def read_Wannier_data(seedname):


    """
    A function used to post-process and save the output of the Wannier90 code

    ...

    Attributes
    ----------
    seedname : string
        location of the Wannier90 output file "seedname_hr.dat"

    Returns
    -------
    "degeneracy.npy"
        Returns the array of degeneracies
    "matrix.npy"
        Returns the array of matrices
    "displacement.npy"
        Returns the array of displacements
    """ 
    
    
    # read data from 'seedname_hr.dat'
    with open(seedname) as h:
        ham_data = h.readlines()
    ham_data = [x.strip() for x in ham_data]
    num_wann = int(ham_data[1])
    nrpts = int(ham_data[2])
    
    # save degeneracy information
    nrows_deg = int(np.ceil(nrpts/15))
    degen = []
    for row_idx in range(3, nrows_deg + 3):
        row_data = list(map(int, ''.join(list(ham_data[row_idx])).split()))
        degen.extend(row_data)
    degen = np.asarray(degen)
    print(degen)
    np.save('degeneracy',degen)
    
    # save matrices and displacements
    matrices = []
    displ = []

    for point in range(1, nrpts+1):
        hamtemp = np.zeros((num_wann, num_wann), dtype = complex)
        for _ in range(1, num_wann**2 + 1):
            row_idx += 1
            row_data = list(map(float, ''.join(list(ham_data[row_idx])).split()))
            row, col = map(int, row_data[3:5])
            re_ham, im_ham = row_data[5:7]
            hamtemp[row - 1][col - 1] = re_ham + 1j * im_ham
        matrices.append(hamtemp)

        disp_data = row_data[:3]
        displ.append(disp_data)

    matrices = np.asarray(matrices)
    displ = np.asarray(displ)
    np.save('matrix', matrices)
    np.save('displacement',displ)    