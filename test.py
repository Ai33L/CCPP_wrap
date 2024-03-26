import _runesfile as rf
import numpy as np

im=3
km=5
first_time_step=False
restart=False
tmf=np.zeros((im,km,1))
qmicro=np.zeros((im,km))
itc=0
ntc=1
cliq=4181
cp=1004
cvap=1996
eps=0.622
epsm1=eps-1
fv=1/eps-1
grav=9.8
hvap=2260
rd=287.052874
rv=461
t0c=273
delt=60
ntk=1
ntr=1
delp=np.ones((im,km))*20000
prslp=np.ones((im,km))*np.array([100000,80000,60000,40000,20000])
psp=np.ones(im)*100010
phil=np.ones((im,km))*100000
qtr=np.zeros((im,km,ntr+2))
prevsq=np.ones((im,km))*0.01
q=np.ones((im,km))*0.01
q1=np.ones((im,km))*0.01
t1=np.ones((im,km))*273
u1=np.ones((im,km))*3
v1=np.ones((im,km))*3
fscav=np.ones(ntc)*0.1
hwrf_samfdeep=False
progsigma=False
cldwrk=np.ones(im)*1000
rn=np.ones(im)*1000
kbot=np.intc(np.ones(im)*2)
ktop=np.intc(np.ones(im)*3)
kcnv=np.intc(np.zeros(im))
islimsk=np.zeros(im)
garea=np.ones(im)*10000
dot=np.ones((im,km))*10
ncloud=1
hpbl=np.ones(im)*1500

ud_mf=np.zeros((im,km))
dd_mf=np.zeros((im,km))
dt_mf=np.zeros((im,km))
cnvw=np.zeros((im,km))
cnvc=np.zeros((im,km))
QLCN=np.ones((im,km))*0.1
QICN=np.ones((im,km))*0.1
w_upi=np.ones((im,km))*0.01
cf_upi=np.ones((im,km))*0.1
CNV_MFD=np.ones((im,km))*1000
CNV_DQLDT=np.ones((im,km))*10
CLCN=np.ones((im,km))*0.01
CNV_FICE=np.ones((im,km))*0.001
CNV_NDROP=np.ones((im,km))*20
CNV_NICE=np.ones((im,km))*20
mp_phys=0
mp_phys_mg=0
clam=0.2
c0s=0.2
c1=0.2
betal=0.2
betas=0.2
evef=0.2
pgcon=0.2
asolfac=0.2
do_ca=True
ca_closure=True
ca_entr=True
ca_trigger=True
nthresh=1
ca_deep=np.ones(im)*0.2
rainevap=np.ones(im)*100
sigmain=np.zeros((im,km))
sigmaout=np.zeros((im,km))
betadcu=0
betamcu=0
betascu=0
maxMF=np.ones(im)*0.5
do_mynnedmf=False

runesobject = rf._runesfile()

runesobject._samfdeepcnv_loop(im,km,first_time_step,\
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
    maxMF, do_mynnedmf)