class Transform:
    def __init__(self, some_string):
        self.some_string = some_string

    def uppercase(self):
        return self.some_string.upper()
    
    @classmethod
    def lowercase(self, text):
        return text.lower()
    
my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz