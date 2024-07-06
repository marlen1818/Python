import os
from pydo import Client

client = Client(token=os.getenv("DO_TOKEN"))
ssh_keys = client.ssh_keys.list()
print(ssh_keys['ssh_keys'])
#ssh_keys = client.ssh_keys.list()

sshKeyName = "Bash-script"

for key in ssh_keys['ssh_keys']:
    if sshKeyName == key['name']:
        ssh_KeyId = key['id']



body = {'name': 'module-droplet', 'size': 's-1vcpu-1gb', 'image': 'ubuntu-20-04-x64', 'ssh-keys': [ssh_KeyId]}

new_droplet = client.droplets.create(body)
print(new_droplet)