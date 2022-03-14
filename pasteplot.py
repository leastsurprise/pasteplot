#!/bin/python3

import sys, re, csv, plotille
import numpy as np

if __name__ == '__main__':

    d = """
x_tax_year,s_city,y_pcnt_red
2010,Auckland,55
2011,Auckland,59
2012,Auckland,64
2013,Auckland,67
2014,Auckland,70
2010,Christchurch,45
2011,Christchurch,48
2012,Christchurch,51
2013,Christchurch,54
2014,Christchurch,57
2010,Dunedin,35
2011,Dunedin,45
2012,Dunedin,55
2013,Dunedin,48
2014,Dunedin,33
2010,Hamilton,14
2011,Hamilton,11
2012,Hamilton,18
2013,Hamilton,27
2014,Hamilton,39
"""

    data = list(csv.reader(d.split('\n'), delimiter=','))
    data.pop(0) # remove leading newline

    column_names = data[0]
    x_axis_label = ''
    y_axis_label = ''
    series_label = ''
    x_axis_idx = 0
    y_axis_idx = 0
    series_idx = 0
    curr_idx = 0
    for cn in column_names:
        if cn.startswith('x_'):
            x_axis_label = cn
            x_axis_idx = curr_idx
        elif cn.startswith('y_'):
            y_axis_label = cn
            y_axis_idx = curr_idx
        elif cn.startswith('s_'):
            series_label = cn
            series_idx = curr_idx
        curr_idx += 1

    data.pop() # remove trailing newline

    # get a list of unique series names
    series_names = []
    for row in data:
        if row[series_idx] not in series_names and row[series_idx] != series_label:
            series_names.append(row[series_idx])
 
    # for each series member, get the x and y values
    series_data = {}
    for sn in series_names:
        series_data[sn] = []
        for row in data:
            if row[series_idx] == sn:
                series_data[sn].append((row[x_axis_idx], row[y_axis_idx]))
    
    # plot the data
    p = plotille.Plotille()
    p.set_option('label_font_size', '10')
    p.set_option('label_font_family', 'monospace')
    p.set_option('label_font_weight', 'bold')
    p.set_option('label_font_color', '#ffffff')

    
