#Задача: найти годных к службе студентов
def get_inductees(names_of_student: list, birthday_years_of_student: list, genders_of_students: list) -> list:
    corrupted_data = []
    going_to_army_soon = []

    for index in range(len(birthday_years_of_student)):
        if isinstance(birthday_years_of_student[index], int):
            if 18 <= 2021 - birthday_years_of_student[index] < 30 and genders_of_students[index] == 'Male':
                going_to_army_soon.append(names_of_student[index])
        if genders_of_students[index] == 'Male' and birthday_years_of_student[index] is None:
            corrupted_data.append(names_of_student[index])

    print(f'going to army{going_to_army_soon}')
    print(f'corrupted data {corrupted_data}')


names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]

get_inductees(names, birthday_years, genders)