import time
import sqlite3
score = 0
party = ""

instructions = "Thank you so much for being willing to take this survey! Below are some FAQ's: \n* No, your name, email, or identity will not be associated with your answers. \n* The survey results are being used for a class project and will not be shared with any wider of an audience. \n* With any further questions please contact Rachael Harris, Morgan Douglas, Andy Strozewski, or Tyson Lindley.\n\nINSTRUCTIONS: please type 'yes' or 'no' as an answer to each question, until you will be asked for a ranking, then please use the numbers 1-5."

print(instructions)

print("\n\n\n")

time.sleep(3)

q1 = input("Are you Black, Hispanic, or Asian?\t")
if q1 == "yes":
    score = 64
    q2 = input("Are you black?\t")
    if q2 == "yes":
        score = 83
        q3 = input("Are you older than 31?\t")
        if q3 == "yes":
            score = 87
            q4 = input("Are you female?\t")
            if q4 == "yes":
                score = 91
                while q4 == "yes":
                    break
            if q4 == "no":
                score = 82
                q5 = input("Are you Baptist?\t")
                if q5 == "yes":
                    score = 89
                    while q5 == "yes":
                        break
                if q5 == "no":
                    score = 78
                    q6 = input("Are you older than 56?\t")
                    if q6 == "yes":
                        score = 86
                        while q6 == "yes":
                            break
                    if q6 == "no":
                        score = 73
                        while q6 == "no":
                            break
        if q3 == "no":
            score = 70
            q4 = input("Are you female?\t")
            if q4 == "yes":
                score = 79
                while q4 == "yes":
                    break
            if q4 == "no":
                score = 62
                while q4 == "no":
                    break
    if q2 == "no":
        score = 43
        q3 = input("Are you Protestant?\t")
        if q3 == "yes":
            score = 1
            q4 = input("Is your family income less than $40,000 per year?\t")
            if q4 == "yes":
                score = 25
                while q4 == "yes":
                    break
            if q4 == "no":
                score = -11
                while q4 == "no":
                    break
        if q3 == "no":
            score = 53
            q4 = input("Have you or a member of your family served in the military?\t")
            if q4 == "yes":
                score = 34
                q5 = input("Are you married?\t")
                if q5 == "yes":
                    score = 20
                    while q5 == "yes":
                        break
                if q5 == "no":
                    score == 48
                    while q5 == "no":
                        break
            if q4 == "no":
                score = 62
                q5 = input("Are you 42 or younger?\t")
                if q5 == "yes":
                    score = 68
                    q6 = input("Is your family income less than $60,000 per year?\t")
                    if q6 == "yes":
                        score = 72
                        while q6 == "yes":
                            break
                    if q6 == "no":
                        score = 61
                        while q6 == "no":
                            break
                if q5 == "no":
                    score = 52
                    q6 = input("Are you an immigrant?\t")
                    if q6 == "yes":
                        score = 42
                        while q6 == "yes":
                            break
                    if q6 == "no":
                        score = 62
                        while q6 == "no":
                            break
            
