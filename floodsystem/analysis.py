from matplotlib.dates import date2num
import numpy as np

def polyfit(dates, levels, p):
    """Returns a pth degree polynomial fit along with the origin offset for given dates and levels"""

    t0 = date2num(dates[-1])
    t = [date2num(i) - t0 for i in dates]

    p_coeff = np.polyfit(t, levels, p)

    return np.poly1d(p_coeff), t0

def relative_levels(levels, station):
    """Converts a list of level data to a list of relative level data for a given station"""

    if not station.typical_range_consistent():
        return None
    else:
        min, max = station.typical_range
        return [(i - min)/(max - min) for i in levels]