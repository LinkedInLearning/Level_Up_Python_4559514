str_origin = "たけのこ、いものこ、さかなのこ"

#逆順にループする
str_reverse= ""
for idx in range(len(str_origin),0,-1):
    str_reverse += str_origin[idx-1]

print(str_reverse)

#スライスで逆順にする
str_reverse = str_origin[::-1]
print(str_reverse)

#reversed関数を使う
lst_reverse = list(reversed(str_origin))
str_reverse = "".join(lst_reverse)
print(str_reverse)

#一度listにして、reverseメソッドを使う
lst_origin = list(str_origin)
lst_origin.reverse()
str_reverse = "".join(lst_origin)
print(str_reverse)


