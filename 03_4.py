"""
    リストを使って二次元集計する
    優勝者数を県別・区分別に集計
    03_4.py
"""
import csv
from pprint import pprint

prefs = ("","北海道","青森県","岩手県","宮城県","秋田県","山形県","福島県","茨城県","栃木県", \
    "群馬県","埼玉県", "千葉県","東京都","神奈川県","新潟県","富山県","石川県","福井県","山梨県", \
    "長野県","岐阜県","静岡県","愛知県","三重県","滋賀県","京都府","大阪府","兵庫県","奈良県", \
    "和歌山県","鳥取県","島根県","岡山県","広島県","山口県","徳島県","香川県","愛媛県","高知県", \
    "福岡県","佐賀県","長崎県","熊本県","大分県","宮崎県","鹿児島県","沖縄県")

sects = ("県名","中学生","高校生","大学生","社会人")

number_of_winners =  [[0]*len(sects) for i in range(len(prefs))]
# pprint(number_of_winners)

for j in range(len(sects)):
    number_of_winners[0][j] = sects[j]

for i in range(1,len(prefs)):
    number_of_winners[i][0] = prefs[i]
# pprint(number_of_winners)

with open("winnersList.csv", "r", encoding="shift_jis") as f:
    reader = csv.reader(f, delimiter=",")
    for line in reader:
        sect = line[3]
        pref = line[6]
        for i in range(1,len(prefs)):
            if pref == number_of_winners[i][0]:
                for j in range(1,len(sects)):
                    if sect == number_of_winners[0][j]:
                        number_of_winners[i][j] += 1

# pprint(number_of_winners)

# with open("winnersAggregate.csv", "w", encoding="shift_jis", newline="") as f:
#     writer = csv.writer(f)
#     for line in number_of_winners:
#         writer.writerow(line)

with open("winnersAggregate.csv", "w", encoding="shift_jis", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(number_of_winners)