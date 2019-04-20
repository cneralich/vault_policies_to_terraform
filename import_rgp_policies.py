#def import_rpg_policies():
import os
import subprocess
from subprocess import call
import requests
import requests.packages.urllib3
import json

my_file=open("main.tf","w")

get_policies = "vault list sys/policies/rgp"
policy_names = os.popen(get_policies)

ignore_list = ['root', 'default', 'Keys', '----']

for policy_name in policy_names:
    name = policy_name.rstrip()
    if name not in ignore_list:
        url = '<VAULT_ADDRESS_HERE>/v1/sys/policies/rgp/%s' % (name)
        headers = {'X-Vault-Token': '<VAULT_TOKEN_HERE>'}

        r = requests.get(url, headers=headers).json()
        policy = r.get('data').get('policy')
        enforcement_level = r. get('data').get('enforcement_level')
        rgp_var = 'resource "vault_rgp_policy" "%s" {\n  name = "%s"\n  enforcement_level = "%s"\n\n  policy = <<EOT\n%sEOT\n}\n\n' % (name, name, enforcement_level, policy)
        my_file.write(rgp_var)
my_file.close()

get_policies = "vault list sys/policies/rgp"
policy_names = os.popen(get_policies)

ignore_list = ['root', 'default', 'Keys', '----']

for policy_name in policy_names:
    name = policy_name.rstrip()
    if name not in ignore_list:
        command = "terraform import vault_rgp_policy.%s %s" % (name, name)
        subprocess.check_call(command.split())
