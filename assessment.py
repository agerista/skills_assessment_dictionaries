<<<<<<< HEAD
"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    A. Abstraction

        This hides details that we do not need.

    B. Encapsulation

        This keeps everything together.

    C.  Polymorphism

        Interchangeability of components.

2. What is a class?

    A class defines a data type.  It tries to define a real life thing.  If we had
    a class person, it would contain: (first name, last name, age, address,
    profession, marital status), etc.


3. What is an instance attribute?

    Instance attributes belong only to the instance, not the class, and are unique

4. What is a method?

    A function inside of a class

5. What is an instance in object orientation?

    An instance is one example of an object.  For our person class, an
    instance would be: (Bob, Jones, 52, 123 Main Street, Plumber, Married).

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

    A class attribute applies to the entire class, an instance attribute only
    applies to that instance.

    We could set a class attribute to (species: homosapien)

    If Bob was a Neandrathal, we could override the class attribute homosapien
    and set (species: Neandrathal). This would only apply to Bob, not the entire
    person class.

"""

# Parts 2 through 5:
# Create your classes and class methods

#Part 2: Classes and Init Methods.
#1 Student - Students can have first and last names and addresses.


class Student(object):
    """Defines a student with first name, last name, and address."""

    def __init__(self, first_name, last_name, address=None):

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Questions include a question and a correct answer. """

    def __init__(self, question, correct_answer):

        self.question = question
        self.correct_answer = correct_answer

    # Part 3: Methods
    # Add a method to the Question class
    def ask_and_evaluate(question, correct_answer):
        """Prints the question to the console and prompts the user for an answer.
        It should return True or False depending on whether the correct answer
        matches the users answer.
        """

        for q in question:
            print question
            answer = raw_input("Enter your answer: ")
            if answer == correct_answer:
                return True

            else:
                return False

#3 Exam -


class Exam(Question):
    """Takes name as a type of exam, not a user name
     and questions as a list of questions.
     """

     #should this be here?

    def __init__(self, name, questions):
        self.name = name
        self.questions = questions = []

    # Part 3: Methods
    # 1 Add a method to the Exam class

    def add_question(self, question, correct_answer):
        """Takes a question and a correct_answer as parameters, makes a
        Question from those, and adds it to the exams list of questions.
        """

        self.questions.append(Question(question, correct_answer))

    # Part 3: Methods
    # 3 Add a method to the Exam class

    # def administer_exam(add_question):
    #     """Administers all of the exams questions, and returns the users
    #     score (as a decimal percentage) at the end.
    #     """

    #     score = 0.0

    #     for question in add_question:

    #         super(Exam, self).ask_and_evaluate(self, question, correct_answer)

    #         if answer is True:
    #             score += 10

    #         else:
    #             score += 0

    #         percent = score / len(questions)

    #         return "You scored {0} %" .format(percent)


# Part 5: Inheritance
# class Quiz(Exam):
#     """A quiz is like an exam, but is pass/fail.  When you call the administer
#     method on a quiz, it should only return True if you passed or False if you
#     failed.
#     """

#     super(Quiz, self).__init__(self, "quiz", questions)
#     Exam.administer_exam([questions])
#     administer([questions])


#     if name == "quiz" or name == "Quiz":

#         if percent > 50:
#             print "Pass"

#         else:
#             print "Fail"


# def take_test(Exam, Student):

#     """takes an exam and a student as parameters, administers the exam, and
#     assigns the score to the student instance as a new attribute called score,
#     print a message to the screen indicating the score.
#     """

#     administer_exam(add_question)
#     print "{0} {1} scored {2}%" .format(first_name, last_name, score)
#     student.score = score




# def example(Exam, Student):
#     """Creates an exam, adds a few questions to the exam (these should be part
#     of the function; no need to prompt the user for questions), creates a
#     student, administers the test for that student using the take test function
#     you just wrote.



#     """

#     add_question("What color is the sky?", "Blue")
#     take_test("final", "Balloonicorn Jones")
=======
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
    word_counts = {}
    phrase = phrase.split()

    for word in phrase:

        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    melons = {
        "Watermelon": 2.95,
        "Cantaloupe": 2.50,
        "Musk": 3.25,
        "Christmas": 14.25,
    }

    if melon_name in melons:
        return melons.get(melon_name)

    else:
        return "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    word_lengths = {}
    for word in words:

        if len(word) not in word_lengths:
            word_lengths[len(word)] = [word]

        else:
            word_lengths[len(word)].append(word)
            word_lengths[len(word)].reverse()


    
    return sorted(word_lengths.items())

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

    english_to_pirate = {
        "sir": "matey",
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
        "is": "be",
    }

    phrase = phrase.split()
    translation = ""

    for word in phrase:

        if word in english_to_pirate:
            translation = translation + " " + english_to_pirate[word]

        else:
            translation = translation + " " + word

    return translation.strip()


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

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    kid_game_dict = {}

    for name in names:

        if name[0] not in kid_game_dict:
            kid_game_dict[name[0]] = [name]

        else:
            kid_game_dict[name[0]].append(name)

    results = []
    results.append(names[0])
    i = 0

    for key in kid_game_dict:
        key = results[-1][-1]
        next = kid_game_dict[key][0]

        if next not in results:
            results.append(next)

        elif next in results:
            i += 1
            next = kid_game_dict[key][i]
            results.append(next)

    return results

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
>>>>>>> fad09d59a8508ae3d2a0355e1c6c3e2a501b13f7
