from datetime import datetime
  
class ReviewObject(object):
    time = ""
    branch = ""
    badlines = []
    warninglines = []
    complimentlines = []
    kotlin_files = []
    non_kotlin_or_text_files = []

    def __init__(self):
        self.time = datetime.now()
        self.branch = ""
        self.badlines = []
        self.warninglines = []
        self.complimentlines = []
        self.kotlin_files = []
        self.non_kotlin_or_text_files = []

    def print_object(self):
        print("moment: "+self.time.__str__())
        print("branch: "+self.branch)
        print("#### kotlin files ####")
        for file in self.kotlin_files:
            print(file)
        # print(self.kotlin_files)
        print("#### non kotlin files ####")
        for file in self.non_kotlin_or_text_files:
            print(file)
        # print(self.non_kotlin_or_text_files)
        print("#### compliments ####")
        for line in self.complimentlines:
            print(line)
            for item in self.complimentlines[line]:
                print(item)
        # print(self.complimentlines)
        print("#### warnings ####")
        for line in self.warninglines:
            print(line)
            for item in self.warninglines[line]:
                print(item)
        # print(self.warninglines)
        print("#### bad lines ####")
        for line in self.badlines:
            print(line)
            for item in self.badlines[line]:
                print(item)
        # print(self.badlines)
