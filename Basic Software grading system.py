#Course = [] is a temporary variable representing a single subject.
Element = [] #Element is a persistent list storing all the selected subjects for later use in calculations.
AverageGPA = [] #Creates a list to input the AvgGPA of a student
Subjects_Added = False #Creates a locking function for Subjects
Marks_Added = False #Creates a locking function for Marks

def Add_Student_Courses(): #By Irfan
    count = 0  # Start count for dynamic indexing
    while count < Sub:
        # Print available subjects with dynamic indexing
        for index, (Course, Available) in enumerate(subjects.items(), start=1): #Broken :D
            printb(f"{index}. {Course}", Available)

        Number_Sub = input("Choose a subject by number (or type 'exit' to finish): ").strip()

        # Allow the user to exit
        if Number_Sub.lower() == 'exit':
            break

        # Try to convert input to an integer
        try:
            IndexSearch = int(Number_Sub) - 1  # Convert to 0-based index
            Course = list(subjects.keys())[IndexSearch] #Looks for the numbered choice from the line of code above

            # Check if the subject is available
            if subjects[Course]:
                subjects[Course] = False  # Mark subject as selected
                Element.append(Course)  # Add to selected subjects
                count += 1  # Increment the count only when a subject is selected
            else:
                print("This subject has already been selected.")
        except (ValueError, IndexError) as e:
            print("Please choose a valid subject number or type 'exit'.")
    print("You have selected the following subjects:")
    for Course in Element:
        print(f"- {Course}")

def Markings(): #Input for marks By Anis
    for index in range(len(Element)):
        course = Element[index]
        while True:
            try:
                mark = float(input(f"Enter the the subject marks {course} (Course {index}):"))
                Marking.append(mark)
                AverageGPA.append((course, mark))
                break
            except ValueError:
                print("Please input a valid number")
    print("\n>Marks has been added<")

#If is_available is True then it'll print
def printb(subject_str, is_available):
    if is_available:
        print(subject_str)

def Display_Report():
    for course , mark , grade in AverageGPATRUE:
        print(f"\n\n{course, mark, grade}\n")
    print(f"This is {Name}'s GPA: {GPA:.2f}\n\n\n")


# Initialize subjects and their selection states
subjects = {
    "Basic of Software Engineering": True,
    "Ethics": True,
    "German": True,
    "Operating System": True,
    "IT Essentials": True,
    "Discrete Mathematics": True,
    "Effective Communications": True
}

Name = input("What is your name? \n: ")
while True: #Main Code By Wafiq
    print("\n=== Grade Management ===")
    print("1. Add Student Grades \n2. Calculate Average Grade \n3. Determine Letter Grade \n4. Display Report \n5. Exit")

    Terminal = input("Select an option (1-5): ")
    try:
        Terminal = int(Terminal)
        if Terminal == 1:
            print("Hello! This is the GPA Calculator")

            Sub = int(input("How many subjects? \n\n> "))

            #Makes sure the user doesn't go over the available Subjects
            if Sub > len(subjects):
                print("Error: Not Available")
                exit()

            Add_Student_Courses()
            Subjects_Added = True
        elif Terminal == 2:
            print("\n--Enter Subject Marks--\n")
            Marking = []
            Markings()
            Marks_Added = True
        elif Terminal == 3:
            if not Subjects_Added or not Marks_Added:
                print("You must add subjects and marks before calculating grades.")
            else:
                AverageGPATRUE = []
                AvgGrade = []

                for course , mark in AverageGPA: #Unpacks the tuple, Board By Rin
                    if mark in range(80,100):
                        grade = "A"
                        AvgGrade.append(4.0)

                    elif mark in range(60,80):
                        grade = "B"
                        AvgGrade.append(3.0)

                    elif mark in range(50,60):
                        grade = "C"
                        AvgGrade.append(2.0)

                    elif mark in range(40,50):
                        grade = "D"
                        AvgGrade.append(1.0)

                    else:
                        grade = "F"
                        AvgGrade.append(0.0)

                    AverageGPACalc = (course , mark , grade)
                    AverageGPATRUE.append(AverageGPACalc)

                TotalAvgGrade = sum(AvgGrade)
                GPA = TotalAvgGrade / Sub if Sub > 0 else 0.0
                print("Done Grading")

        elif Terminal == 4:
            Display_Report()
        elif Terminal == 5:
            print("Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid option. Try again.")
    except ValueError as ve:
        print(f"\nInvalid input. Please input a valid choice: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")