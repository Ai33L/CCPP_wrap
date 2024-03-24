rm -r *.mod
rm -r *.o

gfortran -c -fPIC machine.F physcons.F90 funcphys.f90 progsigma_calc.f90 samfaerosols.F samfdeepcnv.f
gfortran -c -fPIC deepcnvwrap.f90

ar -rcs libdconv.a *.o

python deepcnvbuild.py
python test.py
