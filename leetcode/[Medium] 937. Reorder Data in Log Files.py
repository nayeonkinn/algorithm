class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs = [log.split(' ', 1) for log in logs]
        dig = []

        for i in range(len(logs)):
            if logs[i][1][0].isdigit():
                dig.append(logs[i])
        
        logs = [log for log in logs if log[1][0].isalpha()]
        logs.sort(key = lambda x:(x[1], x[0]))
        
        newlogs = [" ".join(log) for log in logs + dig]
        return newlogs