class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

# What will the following snippets do?
hello = Hello() # Object instantiated
hello.hi()      # Outputs 'Hello'

#hello.bye()     # Will error as bye is not a method 
                # available to the Hello object

#hello.greet()   # Will error as there is no message 
                # passed to the greet method

#hello.greet('Goodbye')
                # Will output 'Goodbye'

Hello.hi()      # Will error because it does not 
                # have an object (a self) to perform
                # the hi method on. Hello().hi() would
                # work, however.