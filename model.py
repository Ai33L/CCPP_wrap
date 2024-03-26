from sympl import (AdamsBashforth, PlotFunctionMonitor)
from climt import get_default_state, get_grid, RRTMGLongwave
import component_deepcnv as dcnv
from datetime import timedelta
import matplotlib.pyplot as plt

def plot_function(fig, state):
    ax = fig.add_subplot(1, 2, 1)
    ax.plot(
        state['air_temperature_tendency_from_longwave'].values.flatten(),
        state['air_pressure'].values.flatten()/100, '-o', label='LW')
    ax.axes.invert_yaxis()
    ax.set_title('Heating Rates')
    ax.grid()
    ax.set_xlabel('K/day')
    ax.set_ylabel('millibar')
    ax.legend()

    ax.set_yscale('log')
    ax.set_ylim(1e3, 10.)
    ax = fig.add_subplot(1, 2, 2)
    ax.plot(
        state['air_temperature'].values.flatten(),
        state['air_pressure'].values.flatten()/100, '-o')
    ax.axes.invert_yaxis()

    ax.set_yscale('log')
    ax.set_ylim(1e3, 10.)
    ax.set_title('Temperature')
    ax.grid()
    ax.set_xlabel('K')
    ax.set_yticklabels([])

    plt.suptitle('Radiative Eq. with SOCRATES')

#monitor = PlotFunctionMonitor(plot_function)
comp=dcnv.SamfDeepConv()
timestep = timedelta(seconds=600)

grid = get_grid(nx=1, ny=1)
state = get_default_state([comp], grid_state = grid)

for i in range(1):

    diagnostics, state = comp(state, timestep)
    state.update(diagnostics)