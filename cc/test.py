__author__ = 'mcpherro'

from django.shortcuts import render
import os
import csv
from CC_DB.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.gis.geos import fromstr
from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos import LineString
from django.contrib.gis.geos import Point

with open('D:\\Users\\mcpherro\\PycharmProjects\\CC\\small_finds.csv', 'rb') as f:
    reader = csv.reader(f)
    n = 0
    for row in reader:
        n += 1
        if n > 1:
            for n in range(1,len(row)):
                print row[n]
                if int(row[n])==-1:
                    row[n] = None
                    print "shannon"
