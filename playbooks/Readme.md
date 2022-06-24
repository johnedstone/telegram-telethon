### Typical ansible commands

#### List uptimes app (bot)

```
export PATH_TO_PRIVATE_VARS_YAML=/path/to/the/list_uptimes_private_vars.yaml

#dry-run
/usr/local/bin/ansible-playbook --check --diff --flush-cache -i inventory.ini list_uptimes_playbook.yaml

#run/play the whole playbook
/usr/local/bin/ansible-playbook --diff --flush-cache -i inventory.ini list_uptimes_playbook.yaml

#skip a role, using a tag, or can be used with --tags to play(run) a role
/usr/local/bin/ansible-playbook --diff --flush-cache --skip-tags optional_prep_work -i inventory.ini list_uptimes_playbook.yaml
```

#### Location app (bot)

```
export PATH_TO_PRIVATE_VARS_YAML=/path/to/the/location_app_private_vars.yaml

#dry-run
/usr/local/bin/ansible-playbook --check --diff --flush-cache --tags location_app -i inventory.ini location_app_playbook.yaml


#play
/usr/local/bin/ansible-playbook --diff --flush-cache --tags location_app -i inventory.ini location_app_playbook.yaml
```

#### Location_to_restapi_app (bot)

```
export PATH_TO_PRIVATE_VARS_YAML=/path/to/the/location_to_restapi_app_private_vars.yaml

#Use dry-run and play commands from above using the location_app_playbook

```

#### geolocation_restapi 

```
export PATH_TO_PRIVATE_VARS_YAML=/path/to/the/geolocation_restapi_private_vars.yaml

#dry-run
/usr/local/bin/ansible-playbook --check --diff --flush-cache -i inventory.ini geolocation_restapi_playbook.yaml


#play
/usr/local/bin/ansible-playbook --diff --flush-cache -i inventory.ini geolocation_restapi_playbook.yaml

```


<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
