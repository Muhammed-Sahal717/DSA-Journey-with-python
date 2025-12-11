student_name = input("Enter your name: ")

ma = int(input("Enter math mark: "))
sc = int(input("Enter science mark: "))
en = int(input("Enter english mark: "))

run = True

while run:
    if (ma < 0) or (ma > 100) or (sc < 0) or (sc > 100) or (en < 0) or (en > 100):
        print("Invalid marks entered!")
        run = False
    else:
        total = ma + sc + en
        avg = total / 2
        perc = (total / 300) * 100

        print(f"Total = {total}\nAverage = {avg}\nPercentage = {perc}%")

        if perc >= 90:
            print("Grade = A")
        elif perc >= 80:
            print("Grade = B")
        elif perc >= 70:
            print("Grade = C")
        elif perc >= 60:
            print("Grade = D")
        else:
            print("Failed")

        marks = [ma, sc, en]
        i = 0
        for mark in marks:
            i = i + 1
            print(f"Subject {i} mark = {mark}")
        
        subjects = ["Math", "Science", "English"]

        combained = zip(subjects, marks)

        print(list(combained))

    break