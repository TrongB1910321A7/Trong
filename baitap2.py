start ={'ATG'}
end={'TAA','TAG','TGA'}
like= {'AA', 'TT','CC','GG'}

# def check_gen(s):
    
#          if s[0:3] in start and s[-3:] in end and len(s) %2 == 0:
            
#              pria = []
b = []
table = []
# dauvao= input("Nhap chuoi dau vao: ")
n,m = list(map(int,input().split()))
def inputArgs():
    for i in range(0, n):
         a.append(i)
    for j in range(0,m):
            b.append(j)
    for i in range(0,n):
        table.append([])
        for j in b:
            table[i].append(j)
    print(n, m)  
    print(a)
    print(b)  
    print(table)      
def simulaDFA(dauvao):
    state= 0 
    print(state)
    for ch in dauvao:
        state = table[state][int(ch)]
        return nt("YES")
#          else:         
#                print("NO")    
    

# s= input()
print('ATGCCCTAG'.split("",3))
# check_gen(s) 

