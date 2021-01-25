"""Unit test for the geo module."""

import floodsystem.geo

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from collections import defaultdict 