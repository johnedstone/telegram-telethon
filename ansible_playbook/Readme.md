### Ansible Commands
```
#dry-run
/usr/local/bin/ansible-playbook --check --diff --flush-cache -i inventory.ini playbook.yaml

#skip a role, using a tag, or can be used with --tags to play(run) a role
/usr/local/bin/ansible-playbook --diff --flush-cache --skip-tags optional_prep_work -i inventory.ini playbook.yaml
```

<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
