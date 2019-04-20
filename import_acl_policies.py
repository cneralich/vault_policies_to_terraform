#def get_acl_policies():
import os
import subprocess
from subprocess import call

my_file=open("main.tf","w")

os.environ["VAULT_ADDR"] = "<VAULT_ADDRESS_HERE>"
os.environ["VAULT_TOKEN"] = "<VAULT_TOKEN_HERE>"

get_policies = "vault list sys/policies/acl"
policy_names = os.popen(get_policies)

ignore_list = ['root', 'default', 'Keys', '----']

for policy_name in policy_names:
    name = policy_name.rstrip()
    if name not in ignore_list:
        get_content = "vault policy read %s" % (name)
        content = os.popen(get_content)
        formatted = content.read()
        acl_var = 'resource "vault_policy" "%s" {\n  name = "%s"\n\n  policy = <<EOT\n%sEOT\n}\n\n' % (name, name, formatted)
        my_file.write(acl_var)
my_file.close()

get_policies = "vault list sys/policies/acl"
policy_names = os.popen(get_policies)

ignore_list = ['root', 'default', 'Keys', '----']

for policy_name in policy_names:
    name = policy_name.rstrip()
    if name not in ignore_list:
        command = "terraform import vault_policy.%s %s" % (name, name)
        subprocess.check_call(command.split())
