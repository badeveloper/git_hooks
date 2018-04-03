from git import Repo, Head, Remote, cmd
import re
import  os.path
from  os import  remove
from shutil import  rmtree
from time import sleep
import  subprocess

class GitProject():
    def __init__(self, project_git_url=None):
        if project_git_url:
            self._project_git_url = project_git_url
            self.default_clone_to = 'C:/Users/ig.yurev/temp/'
            self._project_name = None
            self.to_path = self.default_clone_to + self.name_from_url()
            self.work_dir = os.path.abspath(self.to_path)

    def clone_bare(self, refresh=False):
        if  refresh and os.path.isdir(self.to_path):
           rmtree(self.to_path)
        if not  os.path.exists(self.work_dir):
            cmd_args = ['git', 'clone', '--bare', self._project_git_url, self.to_path]
            bare_clone = subprocess.check_output(cmd_args, shell=True)
            for line in bare_clone.decode().split('\n'):
                print(line)
        else: print('Repo already cloned!')

    def get_remotes(self):
        _remotes = {}
        cmd_args = ['cd',  self.work_dir, '&&', 'git', 'remote',  '-v']
        remotes = subprocess.check_output(cmd_args, shell=True)
        for line in remotes.decode().split('\n'):
            spl_line = re.split('\s+', line)
            if len(spl_line) > 1:
                remote_name = spl_line[0]
                remote_url = spl_line[1]
                one_remote = {remote_name : remote_url}
                _remotes.update(one_remote)
        return  _remotes

    def add_remote(self, name=None, url=None):
         if name and url:
             exists = self.get_remotes()
             if exists.get(name):
                 cmd_args = ['cd',  self.work_dir, '&&', 'git', 'remote', 'set-url', name,  url]
                 change = subprocess.check_output(cmd_args, shell=True)
                 for line in change.decode().split('\n'):
                    print(line)
             else:
                 cmd_args = ['cd', self.work_dir, '&&', 'git', 'remote', 'add', name, url]
                 add = subprocess.check_output(cmd_args, shell=True)
                 for line in add.decode().split('\n'):
                     print(line)

    def name_from_url(self):
        spl_by_slash = re.split('\/+', self._project_git_url)
        if len(spl_by_slash) > 0:
            spl_by_dot = re.split('\.', spl_by_slash[-1])
            if len(spl_by_dot) == 2:
                return spl_by_dot[0]

    def pull(self, remote_name=None, branch_name=None):
        if remote_name and branch_name:
            work_dir = os.path.abspath(self.to_path)
            pull = subprocess.check_output(['cd',  work_dir, '&&', 'git', 'pull', remote_name,  branch_name], shell=True)
            for line in pull.decode().split('\n'):
                print(line)

    def pull(self, fetch_from=None):
        if fetch_from:
            work_dir = os.path.abspath(self.to_path)
            pull = subprocess.check_output(['cd', work_dir, '&&', 'git', 'fetch', fetch_from], shell=True)
            for line in pull.decode().split('\n'):
                print(line)

    def get_all_branches(self):
        print(self.work_dir)
        all_branches = []
        check = subprocess.check_output(['cd',  self.work_dir, '&&', 'git', 'branch', '-r'], shell=True)
        for line in check.decode().split('\n'):
            if len((re.split('->', line))) == 1:
                clean_value = re.sub('\s+', '', line)
                if clean_value:
                    all_branches.append(clean_value)
        return all_branches
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