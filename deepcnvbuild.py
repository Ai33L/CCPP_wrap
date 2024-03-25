import os
from cffi import FFI

desired_compiler = "gcc"

current_dir = os.getcwd()
# include_dirs = os.path.join(current_dir, "climt_socrates/_lib")

ffi_builder = FFI()

ffi_builder.cdef(
    "void samfdeepcnv_loop(int im,int km,bool first_time_step,bool restart,\
    double **tmf,double **qmicro,int itc,int ntc,double cliq,double cp,double cvap,\
    double eps,double epsm1,double fv,double grav,double hvap,double rd,double rv,\
    double t0c,double delt,double ntk,double ntr,double **delp,\
    double **prslp,double *psp,double  **phil,double **qtr,double **prevsq,double **q,double **q1,double **t1,double **u1,double **v1,double *fscav,\
    bool hwrf_samfdeep,bool progsigma,double *cldwrk,double *rn,int *kbot,int *ktop,int *kcnv,\
    int *islimsk,double *garea,double **dot,int ncloud,double *hpbl,double **ud_mf,double **dd_mf,double **dt_mf,double **cnvw,double **cnvc,\
    double **QLCN, double **QICN, double **w_upi, double **cf_upi, double **CNV_MFD,\
    double **CNV_DQLDT,double **CLCN,double **CNV_FICE,double **CNV_NDROP,double **CNV_NICE,int mp_phys,int mp_phys_mg,\
    double clam,double c0s,double c1,double betal,double betas,double evef,double pgcon,double asolfac,\
    bool do_ca, bool ca_closure, bool ca_entr, bool ca_trigger, double nthresh,double *ca_deep,\
    double *rainevap,double **sigmain,double **sigmaout,double betadcu,double betamcu,double betascu,\
    double *maxMF, bool do_mynnedmf);",
    override=True,
)

ffi_builder.set_source(
    "samfdeepcnv",
    """ #include "deepcnvwrap.h" """,
    library_dirs=[os.getcwd()],
    include_dirs=[os.getcwd()],
    libraries=["dconv"],
    extra_link_args=[
        "-lgfortran",
    ],
)

if __name__ == "__main__":  # not when running with setuptools
    ffi_builder.compile(verbose=True)