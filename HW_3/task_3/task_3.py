def read_file(file_path):
    data = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            for line in input_file:
                student, courses = line.split(':')

                courses_list = []
                for course in courses.split(','):
                    course = course.strip()
                    if course:
                        courses_list.append(course.lower())

                data[student.strip()] = courses_list
            return data
    except FileNotFoundError:
        print(f'The file {file_path} was not found')
        return []
    except IOError:
        print(f'An error occurred while reading file: {file_path}')
        return []


def get_students_for_course(file, course_name):
    course_name = course_name.lower()
    students = [student for student, courses in file.items() if course_name in courses]
    return students


def main():
    file = read_file('input.txt')
    course_name = input('Enter course name (attention: the program is not case sensitive): ')
    students = get_students_for_course(file, course_name)

    if students:
        print(f'Students of course "{course_name}": ')
        for student in students:
            print(student)
    else:
        print(f'No students for course "{course_name}": ')


main()

