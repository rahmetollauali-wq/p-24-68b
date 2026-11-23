def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def format_report(data):
    report = []
    for item in data:
        avg = calculate_average(item["scores"])
        line = f"{item['name']}: средний балл = " + avg
        report.append(line)
    return "\n".join(report)


students = [
    {"name": "Алиса", "scores": [5, 4, 5]},
    {"name": "Боб", "scores": []},
    {"name": "Кира", "scores": [3, 4]},
]

print(format_report(students))
