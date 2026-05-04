def later(func, argument):
    def inner():
        return func(argument)
    
    return inner

def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # The system is shutting down!