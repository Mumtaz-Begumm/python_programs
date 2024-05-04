d={0:{1,4},1:{2,3},3:{2,4},4:{},5:{0}}
source=1
q=[source]
vis={source}
while q:
    a=q.pop(0)
    for i in d[a]:
        if i not in vis:
            q.append(i)
            vis.add(i) 
    for i in vis:
        if vis{0}==vis{-1}:
            print(True)
        else:
            print(False) 
