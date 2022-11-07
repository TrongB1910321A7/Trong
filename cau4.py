import re
with open('test.txt','r') as f:
   for i in f:
        if i.find('regular')>0:
            print(i, end='')
