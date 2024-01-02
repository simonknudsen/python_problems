
# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and B, respectively.

def happiness(s1, s2, s3, s4):
    n, m = s1.split(" ")
    n, m = int(n), int(m)
    array = [int(x) for x in s2.split(" ")]
    a = [int(x) for x in s3.split(" ")]
    a_ = {x:1 for x in a}
    b = [int(x) for x in s4.split(" ")]
    b_ = {x:1 for x in b}
    happy_level = 0
    for i in array:
        if a_.get(i):
            happy_level += 1
        if b_.get(i):
            happy_level -= 1
    return happy_level