from matplotlib.dates import date2num
import numpy as np

def polyfit(dates, levels, p):
    t0 = date2num(dates[-1])
    t = [date2num(i) - t0 for i in dates]

    p_coeff = np.polyfit(t, levels, p)

    return np.poly1d(p_coeff), t0