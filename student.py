# ==========================================
# PART 1: Welcome & Student Info
# ==========================================
print("*" * 50)
print("       STUDENT GRADE CALCULATOR       ")
print("*" * 50)

while True:


    student_name = input("\nEnter the student's name: ")

    if student_name.lower() == 'quit':
        print("\nExiting the grade calculator. Goodbye!")
        break # Exit the grade calculator if they type 'quit'

    # We will store each subject's data in a list.
    subjects_data = []
    total_marks = 0.0

    # ==========================================
    # PART 2: Collecting Marks (The Loop)
    # ==========================================
    print(f"\n--- Enter Marks for {student_name} ---")
    print("(Type 'done' when you have entered all subjects)")

    while True:
        # Ask for the subject name first
        subject_name = input("\nEnter subject name (or 'done' to finish): ")
    
        if subject_name.lower() == 'done':
            break  # Exit the loop if they type 'done'
        
        # Ask for the mark and convert it to a float so we can do math with it
        mark = float(input(f"Enter the mark for {subject_name} (0-100): "))
    
        # ==========================================
        # PART 3: Grading & Remarks Logic
        # ==========================================
        if mark >= 70 and mark <= 100:
            grade = "A"
            remark = "Excellent"
        elif mark >= 60 and mark <= 69:
            grade = "B"
            remark = "Very Good"
        elif mark >= 50 and mark <= 59:
            grade = "C"
            remark = "Good"
        elif mark >= 40 and mark <= 49:
            grade = "D"
            remark = "Fair"
        elif mark >= 1 and mark <= 39:
            grade = "E"
            remark = "Pass"
        elif mark > 100:
            grade = "Invalid"
            remark = "Invalid mark entered!"
        else:
            grade = "F"
            remark = "Fail"
        
        # Add the mark to our running total
        total_marks += mark
    
        # Save all this information into our list as a dictionary
        subjects_data.append({
            "Subject": subject_name,
            "Mark": mark,
            "Grade": grade,
            "Remark": remark
        })
        print(f"--> Saved: {subject_name} - Grade {grade}")

# ==========================================
# PART 4: Printing the Final Report Card
# ==========================================
# First, check if they actually entered any subjects to avoid a math error
    if len(subjects_data) > 0:
        
        # Calculate the average mark
        average_mark = total_marks / len(subjects_data)
        
        # Determine the overall average grade using the same logic
        if average_mark >= 70 and average_mark <= 100:
            avg_grade = "A"
        elif average_mark >= 60 and average_mark <= 69:
            avg_grade = "B"
        elif average_mark >= 50 and average_mark <= 59:
            avg_grade = "C"
        elif average_mark >= 40 and average_mark <= 49:
            avg_grade = "D"
        elif average_mark >= 1 and average_mark <= 39:
            avg_grade = "E"

        elif average_mark > 100:
            avg_grade = "Invalid"
        else:
            avg_grade = "F"

        # Print the beautifully formatted report card
        print("\n" + "=" * 50)
        print(f"           OFFICIAL REPORT CARD           ")
        print("=" * 50)
        print(f"Student Name : {student_name}")
        print(f"Subjects     : {len(subjects_data)}")
        print("-" * 50)
        
        # We use f-string alignment to create a nice table format for the subjects, marks, grades and remarks.
        print(f"{'SUBJECT':<15} | {'MARK':<6} | {'GRADE':<7} | {'REMARK'}")
        print("-" * 50)
        
        for item in subjects_data:
            print(f"{item['Subject']:<15} | {item['Mark']:<6.1f} | {item['Grade']:<7} | {item['Remark']}")
            
        print("-" * 50)
        print(f"{'AVERAGE MARK':<15} : {average_mark:.1f}")
        print(f"{'OVERALL GRADE':<15} : {avg_grade}")
        print(f"{'REMARK':<15} : {remark}")       
        print("=" * 50)

    else:
        print("\nNo subjects were entered. Cannot generate a report card.")


        