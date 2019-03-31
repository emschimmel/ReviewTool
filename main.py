
import os
from git import Repo

from ReviewObject import ReviewObject
from config import Config
from global_git_actions import GlobalGitActions


class MainClass(GlobalGitActions):

    available_directories = []
    reviews = []

    def __init__(self):
        GlobalGitActions.git_clone_or_pull(Config.gitpath_with_master, Config.git_base_branch)
        self.run()

    @classmethod
    def run(self):
        self.checkoutAndPullBranches()
        for branch in self.available_directories:
            review = ReviewObject()
            review.branch = branch
            review.non_kotlin_or_text_files, review.kotlin_files = self.get_files(branch)
            review.badlines, review.warninglines, review.complimentlines = self.check_kotlin_files(review.kotlin_files)
            review.print_object()
            self.reviews.append(review)

    @classmethod
    def checkoutAndPullBranches(self):
        missing_branches = set(GlobalGitActions.get_remote_branches()).difference(self.available_directories)
        for branch_name in missing_branches:
            GlobalGitActions.git_clone_or_pull(Config.gitpath+"/"+branch_name, branch_name)
            self.available_directories.append(branch_name)

    @staticmethod
    def get_files(branch):
        kotlin_files = []
        non_kotlin_or_text_files = []
        for root, dirs, files in os.walk(Config.gitpath+"/"+branch):
            if not any(word in root for word in Config.directories_to_ignore):
                [kotlin_files.append(os.path.join(root, file)) for file in files if file.endswith(".kt")]
                [non_kotlin_or_text_files.append(file) for file in files if not file.split('.')[-1] in Config.allowed_file_extentions]
        return non_kotlin_or_text_files, kotlin_files

    @staticmethod
    def check_kotlin_files(kotlin_files):
        badlines = {}
        warninglines = {}
        complimentlines = {}
        for file in kotlin_files:
            with open(file, "r") as fp:
                for index, line in enumerate(fp):
                    badlines = GlobalGitActions._add_to_collection(config_collection=Config.bad_words, collection=badlines, file=file, index=index, line=line)
                    warninglines = GlobalGitActions._add_to_collection(config_collection=Config.warning_words, collection=warninglines, file=file, index=index, line=line)
                    complimentlines = GlobalGitActions._add_to_collection(config_collection=Config.compliment_words, collection=complimentlines, file=file, index=index, line=line)
        return badlines, warninglines, complimentlines




if __name__ == '__main__':
    # play in loop
    MainClass()