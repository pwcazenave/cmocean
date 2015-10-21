import cmocean
import matplotlib.pyplot as plt
import numpy as np

azimuths = np.arange(0, 360, 1)
zeniths = np.arange(40, 70, 1)
values = azimuths * ones((30, 361))
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
ax.pcolormesh(azimuths*pi/180.0, zeniths, values, cmap=cmocean.cm.phase)