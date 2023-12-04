with open("file.txt", "r") as file:
    data = file.readlines()

groups = {}
am = int(input('Введите количество групп: '))

current_group = None
for line in data:
    line = line.strip()

    for i in range(1, am + 1):
        if line.startswith(f"{i} группа"):
            current_group = i
            groups[current_group] = {"сумма": 0, "среднее": 0, "участники": []}
            break

    else:
        parts = line.split()
        if len(parts) >= 2:
            participant, score = parts[0], int(parts[1])
            groups[current_group]["участники"].append((participant, score))
            groups[current_group]["сумма"] += score

max_group = max(groups.items(), key=lambda x: x[1]["сумма"])
print(f"Группа {max_group[0]} набрала наибольшее количество баллов!")
print(f"Сумма баллов: {max_group[1]['сумма']}")
print(f"Среднее арифметическое баллов: {max_group[1]['сумма'] / len(max_group[1]['участники'])}")

with open("file.txt", "w+") as file:
    for group, info in groups.items():
        file.write(f"Группа {group}:\n")
        for participant, score in info["участники"]:
            file.write(f"{participant} {score}\n")
        file.write(f"{info['сумма']} {info['сумма'] / len(info['участники'])}\n")