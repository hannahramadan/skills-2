"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    unique_dict = {}

    words = phrase.split(" ")
    for word in words:
        unique_dict[word] = unique_dict.get(word, 0) + 1

    return unique_dict


def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order.

    Here are a list of melon names and prices:

    Honeydew 2.50
    Cantaloupe 2.50
    Watermelon 2.95
    Musk 3.25
    Crenshaw 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If there are no melons at that price print "None found"

        >>> print_melon_at_price(2.50)
        Cantaloupe
        Honeydew

        >>> print_melon_at_price(2.95)
        Watermelon

        >>> print_melon_at_price(5.50)
        None found
    """

    melons_and_price = {"Honeydew": 2.50,
    "Cantaloupe": 2.50,
    "Watermelon": 2.95,
    "Musk": 3.25,
    "Crenshaw": 3.25,
    "Christmas": 14.25
    }

    matching_price = []

    for melon in melons_and_price:
        if melons_and_price.get(melon) == float(price):
            matching_price.append(melon)
            print(melon)

    if len(matching_price) == 0:
        print("None found")


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    pirate_translation = {"sir": "matey",
    "hotel": "fleabag inn",
    "student": "swabbie",
    "man": "matey",
    "professor": "foul blaggart",
    "restaurant": "galley",
    "your": "yer",
    "excuse": "arr",
    "students": "swabbies",
    "are": "be",
    "restroom": "head",
    "my": "me",
    "is": "be"
    }

    new_list = []
    words = phrase.split(" ")

    for word in words:
        if word in pirate_translation:
            new_list.append(pirate_translation[word])
        else:
            new_list.append(word)

    return_string = " ".join(new_list)

    return return_string


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    first_word = names[0]
    
    new_list = []
    new_list.append(first_word)
    last_letter = first_word[-1]

    names_dict = {}
    names_dict[first_word] = None
    
    i = 0

    while i < len(names):
        if last_letter == names[i][0] and names[i] not in names_dict:
            names_dict[names[i]] = None
            new_list.append(names[i])
            last_letter = names[i][-1]
            i = 0
        else:
            i += 1
    return(new_list)
    
    ##### NOTES AND TESTING BELOW. PLEASE DISREGARD. KEEPING FOR REVIEW.
    # running  = True
    
    # for name in names:
    #     if last_letter == name[0] and name not in names_dict:
    #         names_dict[name] = None
    #         new_list.append(name)
    #         last_letter = name[-1]

    # for i in range (len(names)):
    #         if last_letter == names[i][0] and names[i] not in names_dict:
    #             names_dict[names[i]] = None
    #             new_list.append(names[i])
    #             last_letter = names[i][-1]
    #             i = 0

    # while running == True:
    #     counter = 0
    #     for name in names:
    #         counter += 1
    #         if counter == len(names):
    #             running = False
    #         elif last_letter == name[0] and name not in names_dict:
    #             names_dict[name] = None
    #             new_list.append(name)
    #             last_letter = name[-1]
    #             break
    
    #given list of words
    #add first word to new list
    #add firs word to new dict
    #loop
        #look at last letter of the word [-1]
        #check if any entry in the list begins with that word
        # if yes, check if in dictionary
            #if entry in dictory, continue looking through list
            #if not in dict, add to dict and add to list
