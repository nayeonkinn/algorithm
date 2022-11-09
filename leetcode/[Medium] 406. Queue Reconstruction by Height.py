class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        answer = []
        for person in people:
            answer.insert(person[1], person)

        return answer