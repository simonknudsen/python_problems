
# https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
import re
from collections import namedtuple
from statistics import mean

def python_time_delta(t1, t2):
    MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
              "Nov": 11, "Dec": 12}
    DAYS_IN_MONTHS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    def is_leap_year(year):
        return year % 4 == 0
    def get_days_in_month(year, month):
        if is_leap_year(year) and month == 2:
            return 29
        return DAYS_IN_MONTHS.get(month)
    def get_days_in_year_to_date(year, month, day):
        days = 0
        for m in range(1, month):
            days += get_days_in_month(year, month)
        return days + day
    def get_tz_offset_in_secs(tz_sign, tz_hour, tz_mins):
        if "+" == tz_sign:
            return 0 - tz_hour * 3600 - tz_mins * 60
        return tz_hour * 3600 + tz_mins * 60
    def diff_in_dates_in_secs(d1, d2):
        """Use baseline of the year 2000"""
        secs = 0
        secs += (d1["year"] - d2["year"]) * 365.25 * 24 * 3600
        secs += (get_days_in_year_to_date(d1["year"], d1["month"], d1["day"]) -
                 get_days_in_year_to_date(d2["year"], d2["month"], d2["day"])) * 24 * 3600
        # print(f'get_days_in_year_to_date={get_days_in_year_to_date(d1["year"], d1["month"])} {get_days_in_year_to_date(d2["year"], d2["month"])}')
        secs += (d1["hour"] - d2["hour"]) * 3600
        secs += (d1["mins"] - d2["mins"]) * 60
        secs += (d1["secs"] - d2["secs"]) * 60
        secs += get_tz_offset_in_secs(d1["tz_sign"], d1["tz_hour"], d1["tz_mins"]) - get_tz_offset_in_secs(
            d2["tz_sign"], d2["tz_hour"], d2["tz_mins"])
        return str(round(abs(secs)))
    def python_time_delta_parse_date(t):
        """returns: year,month,day,hour,mins,sec,offset-sign,offset-hours,offset-mins
           input e.g. Sat 02 May 2015 19:54:36 +0530 """
        pattern = re.compile(
            r"[A-Z]{1}[a-z]{2} (\d{2}) ([A-Z]{1}[a-z]{2,20}) (\d{4}) (\d{2}):(\d{2}):(\d{2}) ([-+]{1})(\d{2})(\d{2})")
        m = pattern.search(t)
        return {"year": int(m.group(3)), "month": MONTHS.get(m.group(2)), "day": int(m.group(1)),
                "hour": int(m.group(4)), "mins": int(m.group(5)), "secs": int(m.group(6)),
                "tz_sign": m.group(7), "tz_hour": int(m.group(8)), "tz_mins": int(m.group(9))}
    #print(python_time_delta_parse_date(t1))
    #print(python_time_delta_parse_date(t2))
    return diff_in_dates_in_secs(python_time_delta_parse_date(t1), python_time_delta_parse_date(t2))
    #print(f"hours1={hours1} mins1={mins1} hours2={hours2} mins2={mins2}")

# https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
def most_commons(s):
    c_count = {}
    for c in s:
        if not c_count.get(c):
            c_count[c] = 1
        else:
            c_count[c] += 1
    chars = [(v, k) for k, v in c_count.items()]
    chars.sort(key=lambda x: (0 - x[0]) * 1000 + ord(x[1]))
    for x in chars[:3:]:
        print(f"{x[1]} {x[0]}")


# https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
def piling_up(blocks):
    if not blocks:
        return "No"
    i = 0
    j = len(blocks) - 1
    last_block = None
    while i != j:
        left = blocks[i]
        right = blocks[j]
        #print(f"i={i} j={j} left={left} right={right} last_block={last_block}")
        if ((last_block and left <= last_block) or not last_block) and left >= right:
            last_block = left
            i += 1
        elif ((last_block and right <= last_block) or not last_block) and right >= left:
            last_block = right
            j -= 1
        if last_block and last_block < max(left, right):
            return "No"
    return "Yes"

# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
def python_string_formatting(n):
    max_width = len(bin(n)[2::])
    for i in range(1,n+1):
        print(str(i).rjust(max_width," ") + " " +
              oct(i)[2::].rjust(max_width," ") + " " +
              hex(i)[2::].upper().rjust(max_width," ") + " " +
              bin(i)[2::].rjust(max_width," "))

# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def minion_game(s):
    vowels = {"A":1, "E":1, "I":1, "O":1, "U":1}
    def get_matches(s, start_vowel):
        full_len = len(s)
        subs_count = 0
        for i, c in enumerate(s):
            if start_vowel and vowels.get(c):
                subs_count += full_len - i
            if not start_vowel and not vowels.get(c):
                subs_count += full_len - i
        return subs_count
    vowel_count = get_matches(s, True)
    non_vowel_count = get_matches(s, False)
    if vowel_count > non_vowel_count:
        return f"Kevin {vowel_count}"
    elif vowel_count < non_vowel_count:
        return f"Stuart {non_vowel_count}"
    else:
        return "Draw"

# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
def py_collections_namedtuple(lines):
    i = lines[0].split().index("MARKS")
    #Score = namedtuple('Score', lines[0])
    return f"{mean([int(x.split()[i]) for x in lines[1::]]):.2f}"

if __name__ == '__main__':
    #print(python_time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"))
    #print(python_time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"))
    #most_commons("aabbbccde")
    #python_string_formatting(2)
    print(py_collections_namedtuple([
        "ID         MARKS      NAME       CLASS",
        "1          97         Raymond    7",
        "2          50         Steven     4",
        "3          91         Adrian     9",
        "4          72         Stewart    5",
        "5          80         Peter      6"
    ]))
    print(py_collections_namedtuple([
        "MARKS      CLASS      NAME       ID",
        "92         2          Calum      1",
        "82         5          Scott      2",
        "94         2          Jason      3",
        "55         8          Glenn      4",
        "82         2          Fergus     5"
    ]))


    # Stuart 7501500
