def count_words(text):
    split_text = text.split()
    num_words = 0
    for word in split_text:
        num_words +=1
    return num_words

def get_character_counts(text):
    character_counts={}
    for char in text:
        lowered_char = char.lower()
        if (lowered_char in character_counts):
            character_counts[lowered_char] += 1
        else:
            character_counts[lowered_char] = 1
    return character_counts

def sort_char_counts(dict):
    char_list = []
    for key in dict:
        if  key.isalpha():
                list_dict={}
                list_dict['char'] = key
                list_dict['num'] = dict[key]
                char_list.append(list_dict)
    char_list.sort(key=lambda item:item['char'])
    return char_list