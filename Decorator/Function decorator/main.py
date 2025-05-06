import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Took {}ms amount of time".format((end-start) * 1000))
        return result
    return wrapper

@time_it
def some_method():
    print("Starting Op")
    time.sleep(1)
    print("Work done")

@time_it
def some_method_with_args(a, b):
    print("Starting Op args")
    time.sleep(0.5)
    sum_ = a + b
    print("Work done args")
    return sum_

if __name__ == '__main__':
    print("Call method without args...")
    # time_it(some_method)() # Explicit way
    some_method() # Implicit and cleaner way

    print("Call method with args...")
    val = some_method_with_args(2,3)
    print("Return sum is {}".format(val))
