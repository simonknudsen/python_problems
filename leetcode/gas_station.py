from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        result = -1

        net = [x - y for x, y in zip(gas, cost)]
        print(net)
        if sum(net) < 0:
            return -1
        if len(net) == 1 and sum(net) >= 0:
            return 0
        # positive_idx = [i for i in range(len(net)) if net[i] > 0]
        positive_idx = []
        for i in range(len(net)):
            if i == 0 and net[i] > 0:
                positive_idx.append(i)
            elif net[i-1] <= 0 and net[i] > 0:
                positive_idx.append(i)
        for start in positive_idx:
            net_x = net[start:] + net[:start]
            print(net_x)
            total = 0
            for i in net_x:
                total += i
                if total < 0:
                    break
            if total >= 0:
                return start
        return result

