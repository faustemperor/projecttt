employees = [("Иван", 25, "инженер"), ("Анна", 32, "менеджер"), ("Борис", 45, "директор"), ("Мария", 28, "аналитик")]
filtered_employees = list(filter(lambda x: x[1] > 30, employees))
sorted_employees = sorted(filtered_employees, key=lambda x: x[0])
print(sorted_employees)