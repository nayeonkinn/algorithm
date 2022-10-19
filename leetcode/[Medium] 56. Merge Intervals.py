class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        for i in range(-len(intervals) + 1, 0):
            if intervals[i - 1][1] >= intervals[i][1]:
                intervals.pop(i)
            elif intervals[i - 1][1] >= intervals[i][0]:
                intervals[i][0] = intervals[i - 1][0]
                intervals.pop(i - 1)

        return intervals