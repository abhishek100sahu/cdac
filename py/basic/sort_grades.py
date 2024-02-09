if __name__ == '__main__':
    records = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    def sortScore(score):
        return score[1]
        
    records.sort(key=sortScore)
    
    rec = list()
    
    def sortName(name):
        return name[0]
        
    for idx in range(len(records)-1):
        if records[idx][1] == records[idx + 1][1]:
            rec.append([records[idx]])
            rec.append(records[idx + 1])
    
    rec = sorted(rec, key=sortName)
    
    for r in rec:
        print(r[0])