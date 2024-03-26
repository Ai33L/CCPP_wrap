## Template for a stepper sympl component

import _runesfile as rf
import numpy as np
from sympl import (
    get_constant, set_constant, initialize_numpy_arrays_with_properties,
    Stepper
)

class SamfDeepConv(Stepper):

    input_properties = {
        'air_pressure': {
            'dims': ['mid_levels', '*'],
            'units': 'Pa',
        },
        # 'air_pressure_on_interface_levels': {
        #     'dims': ['interface_levels', '*'],
        #     'units': 'Pa',
        # },
        # 'air_temperature': {
        #     'dims': ['mid_levels', '*'],
        #     'units': 'degK',
        # },
        # 'air_temperature_on_interface_levels': {
        #     'dims': ['interface_levels', '*'],
        #     'units': 'degK',
        # },
        # 'surface_temperature': {
        #     'dims': ['*'],
        #     'units': 'degK',
        # },
        # 'specific_humidity': {
        #     'dims': ['mid_levels', '*'],
        #     'units': 'kg/kg',
        # },
        # 'mole_fraction_of_ozone_in_air': {
        #     'dims': ['mid_levels', '*'],
        #     'units': 'mole/mole',
        # },
    }

    diagnostic_properties = {
        # 'air_temperature': {
        #     'dims': ['mid_levels', '*'],
        #     'units': 'degK day^-1',
        # },
    }

    output_properties = {
        # 'upwelling_longwave_flux_in_air': {
        #     'dims': ['interface_levels', '*'],
        #     'units': 'W m^-2',
        # },
        # 'downwelling_longwave_flux_in_air': {
        #     'dims': ['interface_levels', '*'],
        #     'units': 'W m^-2',
        # },
        # 'air_temperature_tendency_from_longwave': {
        #     'dims': ['mid_levels', '*'],
        #     'units': 'degK day^-1',
        # },
    }

    def __init__(self, first_time_step=True, restart=True, **kwargs):
        
        self._first_time_step=first_time_step
        self._restart=restart

        super(SamfDeepConv, self).__init__(**kwargs)

    def array_call(self, state, timestep):

        km,im=np.shape(state['air_pressure'])

        runesobject = rf._runesfile()

        diagnostics = initialize_numpy_arrays_with_properties(
            self.diagnostic_properties, state, self.input_properties
        )

        new_state = initialize_numpy_arrays_with_properties(
            self.output_properties, state, self.input_properties
        )

        runesobject._samfdeepcnv_loop(im,km,self._first_time_step,\
        self._restart,tmf,qmicro,itc,ntc,cliq,cp,cvap,\
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
            
        return diagnostics, new_state