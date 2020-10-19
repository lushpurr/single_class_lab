class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, favourite_language):
        return "I love " + favourite_language
    


# To run the tests:

# python3 run_tests.py

# Tasks
# Create a class called Student that has the properties Name (str) and Cohort (str).
# Create an __init__ method that takes in a name (str) and a cohort (str - e.g "E41", "G19", etc) to initialise the properties when a new student is created.
# Create a talk method that gets the student to talk, returning "I can talk!".
# Create a method, say_favourite_language that takes in a students favourite programming language and returns it as part of a string (eg. student.say_favourite_language("Python") -> "I love Python").
