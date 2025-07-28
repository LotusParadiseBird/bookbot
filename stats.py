def word_count(text):
    total_words = len(text.split())
    return total_words

def character_count(text):
    character_counts = {}
    for c in text:
        lowered = c.lower()
        if lowered not in character_counts:
            character_counts[lowered] = 0
        character_counts[lowered] += 1
    return character_counts

def sort_counts(counts_dict):
    counts_list = []
    for i in counts_dict:
        char_dict = {"char": i,"num": counts_dict[i]}
        counts_list.append(char_dict)
    counts_list.sort(reverse=True, key=sort_by)
    return counts_list
    

def sort_by(characters):
    return characters["num"]
