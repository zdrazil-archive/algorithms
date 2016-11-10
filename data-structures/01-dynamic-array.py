dynamic_array = [0 for x in range(11)]

def insert(input):
    global dynamic_array

    if dynamic_array.count(0) == 0:
        new_dynamic_array =  [0 for x in range(2 * len(dynamic_array) + 1)]
        for id, val in enumerate(dynamic_array):
            new_dynamic_array[id] = val
        dynamic_array = new_dynamic_array

    for i in dynamic_array:
        if dynamic_array[i] == 0:
            dynamic_array[i] = input
            break

def remove():
    global dynamic_array

    if dynamic_array.count(0) > 0.75 * len(dynamic_array):
        new_dynamic_array = [0 for x in range(int(len(dynamic_array) / 2))]
        for index, val in enumerate(new_dynamic_array):
            new_dynamic_array[index] = dynamic_array[index]
        dynamic_array = new_dynamic_array
    
    for index, value in enumerate(dynamic_array):
        if dynamic_array[index] == 0:
            dynamic_array[index - 1] = 0
        elif i == len(dynamic_array):
            dynamic_array[index] = 0

for i in range(21):
    insert(i)

print(len(dynamic_array))
print(dynamic_array)

for i in range(16):
    remove()

print(len(dynamic_array))
print(dynamic_array)
