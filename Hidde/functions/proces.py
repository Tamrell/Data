from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label

output_file("foo.html")

p = figure(x_range=(0,500), y_range=(0,500))

p.image_url( url=[ "download.jpeg"],
             x=1, y=1, w=500, h=500, anchor="bottom_left")

factories = {
	"RFE": [89,27],
	"KOF": [90,21],
	"RCT": [109,26],
	"ISB": [120,22]
}

sensors = {
	"Sensor1": [62,21],
	"Sensor2": [66,35],
	"Sensor3": [76,41],
	"Sensor4": [88,45],
	"Sensor5": [103,43],
	"Sensor6": [102,22],
	"Sensor7": [89,3],
	"Sensor8": [74,7],
	"Sensor9": [119,42]
}

from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label

output_file("map.html", title="map.py example")

source = ColumnDataSource(data=dict(height=[89, 90, 109, 120],
                                    weight=[27, 21, 26, 22],
                                    names=['RFE', 'KOF', 'RCT', 'ISB']))

source2 = ColumnDataSource(data=dict(height=[61,66,76,88,103,102,89,74,119],
                                    weight=[21,35,41,45,43,22,3,7,42],
                                    names=['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5','sensor6','sensor7','sensor8','sensor9']))


p = figure(title='Map', x_range=(55,130), background_fill_color='#9ecae1')

p.square(x='height', y='weight', size=10, source=source, color='red')
p.scatter(x='height', y='weight', size=8, source=source2, color='black')

labels = LabelSet(x='height', y='weight', text='names', level='glyph',
              x_offset=5, y_offset=5, source=source, render_mode='canvas')

labels2 = LabelSet(x='height', y='weight', text='names', level='glyph',
              x_offset=5, y_offset=5, source=source2, render_mode='canvas')



p.add_layout(labels)
p.add_layout(labels2)


show(p)
