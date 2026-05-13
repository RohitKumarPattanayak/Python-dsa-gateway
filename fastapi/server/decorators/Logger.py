import time
from functools import wraps


def Logger(func):

    @wraps(func)
    async def wrapper(*args,**kwargs):
        start = time.time()

        result = await func(*args,**kwargs)

        end = time.time()

        print(f"{func.__name__} took {end - start:4f} to execute")

        return result
    
    return wrapper

