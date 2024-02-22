def main():
    with open("books/frankenstein.txt") as f:
        letter_dict = {}
        letter_list = []
        total_words = 0
        for line in f:
            words = line.split()
            total_words += len(words)
            file_contents = line.lower()
            for letter in file_contents:
                if letter.isalpha():
                    letter_dict[letter] = letter_dict.get(letter, 0) + 1
    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{total_words} words found in the document")
    for key, value in letter_dict.items():   
        new_dict = {'name': key, 'num': value}
        letter_list.append(new_dict)
    letter_list.sort(reverse=True, key=sort_on)
    for letter_entry in letter_list:
        key = letter_entry['name']
        value = letter_entry['num']
        print (f"The '{key}' character was found {value} times")
    print ("--- End report ---")


def sort_on(dict):
    return dict["num"]

main()



