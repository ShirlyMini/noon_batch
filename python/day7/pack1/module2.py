print(r"This is from pack1\module2")
def func3():
    print("this is func 3")


def func4():
    print("this is func 4")

def func():
    print("this is func from module 2")

class B:
    def method2(self):
        print("method2 from class B")

    def method(self):
        print("method from class B")

class C:
    def method(self):
        print("method from class C module2")


print(r"This is from pack1\module1", __name__)
if __name__=="__main__":
    print(r"This is from pack1\module1", __name__)