! Wrappping module

module deep_convection_wrap

    use iso_c_binding, only: c_int, c_double, c_bool, c_char, c_ptr
    use samfdeepcnv, only: samfdeepcnv_run

    implicit none
    public

    contains

    subroutine samfdeepcnv_loop(im,km,first_time_step,restart,        &
     &    tmf,qmicro,itc,ntc,cliq,cp,cvap,                              &
     &    eps,epsm1,fv,grav,hvap,rd,rv,                                 &
     &    t0c,delt,ntk,ntr,delp,                                        &
     &    prslp,psp,phil,qtr,prevsq,q,q1,t1,u1,v1,fscav,                &
     &    hwrf_samfdeep,progsigma,cldwrk,rn,kbot,ktop,kcnv,             &
     &    islimsk,garea,dot,ncloud,hpbl,ud_mf,dd_mf,dt_mf,cnvw,cnvc,    &
     &    QLCN, QICN, w_upi, cf_upi, CNV_MFD,                           &
     &    CNV_DQLDT,CLCN,CNV_FICE,CNV_NDROP,CNV_NICE,mp_phys,mp_phys_mg,&
     &    clam,c0s,c1,betal,betas,evef,pgcon,asolfac,                   &
     &    do_ca, ca_closure, ca_entr, ca_trigger, nthresh,ca_deep,      &
     &    rainevap,sigmain,sigmaout,betadcu,betamcu,betascu,            &
     &    maxMF, do_mynnedmf) bind (c)

    implicit none

    integer(c_int), intent(in), value  :: im, km, itc, ntc, ntk, ntr, ncloud
    real(c_double), intent(in), dimension(im,km,1) :: tmf
    integer(c_int), intent(in),dimension(im)  :: islimsk
    real(c_double), intent(in), value :: cliq, cp, cvap, eps, epsm1,   &
     &   fv, grav, hvap, rd, rv, t0c, delt
    real(c_double), intent(in),dimension(im) :: psp, garea, hpbl, maxMF
    real(c_double), intent(in), dimension(im,km) :: delp, prslp, dot, phil
    real(c_double), intent(in), dimension(ntc) :: fscav
    logical(c_bool), intent(in), value  :: first_time_step,restart,hwrf_samfdeep,    &
     &     progsigma,do_mynnedmf
    real(c_double), intent(in),value :: nthresh,betadcu,betamcu,      &
     &                                    betascu
    real(c_double), intent(in),dimension(im) :: ca_deep
    real(c_double), intent(in), dimension(im,km) :: sigmain,qmicro,     &
     &     q, prevsq

    real(c_double), intent(out), dimension(im) :: rainevap
    real(c_double), intent(out), dimension(im,km) :: sigmaout
    logical(c_bool), intent(in), value  :: do_ca,ca_closure,ca_entr,ca_trigger
    integer(c_int), intent(inout), dimension(im)  :: kcnv

    ! DH* TODO - check dimensions of qtr, ntr+2 correct?  *DH
    real(c_double), intent(inout), dimension(im,km,ntr+2) ::   qtr
    real(c_double), intent(inout), dimension(im,km) :: q1, t1, &
     &  u1, v1,cnvw,  cnvc

    integer(c_int), intent(out), dimension(im) :: kbot, ktop
    real(c_double), intent(out), dimension(im) :: cldwrk, rn
    real(c_double), intent(out), dimension(im,km) :: ud_mf,dd_mf, dt_mf
      
    ! GJF* These variables are conditionally allocated depending on whether the
    !     Morrison-Gettelman microphysics is used, so they must be declared 
    !     using assumed shape.
    real(c_double), intent(inout), dimension(im,km) ::            &
     &   qlcn, qicn, w_upi, cnv_mfd, cnv_dqldt, clcn                    &
     &,  cnv_fice, cnv_ndrop, cnv_nice, cf_upi
    ! *GJF
    integer(c_int), intent(in), value :: mp_phys, mp_phys_mg

    real(c_double), intent(in), value :: clam,  c0s,  c1,              &
     &                     betal,   betas,   asolfac,                   &
     &                     evef,  pgcon
    

    print *, tmf

    call samfdeepcnv_run (im,km,logical(first_time_step),logical(restart),        &
     &    tmf,qmicro,itc,ntc,cliq,cp,cvap,                              &
     &    eps,epsm1,fv,grav,hvap,rd,rv,                                 &
     &    t0c,delt,ntk,ntr,delp,                                        &
     &    prslp,psp,phil,qtr,prevsq,q,q1,t1,u1,v1,fscav,                &
     &    logical(hwrf_samfdeep),logical(progsigma),cldwrk,rn,kbot,ktop,kcnv,             &
     &    islimsk,garea,dot,ncloud,hpbl,ud_mf,dd_mf,dt_mf,cnvw,cnvc,    &
     &    QLCN, QICN, w_upi, cf_upi, CNV_MFD,                           &
     &    CNV_DQLDT,CLCN,CNV_FICE,CNV_NDROP,CNV_NICE,mp_phys,mp_phys_mg,&
     &    clam,c0s,c1,betal,betas,evef,pgcon,asolfac,                   &
     &    logical(do_ca), logical(ca_closure), logical(ca_entr), logical(ca_trigger), nthresh,ca_deep,      &
     &    rainevap,sigmain,sigmaout,betadcu,betamcu,betascu,            &
     &    maxMF, logical(do_mynnedmf))


    end subroutine samfdeepcnv_loop 

end module deep_convection_wrap