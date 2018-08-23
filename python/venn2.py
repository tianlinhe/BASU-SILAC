from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn2_circles

plt.figure(figsize=(10,10))
# Subset sizes
s = (177-121,384-121,121)
 

v = venn2(subsets=s, set_labels=('IFNAR1-5xlinker-BASU', 'IFNAR1-1xlinker-BioID2'))


# Subset colors
v.get_patch_by_id('10').set_color('plum')
v.get_patch_by_id('01').set_color('yellowgreen')
v.get_patch_by_id('11').set_color('gold')

# Subset alphas
v.get_patch_by_id('10').set_alpha(0.4)
v.get_patch_by_id('01').set_alpha(1.0)
v.get_patch_by_id('11').set_alpha(0.7)

c = venn2_circles(subsets=s, linestyle='solid',color ='white')
# Border styles
#c = venn2_circles(subsets=s, linestyle='solid')
#c[0].set_ls('dashed')  # Line style
#c[0].set_lw(2.0)       # Line width
plt.savefig('BioID2_vs_BASU', format='eps', dpi=1000)

plt.show()
