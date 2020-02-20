def logger(func):
    def wrapper():
        print('Logging execution')
        func()
        print('Logging ended')
    return wrapper


@logger
def sample():
    print('---> Sample function code')


sample()
