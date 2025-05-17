a = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
#a=['aaa', 'bbb', 'ccc']
#a=['abc', 'abc', 'abc']
ans = {}

for el in a:
    if el in ans:
        ans[el] += 1
    else:
        ans[el] = 1
        
for el in ans.values():
    print(el)
