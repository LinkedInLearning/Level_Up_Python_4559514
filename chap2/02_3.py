lst_01 = [0,0,0,1,2,3,1,2,4,5,6,7,8,8,8,2,9,3,4,5]
lst_02 = [10,10,11,11,12,13,11,12,14,15,16,17,18,18,19,18,12,13,14]

set_01 = set(lst_01)
print(lst_01)
print(set_01)

set_02 = set(lst_02)
print(lst_02)
print(set_02)

lst_03 = list(set_01.union(set_02))
print(lst_03)