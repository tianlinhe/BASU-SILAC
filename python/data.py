import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
def f(value):
    return((-1)*math.log(value,2))

def data(input):
    # open the excelfile
    xlsx = pd.ExcelFile(input)
# get the first sheet=master proteins in beads A as an object
    masterproteinsA = xlsx.parse(0)
# only the rows with defined values of Abundance Ratio: (Heavy) / (Light) are kept
    df_A = masterproteinsA[pd.notnull(masterproteinsA['Abundance Ratio: (Heavy) / (Light)'])]
#It keeps master proteins only
    df_A = df_A[df_A.Master == 'Master Protein']
    df_A=df_A.sort_values(['Abundance Ratio: (Heavy) / (Light)'], ascending = False)
    df_A.index = range(len(df_A))
    print (len(df_A))
    
    
    masterproteinsB = xlsx.parse(1)
    df_B = masterproteinsB[pd.notnull(masterproteinsB['Abundance Ratio: (Heavy) / (Light)'])]
    df_B = df_B[df_B.Master == 'Master Protein']
    df_B=df_B.sort_values(['Abundance Ratio: (Heavy) / (Light)'], ascending = False)
    df_B.index = range(len(df_B))  
    print (len(df_B))
    
    masterproteinsC = xlsx.parse(2)
    df_C = masterproteinsC[pd.notnull(masterproteinsC['Abundance Ratio: (Heavy) / (Light)'])]
    df_C = df_C[df_C.Master == 'Master Protein']
    df_C=df_C.sort_values(['Abundance Ratio: (Heavy) / (Light)'], ascending = False)
    df_C.index = range(len(df_C))
    print (len(df_C))
    
    
#compare A and B
    AB_list = [] 
    z1=0
    for x in range (len(df_A)):
        for y in range (len(df_B)):
            if df_B.loc[:,'Accession'][y] == df_A.loc[:, 'Accession'][x]:
                AB_list.append (df_A.loc[:,'Accession'][x])
                z1 += 1
                break   
#compare B and C
    BC_list = [] 
    z2=0
    for x in range (len(df_B)):
        for y in range (len(df_C)):
            if df_B.loc[:,'Accession'][x] == df_C.loc[:, 'Accession'][y]:
                BC_list.append (df_B.loc[:,'Accession'][x])
                z2 += 1
                break  
                
#compare A and C
    AC_list = [] 
    z3=0
    for x in range (len(df_A)):
        for y in range (len(df_C)):
            if df_A.loc[:,'Accession'][x] == df_C.loc[:, 'Accession'][y]:
                AC_list.append (df_A.loc[:,'Accession'][x])
                z3 += 1
                break                
    
    
    
    ABC_union=list(set().union(AB_list,BC_list,AC_list))
    print (len(ABC_union))
    print (ABC_union)
    
#Match A with ABC union
    for item in ABC_union:
        
#the region of A U B U C
    p = 0
    ABC_list = []
    for item in AB_list:
        for t in range (len(df_C)):
            if item == df_C.loc[:,'Accession'][t]:
                p += 1
                ABC_list.append (item)
                break
    print (p)
                
                
                
    
          
data("~/Documents/MS_rawdata/IFNAR1-5xlinker-BASU/20180821.xlsx")
