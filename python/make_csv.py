ABC_union = ['P62241', 'P15880', 'P30041', 'Q9UQ35', 'P46087-4', 'P22102', 'Q1ED39', 'P61254', 'F8W727', 'Q15365', 'P17066', 'P61978-2', 'P11142', 'P36873-2', 'Q00839', 'P78527', 'P62424', 'Q14684', 'K7ES00', 'Q9NX58', 'Q9P2D1', 'P49207', 'P25705', 'O00567', 'P62913', 'P62249', 'P51991', 'P07437', 'Q9H0C2', 'Q9NR30', 'P36578', 'O43684', 'P13639', 'Q08211', 'P07737', 'J3KTA4', 'Q9BU76', 'O60832', 'B4DR61', 'P17987', 'Q13085-4', 'G8JLB6', 'Q6P2Q9', 'P22626', 'P60842', 'P11908-2', 'J3QQ67', 'P42766', 'P18754-2', 'O75643', 'P18077', 'Q15361', 'Q9NWT8', 'Q96GA3', 'P27708', 'U3KQK0', 'P40394-2', 'P16615', 'Q9NY93', 'Q969Q0', 'P07305', 'P11498', 'Q9H583', 'A0A0A6YYL6', 'P05165', 'Q9UNX4', 'Q8N5F7', 'P11387', 'Q13428-4', 'Q00325', 'Q9GZR7', 'P16402', 'Q14004', 'O43143', 'Q9BVP2', 'P50914', 'Q15366-2', 'P68363', 'Q8WWQ0', 'Q06830', 'P68371', 'Q8TA86', 'H3BN98', 'P61247', 'Q5T3I0-3', 'P62854', 'F5H2F4', 'P62829', 'P62753', 'Q14692', 'P62280', 'P61313', 'P62263', 'P62917', 'H3BLZ8', 'P62979', 'Q96RQ3', 'P17181', 'P50991', 'P08238', 'P68104', 'O15371', 'P07195', 'P23396', 'Q9NVP1', 'P18124', 'J3KQE5', 'A0A087WXF8', 'P35268', 'Q8NE71', 'Q14498', 'P47914', 'A0A0U1RQC9', 'P55060', 'Q9BQG0-2', 'P53396', 'Q9BRT6', 'P30050', 'P06733', 'Q9Y3U8', 'P62805', 'O43175', 'P49327', 'Q8IY81', 'H7C2Q8', 'P84098', 'Q8WY36', 'P09874', 'P46776', 'P04264', 'P23526', 'O95478', 'Q9BZE4', 'Q02878', 'P62266', 'Q9NWB6', 'A0A0U1RRH7', 'P46781', 'O75683', 'O75367', 'Q9P0M6', 'P49411', 'E9PR30', 'P00338-3', 'P46013', 'Q9UIF9', 'O14617-5', 'O76021', 'Q9Y2X3', 'Q02543', 'P42677', 'H0YKD8', 'K7ELC7', 'F8W7C6', 'Q96GQ7', 'Q9H0A0', 'A8MUS3', 'Q13838-2', 'P45880-1', 'P26358-2', 'P26373', 'Q6PCB5', 'P26641-2', 'P39023', 'P14618', 'Q8WTT2', 'Q9UQ80', 'Q15233', 'P26640', 'P18583-9', 'H7C2I1', 'Q9P031', 'Q7Z6E9', 'P63244', 'P83731', 'Q99832', 'Q5JTH9']
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

column = ['Protein','Description','H/L in A','H/L in B','H/L in C','Mean H/L']
df = pd.DataFrame(index=range(len(ABC_union)),columns=column)
df['Protein'] = ABC_union
#print (df)

def f(value):
    return((-1)*math.log(value,2))
def make_csv(input):
    xlsx = pd.ExcelFile(input)
# get the first sheet=master proteins in beads A as an object
    masterproteinsA = xlsx.parse(0)
# only the rows with defined values of Abundance Ratio: (Heavy) / (Light) are kept
    df_A = masterproteinsA[pd.notnull(masterproteinsA['Abundance Ratio: (Heavy) / (Light)'])]
#It keeps master proteins only
    df_A = df_A[df_A.Master == 'Master Protein']
    df_A=df_A.sort_values(['Abundance Ratio: (Heavy) / (Light)'], ascending = False)
    df_A.index = range(len(df_A))
    
    masterproteinsB = xlsx.parse(1)
    df_B = masterproteinsB[pd.notnull(masterproteinsB['Abundance Ratio: (Heavy) / (Light)'])]
    df_B = df_B[df_B.Master == 'Master Protein']
    df_B=df_B.sort_values(['Abundance Ratio: (Heavy) / (Light)'], ascending = False)
    df_B.index = range(len(df_B))  
    
    masterproteinsC = xlsx.parse(2)
    df_C = masterproteinsC[pd.notnull(masterproteinsC['Abundance Ratio: (Heavy) / (Light)'])]
    df_C = df_C[df_C.Master == 'Master Protein']
    df_C=df_C.sort_values(['Abundance Ratio: (Heavy) / (Light)'], ascending = False)
    df_C.index = range(len(df_C))
    
    for x in range (len(df)):
        for y in range (len(df_A)):
            if df.loc[:,'Protein'][x] == df_A.loc[:,'Accession'][y]:
                df.iloc[x]['Description'] = df_A.loc[y]['Description']
                df.iloc[x]['H/L in A'] = df_A.loc[y]['Abundance Ratio: (Heavy) / (Light)']
                break
    for x in range (len(df)):
        for y in range (len(df_B)):
            if df.loc[:,'Protein'][x] == df_B.loc[:,'Accession'][y]:
                df.iloc[x]['Description'] = df_B.loc[y]['Description']
                df.iloc[x]['H/L in B'] = df_B.loc[y]['Abundance Ratio: (Heavy) / (Light)']
    for x in range (len(df)):
        for y in range (len(df_C)):
            if df.loc[:,'Protein'][x] == df_C.loc[:,'Accession'][y]:
                df.iloc[x]['Description'] = df_C.loc[y]['Description']
                df.iloc[x]['H/L in C'] = df_C.loc[y]['Abundance Ratio: (Heavy) / (Light)']
                break
    for x in range (len(df)):
        description = df.iloc[x]['Description'].split(" ")
        for item in description:
            if item[0:2] == 'GN':
                df.iloc[x]['Gene Name'] = item[3:]
                break
    
    print (df)
make_csv("~/Documents/MS_rawdata/IFNAR1-5xlinker-BASU/20180821.xlsx")
