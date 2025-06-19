import numpy as np
import matplotlib.pylab as plt

import numpy as np
import matplotlib.pylab as plt

###########################################################
############### L4-L5 - new materials #####################
###########################################################
def LV_field(ax, LV_cc, r1, r2, K1, K2, a12, a21, nb_points=20, cmap='gist_gray', alpha=0.5):
    # plot isocline
    ax.plot([0,K2/a21], [K2,0], color='purple', ls="-", alpha=alpha)
    ax.plot([0,K1], [K1/a12,0], color='g', ls="-", alpha=alpha)

    # define a grid and compute direction at each point
    ymax = ax.set_ylim(ymin=0)[1]                        # get axis limits
    xmax = ax.set_xlim(xmin=0)[1]

    # reset axix lims
    ax.set_xlim((-0.2,K1*11/10))
    ax.set_ylim((-0.2,K2*11/10))
    
    x = np.linspace(0, xmax, nb_points)
    y = np.linspace(0, ymax, nb_points)

    X1 , Y1  = np.meshgrid(x, y)                           # create a grid
    DX1, DY1 = LV_cc(0,[X1, Y1], r1, r2, K1, K2, a12, a21) # compute growth rate on the gridt
    M = (np.hypot(DX1, DY1))                               # Norm of the growth rate 
    M[ M == 0] = 1.                                        # Avoid zero division errors 
    DX1 /= M                                               # Normalize each arrows
    DY1 /= M

    #-------------------------------------------------------
    # Drow direction fields, using matplotlib 's quiver function
    # I choose to plot normalized arrows and to use colors to give information on the growth speed
    Q = ax.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=cmap, alpha=alpha)


def set_plot_style(ax, title=None, xlabel=None, ylabel=None, xscale='linear', yscale='linear', xlims=None, ylims=None, xticks=None, yticks=None, xticklabels=None, yticklabels=None, legend=True, legend_args={}, xticklabels_args={}, yticklabels_args={}):
    ax.set_title(title, fontweight='semibold')
    ax.set_xlabel(xlabel, fontweight='semibold', color='#454545')
    ax.set_ylabel(ylabel, fontweight='semibold', color='#454545')
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)
    if legend: ax.legend(frameon = False,**legend_args)
    if not xlims is None: ax.set_xlim(xlims)
    if not ylims is None: ax.set_ylim(ylims)
    if not xticks is None: ax.set_xticks(xticks)
    if not yticks is None: ax.set_xticks(yticks)
    if not xticklabels is None: ax.set_xticklabels(xticklabels, **xticklabels_args)
    if not yticklabels is None: ax.set_xticklabels(yticklabels, **yticklabels_args)

    for spine in ('top', 'right'): 
        ax.spines[spine].set_visible(False)

###########################################################
################ L6 - new materials #######################
###########################################################
def plot_filled_categorical_time_series(ax, series, y_offset, height, label):
    """Fill the area completely between time steps without gaps."""
    x_vals = series.index.astype(np.int16)
    
    for i in range(len(series) - 1):  # Iterate over consecutive pairs
        category = series.iloc[i]
        ax.fill_betweenx([y_offset, y_offset + height], 
                         x_vals[i], x_vals[i + 1], 
                         color=interaction_colors[category], alpha=0.7, zorder=2)

### Lotka-Volterra colors for interaction types
colors_i =['#C82B2A',
           '#E7570D','#EE7F02',
           '#FAC307','#FEE067',
           '#75D215',
           '#49A8F5','#1A72C3',
           '#9C42CE'
          ]
interaction_coefficients_combinations = {
    'Prey-Prey': '+/+ Pure Competition',
    'Prey-Neut': '+/0 Amensalism',
    'Neut-Prey': '0/+ Impervious',
    'Pred-Prey': '-/+ Predator-prey',
    'Prey-Pred': '+/- Prey-predator',
    'Neut-Neut': '0/0 Neutralism',
    'Pred-Neut': '-/0 Host-parasitic',
    'Neut-Pred': '0/- Parasitic-host',
    'Pred-Pred': '-/- Mutualism'
}
interaction_colors = {
    '+/+ Pure Competition': colors_i[0],
    '+/0 Amensalism': colors_i[1],
    '0/+ Impervious': colors_i[2],
    '-/+ Predator-prey': colors_i[3],
    '+/- Prey-predator': colors_i[4],
    '0/0 Neutralism': colors_i[5],
    '-/0 Host-parasitic': colors_i[6],
    '0/- Parasitic-host': colors_i[7],
    '-/- Mutualism': colors_i[8]
}
###########################################################


###########################################################
############### L10-L11 - new materials ###################
###########################################################
# no new materials
###########################################################



