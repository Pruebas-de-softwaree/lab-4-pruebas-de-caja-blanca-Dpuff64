def process_grades(students):
    passed = []
    failed = []
    overall_average = 0
    total_grades = 0
    counter = 0

    for student in students:
        name = student['name']
        grades = student['grades']
        
        if grades == None:  
            print(f"Student {name} has no grades")
            continue
        
        average = sum(grades) / len(grades)
        total_grades += average
        counter += 1

        if average > 70:  
            passed.append(name)
        elif average >= 50:
            print(f"{name} is in recovery")
        else:
            failed.append(name)
    
    if counter > 0:  
        overall_average = total_grades / counter
    
    return {
        'passed': passed,
        'failed': failed,
        'overall_average': round(overall_average, 2)
    }


if __name__ == "__main__":
    students = [
    {'name': 'Ana', 'grades': [90, 100]},  #Entra la sentencia if average > 70
    {'name': 'David', 'grades': None}      #Entra la sentencia if grades == None
]                                          #Entra la sentencia if counter > 0 por tener mas de 0 estudiantes

    result = process_grades(students)
    print("\nFinal processing result:")
    print(result)
