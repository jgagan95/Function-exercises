#i dont know what this was

def test(string1, string2):
    my_word = list(string1.split(' '))
    instance = list(string2).count(my_word)
    if instance == 0:
        return 0

    return instance
    

#course answer

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())
