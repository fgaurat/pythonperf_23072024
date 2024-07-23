

# def log_sayhello(name):
#     print("LOG",name)
#     r = say_hello(name)
#     print("LOG",r)

#     return r

# def do_log(func):

#     def wrapper(*args,**kwargs):
#         print("LOG",args,kwargs)
#         r = func(*args,**kwargs)
#         print("LOG",r)
#         return r

#     return wrapper

def do_log(log_file="defaultlogfile.log",level="INFO"):

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"LOG {level} to {log_file}", args, kwargs)
            r = func(*args, **kwargs)
            print(f"LOG {level} to {log_file}", r)

        return wrapper

    return decorator


# @do_log("logfile.log")
@do_log(level="DEBUG")
def say_hello(name):
    s = f"Hello {name}"
    return s


def main():
    greetings = say_hello('Fred')
    print(greetings)
    greetings = say_hello(name='Fred')
    print(greetings)


if __name__ == '__main__':
    main()
