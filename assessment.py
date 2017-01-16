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
