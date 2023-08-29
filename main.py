def get_num_of_words(book_text):
    return len(book_text.split())

def get_num_of_character_appearance(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars



def get_report(file_text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_num_of_words(file_text)} words found in the document")

    char_status_dict = get_num_of_character_appearance(file_text)

    sorted_dict = sorted(char_status_dict.items(), key = lambda item: item[1], reverse = True)

    for char_stat in sorted_dict:
        if char_stat[0].isalpha():
            print(f"The '{char_stat[0]}' character was found {char_stat[1]} times ")

    print("--- End report ---")
    
with open("books/frankenstein.txt", "r") as f:
    file_contents = f.read()
    get_report(file_contents)

