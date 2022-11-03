"""Functions for organizing and calculating student exam scores."""
def round_scores(student_scores):
    round_scores = []
    for i in student_scores:
        round_scores.append(round(i))
    return round_scores

def count_failed_students(student_scores):
    failed_students = 0
    for i in student_scores:
        if i<=40:
            failed_students += 1
    return failed_students
            
def above_threshold(student_scores, threshold):
    above_threshold = []
    for i in student_scores:
        if i >= threshold:
            above_threshold.append(i)
    return above_threshold

def letter_grades(highest):
    difference = int(highest / 4) - 10
    letter_grades = []
    for i in range(4):
        letter_grades.append(41 + difference*i)
    return letter_grades

def student_ranking(student_scores, student_names):
    student_ranking = []
    for index,name in enumerate(student_names):
        student_ranking.append(f"{index+1}. {name}: {student_scores[index]}")
    return student_ranking
    
def perfect_score(student_info):
    perfect_score = []
    for name,score in student_info:
        if score == 100:
            perfect_score.append(name)
            perfect_score.append(score)
            break
    return perfect_score
