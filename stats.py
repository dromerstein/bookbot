def count_book_words(t):
    words=t.split()
    count=len(words)
    return(count)

def count_char(t):
    letters= {}
    char_list=list(t)
    for c in char_list:
        lc=c.lower()
        if lc in letters:
             letters[lc] = letters[lc]+1
        else:
             letters[lc] = 1
    return(letters)

def sort_chars_by_count(char_count):
    # Create an empty list to store our dictionaries
    chars_list = []
    
    # Loop through each character and its count in the dictionary
    for char, count in char_count.items():
        # Create a dictionary for this character and add it to our list
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    
    # Define a function to tell sort() which value to use
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list from highest count to lowest
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
