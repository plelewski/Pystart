def cut(s, e):
    def wrapper(func):
        def inner_wrapper(*args):
            return func(args[0][s:e])

        return inner_wrapper
    return wrapper

@cut(1,4)
def cut_the_string(string:str):
    return string


print(cut_the_string('dupa jasiu'))
