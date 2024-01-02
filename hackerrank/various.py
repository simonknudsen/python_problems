
# https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
import re

MONTHS = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}

DAYS_IN_MONTHS = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def is_leap_year(year):
    return year % 4 == 0

def get_days_in_month(year, month):
    if is_leap_year(year) and month == 2:
        return 29
    return DAYS_IN_MONTHS.get(month)

def get_days_in_year_to_date(year, month):
    days = 0
    for m in range(1,month + 1):
        days += get_days_in_month(year, month)
    return days

def get_tz_offset_in_secs(tz_sign, tz_hour, tz_mins):
    if "+" == tz_sign:
        return 0 - tz_hour * 3600 - tz_mins * 60
    return tz_hour * 3600 + tz_mins * 60


def diff_in_dates_in_secs(d1, d2):
    """Use baseline of the year 2000"""
    secs = 0
    secs += (d1["year"] - d2["year"]) * 365.25 * 24 * 3600
    secs += (get_days_in_year_to_date(d1["year"], d1["month"]) - get_days_in_year_to_date(d2["year"], d2["month"])) * 24 * 3600
    secs += (d1["hour"] - d2["hour"]) * 3600
    secs += (d1["mins"] - d2["mins"]) * 60
    secs += (d1["secs"] - d2["secs"]) * 60
    secs += get_tz_offset_in_secs(d1["tz_sign"], d1["tz_hour"], d1["tz_mins"]) - get_tz_offset_in_secs(d2["tz_sign"], d2["tz_hour"], d2["tz_mins"])
    return secs

def python_time_delta_parse_date(t):
    """returns: year,month,day,hour,mins,sec,offset-sign,offset-hours,offset-mins
       input e.g. Sat 02 May 2015 19:54:36 +0530 """
    pattern = re.compile(r"[A-Z]{1}[a-z]{2} (\d{2}) ([A-Z]{1}[a-z]{2,20}) (\d{4}) (\d{2}):(\d{2}):(\d{2}) ([-+]{1})(\d{2})(\d{2})")
    m = pattern.search(t)
    return {"year":int(m.group(3)), "month": MONTHS.get(m.group(2)), "day":int(m.group(1)),
            "hour":int(m.group(4)), "mins":int(m.group(5)), "secs":int(m.group(6)),
            "tz_sign":m.group(7), "tz_hour": int(m.group(8)), "tz_mins":int(m.group(9))}

def python_time_delta(t1, t2):
    pattern = re.compile(r"[A-Z]{1}[a-z]{2} \d{2} [A-Z]{1}[a-z]{2,20} \d{4} \d{2}:\d{2}:\d{2} ([-+]{1})(\d{2})(\d{2})")
    m = pattern.search(t1)
    sign1 = m.group(1)
    hours1 = m.group(2)
    mins1 = m.group(3)
    m = pattern.search(t1)
    sign2 = m.group(1)
    hours2 = m.group(2)
    mins2 = m.group(3)

    print(f"hours1={hours1} mins1={mins1} hours2={hours2} mins2={mins2}")

if __name__ == '__main__':
    python_time_delta("Sun 10 May 2015 13:54:36 -0700", "Sat 02 May 2015 19:54:36 +0530")
    print(python_time_delta_parse_date("Sat 02 May 2015 19:54:36 +0530"))