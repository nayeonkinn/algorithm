class Solution:
    def trap(self, height: List[int]) -> int:
        top = height.index(max(height))
        rain = 0
        
        maxx = height[0]
        for i in range(top + 1):
            if height[i] >= maxx:
                maxx = height[i]
            else:
                rain += maxx - height[i]
        
        maxx = height[-1]
        for i in range(len(height) - 1, top - 1, -1):
            if height[i] >= maxx:
                maxx = height[i]
            else:
                rain += maxx - height[i]

        return rain