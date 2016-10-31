

names_list = []

with open('names.txt') as names:
    names_list = [i.replace('"','') for i in list(names)[0].split(',')]

sorted_names = sorted(names_list)

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
alphabet_scores = {i:rating for i,rating in zip(alphabet, range(1,27))}

total_name_score = 0
for index, name in enumerate(sorted_names):
    position = index + 1
    name_score = sum([alphabet_scores[i] for i in name]) * position

    total_name_score += name_score

print(total_name_score)