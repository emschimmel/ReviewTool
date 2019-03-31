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
            repo = Repo(path=git_path)
            repo.remotes.origin.fetch()
            repo.git.checkout(branch_name)
            repo.remotes.origin.pull()

    @staticmethod
    def get_remote_branches():
        remotes = Repo(Config.gitpath_with_master).git.branch('-r').split('\n')
        remotes.pop()
        return [remote.split('/')[-1] for remote in remotes]

    @staticmethod
    def _add_to_collection(config_collection, collection, file, index, line):
        for word in config_collection:
            if word in line:
                if file in collection:
                    collection[file].append([index, word])
                else:
                    collection[file] = [[index, word]]
        return collection