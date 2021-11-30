# myapp.py

from random import random
from os.path import dirname, join

from bokeh.layouts import column
from bokeh.models import Button, ColumnDataSource, CategoricalColorMapper, Select
from bokeh.palettes import RdYlBu3, d3
from bokeh.plotting import figure, curdoc

import pandas as pd

df = pd.read_csv(join(dirname(__file__), 'data', 'IRIS.csv'))

axis_options = list(df.columns)
axis_options.remove("species")

x_menu = Select(title='Feature 1', value=axis_options[0], options=axis_options)
y_menu = Select(title='Feature 2', value=axis_options[0], options=axis_options)
print(repr(x_menu))



species_types = df["species"].unique()
palette = d3['Category10'][len(species_types)]
color_map = CategoricalColorMapper(factors=species_types,palette=palette)
df['x'] = df[x_menu.value]
df['y'] = df[y_menu.value]
cds = ColumnDataSource(data=df)

p = figure(width=400, height=400)
p.circle(x='x', y='y',
    color={'field': 'species', 'transform': color_map},
    source=cds)
p.xaxis.axis_label = 'Feature 1'
p.yaxis.axis_label = 'Feature 2'

# Add callbacks
def my_text_input_handler(attr, old, new):
    df['x'] = df[x_menu.value]
    df['y'] = df[y_menu.value]
    cds.data = df

x_menu.on_change('value', my_text_input_handler)
y_menu.on_change('value', my_text_input_handler)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(x_menu, y_menu, p))
