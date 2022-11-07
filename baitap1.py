n,m = list(map(int,input("Nhập vào chuoi: ").split()))
a = []
b=[]
f=[]
table = []
for i in range(0, m):
    a.append([])
    for j in range(0, n):
        a.append(j)     
for k in range(0, n):  
    x = float(input("Nhap vao cac trang thai n: "))
    table.append(k)
for d in range(0, m):  
    y = float(input("Nhap vao cac ky tu m: "))
    b.append(y)
for e in range(0, n):  
    y = float(input("Nhap vao cac trang thai F: "))
    f.append(y)    
    # for j in b:
    #     table[i].append(j)
    for i in range(0, m):
  
        for j in range(0, n):
             
            x = float(input("Nhap phan tu thu a[%2d][%2d]: " % (i+1, j+1)))
            a[i].append(x)

print(n,m)
print(b)
print(table)
print(f)
print(a)
   
