str_greet = "私の名前は伊藤　忠司です。年齢は36歳で身長は172.5センチです。"
print(str_greet)

my_name = "伊藤　忠司"
my_age = 36
my_height = 172.5

str_greet = "私の名前は" + my_name + "です。年齢は" + str(my_age) + "歳で身長は" \
    + str(my_height) + "センチです。"
print(str_greet)

str_greet = f"私の名前は{my_name}です。年齢は{my_age}歳で身長は{my_height}センチです。" 
print(str_greet)