## Vault to Terraform
These scripts can be used to import/convert all existing Vault Policies (ACL, RGP, EGP) into Terraform configurations and also import them into state.

## NOTES:
1) Each script requires that you input your VAULT_ADDR ('<VAULT_ADDRESS_HERE>') and VAULT_TOKEN ('<VAULT_TOKEN_HERE>') prior to running.
2) You need to run 'terraform init' in each folder into which you'll be importing state.
3) After the import is complete, you can run a 'terraform plan' and, if the import was successful, you'll see a message indicating that 'No Changes' need to be made.
