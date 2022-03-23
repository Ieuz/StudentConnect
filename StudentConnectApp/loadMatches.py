from StudentConnectApp.models import Student, Answer, Choice

def loadMatches(current_student):


    other_students = Student.objects.exclude(user=current_student.user)
    current_students_answers = Answer.objects.filter(student=current_student)
    for student in other_students:
        score = 0
        compared_students_answers = Answer.objects.filter(
            student=student
        )
        increment = -1
        if compared_students_answers.count() == 0:
            continue
        for answer in current_students_answers:
            increment += 1
            current_choice = answer.choice
            if compared_students_answers[increment].choice == current_choice:
                print(f"Match for {student}")
                score += 1/current_students_answers.count()
        print(f"score is {score}")
        if score > 0.50: # This would be increased over time as we got more members and thus more opportunities for connections.
            print("Attempting an add")
            current_student.matches.add(student)
            current_student.save()
    current_student.matches_ready = True
    current_student.save()    



