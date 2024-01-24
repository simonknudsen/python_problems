
# https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
import re
from collections import namedtuple
from statistics import mean

MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
          "Nov": 11, "Dec": 12}
DAYS_IN_MONTHS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def python_time_delta(t1, t2):
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

    return diff_in_dates_in_secs(python_time_delta_parse_date(t1), python_time_delta_parse_date(t2))

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
    return f"{mean([int(x.split()[i]) for x in lines[1::]]):.2f}"

# https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
def iterables_and_iterators(letters_str, k):
    letters = letters_str.strip().split()
    a_indexes = {}
    for i, c in enumerate(letters):
        if c == "a":
            a_indexes[i:"a"]

# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
def designer_door_mat(n,m):
    for i in range(1, n + 1):
        j = min(i, n + 1 - i)
        if i == n // 2 + 1:
            pad = "-" * ((m - 7) // 2)
            print(pad + "WELCOME" + pad)
        else:
            gates = "|.." * (j - 1)
            line = "-" * ((m - 1) // 2 - len(gates) - 1)
            half = line  + "." + gates
            print(half + "|" + half[::-1])

# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def alphabet_rangoli(n):
    height = n * 2 -1
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = list(reversed(alphabet[0:n]))
    for i in range(1, height + 1):
        j = min(i, height + 1 - i)
        dash = "-" * ((n - j) * 2)
        letter = letters[j-1]
        seq = ""
        if j > 1:
            seq = "-".join([x for x in letters[0:j-1]]) + "-"
        print(dash + seq + letter + seq[::-1] + dash)

# https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
def maximize_it(k,lines):
    nums = []
    for l in lines:
        nums.append(map(int, l.strip().split()))
    print(nums)
    nums = [sorted([x**2 % k for x in y],reverse=True) for y in nums]
    print(nums)
    indexes = [0] * len(nums)
    max_v = 0
    #while True:
    #    val = [nums[for i in range(len(nums))]

def fiboccai(n):
    if n == 1:
        return 10
    if n ==2:
        return 20
    else:
        return 23 * n

def the_captains_room(k, room_entries):
    potential_rooms = set()
    room_count = {}
    for x in room_entries:
        if room_count.get(x):
            room_count[x] += 1
            if room_count[x] == 2:
                potential_rooms.remove(x)
        else:
            room_count[x] = 1
            potential_rooms.add(x)
    return potential_rooms.pop()


if __name__ == '__main__':
    #print(python_time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"))
    #print(python_time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"))
    #most_commons("aabbbccde")
    #python_string_formatting(2)
    #designer_door_mat(7,21)
    #designer_door_mat(9, 27)
    #alphabet_rangoli(5)
    #maximize_it(1000, ["2 5 4",
    #                        "3 7 8 9",
   #                         "5 5 7 8 9 10"])
    """
    5
[1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
    """
    print(the_captains_room(5, [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]))
    with open("../data/the_captains_room.txt") as f:
        room_entries = map(int, f.readline().split())
        print(the_captains_room(5, room_entries))
        # 4390
"""
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10

["2 5 4", 
"3 7 8 9", 
"5 5 7 8 9 10"]

"""