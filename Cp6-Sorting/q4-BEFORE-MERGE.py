# Question : Merge two sorted arrays


n_arr = [
    int(item)
    for item in input('Enter comma separated sorted values : ').split(',')
    if item.strip() != ''
]

m_arr = [
    int(item)
    for item in input('Enter comma separated sorted values : ').split(',')
    if item.strip() != ''
]

i = j = 0
n,m=len(n_arr),len(m_arr)
res=[]
while i<n and j<m:
    if n_arr[i] <= m_arr[j]:
        res.append(n_arr[i])
        i+=1
    else:    
        res.append(m_arr[j])
        j+=1
if j<m:
    for _j in range(j,m):
        res.append(m_arr[_j])
        
if i<n:
    for _i in range(i,n):
        res.append(n_arr[_i])    

print(res)
