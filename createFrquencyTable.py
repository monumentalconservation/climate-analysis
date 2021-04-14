from base import *

CSVFilename = 'measured-climate-data/measured-with-observed-only.csv' ### <<<<< Change this file when needed
data = pd.read_csv(CSVFilename, index_col=False)
df = data[['date','PET','amount']]
# split data into quantiles
df['quantile'] = pd.qcut(df['PET'],q=10,precision=0)
# label the quantiles with integers
df['quantile_no'] = pd.qcut(df["PET"],q=10,labels=False,precision=0)


# building a reference table for the bins
bin_labels_5 = ['0','1','2','3','4','5','6','7','8','9']
results, bin_edges = pd.qcut(df["PET"],q=10,labels=False,precision=0,retbins=True)
results_table = pd.DataFrame(zip(bin_edges, bin_labels_5),
                            columns=['Threshold', 'Tier'])
results_table.to_csv('for-modeling/bin-threshold.csv')

df1 = df.loc[df['amount'] == 1.0]
df2 = df.loc[df['amount'] == 2.0]
df3 = df.loc[df['amount'] == 3.0]
df4 = df.loc[df['amount'] == 4.0]
df5 = df.loc[df['amount'] == 5.0]


df11 = len(df1[df1['quantile_no'] == 0])
df12 = len(df1[df1['quantile_no'] == 1])
df13 = len(df1[df1['quantile_no'] == 2])
df14 = len(df1[df1['quantile_no'] == 3])
df15 = len(df1[df1['quantile_no'] == 4])
df16 = len(df1[df1['quantile_no'] == 5])
df17 = len(df1[df1['quantile_no'] == 6])
df18 = len(df1[df1['quantile_no'] == 7])
df19 = len(df1[df1['quantile_no'] == 8])
df10 = len(df1[df1['quantile_no'] == 9])
df1_list = [df11,df12,df13,df14,df15,df16,df17,df18,df19,df10]

df21 = len(df2[df2['quantile_no'] == 0])
df22 = len(df2[df2['quantile_no'] == 1])
df23 = len(df2[df2['quantile_no'] == 2])
df24 = len(df2[df2['quantile_no'] == 3])
df25 = len(df2[df2['quantile_no'] == 4])
df26 = len(df2[df2['quantile_no'] == 5])
df27 = len(df2[df2['quantile_no'] == 6])
df28 = len(df2[df2['quantile_no'] == 7])
df29 = len(df2[df2['quantile_no'] == 8])
df20 = len(df2[df2['quantile_no'] == 9])
df2_list = [df21,df22,df23,df24,df25,df26,df27,df28,df29,df20]


df31 = len(df3[df3['quantile_no'] == 0])
df32 = len(df3[df3['quantile_no'] == 1])
df33 = len(df3[df3['quantile_no'] == 2])
df34 = len(df3[df3['quantile_no'] == 3])
df35 = len(df3[df3['quantile_no'] == 4])
df36 = len(df3[df3['quantile_no'] == 5])
df37 = len(df3[df3['quantile_no'] == 6])
df38 = len(df3[df3['quantile_no'] == 7])
df39 = len(df3[df3['quantile_no'] == 8])
df30 = len(df3[df3['quantile_no'] == 9])
df3_list = [df31,df32,df33,df34,df35,df36,df37,df38,df39,df30]

df41 = len(df4[df4['quantile_no'] == 0])
df42 = len(df4[df4['quantile_no'] == 1])
df43 = len(df4[df4['quantile_no'] == 2])
df44 = len(df4[df4['quantile_no'] == 3])
df45 = len(df4[df4['quantile_no'] == 4])
df46 = len(df4[df4['quantile_no'] == 5])
df47 = len(df4[df4['quantile_no'] == 6])
df48 = len(df4[df4['quantile_no'] == 7])
df49 = len(df4[df4['quantile_no'] == 8])
df40 = len(df4[df4['quantile_no'] == 9])
df4_list = [df41,df42,df43,df44,df45,df46,df47,df48,df49,df40]

df51 = len(df5[df5['quantile_no'] == 0])
df52 = len(df5[df5['quantile_no'] == 1])
df53 = len(df5[df5['quantile_no'] == 2])
df54 = len(df5[df5['quantile_no'] == 3])
df55 = len(df5[df5['quantile_no'] == 4])
df56 = len(df5[df5['quantile_no'] == 5])
df57 = len(df5[df5['quantile_no'] == 6])
df58 = len(df5[df5['quantile_no'] == 7])
df59 = len(df5[df5['quantile_no'] == 8])
df50 = len(df5[df5['quantile_no'] == 9])
df5_list = [df51,df52,df53,df54,df55,df56,df57,df58,df59,df50]

data = { '1': df1_list, '2': df2_list, '3': df3_list, '4': df4_list, '5': df5_list}
ndf = pd.DataFrame(data=data)

ndf = ndf.transpose()
ndf.to_csv('for-modeling/freqency.csv')



ndf['0rf'] = ndf.apply(lambda row: row[0]/(ndf[0].sum()), axis = 1) 
ndf['1rf'] = ndf.apply(lambda row: row[1]/(ndf[1].sum()), axis = 1) 
ndf['2rf'] = ndf.apply(lambda row: row[2]/(ndf[2].sum()), axis = 1) 
ndf['3rf'] = ndf.apply(lambda row: row[3]/(ndf[3].sum()), axis = 1) 
ndf['4rf'] = ndf.apply(lambda row: row[4]/(ndf[4].sum()), axis = 1) 
ndf['5rf'] = ndf.apply(lambda row: row[5]/(ndf[5].sum()), axis = 1) 
ndf['6rf'] = ndf.apply(lambda row: row[6]/(ndf[6].sum()), axis = 1) 
ndf['7rf'] = ndf.apply(lambda row: row[7]/(ndf[7].sum()), axis = 1) 
ndf['8rf'] = ndf.apply(lambda row: row[8]/(ndf[8].sum()), axis = 1) 
ndf['9rf'] = ndf.apply(lambda row: row[9]/(ndf[9].sum()), axis = 1) 

relFre = ndf[['0rf','1rf','2rf','3rf','4rf','5rf','6rf','7rf','8rf','9rf']].copy()
relFre.to_csv('for-modeling/relative-freqency.csv')

cum = relFre.cumsum()
cum.columns = ['0','1','2','3','4','5','6','7','8','9']
cum.to_csv('for-modeling/cumulative-freqency.csv')



  
