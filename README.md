# win_git_ansible
This module is for git clone using ansible playbook for Windows.


# How to Use?
1. Install GitPython - ```pip3 install gitpython```
2. Create library folder and add _win_git.py_ and _win_git_doc.py_ into it.
3. Create _ansible.cfg_ in your ansible project folder

For the custom modules, ansible will start searching for the code at 'DEFAULT_MODULE_PATH'; once the code for the custom module is not found at ‘DEFAULT_MODULE_PATH‘, then the ansible looks for the modules in a directory called 'library' at the same directory as the playbook. For example, if my playbook name is example.yml, I will create a directory called 'library‘ at the same level as my playbook and a module file called.’library/win_git.py‘

Add the following in _ansible.cfg_
```
[defaults]
library = ./library
```

# My ansible project directory:
   
 ```bash
    windows
    ├── ansible.cfg
    ├── example.yml
    ├── library
    │   ├── win_git_doc.py
    │   └── win_git.py
    ├── roles
    │   ├── copy_tools_packages
    │   │   ├── tasks
    │   │   │   └── main.yml
    │   │   └── vars
    │   │       └── main.yml
    │   ├── create_dir
    │   │   ├── tasks
    │   │   │   └── main.yml
```





# Example playbook using win_git:
```
---
- hosts: win
  gather_facts: True
  tasks:
  - name: Git Clone
    win_git:
     repo_url: 'ssh://git@bitbucket.micron.com/cxlsys/mxlib.git'
     dest_dir: 'C:\\test\\test\\mxlib'
     branch: 'lake_huron'
     action: 'gitclone'

```
