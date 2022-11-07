import math
import re
from traceback import print_tb
with open ('test.txt', 'r') as f:
    data= f.readline()

    # x= re.findall(r'^t\w+', data)
   
    matches = re.match(r'[tc]',data)

    for i in f:
         matches = re.match(r'[tc]',i)
         if matches:
             print(matches.string)
         else:
            print("NO")