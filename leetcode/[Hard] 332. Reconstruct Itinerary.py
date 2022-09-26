class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        
        ch = defaultdict(list)
        for t in sorted(tickets, reverse = True):
            ch[t[0]] += [t[1]]

        stack, itinerary = ['JFK'], []
        while stack:
            while ch[stack[-1]]:
                stack.append(ch[stack[-1]].pop())
            itinerary.append(stack.pop())
        
        return itinerary[::-1]
    