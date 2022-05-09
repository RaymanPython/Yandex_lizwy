uzed_post_names = [input() for i in range(int(input()))]
new_names = [input() for i in range(int(input()))]
new_post_names = []
for i in range(len(new_names)):
    counter = 0
    for j in range(len(uzed_post_names)):
        if new_names[i] in uzed_post_names[j]:
            counter += 1
    if counter == 0:
        new_post_names.append(new_names[i] + '@untitled.py')
    else:
        new_post_names.append(new_names[i] + str(counter) + '@untitled.py')
    uzed_post_names.append(new_post_names[-1])
print(*new_post_names, sep='\n')
