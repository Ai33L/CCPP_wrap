from sympl import (
    PlotFunctionMonitor, AdamsBashforth, NetCDFMonitor, get_constant
)
from climt import SimplePhysics, get_default_state
import numpy as np
from datetime import timedelta

from climt import EmanuelConvection, RRTMGShortwave, RRTMGLongwave, SlabSurface
import matplotlib.pyplot as plt
import component_deepcnv as dcnv


def plot_function(fig, state):
    ax = fig.add_subplot(2, 2, 1)
    ax.plot(
        state['convective_cloud_cover'].values.flatten(),
        state['air_pressure'].to_units('mbar').values.flatten(), '-o')
    ax.set_title('Conv. heating rate')
    ax.set_xlabel('K/day')
    ax.set_ylabel('millibar')
    ax.grid()

    ax.axes.invert_yaxis()
    ax = fig.add_subplot(2, 2, 2)
    ax.plot(
        state['air_temperature'].values.flatten(),
        state['air_pressure'].to_units('mbar').values.flatten(), '-o')
    ax.set_title('Air temperature')
    ax.axes.invert_yaxis()
    ax.set_xlabel('K')
    ax.grid()

    ax = fig.add_subplot(2, 2, 3)
    ax.plot(
        state['air_temperature_tendency_from_longwave'].values.flatten(),
        state['air_pressure'].to_units('mbar').values.flatten(), '-o',
        label='LW')
    ax.plot(
        state['air_temperature_tendency_from_shortwave'].values.flatten(),
        state['air_pressure'].to_units('mbar').values.flatten(), '-o',
        label='SW')
    ax.set_title('LW and SW Heating rates')
    ax.legend()
    ax.axes.invert_yaxis()
    ax.set_xlabel('K/day')
    ax.grid()
    ax.set_ylabel('millibar')

    ax = fig.add_subplot(2, 2, 4)
    net_flux = (state['upwelling_longwave_flux_in_air'] +
                state['upwelling_shortwave_flux_in_air'] -
                state['downwelling_longwave_flux_in_air'] -
                state['downwelling_shortwave_flux_in_air'])
    ax.plot(
        net_flux.values.flatten(),
        state['air_pressure_on_interface_levels'].to_units(
            'mbar').values.flatten(), '-o')
    ax.set_title('Net Flux')
    ax.axes.invert_yaxis()
    ax.set_xlabel('W/m^2')
    ax.grid()
    plt.tight_layout()


monitor = PlotFunctionMonitor(plot_function)

timestep = timedelta(minutes=5)

# convection = EmanuelConvection()
convection = dcnv.SamfDeepConv()
radiation_sw = RRTMGShortwave()
radiation_lw = RRTMGLongwave()
slab = SlabSurface()
simple_physics = SimplePhysics()

convection.current_time_step = timestep


state = get_default_state([simple_physics, convection,
                           radiation_lw, radiation_sw, slab])


Rd = get_constant('gas_constant_of_dry_air', 'J kg^-1 K^-1')
Cp_dry =\
    get_constant('heat_capacity_of_dry_air_at_constant_pressure',
                    'J kg^-1 K^-1')
state['air_temperature'].values[:] = 300*np.power((state['air_pressure']/state['surface_air_pressure']), Rd/Cp_dry)
state['surface_albedo_for_direct_shortwave'].values[:] = 0.5
state['surface_albedo_for_direct_near_infrared'].values[:] = 0.5
state['surface_albedo_for_diffuse_shortwave'].values[:] = 0.5

state['zenith_angle'].values[:] = np.pi/2.5
state['surface_temperature'].values[:] = 300.
state['ocean_mixed_layer_thickness'].values[:] = 5
state['area_type'].values[:] = 'sea'
state['specific_humidity'][:3]=0.9

time_stepper = AdamsBashforth([radiation_lw, radiation_sw, slab])

for i in range(20000):
    # convection.current_time_step = timestep
    # diagnostics, state = time_stepper(state, timestep)
    # state.update(diagnostics)
    # diagnostics, new_state = simple_physics(state, timestep)
    # state.update(diagnostics)
    # state.update(new_state)
    diagnostics, new_state = convection(state, timestep)
    state.update(diagnostics)
    state.update(new_state)
    if (i+1) % 100 == 0:
        # monitor.store(state)
        # plt.pause(0.1)
        # print(i, state['surface_temperature'].values)
        # print(state['surface_upward_sensible_heat_flux'])
        # print(state['surface_upward_latent_heat_flux'])
        print(state['lwe_thickness_of_deep_convective_precipitation_amount'].values)
        print(state['vertical_index_at_cloud_base'].values)
        print(state['vertical_index_at_cloud_top'].values)
        print(state['specific_humidity'][:,0])
    state['time'] += timestep
    state['eastward_wind'].values[:] = 3.
    state['specific_humidity'][:3]=0.9