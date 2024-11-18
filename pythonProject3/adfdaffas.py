students = [("Алексей", 19), ("Мария", 21), ("Дмитрий", 22), ("Ольга", 20)]
filtered_students = list(filter(lambda x: x[1] > 20, students))
result = [student[0] for student in filtered_students]
print(result)