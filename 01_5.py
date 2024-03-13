str_origin = 'このたけがけにたけたてかけたのはたけたてかけたかったからたけたてかけた'

#スライスで一文字飛ばし
str_new = str_origin[::2]
print(str_origin)
print(str_new)

#たとえば途中から
str_new = str_origin[5:20:2]
print(str_origin)
print(str_new)

#あえてforループで
str_new= ""
for idx in range(0, len(str_origin) ,2):
    str_new += str_origin[idx]

print(str_origin)
print(str_new)