import time


def wait_until_minute_flip(period):
    """
    Wait until time hits mins = modulo <period>
    period = 10 = synch to 00, 10, 20 etc mins past the hour
    :return:
    """
    while True:
        a = time.ctime()
        parts = a.split(' ')
        time_str = parts[3]
        mins = int(time_str.split(':')[1])
        secs = int(time_str.split(':')[2])
        time.sleep(0.2)
        if mins % period == 0 and secs == 0:
            return


if __name__ == '__main__':
    wait_until_minute_flip(10)
