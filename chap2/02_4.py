tpl_01 = ("りんご","いちご","みかん","キウイ","ぶどう")
lst_01 = [150,500,300,400]

#タプルとリストからタプルを
for price_card in zip(tpl_01,lst_01):
    print(price_card)
#dict関数でディクショナリーに
dict_01 = dict(zip(tpl_01, lst_01))
print(dict_01)
#zip関数では短いほうに合わせられるので「ぶどう」のprice_cardは作られない

from itertools import zip_longest
tpl_01 = ("りんご","いちご","みかん","キウイ","ぶどう")
lst_01 = [150,500,300,400]

#長いほうに合わせる
for price_card in zip_longest(tpl_01,lst_01):
    print(price_card)

#足りない値を埋める
dict_01 = dict(zip_longest(tpl_01, lst_01, fillvalue='時価'))
print(dict_01)