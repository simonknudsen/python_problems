class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    result = []
    #print(stream)
    if type(stream) == EvenStream:
        stream = EvenStream()
    for _ in range(n):
        result.append(stream.get_next())
    return result

def process(input):
    #queries = int(input[0])
    result = []
    for i in input[1::]:
        #print(i)
        stream_name, n = i.split()
        n = int(n)
        if stream_name == "even":
            #print("EVEN")
            result += print_from_stream(n)
        else:
            #print(f"ODD {print_from_stream(n, OddStream())}")
            result += print_from_stream(n, OddStream())
    return result
