import random
import time
import datetime
    
def str_time_prop(start, end, time_format, prop):

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M', prop)


def random_timestamp(start, end):
    r_date = random_date(start, end, random.random())
    r_timestamp = time.mktime(datetime.datetime.strptime(r_date, '%m/%d/%Y %I:%M').timetuple())
    return r_timestamp


