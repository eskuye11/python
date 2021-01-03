def student_rank(students):
    """ This function takes  ('dictionary' or 'list of (name, grade) tuples')
        of students 'name' and 'numeric' grades and Returns the names and
        'letter' grade's as  (student_name, letter_grade) if a student had a single grade
        or (student_name, [letter_grades]) if a student had multiple grades
                Dict returns Dict    and   List returns List

         example_dict = {'Mary': 89, 'Mark': [85, 92], 'John': 100,
         'Tina': 95, 'Sara': (89, 95, 99), 'Kelly': 95}        one grade or more or mix """

    ranks = {range(90, 101): 'A', range(80, 90): 'B', range(70, 80): 'C',
             range(60, 70): 'D', range(0, 60): 'F'}

    if isinstance(students, dict):
        letter_grades = dict()
        for student, grades in students.items():

            all_grades = []       # if the student have more than one grade  .  .  .
            if type(grades) == list or type(grades) == tuple:
                for grade in grades:
                    if type(grade) != str:
                        for rank in ranks:
                            if grade in rank:
                                all_grade = ranks.get(rank)
                                all_grades.append(all_grade)
                    else:
                        all_grades.append('Type-Err! ')
                letter_grades[student] = all_grades
            else:                 # if the student has only a single grade . . .
                if type(grades) != str:
                    for rank in ranks:
                        if grades in rank:
                            results = ranks.get(rank)
                            letter_grades[student] = results
                else:
                    letter_grades[student] = 'Type-Err! '
        return letter_grades

    elif isinstance(students, list):             # Check if it is a list
        if all(isinstance(item, tuple) for item in students):  # to check it is a list of tuples
            try:
                letter_gradeL = []
                for student, grades in students:
                    if type(grades) != str:
                        for rank in ranks:
                            if grades in rank:
                                results = ranks.get(rank)
                                letter_gradeL.append((student, results))
                    else:
                        letter_gradeL.append((student, 'Type-Err! '))
                return letter_gradeL

            except ValueError as e:
                print("list of 'two pair tuples' only ")
        else:
            print(" All items in the list need to be  'tuples'")
    else:
        print("This func only take a 'Dict' or  a 'List of tuple'  ")


# test
class1 = {'Mary': 89, 'Mark': [85, 92], 'John': 100, 'Tina': 95, 'Sara': (89, 95, 99), 'Kelly': 95}
mm = [('mom', 55), ('dad', 70), ('eyo', 89), ('esk', 94), ('Can', 98)]


if __name__ == '__main__':
    # mylist = student_rank(mm)
    # for key in mylist:
    #     print(key)
    print()
    mydict = student_rank(class1)
    for key in mydict.items():
        print(key)