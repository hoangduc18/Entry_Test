import json


# Word count dictionary
def def_word_cnt(input):
    words_array = input.split()
    words_dict = {}
    for word in words_array:
        if words_dict.get(word) is not None:
            word_cnt = words_dict.get(word)
            word_cnt += 1
            words_dict.update({word: word_cnt})
        else:
            words_dict[word] = 1
    try:
        with open("result.json", "w") as file:
            json.dump(words_dict, file)
        return "success"
    except Exception as error:
        print(error)


print(def_word_cnt("hello i am Duc hello"))


# Generate 100 files result.json without using loop
def recursive_file_generator(count):
    if count <= 100:
        file_name = f"result_{count}"
        f = open(f"{file_name}.json", "x")
        f.close()
        count += 1
        recursive_file_generator(count)


recursive_file_generator(1)
