class A:
    def process(self):
        print("A Process")


class B:
    def process(self):
        print("B Process")


class C(A, B):
    def process(self):
        print("C Process")

obj = C()
obj.process()

