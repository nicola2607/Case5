import pandas as pd
from scipy.stats import shapiro, mannwhitneyu
import numpy as np

def main():
    path = '/Users/nicolaschreyer/Desktop/WS 21:22/VU Betriebliche Informationssysteme/Case 5/unbearbeitet_StudentData_FlyUIBK.csv'
    dframe = pd.read_csv(path, sep=';')
    indexNames = dframe[dframe['Actual arrival time'] == 'Cancelled'].index
    dframe.drop(indexNames, inplace=True)
    dframe = dframe.astype({"Arrival delay in minutes": 'int64'})
    dframe1 = dframe.loc[(dframe['Airline'] == 'FlyUIBK') & (dframe['Arrival delay in minutes'] > 0)].copy()
    dframe2 = dframe.loc[(dframe['Airline'] == 'LDA') & (dframe['Arrival delay in minutes'] > 0)].copy()
    dframe1['log'] = np.log(dframe1['Arrival delay in minutes'])
    dframe2['log'] = np.log(dframe2['Arrival delay in minutes'])
    FlyUIBK_shapiro_wilk_test = shapiro(dframe1['log'])
    LDA_shapiro_wilk_test = shapiro(dframe2['log'])
    print('FlyUIBK data:', FlyUIBK_shapiro_wilk_test)
    print('LDA data:', LDA_shapiro_wilk_test)
    wilcoxon = mannwhitneyu(dframe2['Arrival delay in minutes'], dframe1['Arrival delay in minutes'], alternative='less')
    print(wilcoxon)
    return

if __name__ == '__main__':
    main()


