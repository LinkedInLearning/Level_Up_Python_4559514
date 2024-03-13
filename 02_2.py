set_01 = {"りんご","いちご","みかん","キウイ","ぶどう","バナナ"}    #わたしの好きな果物
set_02 = {"いちじく","キンカン","ぶどう","バナナ","パイナップル"}   #あなたの好きな果物

print(f"排他的論理和 {set_01.symmetric_difference(set_02)}")

print(f"和集合 {set_01.union(set_02)}")

print(f"差集合 {set_01.difference(set_02)}")

print(f"積集合 {set_01.intersection(set_02)}")