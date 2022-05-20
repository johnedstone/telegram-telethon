### Description
This repository contains ...
* several Telegram bots using the python Telethon library
* as well as one or more Django REST API using for posting or getting data
  to and from these bots.

* The `playbooks` folder contains the ansible playbooks to install the bots and API(s) on an
AWS EC2 instance running Nginx and MariaDB, e.g a t3.micro "bitnami-wordpresspro-5.9.3-17-r06-linux-debian-10-x86_64-hvm-ebs-nami-78b1d030-4c7d-4ade-b8e6-f8dc86941303" AMI

#### Current State
  In progress, ... stay tuned!

#### To Do
* Add Ansible role for using Postgres instead of MariaDB 

### Related Readme's
* Readme_initial_setup.md
* [Typical ansible commands](https://github.com/johnedstone/telegram-telethon/tree/main/ansible_playbook)

<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
