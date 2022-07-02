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
This playbook is used for for this app as well as Location_to_restapi_app.

```
export PATH_TO_PRIVATE_VARS_YAML=/path/to/the/location_app_private_vars.yaml

#dry-run
/usr/local/bin/ansible-playbook --check --diff --flush-cache --tags location_app -i inventory.ini location_app_playbook.yaml


#play
/usr/local/bin/ansible-playbook --diff --flush-cache --tags location_app -i inventory.ini location_app_playbook.yaml
```

#### Location_to_restapi_app (bot)
Same playbook as for the Location app (above), only the private_vars is different.

```
export PATH_TO_PRIVATE_VARS_YAML=/path/to/the/location_to_restapi_app_private_vars.yaml

#Use dry-run and play commands from above using the location_app_playbook

```

### geolocation_restapi
#### Notes for post ansible install
* create user that has the permission to post geolocation:Call post geolocation
* create user that has the permission to post geolocation:Can view all data
* create user that has the permission to post geolocation:Can view randomized data only
* Consider using groups with these permissions and adding the user(s) to the appropriate group

#### ansible command(s) for installing

```
export PATH_TO_PRIVATE_VARS_YAML=/path/to/the/geolocation_restapi_private_vars.yaml

#dry-run
/usr/local/bin/ansible-playbook --check --diff --flush-cache -i inventory.ini [ --tags mariadb_setup | --skip-tags mariadb_setup ] geolocation_restapi_playbook.yaml


#play
/usr/local/bin/ansible-playbook --diff --flush-cache -i inventory.ini geolocation_restapi_playbook.yaml

```

#### Testing hello_world.py after ansible install
```
gunicorn -b 0.0.0.0:8000 hello_world:app
#or simply
gunicorn hello_world:app
```

#### ToDo
* actual geolocation project
    * rsync files exclude migrations
    * run migrations

### Thinking about number of gunicorn workers
* reference: https://dev.to/kokospapa8/gunicorn-performance-analysis-on-aws-ec2-28jl
* For EC2 T3 with 2cpu and 1G: workers either 3 or 5.  02-Jul-2022: --worker 3

#### Django install: other examples
    * https://www.section.io/engineering-education/django-ansible-deployment/
    * https://realpython.com/automating-django-deployments-with-fabric-and-ansible/
    * https://www.guguweb.com/2017/05/02/how-to-deploy-a-django-project-in-15-minutes-with-ansible/
    * https://github.com/liip/django-ansible

<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
