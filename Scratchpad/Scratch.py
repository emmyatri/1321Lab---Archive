def calculate_average(scores):
    """Calculate the average of a list of scores"""
    return sum(scores) / len(scores)

def get_grade(avg):
    """Determine letter grade based on average score"""
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
    # List to store all student dictionaries
    students = []

    while True:
        # Get student name
        name = input("\nEnter student name (or 'done' to finish): ")
        if name.lower() == 'done':
            break

        # Get scores for three subjects
        scores = []
        subjects = ['first', 'second', 'third']

        for subject in subjects:
            while True:
                try:
                    score = float(input(f"Enter {subject} subject score (0-100): "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Score must be between 0 and 100. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        # Calculate total and average
        total_score = sum(scores)
        average_score = calculate_average(scores)

        # Get letter grade
        grade = get_grade(average_score)

        # Determine pass/fail status
        status = "PASS" if grade != 'F' else "FAIL"

        # Create student dictionary and add to list
        student = {
            "name": name,
            "scores": scores,
            "total": total_score,
            "average": average_score,
            "grade": grade,
            "status": status
        }
        students.append(student)

    # Display results
    print("\n=== Student Performance Report ===")

    # Display individual student information
    for student in students:
        print(f"\nStudent: {student['name']}")
        print(f"Scores: {student['scores']}")
        print(f"Total: {student['total']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")
        print(f"Status: {student['status']}")

    # Calculate and display class statistics
    if students:
        class_average = sum(s['average'] for s in students) / len(students)
        passed_students = sum(1 for s in students if s['status'] == "PASS")
        failed_students = len(students) - passed_students

        # Find top performing student
        top_student = max(students, key=lambda x: x['average'])

        print("\n=== Class Statistics ===")
        print(f"Class Average Score: {class_average:.2f}")
        print(f"Number of students who passed: {passed_students}")
        print(f"Number of students who failed: {failed_students}")
        print(f"Top performing student: {top_student['name']} (Average: {top_student['average']:.2f})")

if __name__ == "__main__":
    main()