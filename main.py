# library
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

sns.set_style({'font.family': 'Palatino'})
sns.axes_style()
# import data
# jet
# CMRmap_r
# RdBu
# Blues
# RdPu
# Reds


text = np.asarray([['Core 1', 'Core 2', 'Core 3', 'Core 4'],
                   ['Core 8', 'Core 7', 'Core 6', 'Core 5'],
                   ['Core 9', 'Core 10', 'Core 11', 'Core 12'],
                   ['Core 16', 'Core 15', 'Core 14', 'Core 13']])

#################
# Before
# data = np.array([[84.87170464,84.1507913,78.21578247,74.02946912],
#                  [68.84246698,71.73186586,72.80543605,69.95228358],
#                  [56.67959056,57.80314077,57.73425793,56.45408162],
#                  [54.31462061,54.85530398,54.79896552,54.14518602]])

# After
# data = np.array([[74.17279291,75.82977917,73.98138391,72.87782795],
#                  [74.68774745,74.15612038,74.77905541,75.83736682],
#                  [72.50234151,71.77314231,75.15322789,71.25439513],
#                  [71.2170163,72.65242512,73.03358443,73.46790763]])

# Ansari
data = np.array([[71.46051656, 74.26105061, 73.9252881, 72.6539299],
                 [74.87693431, 76.99988492, 81.21668932, 74.83643309],
                 [73.49146051, 76.33109132, 75.50888518, 73.72534981],
                 [72.43574055, 74.44577961, 74.96136376, 73.09349395]])

# Medina
data = np.array([[82.22666513,83.2348262,80.54928209,79.02505285],
                 [71.44811443,77.11045082,79.92632215,76.10229766],
                 [67.64302987,91.63443259,68.65864728,63.06032544],
                 [57.82747665,57.91641538,59.45493854,69.50542373]])

labels = (
    np.asarray(["{0}\n({1:.2f})".format(text, data) for text, data in zip(text.flatten(), data.flatten())])).reshape(4,
                                                                                                                     4)

ax = sns.heatmap(data, vmin=45, vmax=95, annot=labels, linewidths=4, linecolor='black', square=True,
                 annot_kws={"size": 18, "weight": "bold"}, cmap='jet', fmt="",
                 cbar_kws=dict(ticks=np.arange(45, 100, 5).tolist()))

ax.tick_params(axis='both', which='both', length=0)
ax.xaxis.set_major_locator(ticker.MultipleLocator(base=20))
ax.yaxis.set_major_locator(ticker.MultipleLocator(base=10))
cbar = ax.collections[0].colorbar
# here set the labelsize by 20
cbar.ax.tick_params(labelsize=13)
ax.figure.axes[-1].xaxis.label.set_size(14)
ax.figure.axes[-1].xaxis.label.set_text("[°C]")

fig = ax.get_figure()
plt.show()
fig.savefig('test.svg')
