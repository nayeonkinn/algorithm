class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binarySearch(left, right):
            if left <= right:
                mid = (left + right) // 2
                if numbers[mid] == t:
                    return mid
                elif numbers[mid] > t:
                    return binarySearch(left, mid - 1)
                else:
                    return binarySearch(mid + 1, right)
            else:
                return -1
        
        for i in range(len(numbers) - 1):
            t = target - numbers[i]
            j = binarySearch(i + 1, len(numbers) - 1)
            if j != -1:
                return [i + 1, j + 1]