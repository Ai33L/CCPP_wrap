## Template for a stepper sympl component

import _runesfile as rf
import numpy as np
from sympl import (
    get_constant, set_constant, initialize_numpy_arrays_with_properties,
    Stepper
)
from climt._core import ensure_contiguous_state

class SamfDeepConv(Stepper):

    input_properties = {
        'air_pressure': {
            'dims': ['mid_levels', '*'],
            'units': 'Pa',
        },
        # 'tendency_of_vertically_diffused_tracer_concentration': {
        #     'dims': ['tracers', 'mid_levels', '*'],
        #     'units': 'kg kg^-1 s^-1',
        # },
        'instantaneous_tendency_of_specific_humidity_due_to_microphysics': {
            'dims': ['mid_levels', '*'],
            'units': 'kg kg^-1 s^-1',
        },
        'air_pressure_on_interface_levels': {
            'dims': ['interface_levels', '*'],
            'units': 'Pa',
        },
        'surface_air_pressure': {
            'dims': ['*'],
            'units': 'Pa',
        },
        'specific_humidity': {
            'dims': ['mid_levels', '*'],
            'units': 'kg/kg',
        },
         'air_temperature': {
            'dims': ['mid_levels', '*'],
            'units': 'degK ',
        },
        'northward_wind': {
            'dims': ['mid_levels', '*'],
            'units': 'm s^-1',
        },
        'eastward_wind': {
            'dims': ['mid_levels', '*'],
            'units': 'm s^-1',
        },
        'flag_deep_convection': {
            'dims': ['*'],
            'units': 'dimensionless',
        },
        'area_type': {
            'dims': ['*'],
            'units': 'dimensionless',
        },
        'lagrangian_tendency_of_air_pressure': {
            'dims': ['mid_levels', '*'],
            'units': 'Pa s^-1',
        },
        'atmosphere_boundary_layer_thickness': {
            'dims': ['*'],
            'units': 'm',
        },
        'prognostic_updraft_area_fraction_in_convection': {
            'dims': ['mid_levels', '*'],
            'units': 'dimensionless',
        },
        'cellular_automata_area_fraction_for_deep_convection_from_coupled_process': {
            'dims': ['*'],
            'units': 'dimensionless',
        },
        'maximum_mass_flux': {
            'dims': ['*'],
            'units': 'm s^-1',
        },
    }

    diagnostic_properties = {
        'cloud_work_function': {
            'dims': ['*'],
            'units': 'm^2 s^-2',
        },
        'lwe_thickness_of_deep_convective_precipitation_amount': {
            'dims': ['*'],
            'units': 'm',
        },
        'vertical_index_at_cloud_base': {
            'dims': ['*'],
            'units': 'index',
        },
        'vertical_index_at_cloud_top': {
            'dims': ['*'],
            'units': 'index',
        },
    }

    output_properties = {
        'specific_humidity': {
            'dims': ['mid_levels', '*'],
            'units': 'kg/kg',
        },
        'air_temperature': {
            'dims': ['mid_levels', '*'],
            'units': 'degK ',
        },
        'northward_wind': {
            'dims': ['mid_levels', '*'],
            'units': 'm s^-1',
        },
        'eastward_wind': {
            'dims': ['mid_levels', '*'],
            'units': 'm s^-1',
        },
        'flag_deep_convection': {
            'dims': ['*'],
            'units': 'dimensionless',
        },
        'instantaneous_atmosphere_updraft_convective_mass_flux': {
            'dims': ['mid_levels', '*'],
            'units': 'kg m^-2',
        },
        'instantaneous_atmosphere_downdraft_convective_mass_flux': {
            'dims': ['mid_levels', '*'],
            'units': 'kg m^-2',
        },
        'instantaneous_atmosphere_detrainment_convective_mass_flux': {
            'dims': ['mid_levels', '*'],
            'units': 'kg m^-2',
        },
        'updraft_area_fraction_updated_by_physics': {
            'dims': ['mid_levels', '*'],
            'units': 'dimensionless',
        },
        'physics_field_for_coupling': {
            'dims': ['*'],
            'units': 'm^2 s^-2',
        },
    }
    extra_init_properties = {
    # 'tendency_of_vertically_diffused_tracer_concentration': {'value': 0.,
    #         'units': 'kg kg^-1 s^-1',
    #         'domain': 'atmosphere'},
    'instantaneous_tendency_of_specific_humidity_due_to_microphysics': {'value': 0.,
            'units': 'kg kg^-1 s^-1',
            'domain': 'atmosphere'},
    'flag_deep_convection': {'value': 0,
            'units': 'dimensionless',
            'domain': 'atmosphere_horizontal'},
    'lagrangian_tendency_of_air_pressure': {'value': 0,
            'units': 'Pa s^-1',
            'domain': 'atmosphere'},
    'atmosphere_boundary_layer_thickness': {'value': 1000,
            'units': 'm',
            'domain': 'atmosphere_horizontal'},
    'prognostic_updraft_area_fraction_in_convection': {'value': 0.2,
            'units': 'dimensionless',
            'domain': 'atmosphere'},
    'cellular_automata_area_fraction_for_deep_convection_from_coupled_process': {'value': 0.2,
            'units': 'dimensionless',
            'domain': 'atmosphere_horizontal'},
    'maximum_mass_flux': {'value': 1,
            'units': 'm s^-1',
            'domain': 'atmosphere_horizontal'},
    }

    def __init__(self, first_time_step=True, restart=True, itc=0, ntc=0, t0c=273.15, ntk=0,
                 ntr=0, hwrf_samfdeep=True, prosigma=True, ncloud=1, 
                 betadcu=0, betamcu=0, betascu=0, mp_phys=0, mp_phys_mg=0, clam=0.2, c0s=0.2,
                 c1=0.2, betal=0.2, betas=0.2, evef=0.2, pgcon=0.2, asolfac=0.2, do_ca=True,
                 ca_closure=True, ca_entr=True, ca_trigger=True, nthresh=1, do_mynnedmf=False,**kwargs):
        
        self._first_time_step=first_time_step
        self._restart=restart
        self._itc=itc
        self._ntc=ntc
        self._cp = get_constant('heat_capacity_of_dry_air_at_constant_pressure', 'J/kg/degK')
        self._cliq = get_constant('heat_capacity_of_liquid_water', 'J/kg/degK')
        self._cvap = get_constant('heat_capacity_of_water_vapor_at_constant_pressure', 'J/kg/degK')
        self._grav=get_constant('gravitational_acceleration', 'm s^-2')
        self._hvap=get_constant('latent_heat_of_vaporization_of_water', 'J kg^-1')
        self._rd=get_constant('gas_constant_of_dry_air', 'J kg^-1 K^-1')
        self._rv=get_constant('gas_constant_of_water_vapor', 'J kg^-1 K^-1')
        self._eps=self._rd/self._rv
        self._epsm1=(self._rd/self._rv)-1
        self._fv=(self._rv/self._rd)-1
        self._t0c=t0c
        self._ntk=ntk
        self._ntr=ntr
        self._hwrf_samfdeep=hwrf_samfdeep
        self._prosigma=prosigma
        self._ncloud=ncloud
        self._betadcu=betadcu
        self._betamcu=betamcu
        self._betascu=betascu
        self._mp_phys=mp_phys
        self._mp_phys_mg=mp_phys_mg
        self._clam=clam
        self._c0s=c0s
        self._c1=c1
        self._betal=betal
        self._betas=betas
        self._evef=evef
        self._pgcon=pgcon
        self._asolfac=asolfac
        self._do_ca=do_ca
        self._ca_closure=ca_closure
        self._ca_entr=ca_entr
        self._ca_trigger=ca_trigger
        self._nthresh=nthresh
        self._do_mynnedmf=do_mynnedmf

        super(SamfDeepConv, self).__init__(**kwargs)

    # @ensure_contiguous_state
    def array_call(self, state, timestep):

        km,im=np.shape(state['air_pressure'])

        runesobject = rf._runesfile()

        diagnostics = initialize_numpy_arrays_with_properties(
            self.diagnostic_properties, state, self.input_properties
        )

        new_state = initialize_numpy_arrays_with_properties(
            self.output_properties, state, self.input_properties
        )

        tmf=np.zeros((im,km,1)) #diffused tracer
        phil=np.ones((im,km))*100 #geopot
        qtr=np.zeros((im,km,2)) #convective tracers
        fscav=np.array([]) #chemical tracer
        garea=np.ones(im)*100000 #area of cell
        prevsq=np.ones((im,km))*0.1 #previous specific humidity

        #many inout arrays
        cnvw=np.ones((im,km))*100
        cnvc=np.ones((im,km))*100
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

        new_state['air_temperature'][:] = state["air_temperature"]
        new_state['specific_humidity'][:] = state['specific_humidity']
        new_state['northward_wind'][:] = state['northward_wind']
        new_state['eastward_wind'][:] = state['eastward_wind']
        new_state['flag_deep_convection'][:] = state['flag_deep_convection']

        runesobject._samfdeepcnv_loop(im,km,self._first_time_step,\
        self._restart,tmf,
        state['instantaneous_tendency_of_specific_humidity_due_to_microphysics'],
        self._itc,self._ntc,self._cliq,self._cp,self._cvap,\
        self._eps,self._epsm1,self._fv,self._grav,self._hvap,self._rd,self._rv,\
        self._t0c,timestep.total_seconds(),self._ntk,self._ntr,
        state['air_pressure_on_interface_levels'][:-1]-state['air_pressure_on_interface_levels'][1:],
        state['air_pressure'],state['surface_air_pressure'],phil,qtr,prevsq,state['specific_humidity'].copy(),
        new_state['specific_humidity'],new_state['air_temperature'],new_state['eastward_wind'],new_state['northward_wind'],
        fscav,self._hwrf_samfdeep,self._prosigma,diagnostics['cloud_work_function'],
        diagnostics['lwe_thickness_of_deep_convective_precipitation_amount'],
        diagnostics['vertical_index_at_cloud_base'],diagnostics['vertical_index_at_cloud_top'],
        new_state['flag_deep_convection'],state['area_type'],garea,state['lagrangian_tendency_of_air_pressure'],
        self._ncloud,state['atmosphere_boundary_layer_thickness'],
        new_state['instantaneous_atmosphere_updraft_convective_mass_flux'],
        new_state['instantaneous_atmosphere_downdraft_convective_mass_flux'],
        new_state['instantaneous_atmosphere_detrainment_convective_mass_flux'],
        cnvw,cnvc,\
        QLCN, QICN, w_upi, cf_upi, CNV_MFD,\
        CNV_DQLDT,CLCN,CNV_FICE,CNV_NDROP,CNV_NICE,self._mp_phys,self._mp_phys_mg,\
        self._clam,self._c0s,self._c1,self._betal,self._betas,self._evef,self._pgcon,self._asolfac,\
        self._do_ca, self._ca_closure, self._ca_entr, self._ca_trigger, self._nthresh,
        state['cellular_automata_area_fraction_for_deep_convection_from_coupled_process'],
        new_state['physics_field_for_coupling'],state['prognostic_updraft_area_fraction_in_convection'],
        new_state['updraft_area_fraction_updated_by_physics'],
        self._betadcu,self._betamcu,self._betascu, state['maximum_mass_flux'], self._do_mynnedmf)
            
        return diagnostics, new_state