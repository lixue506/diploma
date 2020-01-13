# -*- coding:utf-8 -*-
import time
import datetime

def get_current_time():
    time_stamp = time.time()  # 当前时间的时间戳
    local_time = time.localtime(time_stamp)  #
    str_time = time.strftime('%Y-%m-%d', local_time)
    print(str_time)

    today = datetime.date.today()
    print(today)


if __name__ == "__main__":
    get_current_time()
