# def print_upper_words(words):
#     for char in words:
#         print(char.upper())
        
def print_upper_words(words, letter1, letter2):
    for word in words:
        if word.startswith(f"{letter1}") or word.startswith(f"{letter2}"):
            print(word)