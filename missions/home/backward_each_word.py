import re


def backward_string_by_word(text: str) -> str:
    print(f"text: '{text}'")
    return_text = ""
    text_list = re.split(r"(\s+)", text)
    print(f"split text list: {text_list}")
    for i in range(len(text_list)):
        reversed_word = ""
        for character in reversed(text_list[i]):
            reversed_word += character
        return_text += reversed_word

    print(f"return_text: '{return_text}'\n")
    return return_text


if __name__ == "__main__":
    print("Example:")
    print(backward_string_by_word(""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word("") == ""
    assert backward_string_by_word("world") == "dlrow"
    assert backward_string_by_word("hello world") == "olleh dlrow"
    assert backward_string_by_word("hello   world") == "olleh   dlrow"
    assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"
    assert backward_string_by_word("olleH Hello") == "Hello olleH"
    print("Coding complete? Click 'Check' to earn cool rewards!")
