class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data = [format(num, '08b') for num in data]

        queue = []
        for num in data:
            if not queue:
                if num[:1] == '0':
                    pass
                elif num[:3] == '110':
                    queue.append('10')
                elif num[:4] == '1110':
                    queue.extend(['10', '10'])
                elif num[:5] == '11110':
                    queue.extend(['10', '10', '10'])
                else:
                    return False
            else:
                if not num.startswith(queue.pop(0)):
                    return False
        
        if queue:
            return False
        
        return True
