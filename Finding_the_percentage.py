#functions
#execution
def score(student_marks,query_name):
    for key,values in student_marks.items():
        if key == query_name:
            average = sum(values) / len(values)
    print('{:.2f}'.format(average))
    


#input part
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score(student_marks,query_name)
