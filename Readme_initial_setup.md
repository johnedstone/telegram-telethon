### Initial setup
Do the following on a new image.
After this, there is no need to run these commands

```
sudo apt install -y rsync git python-apt python3-pymysql python3-pip virtualenv
sudo apt autoremove
sudo apt autoclean
sudo pip3 install ansible 

# Current ansible version
/usr/local/bin/ansible --version
ansible [core 2.11.1] 
  config file = None
  configured module search path = ['/home/bitnami/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.7/dist-packages/ansible
  ansible collection location = /home/bitnami/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/local/bin/ansible
  python version = 3.7.3 (default, Jan 22 2021, 20:04:44) [GCC 8.3.0]
  jinja version = 2.10
  libyaml = True

/usr/local/bin/ansible-galaxy collection install community.mysql

cd /home/bitnami && git clone  <this repository>

sudo mkdir /opt/bitnami/apps
sudo chown bitnami:daemon /opt/bitnami/apps
mkdir /opt/bitnami/apps/configuration
touch /opt/bitnami/apps/configuration/private_vars.yaml
```

<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->

