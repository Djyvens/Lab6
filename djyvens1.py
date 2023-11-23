def remove_spaces_and_unique_chars(input_string):
    string_without_spaces = ""
    for char in input_string:
        if char != " ":
            string_without_spaces += char
    unique_characters = ""
    for char in string_without_spaces:
        count = 0
        for inner_char in string_without_spaces:
            if inner_char == char:
                count += 1
        if count == 1:
            unique_characters += char
    return unique_characters
user_input = input("Введите строку: ")
result = remove_spaces_and_unique_chars(user_input)
print("Результат:", result)