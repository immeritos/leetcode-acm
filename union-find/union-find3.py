num = int(input())

arr = [input().split() for _ in range(num)]

phone_to_id = {}

for i in range(num):
    if phone in phone_to_id:
        phone_to_id[phone].append(i)
    else:
        phone_to_id[phone] = [i]
        
fa = [i for i in range(num)]

def find(x):
    if x != fa[x]:
        fa[x] = find(fa[x])
    return fa[x]

def merge(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        fa[x] = y
        
def same(x, y):
    return find(x) == find(y)

for phone in phone_to_id:
    first_id = phone_to_id[phone][0]
    for i in range(1, len(phone_to_id[phone])):
        merge(first_id, phone_to_id[phone][i])
        
root_to_name = {}
root_to_phones = {}

for i in range(num):
    root = find(i)
    
    if root in root_to_name:
        if arr[i][0] <= root_to_name[root]:
            root_to_name[root] = arr[i][0]
    else:
        root_to_name[root] = arr[i][0]

for phone in arr[i][1:]:
    if root in root_to_phones:
        root_to_phones[root].add(phone)
    else:
        root_to_phones[root] = {phone}
        
res = []

for root in root_to_name:
    res.append([root_to_name[root]] + sorted(list(root_to_phones[root])))
    
res.sort()

for x in res:
    print(' '.join(x))