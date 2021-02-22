# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""
def do_nothing(x):
    """Returns input"""
    return x

def sorted_by_key(x, i, reverse=False, f=do_nothing):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """
    # Sort by distance
    def key(element):
        return f(element[i])

    return sorted(x, key=key, reverse=reverse)
