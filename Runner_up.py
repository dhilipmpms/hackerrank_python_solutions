def runner(students):
    students = list(students)
    students.sort(reverse=True)
    for score in range(len(students)):
        if students[score] != students[score+1]:
            runner_up=students[score+1]
            break
        
    return(runner_up)






if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    run = runner(arr)
    print(run)
