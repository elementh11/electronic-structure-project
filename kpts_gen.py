import numpy as np


def gen_kpts(nk1, nk2, nk3):
    kx = np.linspace(0, 1, nk1)
    ky = np.linspace(0, 1, nk2)
    kz = np.linspace(0, 1, nk3)
    weightlist = np.ones((nk1 * nk2 * nk3, 1)) / (nk1 * nk2 * nk3)
    klist = np.empty([0,3])

    for k1 in kx:
        k1val = np.array([k1, 0, 0]) if nk1 > 1 else np.array([0, 0, 0])
        for k2 in ky:
            k2val = np.array([0, k2, 0]) if nk2 > 1 else np.array([0, 0, 0])
            for k3 in kz:
                k3val = np.array([0, 0, k3]) if nk3 > 1 else np.array([0, 0, 0])
                kval = k1val + k2val + k3val
                print(kval)
                klist = np.vstack((klist, kval))
    
    list = np.hstack((klist, weightlist))

    return list


my_kpts = gen_kpts(5, 5, 1)


np.savetxt("kptBZ.csv", my_kpts, fmt="%10.6f", delimiter=",")

