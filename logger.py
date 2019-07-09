def info(msg):
    log('+', msg)


def error(msg):
    log('!', msg)


def warning(msg):
    log('-', msg)


def debug(msg):
    log('DEBUG', msg)


def header(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


def log(sign, msg):
    print('[{0}] {1}'.format(sign, msg))


def show_progress(i: str, o: str, items):
    info('{0}{2} -> {1}'.format(i, o, ' ' * (len(max(items, key=len)) - len(i))))
