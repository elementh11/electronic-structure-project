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
        klist = np.empty([0,3])

        # TODO: adjust the weights at the boundaries of the Brillouin zone
        weightlist = np.ones((self.nk1 * self.nk2 * self.nk3, 1)) / (self.nk1 * self.nk2 * self.nk3)

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


