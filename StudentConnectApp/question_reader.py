import os 

def read_questions():
    questions = []
    i = -1

    with open('StudentConnectApp/questions.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            if line[0] != " ":
                #print(" ".join((line.split(" ")[0:])), [])
                i += 1
                questions.append((" ".join((line.split(" ")[0:])).strip(), []))
            else:
                questions[i][1].append(" ".join((line.split(" ")[0:])).strip())

    return (questions)        