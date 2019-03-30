import os
from git import Repo

from config import Config


class GlobalGitActions():

    @classmethod
    def git_clone_or_pull(self, git_path, branch_name, else_pull=True):
        if not os.path.exists(git_path):
            print(branch_name + " doesn't exists, creating")
            os.makedirs(git_path)
            # Repo.clone_from(Config.git_url, Config.gitpath_with_master)
            Repo.clone_from(url=Config.git_url, to_path=git_path, branch=branch_name)
        elif else_pull:
            print(branch_name + " exists, pulling")
            Repo(path=git_path).remotes.origin.fetch()
            Repo(path=git_path).remotes.origin.pull()
