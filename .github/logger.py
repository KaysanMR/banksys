from accounts import save, load


def log_function(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        log = [[f"{function.__name__} run with args {args, kwargs}, returned: {result}"]]
        save(log, "log.csv")
        return result

    return wrapper


@log_function
def hello(a=1, b=2, word="world"):
    print("Hello " + word)
    return a + b


if __name__ == "__main__":
    # lists = ["A", "B", "C"]
    # save(lists, "log.csv")
    # loader = (load("log.csv"))
    # print(loader)
    hello(a=15, word="Khalid")
