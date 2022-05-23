### Running the bots
* The bot can be temporarily run by the following commands.  Otherwise,
use the ansible playbook to install and run by systemd
```
cd bots/
pipenv shell
export PATH_TO_ENV_FILE=/path/to/env_variables
python list_uptimes.py
```

* Samaple env variables file for list_uptimes bot
```
TOKEN_LIST_UPTIMES_BOT='your-unique-bot-token'
APP_NAME='list_uptimes'
API_ID='your-app-id'
API_HASH='your-app-hash'
REST_API='https://rest.api/enpoint'
PARAMS='{"ordering": "-created_at"}'

LOG_TO_FILE='no'
#LOG_DIR=/path/to/logs # Not neccessary unless above is 'yes'
```

* Samaple env variables file for the location bot
```
TOKEN_LOCATION_BOT='your-unique-bot-token'
APP_NAME='location_bot'
API_ID='your-app-id'
API_HASH='your-app-hash'
REST_API='not_using_yet'
PARAMS='{"not_using": true}'

LOG_TO_FILE='no'
#LOG_DIR=/path/to/logs # Not neccessary unless above is 'yes'
```

<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
