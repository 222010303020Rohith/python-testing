class A:
    def method1(self):
        print("from m1")
    def method2(self):
        print("from m2")

class B(A):
    def method3(self):
        print("from m3")
    def method4(self):
        print("from m4")

C = B()
C.method1()  # This will print "from m1"
