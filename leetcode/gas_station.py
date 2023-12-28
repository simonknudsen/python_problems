from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        result = -1
        for offset in range(len(gas)):
            c_gas = 0
            for i in range(len(gas)):
                index = (offset + i) % len(gas)
                c_gas += gas[index] - cost[index]
                if c_gas < 0:
                    break
            if c_gas >= 0:
                return offset
        return result

