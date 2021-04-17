from time import time, sleep

def execution_time(function):
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        stop = time()
        print(round(stop - start, 5), *args)
        return result

    return wrapper


@execution_time
def power(a, b):
    sleep(1.1)
    return a ** b


print(power(2, 2))
print(power(2, 8))
