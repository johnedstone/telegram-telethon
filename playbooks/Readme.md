### Typical ansible commands
```
export PATH_TO_PRIVATE_VARS_YAML=/path/to/the/list_uptimes_private_vars.yaml

#dry-run
/usr/local/bin/ansible-playbook --check --diff --flush-cache -i inventory.ini list_uptimes_playbook.yaml

#run/play the whole playbook
/usr/local/bin/ansible-playbook --diff --flush-cache -i inventory.ini list_uptimes_playbook.yaml

#skip a role, using a tag, or can be used with --tags to play(run) a role
/usr/local/bin/ansible-playbook --diff --flush-cache --skip-tags optional_prep_work -i inventory.ini list_uptimes_playbook.yaml
```

<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
