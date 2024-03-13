a = -5

# -1を掛ける
print(a * -1)

# abs関数を使う
print(abs(a))

# 関数を自作する
def my_abs(x):
    if x < 0:
        return x * -1
    else:
        return x

print(my_abs(-3))
print(my_abs(3))

# 三項演算子
a = -5

x = a if a >= 0 else a * -1
print(x)

a = 0 
x = a if a >= 0 else a * -1
print(x)

a = 5
x = a if a >= 0 else a * -1
print(x)
