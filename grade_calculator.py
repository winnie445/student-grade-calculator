
def calculate_grade(average):
    if average >= 80:
        return "Mastery"
    elif average >= 65:
        return "Proficient"
    elif average >= 50:
        return "Competent"
    else:
        return "Not Yet Competent"


def main():
    print("================================")
    print("       GRADE CALCULATOR")
    print("================================")

    name = input("Enter student's name: ")

    try:
        number_of_subjects = int(input("Enter number of subjects: "))

        if number_of_subjects <= 0:
            print("Please enter at least one subject.")
            return

        total = 0

        for i in range(1, number_of_subjects + 1):
            while True:
                try:
                    mark = float(input(f"Enter mark for subject {i} (0-100): "))

                    if 0 <= mark <= 100:
                        total += mark
                        break
                    else:
                        print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

        average = total / number_of_subjects
        grade = calculate_grade(average)

        print("\n========== RESULTS ==========")
        print(f"Student: {name}")
        print(f"Total marks: {total:g}")
        print(f"Average: {average:.2f}%")
        print(f"Grade: {grade}")
        print("=============================")


if __name__ == "__main__":
    main()
