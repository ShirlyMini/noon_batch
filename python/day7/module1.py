def func1():
    print("this is func 1")

def func2():
    print("this is func 2")

def func():
    print("this is func from module 1")

class A:
    def method1(self):
        print("method1 from class A")

    def method(self):
        print("method from class A")

    @classmethod
    def method_class(cls):
        print("class method from class A")

    @staticmethod
    def method_static():
        print("static method from class A")

class C:
    def method(self):
        print("method from class C module1")