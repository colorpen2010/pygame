opener=open('save.txt','w')
print('lol',file=opener)
opener.close()


import os
if os.path.exists('save.txt'):
    pop=open('save.txt','r')
    awa=pop.read()
    print(awa)