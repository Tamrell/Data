import sys
import pandas as pd
import Angelo.EDA_wc as wc


if __name__ == '__main__':

    # Check command line argument validity. #### May change in the future. ####
    if len(sys.argv) != 3:
        print('Usage: python main.py [mode] [specification]')
        exit(1)

    # Create a complete dataframe of all data.
    df_m = pd.read_excel("Final Data/Meteorological Interpolated.xlsx",
                          index_col='Timestamp')
    df_s = pd.read_excel("Final Data/Sensor Data.xlsx", index_col='Timestamp')
    df = pd.concat([df_m, df_s], sort=True)

    # Run option #### Function for the command line args needed! ####
    if sys.argv[1] == '-e':
        print('Exploratory Data Analysis')
        if sys.argv[2] == '-wc':
            print('Wind direction versus chemical readings.')
            wc.correlation(df)
