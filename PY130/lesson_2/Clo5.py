def later2(function, first_arg):
    def new_func(second_arg):
        return function( first_arg, second_arg)
    
    return new_func

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!