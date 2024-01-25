from datetime import datetime as DT

def work_speed(func):
    def wrapper(cases):
        start = DT.now().timestamp()
        quotes = func(cases)
        end = DT.now().timestamp()
        result = end - start
        print(f"Query speed: {round(result, 4)} s")
        return quotes
    return wrapper
