from __future__ import division

import pandas as pd
import numpy as np
import matplotlib.mlab as ml
import matplotlib.pyplot as pp

from mpl_toolkits.axes_grid1 import AxesGrid
from scipy.interpolate import Rbf
from pylab import imread, imshow


# layout_name = "Layout"
#
# layout = imread('input/%s.png' % (layout_name))

# a = tb.tabarray(SVfile='input/mapping.csv')
# a = pd.read_csv('input/newmapping.csv')

s_beacons = ['rssi']
# strengths = 'rssi'

# grid_width = 797
# grid_height = 530
#
# image_width = 2544
# image_height = 1691
#
# grid_width = image_width // 3.2
# grid_height = image_height // 3.2

# num_x = image_width / 4
# num_y = num_x / (image_width / image_height)

# num_x = image_width // 8
# num_y = num_x // (image_width // image_height)
#
# print("Resolution: %0.2f x %0.2f" % (num_x, num_y))
#
# x = np.linspace(0, grid_width, num_x)
# y = np.linspace(0, grid_height, num_y)
#
# gx, gy = np.meshgrid(x, y)
# gx, gy = gx.flatten(), gy.flatten()
#
# levels = [-85, -80, -75, -70, -65, -60, -55, -50, -45, -40, -35, -30, -25]
#
# interpolate = True

def add_inner_title(ax, title, loc, size=None, **kwargs):
    from matplotlib.offsetbox import AnchoredText
    from matplotlib.patheffects import withStroke

    if size is None:
        size = dict(size=pp.rcParams['legend.fontsize'])

    at = AnchoredText(title, loc=loc, prop=size,
                      pad=0., borderpad=0.5,
                      frameon=False, **kwargs)

    at.set_zorder(200)

    ax.add_artist(at)

    at.txt._text.set_path_effects([withStroke(foreground="w", linewidth=3)])

    return at

def save_single_plot(layout_fn, csv_fn, output_fn):

    layout = imread(layout_fn)
    a = pd.read_csv(csv_fn)

    image_width = len(layout[0])
    image_height = len(layout)

    print("Image Width: %d; Image Height: %d" % (image_width, image_height))

    grid_width = image_width
    grid_height = image_height

    num_x = image_width // 8
    num_y = num_x // (image_width // image_height)

    print("Resolution: %0.2f x %0.2f" % (num_x, num_y))

    x = np.linspace(0, grid_width, num_x)
    y = np.linspace(0, grid_height, num_y)

    gx, gy = np.meshgrid(x, y)
    gx, gy = gx.flatten(), gy.flatten()

    levels = [-85, -80, -75, -70, -65, -60, -55, -50, -45, -40, -35, -30, -25]

    interpolate = True

    f = pp.figure()

    # f.suptitle("RSSI Heatmap")

    # Adjust the margins and padding
    # f.subplots_adjust(hspace=0.1, wspace=0.1, left=0.05, right=0.95, top=0.85,
    #         bottom=0.15)

    # Create a grid of subplots using the AxesGrid helper
    image_grid = AxesGrid(f, 111, nrows_ncols=(1, 1), axes_pad=0.1,
            label_mode="1", share_all=True, cbar_location="right",
            cbar_mode="single", cbar_size="3%")

    for beacon, i in zip(s_beacons, range(len(s_beacons))):
        # Hide the axis labels
        image_grid[i].xaxis.set_visible(False)
        image_grid[i].yaxis.set_visible(False)

        if interpolate:
            # Interpolate the data
            rbf = Rbf(a['Drawing X'], a['Drawing Y'], a[beacon],
                    function='linear')

            z = rbf(gx, gy)
            z = z.reshape((num_y, num_x))

            # Render the interpolated data to the plot
            image = image_grid[i].imshow(z, vmin=-85, vmax=-25, extent=(0,
                image_width, image_height, 0), cmap='RdYlBu_r', alpha=1)

            #c = image_grid[i].contourf(z, levels, alpha=0.5)
            #c = image_grid[i].contour(z, levels, linewidths=5, alpha=0.5)
        else:
            z = ml.griddata(a['Drawing X'], a['Drawing Y'], a[beacon], x, y)

            c = image_grid[i].contourf(x, y, z, levels, alpha=0.5)

        image_grid[i].imshow(layout, interpolation='bicubic', zorder=100)

    # Setup the data for the colorbar and its ticks
    image_grid.cbar_axes[0].colorbar(image)
    image_grid.cbar_axes[0].set_yticks(levels)

    # Add inset titles to each subplot
    for ax, im_title in zip(image_grid, s_beacons):
        t = add_inner_title(ax, "Layout Name: %s" % layout_fn, loc=3)

        t.patch.set_alpha(0.5)

    # pp.show()
    pp.savefig(output_fn, bbox_inches='tight', transparent=True)

if __name__ == "__main__":
    import sys
    print(sys.argv)
    save_single_plot(sys.argv[1], sys.argv[2], sys.argv[3]);

    # save_single_plot("input/Layout.png", "input/newmapping.csv", "output/test.png");
    # grid_plots()
    # max_plot()
