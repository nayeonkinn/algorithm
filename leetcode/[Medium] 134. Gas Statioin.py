class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0, 0
        for i in range(len(gas)):
            if fuel + gas[i] - cost[i] < 0:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        
        return start