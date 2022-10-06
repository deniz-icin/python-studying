
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    queryName_score = student_marks[query_name]

    a = sum(queryName_score)
    b = len(queryName_score)
    result = a/b
    
    print("%.2f" % result)
