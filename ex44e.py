class Other(object):

    def override(self):
        print("OTHER OVERRIDE()")

    def implicit(self):
        print("OTHER IMPLICIT()")

    def altered(self):
        print("OTHER ALTERED()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER ALTERED()")
        self.other.altered()
        print("Child, After Other altered()")

son = Child()

son.implicit()
son.override()
son.altered()
