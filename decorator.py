import time

def run_with_time(func):
    def wrapper(*args, **kw):
        start_time = time.time()
        end_time = time.time()
        print(end_time - start_time)
    return wrapper

def common_function(*args, **kwargs):
    pass

@run_with_time
def action():
    return [i for i in range(100000)]
     #start_time=time.time()
     #action()
     #end_time=time.time()
     #print(end_time-start_time)

#run_with_time(action)
action('hello')