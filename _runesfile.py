import samfdeepcnv
import numpy as np
import runes_script_convert as rsc 

conv_mat = rsc.runes()

class _runesfile (object):

    def _samfdeepcnv_loop(self, im,km,first_time_step,\
    restart,tmf,qmicro,itc,ntc,cliq,cp,cvap,\
    eps,epsm1,fv,grav,hvap,rd,rv,\
    t0c,delt,ntk,ntr,delp,\
    prslp,psp,phil,qtr,prevsq,q,q1,t1,u1,v1,fscav,\
    hwrf_samfdeep,progsigma,cldwrk,rn,kbot,ktop,kcnv,\
    islimsk,garea,dot,ncloud,hpbl,ud_mf,dd_mf,dt_mf,cnvw,cnvc,\
    QLCN, QICN, w_upi, cf_upi, CNV_MFD,\
    CNV_DQLDT,CLCN,CNV_FICE,CNV_NDROP,CNV_NICE,mp_phys,mp_phys_mg,\
    clam,c0s,c1,betal,betas,evef,pgcon,asolfac,\
    do_ca, ca_closure, ca_entr, ca_trigger, nthresh,ca_deep,\
    rainevap,sigmain,sigmaout,betadcu,betamcu,betascu,\
    maxMF, do_mynnedmf):
        
        tmf_c = conv_mat.convert_to_from_cffi(tmf)
        qmicro_c = conv_mat.convert_to_from_cffi(qmicro)
        delp_c = conv_mat.convert_to_from_cffi(delp)
        prslp_c = conv_mat.convert_to_from_cffi(prslp)
        psp_c = conv_mat.convert_to_from_cffi(psp)
        phil_c = conv_mat.convert_to_from_cffi(phil)
        qtr_c = conv_mat.convert_to_from_cffi(qtr)
        prevsq_c = conv_mat.convert_to_from_cffi(prevsq)
        q_c = conv_mat.convert_to_from_cffi(q)
        q1_c = conv_mat.convert_to_from_cffi(q1)
        t1_c = conv_mat.convert_to_from_cffi(t1)
        u1_c = conv_mat.convert_to_from_cffi(u1)
        v1_c = conv_mat.convert_to_from_cffi(v1)
        fscav_c = conv_mat.convert_to_from_cffi(fscav)
        cldwrk_c = conv_mat.convert_to_from_cffi(cldwrk)
        rn_c = conv_mat.convert_to_from_cffi(rn)
        kbot_c = conv_mat.convert_to_from_cffi(kbot, type='integer')
        ktop_c = conv_mat.convert_to_from_cffi(ktop, type='integer')
        kcnv_c = conv_mat.convert_to_from_cffi(kcnv, type='integer')
        islimsk_c = conv_mat.convert_to_from_cffi(islimsk, type='integer')
        garea_c = conv_mat.convert_to_from_cffi(garea)

        dot_c = conv_mat.convert_to_from_cffi(dot)
        hpbl_c = conv_mat.convert_to_from_cffi(hpbl)
        ud_mf_c = conv_mat.convert_to_from_cffi(ud_mf)
        dd_mf_c = conv_mat.convert_to_from_cffi(dd_mf)
        dt_mf_c = conv_mat.convert_to_from_cffi(dt_mf)
        cnvw_c = conv_mat.convert_to_from_cffi(cnvw)
        cnvc_c = conv_mat.convert_to_from_cffi(cnvc)
        QLCN_c = conv_mat.convert_to_from_cffi(QLCN)
        QICN_c = conv_mat.convert_to_from_cffi(QICN)
        w_upi_c = conv_mat.convert_to_from_cffi(w_upi)
        cf_upi_c = conv_mat.convert_to_from_cffi(cf_upi)
        CNV_MFD_c = conv_mat.convert_to_from_cffi(CNV_MFD)
        CNV_DQLDT_c = conv_mat.convert_to_from_cffi(CNV_DQLDT)
        CLCN_c = conv_mat.convert_to_from_cffi(CLCN)
        CNV_FICE_c = conv_mat.convert_to_from_cffi(CNV_FICE)
        CNV_NDROP_c = conv_mat.convert_to_from_cffi(CNV_NDROP)
        CNV_NICE_c = conv_mat.convert_to_from_cffi(CNV_NICE)
        
        ca_deep_c = conv_mat.convert_to_from_cffi(ca_deep)
        rainevap_c = conv_mat.convert_to_from_cffi(rainevap)
        sigmain_c = conv_mat.convert_to_from_cffi(sigmain)
        sigmaout_c = conv_mat.convert_to_from_cffi(sigmaout)
        maxMF_c = conv_mat.convert_to_from_cffi(maxMF)

        samfdeepcnv.lib.samfdeepcnv_loop(im,km,first_time_step,\
        restart,tmf_c,qmicro_c,itc,ntc,cliq,cp,cvap,\
        eps,epsm1,fv,grav,hvap,rd,rv,\
        t0c,delt,ntk,ntr,delp_c,\
        prslp_c,psp_c,phil_c,qtr_c,prevsq_c,q_c,q1_c,t1_c,u1_c,v1_c,fscav_c,\
        hwrf_samfdeep,progsigma,cldwrk_c,rn_c,kbot_c,ktop_c,kcnv_c,\
        islimsk_c,garea_c,dot_c,ncloud,hpbl_c,ud_mf_c,dd_mf_c,dt_mf_c,cnvw_c,cnvc_c,\
        QLCN_c, QICN_c, w_upi_c, cf_upi_c, CNV_MFD_c,\
        CNV_DQLDT_c,CLCN_c,CNV_FICE_c,CNV_NDROP_c,CNV_NICE_c,mp_phys,mp_phys_mg,\
        clam,c0s,c1,betal,betas,evef,pgcon,asolfac,\
        do_ca, ca_closure, ca_entr, ca_trigger, nthresh,ca_deep_c,\
        rainevap_c,sigmain_c,sigmaout_c,betadcu,betamcu,betascu,\
        maxMF_c, do_mynnedmf)