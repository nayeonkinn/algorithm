class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks).values()
        common_cnt = max(counter)
        common_friends = list(counter).count(common_cnt)

        return max(len(tasks), (common_cnt - 1) * (n + 1) + common_friends)