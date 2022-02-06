#Задача вывести студентов по убыванию количества суммы балов учитывая экстра баллы

import operator
candidates = [
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1}
]

top_candidates = {}

for cand in candidates:     # Убираем вложенность словарей
    cand['scores']['extra_scores'] = cand['extra_scores']
    top_candidates[cand['name']] = cand['scores']

scores = {}     # создаём словврь только с ключами(именами студентов) и суммой значений по всем предметам
for item in top_candidates:
        for value in top_candidates[item]:
            if item not in scores:
                scores[item] = top_candidates[item][value]
            else:
                scores[item] += top_candidates[item][value]

sorted_tuples = list(reversed(sorted(scores.items(), key=operator.itemgetter(1)))) # сортирую по значению от наибольшего к наименьшему

for student in range(20):   # вывожу первые 20 записей по кол-ву баллов
    print(sorted_tuples[student])
