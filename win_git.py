#!/usr/bin/python3
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.module_utils.basic import AnsibleModule
from git import Repo
import os

def get_clone(repo_url, dest_dir, branch):
    if not os.path.exists(dest_dir):
        Repo.clone_from(repo_url, dest_dir, branch=branch)
    else:
        repo = Repo(dest_dir)
        repo.remotes[0].pull()
def main():
    # Define the args required by the module
    # update the aruments as per your requirements
    module_args = dict(
        repo_url=dict(type='str', required=True),
        branch=dict(type='str', required=True),
        dest_dir=dict(type='str', required=True),
        action=dict(type='str', required=True),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        #supports_check_mode=True
    )

    result = dict(
        msg = '',
        stdout = '',
        stdout_lines = [],
        stderr = '',
        stderr_lines = [],
        rc = 0,
        failed = False,
        changed=False
    )
    allowed_actions = ['gitclone']
    if module.params['action'] not in allowed_actions:
        result['failed'] = True
        result['stderr'] = "Invalid argument supplied to this module"
        module.exit_json(**result)
    repo_url =  module.params['repo_url']
    dest_dir =  module.params['dest_dir']
    action =  module.params['action']
    branch =  module.params['branch']
    if action == 'gitclone':
        get_clone(repo_url, dest_dir, branch)
        #result['stdout'] = gitclone
        module.exit_json(**result)
    module.exit_json(**result)

if __name__ == '__main__':
    main()
