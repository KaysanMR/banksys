from file_manager import write
from display import current_time


def log_entry(action, session="SYSTEM"):
    log = f"{current_time(2)}: [{session}] {action}\n"
    write(log, "log.txt")


if __name__ == "__main__":
    pass
