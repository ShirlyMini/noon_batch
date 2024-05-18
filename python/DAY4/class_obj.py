# class- template, blueprint-- logical entity--no mem alloc will happen
# attribute- variables and method
class resume_template:
    name="xyz"#

    def func1(self, edu):
        print("project desc", edu)

# object - real time enity--- mem allocation will happen
# print(resume_template)##<class '__main__.resume_template'>## class name
# print(resume_template())##<__main__.resume_template object at 0x000001D723EF41D0>

# to create n intstance

obj1=resume_template()
print(obj1.name)
obj1.name="pooja"
print(obj1.name)
obj1.func1("BE")



obj2=resume_template()
print(obj2.name)
obj2.name="ram"
print(obj2.name)
obj2.func1("ME")


