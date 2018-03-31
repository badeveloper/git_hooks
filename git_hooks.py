from git import Repo
import re
import  os.path
from  os import  remove
from shutil import  rmtree

class GitProject():
    def __init__(self, project_git_url=None):
        self._project_git_url = project_git_url
        self.default_clone_to = './'
        self._project_name = None
    def show_url(self):
        print(self._project_git_url)

    def name_from_url(self):
        project_name = re.search('(?<=\/)(\w+)(?=\.git)', self._project_git_url)
        if project_name:
            self._project_name = project_name.group()
        return self._project_name

    def clone(self, flush_repo=False, to_path=None):
        if not to_path:
            self.to_path = self.default_clone_to +  self.name_from_url()
        else:
            self.to_path = to_path

        if os.path.exists(self.to_path) and os.path.isdir(self.to_path) and flush_repo:
            rmtree(self.to_path)

        _clone = Repo.clone_from(url=self._project_git_url, to_path=self.to_path)
        print(_clone)





project_url='https://github.com/badeveloper/testproject.git'

demo_proj = GitProject(project_git_url=project_url)
demo_proj.show_url()
print(demo_proj.name_from_url())
demo_proj.clone(flush_repo=True)

# #proj = GitProject(project_http_url='https://github.com/badeveloper/testproject.git')
# #proj.show_url()
# project_http_url='https://github.com/badeveloper/testproject.git'
# #demo_repo = Repo.clone_from(url=project_http_url, to_path='./testproject')
# cloned_repo = Repo('./testproject')
#
# add_remote = cloned_repo.cre
#
# check = cloned_repo.__class__ is Repo
# print(check)