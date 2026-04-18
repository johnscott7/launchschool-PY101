class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer()) # Should still return 'Amazon' because tv is of the Television class
print(tv.model())       # will definitely return 'Omni Fire'

print(Television.manufacturer())    # Will definitely return 'Amazon'
print(Television.model())           # Will definitely error because needs an instance (has no self)