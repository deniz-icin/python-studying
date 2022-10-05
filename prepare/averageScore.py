
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
new_marks = []    

for i in range(len(student_marks)):
    if query_name == student_marks[name]:
        new_marks.append(scores)
        
a = 0
b = len(student_marks)

for _ in new_marks:
    a+=sum(_)
    
print(a/b)

##duzelt