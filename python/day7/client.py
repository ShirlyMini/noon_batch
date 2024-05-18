# module- collection of fun/class
# approach 1
# import module1
# import module2
#
# module1.func1()
# module1.func2()
#
# module2.func3()
# module2.func4()
#
# module1.func()
# module2.func()


# approach 2

# from module1 import func1,func, func2
# from module2 import func3,func, func4
#
# func1()
# func2()
# func3()
# func4()
# func()

# app 3
# from module1 import *
# from module2 import *
#
# func1()
# func2()
# func3()
# func4()
# func()


##############################################
# class
##############################################

# # appr1
# import module1
# import module2

# obj1=module1.A()
# obj1.method1()
# obj1.method()
# obj1.method_class()
# module1.A.method_class()
# obj1.method_static()
# module1.A.method_static()
#
# obj2=module2.B()
# obj2.method2()
# obj2.method()

# obj3=module1.C()
# obj3.method()
# obj4=module2.C()
# obj4.method()

#
# # appr2
# from module1 import A, C
# from module2 import B, C
#
# obj1=A()
# obj1.method1()
# obj1.method()
# obj1.method_class()
# A.method_class()
# obj1.method_static()
# A.method_static()
#
# obj2=B()
# obj2.method2()
# obj2.method()

# obj3=C()
# obj3.method()
# obj4=C()
# obj4.method()


##########################################################################
# Package- collection of modules
#######################################################3333
from pack1.module1 import *
from pack1.module2 import *

func1()
func2()
func3()
func()
# print(__name__)#__main__

from pack1.pack2.module1 import *
func1()
func2()