# Pre-processing by Angelo Groot
For each of the 4 categories of pre-processing is a seperate .py file:
- cleaning.py
- integration.py
- transformation.py
- reduction.py

these can all be ran by typing into the terminal:
`python main.py`


## notes
- manual linear regression on points where 300+ -> 100-?
- Cubic spline seems to be unable to fill the last 2 entries.
- The period from 2016-4-30:22:00 to 2016-08-04-17:00 has been neglected in the interpolation because of unavailable data.
- apparantly, there are hours missing in the readings


### Invested time in the project

n'th of June | what?
--- | ---   
3-10 | Data exploration for cleaning.etc
11 | tried to improve upon the data set format
12 | temporarily gave up improving the data set, started trying to interpolate wind direction linearly
13 | got the idea to interpolate wind direction according to its independent vectors, finished interpolation methods for Cubic rom-spline and linear interpolation
14 | bugfixing
15 | bugfixing
16 | more bugfixing
17 | Fixed "bugs" in interpolation methods, created a program that makes plots of all the combinations of sensors with their readings during wind speeds. also plotted all chems to the wind speed.
18 | Worked on scatterplots for chemical abundancy, tried to use bokeh with markdown pages
19 | Made cumulative abundancy plots for the chemicals at each sensor
20 | Updated the final data
21 | Worked on the report and plots
22 | Worked on the report
23 | --
24 | made different correction functions for sensor 4
25 | explored github pages and possibilities therein
26 | worked on the report, exploring different visualisations for data
27 |
