def check_errors(course_input):
    course_no, credits, grade = course_input
    if not course_no.isalnum():
        return "improper course no"
    if not credits.isdigit() or int(credits) not in [1, 2, 4]:
        return "incorrect credit"
    if grade not in ["A+", "A", "A-", "B", "B-", "C", "C-", "D", "F"]:
        return "incorrect grade"
    return None

def calculate_sgpa(courses):
    grades = {"A+": 10, "A": 9, "A-": 8, "B": 7, "B-": 6, "C": 5, "C-": 4, "D": 3, "F": 0}
    total_credits = 0
    total_marks = 0
    for course in courses:
        course_no, credits, grade = course
        credits = int(credits)
        total_credits += credits
        total_marks += grades[grade] * credits
    sgpa = total_marks / total_credits
    return sgpa

def main():
    courses = []
    while True:
        course_input = input("Enter course no, credits, and grade (e.g. CSE101 4 A): ")
        if not course_input:
            break
        course_input = course_input.split()
        error = check_errors(course_input)
        if error:
            print(error)
        else:
            courses.append(course_input)
    courses.sort()
    for course in courses:
        course_no, credits, grade = course
        print(f"{course_no}: {grade}")
    sgpa = calculate_sgpa(courses)
    print(f"SGPA: {sgpa:.2f}")

if __name__ == "__main__":
    main()
