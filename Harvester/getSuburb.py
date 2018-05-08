#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import csv
import fiona
from shapely.geometry import Point, shape

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SA2_SHP = DIR_PATH + '/sa2/SA2_2016_AUST.shp'

class CoordinateToSA2():
    def __init__(self):
        self.suburbs = self.readShpInfo()

    def readShpInfo(self):
        suburbs = []
        with fiona.open(SA2_SHP) as source:
            for suburb in source:
                if suburb['geometry'] and suburb['properties']['STE_NAME16'] == 'Victoria':
                    suburbs.append(suburb)

            return suburbs

    def sa2_maincode(self, coordinates):
        point = Point(tuple(coordinates))
        for suburb in self.suburbs:
            if point.within(shape(suburb['geometry'])):
                sa2_maincode = suburb['properties']['SA2_MAIN16']
                sa2_name = suburb['properties']['SA2_NAME16']

                return sa2_maincode, sa2_name

        return None
