"""class myclass:
  x = 10
p1=myclass
print(p1.x)
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p2 = Person("Dave",29)
p1.myfunc()
p2.myfunc()