


class Animal:
    x=10
    def foo(self):
        print(self.x)

class Running:
    x=55

# class Dog(Animal,Running):  #10
class Dog(Running,Animal):     #55

    pass

d=Dog()
d.foo()

def f1(action,**kwargs):
    print('action',action)
    print(kwargs)

# f1({'name':'chao'})
f1(1,x=1,y=3)