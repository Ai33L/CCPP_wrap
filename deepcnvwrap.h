void samfdeepcnv_loop(int im,int km,_Bool first_time_step,_Bool restart,\
    double **tmf,double **qmicro,int itc,int ntc,double cliq,double cp,double cvap,\
    double eps,double epsm1,double fv,double grav,double hvap,double rd,double rv,\
    double t0c,double delt,double ntk,double ntr,double **delp,\
    double **prslp,double *psp,double  **phil,double **qtr,double **prevsq,double **q,double **q1,double **t1,double **u1,double **v1,double *fscav,\
    _Bool hwrf_samfdeep,_Bool progsigma,double *cldwrk,double *rn,int *kbot,int *ktop,int *kcnv,\
    int *islimsk,double *garea,double **dot,int ncloud,double *hpbl,double **ud_mf,double **dd_mf,double **dt_mf,double **cnvw,double **cnvc,\
    double **QLCN, double **QICN, double **w_upi, double **cf_upi, double **CNV_MFD,\
    double **CNV_DQLDT,double **CLCN,double **CNV_FICE,double **CNV_NDROP,double **CNV_NICE,int mp_phys,int mp_phys_mg,\
    double clam,double c0s,double c1,double betal,double betas,double evef,double pgcon,double asolfac,\
    _Bool do_ca, _Bool ca_closure, _Bool ca_entr, _Bool ca_trigger, double nthresh,double *ca_deep,\
    double *rainevap,double **sigmain,double **sigmaout,double betadcu,double betamcu,double betascu,\
    double *maxMF, _Bool do_mynnedmf);
