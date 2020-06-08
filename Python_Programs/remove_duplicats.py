
# Script to remove Duplicates

a = [1,2,3,3,4,4,4,4,1,1,1,1,2,3,6,7,8,8,8,8,9,9]

def remove_dupicates(a):
    b = []
    if a:
        for i in a:
            if i not in b:
                b.append(i)
    else:
        return a
    return b

print(remove_dupicates(a))
