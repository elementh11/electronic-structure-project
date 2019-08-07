
from helper import Kpoints


#k=Kpoints(7,4,1,"kptsBZ.csv")
k=Kpoints(7,4,1)

klist = k.gen_kpts()

k.save_kpts(klist)