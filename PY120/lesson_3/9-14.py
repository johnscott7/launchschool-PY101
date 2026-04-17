class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)

# This will cause an error because var_a is
# not an inherited variable, it is a variable
# assigned during initialization, and super() 
# is never called for the class B instance.