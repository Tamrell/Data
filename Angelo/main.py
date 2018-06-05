import pandas as pd

if __name__ == '__main__':
    d_file = "data/Meteorological Data.xlsx"
    d_xls = pd.read_excel(d_file, index_col=None)
    print(d_xls)
    # for i in d_xls:
    #     for j in d_xls[i]:
    #         if j:
    #             print(j)
    #d_xls.to_csv('Met_data.csv', encoding='utf-8')

    d2_file = "data/Sensor Data.xlsx"
    d2_xls = pd.read_excel(d2_file, index_col=None)
    d2_xls = d2_xls.sort_values(['Chemical'], )
    print(d2_xls)
