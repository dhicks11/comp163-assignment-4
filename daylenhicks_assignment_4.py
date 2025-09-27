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

study_options = ["Programming", "Math", "English", "History"]

print("\nChoose a subject to study:")
print("Options:", study_options)

choice = input("Your choice:")

if choice in study_options:
    print("Great! Your choice is:", choice)

    if choice == "Programming" or choice == "Math":
        current_gpa = current_gpa + 0.3
        social_points = social_points - 10
        print(f"Your gpa now is {current_gpa}")
        print(f"Your social points: {social_points}")
    elif choice == "English" and current_gpa >= 2.5:
        current_gpa = current_gpa + 0.1
        social_points = social_points + 10
    else:
        stress_level  = stress_level + 15
elif choice not in study_options:
    print("Invalid choice, you lose social points & study hours :(")
    study_hours = study_hours - 5
    social_points = social_points - 5

print("\nWAIT")
print("There is a big party on campus tonight :)")
print("Do you want to slide?")
print("PS....All your friends are going")
print("Options: Yes or No")

party_choice = input("Your choice (Yes/no): ")

if party_choice is not [] and party_choice is ["Yes"]:
    print("You had a blast!")
    social_points = social_points + 20
    stress_level = stress_level - 10
    if social_points > 60:
        print("But...You partied way too hard, got drunk and lost focus for your final.")
        current_gpa = current_gpa - 0.3
else:
    print("You decided to stay in and study more for your final.")
    study_hours = study_hours + 3
    stress_level = stress_level + 2

print("\nFinal Exam Approach:")
print("1) Study VERY HARD")
print("2) Study lightly")
print("3) Go over one thing and Just Wing IT!")

study_choice = ("1, 2, 3")

if study_choice is not None and study_choice != "":
    if study_choice == "1":
        if current_gpa >= 3.7:
            print("Congratulations! You have passed with flying colors :)")
            current_gpa = current_gpa + 0.4
            stress_level = stress_level - 25 #passing takes a lot of stress off
    else:
        print("Sorry, you put in immense effort. Manage your time a little better next time.")
        current_gpa = current_gpa + 0.1
        stress_level = stress_level + 5
elif study_choice == "2":
    print("Good job, you scored pretty decently!")
    current_gpa = current_gpa + 0.1
    stress_level = stress_level -5
elif study_choice == "3":
    print("You failed, focus on your studies more next time!")
    current_gpa = current_gpa - 0.5 #GPA penalty for poor preparation
    stress_level = stress_level + 25
else:
    print("Invalid choice, Try again")

# FINAL STATS DISPLAY
print("\n=== Final Statistics ===")
print(f"GPA: {current_gpa}")
print(f"Study hours: {study_hours}")
print(f"Social points: {social_points}")
print(f"Stress Levels:  {stress_level}")
