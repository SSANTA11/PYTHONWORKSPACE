def student_info(name, age, grade="Not assigned", *subjects, **contact):
    print(f'Name: {name}')
    print(f'Age: {age}')
    print(f'Grade: {grade}')
    print(f'Subjects: {", ".join(subjects)}')
    print('Contact information:')
    for key, value in contact.items():
        print(f'    {key}: {value}')

# 함수 호출 예시
student_info('Alice', 20, 'Sophomore', 'Math', 'Science', email='alice@example.com', phone='123-456-7890')
