
from helper import Kpoints


# instantiate class Kpoints(nk1, nk2, nk3, "filename_to_save")
k=Kpoints(7,4,1)

klist = k.gen_kpts()

k.save_kpts(klist)
