# Maria Escobar
# File Name: student_gpa_checker.py
#This app accepts student names and GPAs and checks if the student qualifies for the Dean's List or the Honor Roll.
# It will ask for and accept student last names, first names, and GPAs. The program will then check if the GPA meets the 
# criteria for the Dean's List or the Honor Roll and print the corresponding messages. The program stops when the last name 'ZZZ' is entered.
def main():
    while True:
        # Ask for the last name
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        
        # Check if the last name is 'ZZZ' to quit the program
        if last_name == 'ZZZ':
            print("Exiting program.")
            break

        # Ask for the first name
        first_name = input("Enter the student's first name: ")
        
        # Ask for the GPA 
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid input. Please enter a valid GPA.")
            continue
        
        # Check if the student qualifies for the Dean's List
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        
        # Check if the student qualifies for the Honor Roll
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        
        # If GPA does not meet any of the above criteria
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or the Honor Roll.")

# Run the app
if __name__ == "__main__":
    main()
