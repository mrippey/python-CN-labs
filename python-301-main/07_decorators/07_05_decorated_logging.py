# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.



from time import time 

def log_time(time_interval):
    def log(func):
        def wrap(*args, **kwargs):
            start = int(round(time_interval * 1000))
            func(*args, **kwargs)
            end = int(round(time_interval * 1000)) - start
            print(f'Function: {func.__name__}, Total execution time: {start-end}ms.\n')
        return wrap 
    return log 

@log_time(20)
def func_execution_time(i):
    for _ in range(i):
        print(_)

func_execution_time(10)