
#%%
import functools
def decore_message(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        try:
            value,message = func(*args, **kwargs)
        except Exception as e:
            value = -1
            message = f"Error @ {func.__name__}({e})"
#        print(message)
        return value,message
    return wrapper_decorator


if __name__ == "__main__":
    print('Main: preprocessing Module')

