a = [2, 7, 9, 5, 8, 7, 4]
k = 6
p = []
for i in range(0,len(a)-k+1):
    c = 0
    for j in range(i,i+k):
        print(a[j])
        # if a[j]>k:
        #     c+=1
        #     p.append(c)
# print(p)