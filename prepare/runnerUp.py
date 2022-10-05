
name_score=[]
scoreList=[]

for i in range(int(input())):
    name = input()
    score = float(input())
    name_score.append([name,score])
    scoreList.append(score)

new_score=[]

for i in range(len(scoreList)):
    if scoreList[i] != min(scoreList):
        new_score.append(scoreList[i])

runnerUpScore = min(new_score)
runnerUps = []

for i in range(len(name_score)):
    if name_score[i][1] == runnerUpScore:
        runnerUps.append(name_score[i][0])

runnerUps.sort()

for i in range(len(runnerUps)):
    print(runnerUps[i])