class Parent(object):

    def implicit(self):
        print("Parent implicit()")

class Child(Parent):
    print("THis is Child")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

