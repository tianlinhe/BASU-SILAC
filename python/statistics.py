import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import nanmedian, NaN

def statistics(input,crapome,output):
    df = pd.read_csv(input)
    df.drop(['Median'], axis=1)
    df = df[pd.notnull(df['Gene Name'])]
    std = []
    median = []
    #print (len(df))
    for i in range (len(df)):
        
        ABC = np.array (df.iloc[i][4:7],dtype=float)
        std.append(np.nanstd(ABC))
        median.append(np.nanmedian(ABC))
        
    df['SD'] = std
    df['Median'] = median
    df.index = range(len(df))
    #print (df)
    #print (len(df))
    df_crap = pd.read_csv(crapome, sep="\t", header=None)
    df_crap.columns = df_crap.iloc[0]
    df_crap= df_crap.drop(df_crap.index[0])
    df_crap.index = range(len(df_crap)) 
    print (len(df_crap))
    #print (df_crap)
    #print (df_crap.loc[:,'Num of Expt. (found/total)'])
    
    
    df['Num of Expt. (found/total)']=df_crap.loc[:,'Num of Expt. (found/total)']
    #print (df)
    ratio = []
    for i in range (len(df)):
        
        if pd.isnull(df.iloc[i]['Num of Expt. (found/total)']) is False:
            
            event = df.iloc[i]['Num of Expt. (found/total)'].split(" ")[0]
            total = df.iloc[i]['Num of Expt. (found/total)'].split(" ")[2]
            percent = float(event)/float(total) 
            ratio.append(percent)
            
        else:
            ratio.append(NaN)
    
    df['Percentage of Expt. (found/total)'] = ratio
    df=df.sort_values(['Percentage of Expt. (found/total)'], ascending = False)
    print (df)
    
    df.to_csv(output)
    
#statistics("~/Documents/MS_rawdata/IFNAR1-5xlinker-BASU/csv/ABC_union.csv","~/Documents/MS_rawdata/IFNAR1-5xlinker-BASU/csv/ABC_crapome.txt","~/Documents/MS_rawdata/IFNAR1-5xlinker-BASU/csv/ABC_forscatter.csv")
#statistics("~/Documents/MS_rawdata/IFNAR1-5xlinker-BASU/csv/ABC_union.csv","~/Downloads/1534841272373_gp.txt","~/Documents/MS_rawdata/IFNAR1-5xlinker-BASU/csv/ABC3.csv")