elif q1 == "no":
    score = -8
    q2 = input("Is religion an important part of your life?\t")
    if q2 == "yes":
        score = -33
        q3 = input("Are you Protestant?\t")
        if q3 == "yes":
            score = -48
            q4 = input("Are you straight?\t")
            if q4 == "yes":
                score = -51
                q5 = input("Are you female?\t")
                if q5 == "yes":
                    score = -41
                    q6 = input("Are you married?\t")
                    if q6 == "yes":
                        score = -50
                        q7 = input("Have you ever been part of a labor union?\t")
                        if q7 == "yes":
                            score = -28
                            while q7 == "yes":
                                break
                        elif q7 == "no":
                            score = -55
                            q8 = input("Are you Baptist?\t")
                            if q8 == "yes":
                                score = -68
                                while q8 == "yes":
                                    break
                            if q8 == "no":
                                score = -50
                                while q8 == "no":
                                    break
                    elif q6 == "no":
                        score = -29
                        q7 = input("Do you live in the south?\t")
                        if q7 == "yes":
                            score = -41
                            while q7 == "yes":
                                break
                        if q7 == "no":
                            q8 = input("Do you have a college degree?\t")
                            if q8 == "yes":
                                score = -8
                                while q8 == "yes":
                                    break
                            if q8 == "no":
                                score = -24
                                while q8 == "no":
                                    break
                elif q5 == "no":
                    score = -63
                    q6 = input("Are you 42 or younger?\t")
                    if q6 == "yes":
                        score = -49
                        q7 = input("Have you or a family member served in the military?\t")
                        if q7 == "yes":
                            score = -57
                            while q7 == "yes":
                                break
                        if q7 == "no":
                            score = -42
                            while q7 == "no":
                                break
                    if q6 == "no":
                        q7 == input("Do you live in the south?\t")
                        if q7 == "yes":
                            score = -75
                            while q7 == "yes":
                                break
                        if q7 == "no":
                            score = -62
                            q8 = input("Have you or a family member served in the military?\t")
                            if q8 == "yes":
                                score = -67
                                while q8 == "yes":
                                    break
                            if q8 == "no":
                                score = -52
                                while q8 == "no":
                                    break
            elif q4 == "no":
                score = 27
                while q4 == "no":
                    break
        elif q3 == "no":
            score = -14
            q4 = input("Are you straight?\t")
            if q4 == "yes":
                score = -18
                q5 = input("Are you Jewish?\t")
                if q5 == "yes":
                    score = 28
                    while q5 == "yes":
                        break
                if q5 == "no":
                    score = -20
                    q6 = input("Are you female?\t")
                    if q6 == "yes":
                        score = -11
                        q7 = input("Are you married?\t")
                        if q7 == "yes":
                            score = -20
                            q8 = input("Do you live in the south?\t")
                            if q8 == "yes":
                                score = -38
                                while q8 == "yes":
                                    break
                            if q8 == "no":
                                score = -13
                                while q8 == "no":
                                    break
                        if q7 == "no":
                            score = 0
                            q8 = input("Have you ever been part of a labor union?\t")
                            if q8 == "yes":
                                score = 17
                                while q8 == "yes":
                                    break
                            if q8 == "no":
                                score = -4
                                while q8 == "no":
                                    break
                    if q6 == "no":
                        score = -31
                        q7 = input("Are you 39 or younger?\t")
                        if q7 == "yes":
                            score = -13
                            q8 = input("Have you ever been part of a labor union?\t")
                            if q8 == "yes":
                                score = 10
                                while q8 == "yes":
                                    break
                            if q8 == "no":
                                score = -21
                                while q8 == "no":
                                    break
                        if q7 == "no":
                            q8 = input("Have you ever been part of a labor union?\t")
                            if q8 == "yes":
                                score = -29
                                while q8 == "yes":
                                    break
                            if q8 == "no":
                                score = -46
                                while q8 == "no":
                                    break
            if q4 == "no":
                score = 27
                q5 = input("Are you female?\t")
                if q5 == "yes":
                    score = 41
                    while q5 == "true":
                        break
                if q5 == "no":
                    score = 16
                    while q5 == "true":
                        break                                               
    elif q2 == "no":
        score = 37
        q3 = input("Are you straight?\t")
        if q3 == "yes":
            score = 30
            q4 = input("Did you attend college?\t")
            if q4 == "yes":
                score = 40
                q5 = input("Are you Protestant?\t")
                if q5 == "yes":
                    score = 3
                    q6 = input("Are you female?\t")
                    if q6 == "yes":
                        score = 28
                        while q6 == "yes":
                            break
                    if q6 == "no":
                        score = -19
                        while q6 == "no":
                            break
                if q5 == "no":
                    score = 46
                    q6 = input("Are you Catholic?\t")
                    if q6 == "yes":
                        score = 14
                        q7 = input("Are you female?\t")
                        if q7 == "yes":
                            score = 29
                            while q7 == "yes":
                                break
                        if q7 == "no":
                            score = 2
                            while q7 == "no":
                                break
                    if q6 == "no":
                        score = 52
                        q7 = input("Are you female?\t")
                        if q7 == "yes":
                            score = 60
                            q8 = input("Do you have a child under 18?\t")
                            if q8 == "yes":
                                score = 44
                                while q8 == "yes":
                                    break
                            if q8 == "no":
                                score = 66
                                while q8 == "no":
                                    break
                        if q7 == "no":
                            score = 42
                            q8 = input("Do you have a college degree?\t")
                            if q8 == "yes":
                                score = 48
                                while q8 == "yes":
                                    break
                            if q8 == "no":
                                score = 31
                                while q8 == "no":
                                    break
            if q4 == "no":
                score = 7
                q5 = input("Are you female?\t")
                if q5 == "yes":
                    score = 25
                    q6 = input("Are you married?\t")
                    if q6 == "yes":
                        score = 15
                        while q6 == "yes":
                            break
                    if q6 == "no":
                        score = 36
                        while q6 == "no":
                            break
                if q5 == "no":
                    score = 36
                    while q5 == "true":
                        break
        if q3 == "no":
            score = 74
            q4 = input("Did you attend college?\t")
            if q4 == "yes":
                score = 79
                while q4 == "yes":
                    break
            if q4 == "no":
                score = 59
                while q4 == "no":
                    break

time.sleep(1.5)

  
survey = input("\n\nHow much of this information would you say that your friends and family know about you or do you willingly share with others? ('all', 'most', 'some')\t")   

time.sleep(1.5)

initialResponse = input("\n\nHow intrusive did you feel as though the survey was on a scale of 1-5 (1 being the least intrusive, 5 being the most)\t")


time.sleep(1)

print("\n\n* * * Calculating * * * \n\n")

time.sleep(2)

print("Based on your answer to these questions, we were able to guess your political affiliation, as well as a numerical score.")
print("The numerical score is the percentage point difference (range: 0-100) in party identification")   

time.sleep(2)   

print("\n\nIn this case, we guessed that you were")                          

if score > 0:
    print("Democrat with a " + str(score) + " percentage point difference in party identification")
    party = "D"
    
if score < 0:
    print("Republican with a " + str(score) + " percentage point differnece in party identification")
    party = "R"
    
time.sleep(1.5)

survey = input("\n\nDo you feel as though our guess is correct? ('yes' or 'no')\t")

time.sleep(1.5)
    

postResponse = input("\n\nNow knowing the results, how intrusive did you feel as though the survey was on a scale of 1-5? (1 being the least intrusive, 5 being the most)\t")


datafile = open("results.txt", "a")
written = str("\n" + str(score) +  "," + party + "," + survey + "," + str(initialResponse) + "," + str(postResponse))
datafile.write(written)
datafile.close()