from git import Repo
import re
import  os.path
from  os import  remove
from shutil import  rmtree
from time import sleep

class GitProject():
    def __init__(self, project_git_url=None):
        if project_git_url:
            self._project_git_url = project_git_url
            self.default_clone_to = './'
            self._project_name = None
            self.repo_obj = None
            self.to_path = self.default_clone_to + self.name_from_url()
            if not  self.repo_obj:
                   self.init_repo_obj()

    def init_repo_obj(self):
        if os.path.exists(self.to_path) and os.path.isdir(self.to_path):
            repo_obj = Repo(self.to_path)
            if isinstance(repo_obj, Repo):
                self.repo_obj = repo_obj
        else:
            self.clone(to_path=self.to_path)

    def show_url(self):
        print(self._project_git_url)

    def name_from_url(self):
            spl_by_slash = re.split('\/+', self._project_git_url)
            if len(spl_by_slash) > 0:
                spl_by_dot = re.split('\.', spl_by_slash[-1])
                if len(spl_by_dot) == 2:
                    return spl_by_dot[0]

    def clone(self, flush_repo=False, to_path=None):
        if to_path:
            self.to_path = to_path
        if os.path.exists(self.to_path) and os.path.isdir(self.to_path) and flush_repo:
            rmtree(self.to_path)
        self.repo_obj = Repo.clone_from(url=self._project_git_url, to_path=self.to_path)


    def add_remote(self, remote_addr=None, remote_name = None):
        if remote_addr and remote_name:
            if self.repo_obj:
                  remotes_names = [remote[0] for remote in self.get_remotes()]
                  if remote_name in remotes_names:
                      self.repo_obj.delete_remote(self.repo_obj.remote(name=remote_name))
                      self.repo_obj.create_remote(name=remote_name, url=remote_addr)
                  else: self.repo_obj.create_remote(name=remote_name, url=remote_addr)

    def get_remotes(self):
        remotes_list = []
        remotes = self.repo_obj.remotes
        for remote in remotes:
            remotes_list.append([remote.name, remote.url])
        return remotes_list

    def pull(self, remote_name=None):
        if remote_name:
            _remote = self.repo_obj.remote(name=remote_name)
            print(type(_remote))
            _remote.pull






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