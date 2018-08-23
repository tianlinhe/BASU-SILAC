# Import the library
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles
#from matplotlib_venn import venn2


plt.figure(figsize=(10,10))
# Make the diagram

s=(190-148-110+99, 214-148-117+99, 148-99, 150-110-117+99,110-99,117-99,99)
v=venn3(subsets = s,set_labels=('A',"B","C"))


v.get_patch_by_id('001').set_color('silver')
v.get_patch_by_id('011').set_color('plum')
v.get_patch_by_id('101').set_color('gold')
v.get_patch_by_id('111').set_color('yellowgreen')
c = venn3_circles(subsets=s, linestyle='solid',color ='white')
#c[0].set_ls('dotted')  # Line style
#c[1].set_ls('dashed')
#c[2].set_lw(1.0) 

plt.savefig('20180817venn.eps', format='eps', dpi=1000)
#v.get_patch_by_id('100').set_alpha(1.0)
#v.get_patch_by_id('100').set_color('white')
plt.show()
