class P1:
    def __init__(self, a):
        self.a = a
    def walk(self):
        print('walk')
        print(self.a)

obj = P1(1)
print(obj.a)
obj.walk()




