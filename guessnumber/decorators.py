

def log(level):
    def log_decorator(f):
        def wrapped(*args, **kwargs):
            print(level + ": " + f.__name__ + " is called with", args)
            return f(*args, **kwargs)
        return wrapped
    return log_decorator

