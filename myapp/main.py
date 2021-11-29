# myapp.py

from random import random

from bokeh.layouts import column
from bokeh.models import Button, ColumnDataSource, CategoricalColorMapper, Dropdown
from bokeh.palettes import RdYlBu3, d3
from bokeh.plotting import figure, curdoc

import pandas as pd

df = pd.read_csv("IRIS.csv")
print(df.head())

axis_options = list(df.columns)
axis_options.remove("species")

x_menu = Dropdown(label="Dropdown button", button_type="warning", menu=axis_options)
y_menu = Dropdown(label="Dropdown button", button_type="warning", menu=axis_options)

cds = ColumnDataSource(data=df)

species_types = df["species"].unique()
palette = d3['Category10'][len(species_types)]
color_map = CategoricalColorMapper(factors=species_types,palette=palette)

p = figure(width=400, height=400)
p.circle(x='sepal_length', y='sepal_width',
    color={'field': 'species', 'transform': color_map},
    source=cds)
p.xaxis.axis_label = 'attr 1'
p.yaxis.axis_label = 'attr 2'

# put the button and plot in a layout and add to the document
curdoc().add_root(column(x_menu, y_menu, p))
