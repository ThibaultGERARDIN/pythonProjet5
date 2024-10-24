students = {
    "Alice": {"Mathematiques": 90, "Francais": 80, "Histoire": 95},
    "Bob": {"Mathematiques": 75, "Francais": 85, "Histoire": 70},
    "Charlie": {"Mathematiques": 88, "Francais": 92, "Histoire": 78},
}


def main():
    student_name = input("Entrez le nom de l'étudiant : ")
    if student_name in students:
        print(
            f"Notes de {student_name} :\n"
            f"Mathématiques : {students[student_name]["Mathematiques"]}\n"
            f"Français : {students[student_name]["Francais"]}\n"
            f"Histoire : {students[student_name]["Histoire"]}\n"
        )
        student_mean = (
            students[student_name]["Mathematiques"]
            + students[student_name]["Francais"]
            + students[student_name]["Histoire"]
        ) / 3
        print(f"Moyenne de l'étudiant {student_name} : {student_mean}")
    else:
        print(f"L'étudiant {student_name} n'existe pas.")


if __name__ == "__main__":
    main()
