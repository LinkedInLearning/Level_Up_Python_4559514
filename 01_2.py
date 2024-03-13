# リストを作ってループする
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = 0
for i in lst:
    ans += i

print(ans)
# range関数を使う
ans = 0
for i in range(1,11):
    ans += i

print(ans)

#sum関数を使う
ans = sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(ans)
