class MyClass:
    class_attribute=10
    def __init__(self,value):
        self.instance_attribute=value
obj=MyClass(20)
print(obj.class_attribute)