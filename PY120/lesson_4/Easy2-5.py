class Greeting:
    def greet(self, message):
        print(message)

class Hello:
    def hi(self):
        self.greet('Hello')

    @classmethod
    def hi(cls):
        greeting = Greeting()
        greeting.greet('Hi')

Hello.hi()