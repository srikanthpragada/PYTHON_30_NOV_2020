class A:
    def process(self):
        print("A Process")


class B(A):
    pass


class C(A):
    def process(self):
        print("C Process")


class D(B, C):
    pass


obj = D()
obj.process()
print(D.mro())
