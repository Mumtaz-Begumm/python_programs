d={0:[1,4],1:[0,2,3],2:[1,3],3:[1,2],4:[0,3],5:[1]}
def dfs(start,vis):
    vis.add(start)
    for i in d[start]:
        if i not in vis:
            dfs(i,vis)
print(dfs(0,{}))




q=[source]
vis={source}
while q:
    a=q.pop(0)
    if a==destination:
        return True
    for i in d[a]:
        if i not in vis:
            q.append(i)
            vis.add(i)  