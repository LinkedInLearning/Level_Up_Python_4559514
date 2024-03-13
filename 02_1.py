# forループでリスト生成
lst_01 = [1,2,3,4,5,6,7,8,9,10,11,12]

lst_02 = [] #空のリスト
for i in lst_01:
    if i < 10:
        lst_02.append(i**2)

print(f"lst_02 {lst_02}")

#リスト内包表記とifの組み合わせ
lst_03 = [i**2 for i in lst_01 if i<10]   
print(f"lst_03 {lst_03}")