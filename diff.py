import os
from git import Repo

from config import Config
from global_git_actions import GlobalGitActions


class DiffClass(GlobalGitActions):

    def __init__(self, branch_origin, branch_to_compair):
        GlobalGitActions.git_clone_or_pull(Config.gitpath_with_master, branch_origin)
        GlobalGitActions.git_clone_or_pull(Config.gitpath_with_master, branch_to_compair)
        self.diff(branch_origin, branch_to_compair)

    def diff(self, branch_origin, branch_to_compair):
        repo = Repo(Config.gitpath_with_master)
        commit_dev = repo.commit(branch_to_compair)
        commit_origin_dev = repo.commit(branch_origin)
        diff_index = commit_origin_dev.diff(commit_dev)
        print(diff_index)


if __name__ == '__main__':
    # play in loop
    branch_origin = "master"
    branch_to_compair = "develop"
    DiffClass(branch_origin, branch_to_compair)