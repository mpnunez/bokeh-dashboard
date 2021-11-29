# myapp.py

from random import random

from bokeh.layouts import column
from bokeh.models import Button, ColumnDataSource, CategoricalColorMapper
from bokeh.palettes import RdYlBu3, d3
from bokeh.plotting import figure, curdoc

import pandas as pd

df = pd.read_csv("IRIS.csv")
print(df.head())

species_types = df["species"].unique()

cds = ColumnDataSource(data=df)

palette = d3['Category10'][len(species_types)]
color_map = CategoricalColorMapper(factors=species_types,palette=palette)

p = figure(width=400, height=400)
p.circle(x='sepal_length', y='sepal_width',
    color={'field': 'species', 'transform': color_map},
    source=cds)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(p))
