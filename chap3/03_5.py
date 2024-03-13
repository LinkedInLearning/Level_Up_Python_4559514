import csv
from pprint import pprint

orders_data = {}

with open("ordersList.csv", "r", encoding="shift_jis") as f:
    reader = csv.reader(f, delimiter=",")
    for line in reader:
        t_code = line[2]    #得意先コード
        s_code = line[9]    #商品コード
        quantity = line[12]
        amount = line[14]
        orders_data.setdefault(t_code, {"name": line[3],"quantity": 0, "amount":0})
        orders_data[t_code].setdefault(s_code, {"name": line[10], "quantity": 0, "amount":0}) 
        orders_data[t_code][s_code]["quantity"] += int(quantity)
        orders_data[t_code][s_code]["amount"] += int(amount)
        orders_data[t_code]["quantity"] += int(quantity)
        orders_data[t_code]["amount"] += int(amount)

pprint(orders_data)

#DictWriterメソッドを使わないことを説明する
with open("ordersAggregate.csv", "w", encoding="shift_jis", newline="") as f:
    writer = csv.writer(f)
    line = ["得意先","受注数量","受注金額","商品名","受注数量","受注金額", ]
    writer.writerow(line)
    for order_data in orders_data.values(): 
        line = []
        line.append(order_data["name"])
        line.append(order_data["quantity"])
        line.append(order_data["amount"])
        writer.writerow(line)
        for s_data in order_data.values():
            if isinstance(s_data,dict):
                line=[]
                for i in range(3):        
                    line.append("")
                line.append(s_data["name"])
                line.append(s_data["quantity"])
                line.append(s_data["amount"])
                writer.writerow(line)