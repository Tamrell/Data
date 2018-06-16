import pandas
from bokeh.io import output_file, show
from bokeh.layouts import column, widgetbox
from bokeh.plotting import figure
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider

SensorData = pandas.read_excel('../Final Data/Sensor Data.xlsx')

'''selected = pandas.Series(SD.loc[(SD['Monitor'] == 1) & (SD['Chemical'] == 'Methylosmolene') & (SD['Reading'] < 25)]['Reading']).values
'''
chemicals = ['Methylosmolene','Chlorodinine','AGOC-3A','Appluimonia']

output = {}
for sensor in range(1,10):
	output[sensor] = {}
	output_file('sensor%i'%sensor)
	for i in range(len(chemicals)):
		chemical = chemicals[i]
		reading = pandas.Series(SensorData.loc[(SensorData['Chemical'] == chemical) & (SensorData['Monitor'] == sensor)]['Reading']).values
		datetime = pandas.Series(SensorData.loc[(SensorData['Chemical'] == chemical) & (SensorData['Monitor'] == sensor)]['Timestamp']).values
		datetime = range(len(reading))
		output[sensor][i] = figure(plot_width=1000, plot_height=250, title='%s'%chemical,y_range=(0,5))
		output[sensor][i].line(datetime,reading)
	show(column([output[sensor][i] for i in output[sensor]]))

'''	
output_file("layout_widgets.html")

# create some widgets
slider = Slider(start=0, end=10, value=1, step=.1, title="Slider")
button_group = RadioButtonGroup(labels=["Option 1", "Option 2", "Option 3"], active=0)
select = Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])
button_1 = Button(label="Button 1")
button_2 = Button(label="Button 2")

# put the results in a row
show(widgetbox(button_1, slider, button_group, select, button_2, width=300))

import numpy as np
'''

from bokeh.layouts import row, widgetbox
from bokeh.models import CustomJS, Slider
from bokeh.plotting import figure, output_file, show, ColumnDataSource

reading = pandas.Series(SensorData.loc[(SensorData['Chemical'] == 'Methylosmolene') & (SensorData['Monitor'] == 1)]['Reading']).values
datetime = range(len(reading))

source = ColumnDataSource(data=dict(x=datetime, y=reading))

plot = figure(y_range=(-10, 10), plot_width=400, plot_height=400)

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

callback = CustomJS(args=dict(source=source), code="""
    var data = source.data;
    var A = amp.value;
    var k = freq.value;
    var phi = phase.value;
    var B = offset.value;
    var x = data['x']
    var y = data['y']
    for (var i = 0; i < x.length; i++) {
        y[i] = B + A*Math.sin(k*x[i]+phi);
    }
    source.change.emit();
""")

amp_slider = Slider(start=0.1, end=10, value=1, step=.1,
                    title="Amplitude", callback=callback)
callback.args["amp"] = amp_slider

freq_slider = Slider(start=0.1, end=10, value=1, step=.1,
                     title="Frequency", callback=callback)
callback.args["freq"] = freq_slider

phase_slider = Slider(start=0, end=6.4, value=0, step=.1,
                      title="Phase", callback=callback)
callback.args["phase"] = phase_slider

offset_slider = Slider(start=-5, end=5, value=0, step=.1,
                       title="Offset", callback=callback)
callback.args["offset"] = offset_slider

layout = row(
    plot,
    widgetbox(amp_slider, freq_slider, phase_slider, offset_slider),
)

output_file("slider.html", title="slider.py example")

show(layout)