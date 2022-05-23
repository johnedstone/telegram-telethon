### Running the bots
* The bots can be temporarily run by the following commands.  Otherwise,
use the ansible playbook to install and run by systemd

#### List uptimes bot
```
cd bots/
pipenv shell
export PATH_TO_ENV_FILE=/path/to/list_uptimes_env_variables
python list_uptimes.py
```

* Sample env variables file for list_uptimes bot
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

#### Location app bot
```
cd bots/
pipenv shell
export PATH_TO_ENV_FILE=/path/to/location_app_env_variables
python location_app.py
```

* Sample env variables file for the location_app bot
```
TOKEN_LOCATION_BOT='your-unique-bot-token'
APP_NAME='location_app'
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
