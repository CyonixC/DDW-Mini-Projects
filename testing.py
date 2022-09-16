import random

def gen_random_int(number, seed):
    random.seed(seed)
    arr = []
    for _ in range(number):
        arr.append(random.randint(0,10))
    return arr

def generate():
    number = 10
    seed = 200

    # call gen_random_int() with the given number and seed
    # store it to the variable array
    arr = gen_random_int(number,seed)

    # convert the items into one single string 
    # the number should be separated by a comma
    # and a full stop should end the string.

    array_str = ", ".join([str(num) for num in arr])
    array_str += "."
    print(array_str)
    array = array_str[:-1].split(", ")
    for outer in range(1,len(array)):
        for inner in range(outer, 0 , -1):
            if array[inner] < array[inner - 1]:
                array[inner], array[inner - 1] = array[inner- 1], array[inner]
    array_str = ", ".join([str(num) for num in array])
    array_str += "."
    print("".join(array_str.split()))

generate()