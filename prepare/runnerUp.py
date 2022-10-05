
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
runnerUp = []

for i in range(len(name_score)):
    if name_score[i][1] == runnerUpScore:
        runnerUp.append(name_score[i][0])

runnerUp.sort()

for i in range(len(runnerUp)):
    print(runnerUp[i])