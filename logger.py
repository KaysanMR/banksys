from file_manager import write
from display import current_time


def log_function(function):

    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        log = f"{current_time(2)}: {function.__name__} returned: {result}\n"
        write(log, "log.txt")
        return result

    return wrapper


if __name__ == "__main__":
    def hello(a=1, b=2, word="world"):
        print("Hello " + word)
        return a + b


    session_user = "ADM1707479281A"
    hello(a=15, word="Khalid")
    hello(word="Bakyt")
