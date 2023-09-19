sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 5000}
}

for emp in sample_dict:
    sample_dict[emp]['salary'] *= 1.05

print(sample_dict)
