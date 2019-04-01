import os
from git import Repo

from ReviewObject import ReviewObject
from config import Config
from global_git_actions import GlobalGitActions


class DiffClass(GlobalGitActions):

    def __init__(self, branch_origin, branch_to_compair):
        GlobalGitActions.git_clone_or_pull(Config.gitpath_with_master, branch_origin)
        GlobalGitActions.git_clone_or_pull(Config.gitpath_with_master, branch_to_compair)
        self.run(branch_origin, branch_to_compair)

    def run(self, branch_origin, branch_to_compair):
        review = ReviewObject()
        review.branch = branch_to_compair

        files, review.badlines, review.warninglines, review.complimentlines = self.diff(branch_origin, branch_to_compair)

        review.kotlin_files = [file for file in files if file.endswith(".kt")]
        review.non_kotlin_or_text_files = [file for file in files if not file.split('.')[-1] in Config.allowed_file_extentions]
        review.print_object()

    def diff(self, branch_origin, branch_to_compair):
        repo = Repo(Config.gitpath_with_master)
        commit_dev = repo.commit(branch_to_compair)
        commit_origin_dev = repo.commit(branch_origin)
        diff_index = commit_origin_dev.diff(commit_dev, create_patch=True)
        # print(diff_index)
        badlines = {}
        warninglines = {}
        complimentlines = {}
        files = []
        for diff in diff_index:
            diff_str = str(diff)
            file = ""
            for index, line in enumerate(diff_str.splitlines()):
                if index == 0:
                    file = line
                    files.append(line)
                    continue
                if line.startswith("+"):
                    badlines = GlobalGitActions._add_to_collection(config_collection=Config.bad_words,
                                                                   collection=badlines, file=file, index=line,
                                                                   line=line)
                    warninglines = GlobalGitActions._add_to_collection(config_collection=Config.warning_words,
                                                                       collection=warninglines, file=file, index=line,
                                                                       line=line)
                    complimentlines = GlobalGitActions._add_to_collection(config_collection=Config.compliment_words,
                                                                          collection=complimentlines, file=file,
                                                                          index=line, line=line)
                # print(line)

        return files, badlines, warninglines, complimentlines
        # for diff_item in diff_index.iter_change_type('M'):
        #     print("A blob:\n{}".format(diff_item.a_blob.data_stream.read().decode('utf-8')))
        #     print("B blob:\n{}".format(diff_item.b_blob.data_stream.read().decode('utf-8')))

if __name__ == '__main__':
    branch_origin = "develop"
    branch_to_compair = "feature/31699"
    DiffClass(branch_origin, branch_to_compair)
