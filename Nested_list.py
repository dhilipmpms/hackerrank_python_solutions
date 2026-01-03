def score_up(student_name_score):
    
    students_score=[]
    for students in student_name_score:
        students_score.append(students[1])
    sorted_score= sorted(set(students_score))
    second_lowest_grade=sorted_score[1]
    
    
    second_lowest_name=[]
    for students in student_name_score:
        if students[1]==second_lowest_grade:
            second_lowest_name.append(students[0])
    second_lowest_name.sort()
    
    for name in second_lowest_name:
        print(name)


if __name__ == '__main__':
    
    student_name_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_name_score.append([name,score]) 
    score_up(student_name_score)
        
