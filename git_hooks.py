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
        self.repo_obj = None
        self.to_path = self.default_clone_to + self.name_from_url()
        self.repo_obj = self.init_repo_obj()
        if not  self.repo_obj:
            print ('NOT INIT REPO OBJ!!!')

    def init_repo_obj(self):
        if os.path.exists(self.to_path) and os.path.isdir(self.to_path):
            repo_obj = Repo(self.to_path)
            if isinstance(repo_obj, Repo):
                return repo_obj
        else:
            repo_obj = self.clone(to_path=self.to_path)
            return  repo_obj

    def show_url(self):
        print(self._project_git_url)

    def name_from_url(self):
        project_name = re.search('(?<=\/)(\w+)(?=\.git)', self._project_git_url)
        if project_name:
            self._project_name = project_name.group()
        return self._project_name

    def clone(self, flush_repo=False, to_path=None):
        if to_path:
            self.to_path = to_path
        if os.path.exists(self.to_path) and os.path.isdir(self.to_path) and flush_repo:
            rmtree(self.to_path)
        self.repo_obj = Repo.clone_from(url=self._project_git_url, to_path=self.to_path)

    def add_remote(self, remote_addr=None, remote_name = None):
        if remote_addr and remote_name:
            if not self.repo_obj:
                self.repo_obj = Repo(self.to_path)
            if self.repo_obj:
                self.repo_obj.create_remote(remote_name, remote_addr)









#demo_proj.clone(flush_repo=True)
#demo_proj.add_remote('https://msk-dpro-gka003.x5.ru:8443/invoice_discounting/msa-service-ucd.git', 'sinimex')

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