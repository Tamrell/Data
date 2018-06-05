import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource


if __name__ == '__main__':
    # d_file = "data/Meteorological Data.xlsx"
    # d_xls = pd.read_excel(d_file, index_col=None)
    # print(d_xls)

    d2_file = "data/Sensor Data.xlsx"
    d2_xls = pd.read_excel(d2_file, index_col=None)
    d2_xls = d2_xls.sort_values(['Chemical', 'Date Time ', 'Monitor'])
    print(d2_xls)

    data = {'x_values': [1, 2, 3, 4, 5],
            'y_values': [6, 7, 2, 3, 6]}

    source = ColumnDataSource(d2_xls)
    p = figure()
    p.circle(x='Sensor', y='Chemical', source=d2_xls)
    show(p)
