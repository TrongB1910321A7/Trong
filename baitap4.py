import json
with open ('namefile.json','r') as f:
    data= json.load(f)
    delta= data["delta"]
    status= data["Q"]
    start= data["q0"]
    sigma= data["sigma"]
    f= data["f"]
    a= []
    n = int (input())
    for i in range(n):
        i = input("Nhap so phan tu i: ")
        a.append(i)
      
def process( st,i, current):
        if i == len(st):
        
            if current in f:
                return True
            else:
                return False
        else:
             ch =st[i]
             if ch in delta[current]:
                for status in delta[current][ch]:
                    r= process(st,i+1, status)
                    if(r):
                       
                        return True
             else:
                    return False            
def checksigma(st):
    for i in st:
        if i not in sigma:
            return False
    return True 



for st in a:
    if checksigma(st):
        if process(st,0,start):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")                      