
import os
from git import Repo

from config import Config

class MainClass():

    available_directories = []

    def __init__(self):
        if not os.path.exists(Config.gitpath_with_master):
            os.makedirs(Config.gitpath_with_master)
            Repo.clone_from(Config.git_url, Config.gitpath_with_master)
        self.run()

    def run(self):
        self.checkoutAndPullBranches()
        non_kotlin_or_text_files, kotlin_files = self.get_files()
        badlines, warninglines, complimentlines = self.check_kotlin_files(kotlin_files)
        print(badlines)
        print(warninglines)
        print(complimentlines)

    def checkoutAndPullBranches(self):
        missing_branches = set([h.name for h in Repo(Config.gitpath_with_master).heads]).difference(self.available_directories)
        print(missing_branches)
        for branch_name in missing_branches:
            if not os.path.exists(Config.gitpath+"/"+branch_name):
                print(branch_name+" doesn't exists, creating")
                Repo.clone_from(url=Config.git_url, to_path=Config.gitpath+"/"+branch_name, branch=branch_name)
            else:
                print(branch_name + " exists, pulling")
                Repo(path=Config.gitpath+"/"+branch_name).remotes.origin.pull()
            self.available_directories.append(branch_name)


    @staticmethod
    def get_files():
        kotlin_files = []
        non_kotlin_or_text_files = []
        for root, dirs, files in os.walk(Config.gitpath):
            [kotlin_files.append(os.path.join(root, file)) for file in files if file.endswith(".kt")]
            [non_kotlin_or_text_files.append(file) for file in files if not file.endswith(".kt") and not file.endswith(".txt") and not file.endswith(".yml")]
        return non_kotlin_or_text_files, kotlin_files

    @classmethod
    def check_kotlin_files(self, kotlin_files):
        badlines = {}
        warninglines = {}
        complimentlines = {}
        print(kotlin_files)
        for file in kotlin_files:
            print(file)
            with open(file, "r") as fp:
                for index, line in enumerate(fp):
                    badlines = self.__add_to_collection(config_collection=Config.bad_words, collection=badlines, file=file, index=index, line=line)
                    warninglines = self.__add_to_collection(config_collection=Config.warning_words, collection=warninglines, file=file, index=index, line=line)
                    complimentlines = self.__add_to_collection(config_collection=Config.compliment_words, collection=complimentlines, file=file, index=index, line=line)
        return badlines, warninglines, complimentlines

    @staticmethod
    def __add_to_collection(config_collection, collection, file, index, line):
        for word in config_collection:
            if word in line:
                if file in collection:
                    collection[file].append([index, word])
                else:
                    collection[file] = [[index, word]]
        return collection

    def value_non_kotlin_files_by_extention(self, non_kotlin_files):
        pass


if __name__ == '__main__':
    # play in loop
    MainClass()