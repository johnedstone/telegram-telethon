### Description
This repository contains ...
* Three Telegram bots using the python Telethon library
    * list_uptimes: which pulls data from a rest api server and displays it on a Telegram bot
    * location_app: which logs to stdout and stderr the data from the Telegram Location widget
    * location_to_restapi_app which posts the Telegram Location widget to a restapi server

* as well as the  Django REST API which is the rest api that the third bot (above) posts to.
  to and from these bots.

* The `playbooks` folder contains the ansible playbooks to install the bots and REST API on an
AWS EC2 instance running Nginx and MariaDB, e.g a t3.micro "bitnami-wordpresspro-5.9.3-17-r06-linux-debian-10-x86_64-hvm-ebs-nami-78b1d030-4c7d-4ade-b8e6-f8dc86941303" AMI

#### Current State
  * list_uptimes, location_app, location_to_restapi_app bots finished, including ansible playbooks for installing them
  * 22-May-2022: Starting work on rest api described above

#### To Do
* Add Ansible role for using Postgres instead of MariaDB 

### Related Readme's
* Readme_initial_setup.md
* [Typical ansible commands](https://github.com/johnedstone/telegram-telethon/tree/main/ansible_playbook)

<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
