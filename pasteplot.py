#!/usr/bin/python3
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
    data.pop(0) # remove first row

    # get a list of unique series names
    series_data = {}
    series_list = []
    for row in data:
        if row[series_idx] not in series_data.keys():
            current_series = row[series_idx]
            series_list.append(current_series)
            series_data[current_series] = {'x': [], 'y': []}
        series_data[current_series]['x'].append(int(row[x_axis_idx]))
        series_data[current_series]['y'].append(int(row[y_axis_idx]))

    fig = plotille.Figure()
    fig.width = 80
    fig.height = 30
    fig.set_x_limits(2010, 2014)
    fig.set_y_limits(0, 100)
    fig.color_mode = 'byte'

    for series in series_list: 
        fig.plot(series_data[series]['x'], series_data[series]['y'], label=series)

    print(fig.show(legend=True))

    
