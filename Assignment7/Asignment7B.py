#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment7B

def calculate_average(scores):
    return round(sum(scores)/len(scores),2)

def grade_scale(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'

    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


def main():
    students = []

    while True:

        num_students = int(input("Enter the number of students: "))

        for i in range(num_students):
            print(f"\nEnter the details for student {i+1}:")

            name = input("Enter student name: ")

            scores = []
            subjects = ['Math', 'English', 'Science']

            for subject in subjects:
                while True:
                    try:
                        score = float(input(f"Enter score for {subject}: "))
                        if 0 <= score <=100:
                            scores.append(score)
                            break
                        else:
                            print("Score must be between 0 and 100.")
                    except ValueError:
                        print("Invalid input, please enter a number")
            total_score = sum(scores)
            avg = round((calculate_average(scores)),2)
            grade = grade_scale(avg)
            status = 'Pass' if grade != 'F' else 'Fail'

            print(f"Total score: {total_score} \nAverage score: {avg}")
            print(f"Grade: {grade}")
            print(f"Status: {status}")

            student = {
                "name": name,
                "scores": scores,
                "total": total_score,
                "average": avg,
                "grade": grade_scale(avg),
                "status": status
            }
            students.append(student)

        print()
        break

    print("=============================="
          "\n      Summary Report       "
          "\n==============================")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Scores: {student['scores']}")
        print(f"Total: {student['total']}")
        print(f"Average: {student['average']}")
        print(f"Grade: {student['grade']}")
        print(f"Status: {student['status']}")
        print("")

    if students:
        class_average = sum(s['average'] for s in students) / len(students)
        top_student = max(students, key=lambda x: x['average'])
        passed = sum(1 for s in students if s['status']=="Pass")
        failed = len(students) - passed

        print(f"\nClass Average: {class_average}")
        print(f"Students Passed: {passed}")
        print(f"Students Failed: {failed}")
        print(f"Top Student: {top_student['name']}")

if __name__ == "__main__":
    main()