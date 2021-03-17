import datetime
import pytz


# https://stackabuse.com/how-to-get-the-current-date-and-time-in-python/
# 2021-03-07 20:55:08.94343+00.00
def get_jena_timestamp():
    """
    Timestamp format used in Depep Learning in Python book for temperature forecasting
    :return:
    """

    utc_current_datetime = datetime.datetime.now(pytz.timezone("UTC")).__str__()
    # print(utc_current_datetime)
    date_part = utc_current_datetime.split(' ')[0]
    time_part = utc_current_datetime.split(' ')[1].split('.')[0]
    date_parts = date_part.split('-')
    year = date_parts[0]
    month = date_parts[1]
    day = date_parts[2]

    jena_timestamp = day + '.' + month + '.' + year + ' ' + time_part

    return jena_timestamp


if __name__ == '__main__':
    a = get_jena_timestamp()
    print(a)