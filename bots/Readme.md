### Running the bots
* The bot can be temporarily run by the following commands.  Otherwise,
use the ansible playbook to install and run by systemd
```
cd bots/
pipenv shell
export PATH_TO_ENV_FILE=/path/to/env_variables
python list_uptimes.py
```

* Samaple env variables file
```
TOKEN_LIST_UPTIMES_BOT='unique-bot-token'
API_ID='app-id'
API_HASH='app-hash'
REST_API='https://rest.api/enpoint'
PARAMS='{"ordering": "-created_at"}'

LIST_UPTIMES_LOG_TO_FILE='no'
# These two are not necessary if the above is not 'yes'
#LIST_UPTIMES_LOG='/path/to/log_file'
#LIST_UPTIMES_ERROR='/path/to/error_log_file'
```

<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
