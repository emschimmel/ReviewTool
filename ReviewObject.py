
class ReviewObject(object):
    time = ""
    branch = ""
    badlines = []
    warninglines = []
    complimentlines = []
    kotlin_files = []
    non_kotlin_or_text_files = []

    def __init__(self):
        self.time = ""
        self.branch = ""
        self.badlines = []
        self.warninglines = []
        self.complimentlines = []
        self.kotlin_files = []
        self.non_kotlin_or_text_files = []

    def print_object(self):
        print("branch: "+self.branch)
        print("kotlin files")
        print(self.kotlin_files)
        print("non kotlin files")
        print(self.non_kotlin_or_text_files)
        print("compliments")
        print(self.complimentlines)
        print("warnings")
        print(self.warninglines)
        print("bad lines")
        print(self.badlines)