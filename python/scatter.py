import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
def f(value):
    return(math.log(value,2))

def one_d_dot(input):
    df = pd.read_csv(input)
    
    df=df.sort_values(['Median'], ascending = False)
    foldchange = np.array(df.loc[:,'Median'])
    f1 = np.vectorize(f, otypes=[np.float])
    x = f1(foldchange)
    df['LOG2 (H/L)']=x
    df.index = range(len(df))

#value of p makes it a sigmoidal shape. 
    p = np.linspace(1,0,len(x))         
    plt.figure(figsize=(10,10))
#plot the dots with 8 colors   
    fh, ax = plt.subplots(1,1)
    colors = ['grey','firebrick']
    ax.grid(color='grey', linestyle='dotted', linewidth=1)

    for row_num in range(len(foldchange)):
        ax.scatter(df.loc[:,'LOG2 (H/L)'][row_num],p[row_num],facecolors='none', edgecolors='grey')
        print (df.loc[:,'LOG2 (H/L)'][row_num])
        print (p[row_num])
    #print (df)
     
 #add annotations for proteins in dic(indicators)       
    indicators = {'P50747':'Biotin ligase','H7C2I1':'PRMT1','P17181':'IFNAR1','P42224':'STAT1','P09914':"IFIT1","P19525":"EIF2AK2","Q9UII4":"HERC5","P63244":"RACK1"}
    for item in indicators:
        for row_num in range(len(foldchange)):
            if item == df.loc[:,'Protein'][row_num]:
                #ax.annotate(indicators[item],(df.loc[:,'LOG2 (H/L)'][row_num],p[row_num]),arrowprops=dict(facecolor='black', shrink=0.05))
                ax.annotate(indicators[item],(df.loc[:,'LOG2 (H/L)'][row_num],p[row_num]))
                
                ax.scatter(df.loc[:,'LOG2 (H/L)'][row_num],p[row_num],facecolors='none', edgecolors='red')
                break
                               
    #ax.axes.get_yaxis().set_visible(False)
    plt.ylabel('Fraction')
    plt.xlabel('LOG2 (H/L)')
    plt.savefig('BASU_scatter.eps', format='eps', dpi=1000)
    plt.show()
    
      
one_d_dot("~/Documents/MS_rawdata/IFNAR1-5xlinker-BASU/csv/ABC_forscatter.csv")
