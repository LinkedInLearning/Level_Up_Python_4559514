#リスト内のリストをディープコピーする

lst_a1 = [100,102]
lst_b1 = [110,240]
lst_a = [lst_a1,lst_b1]
print(lst_a)
lst_b = lst_a.copy()
print(f"lst_aのオブジェクトIDは{id(lst_a)}")
print(f"lst_bのオブジェクトIDは{id(lst_b)}")
for pt in lst_a:    #Shallow copy
    print(f"lst_a内のPointクラスのオブジェクトのIDは{id(pt)}")

for pt in lst_b:    #Shallow copy
    print(f"lst_b内のPointクラスのオブジェクトのIDは{id(pt)}")


import copy
lst_c = copy.copy(lst_a)
print(f"lst_aのオブジェクトIDは{id(lst_a)}")
print(f"lst_cのオブジェクトIDは{id(lst_c)}")
for pt in lst_a:    #Shallow copy
    print(f"lst_a内のPointクラスのオブジェクトのIDは{id(pt)}")

for pt in lst_c:    #Shallow copy
    print(f"lst_c内のPointクラスのオブジェクトのIDは{id(pt)}")


lst_d = copy.deepcopy(lst_a)    
print(f"lst_aのオブジェクトIDは{id(lst_a)}")
print(f"lst_dのオブジェクトIDは{id(lst_d)}")
for pt in lst_a:    #Shallow copy
    print(f"lst_a内のPointクラスのオブジェクトのIDは{id(pt)}")

for pt in lst_d:    #Shallow copy
    print(f"lst_d内のPointクラスのオブジェクトのIDは{id(pt)}")
