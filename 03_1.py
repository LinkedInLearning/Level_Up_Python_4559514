class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):  #特殊メソッド、ダンダーメソッド
        return f'({self.x}, {self.y})'

'''
__str__はオブジェクトの文字列表現のためのメソッドです。
人間が読める出力を提供することを目的としています。
'''
pt_a = Point(120,220)
print(pt_a)