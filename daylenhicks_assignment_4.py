student_name = "Daylen Hicks"
current_gpa = 3.9
study_hours = 19
social_points = 60
stress_level = 80

print("Welcome to My College Life Adventure Game")
print(f"Student: {student_name}")
print(f"GPA: {current_gpa}")
print(f"Study hours: {study_hours}")
print(f"Social points: {social_points}")
print(f"stress_level: {stress_level}")

print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice:")
if choice == "A":
    study_hours = study_hours + 6
    stress_level = stress_level - 10
elif choice == "B":
    study_hours = study_hours + 10
    stress_level = stress_level + 10
elif choice == "C":
    if current_gpa >=3.5:
        study_hours = study_hours + 15
        stress_level = stress_level + 10
    else:
        study_hours = study_hours + 15
        stress_level = stress_level + 25

else:
    print("Sorry, Pick again")
    study_hours = study_hours + 10
    stress_level = stress_level + 10

print("Study Hours:", study_hours)
print("Stress Level:", stress_level)
