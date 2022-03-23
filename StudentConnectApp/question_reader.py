def read_questions():
    questions = []
    i = -1

    with open('StudentConnectApp/questions.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            if line[0] != " ":
                i += 1
                questions.append((" ".join((line.split(" ")[1:])).strip(), []))
            else:
                questions[i][1].append(" ".join((line.split(" ")[4:])).strip())

    return (questions)        

read_questions()