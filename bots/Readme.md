### Running the bots
* The bot can be temporarily run by the following commands.  Otherwise,
use the ansible playbook to run by systemd
```
cd bots/
pipenv shell
export LIST_UPTIMES_ENV=/path/to/env_variables
python list_uptimes.py
```

* Samaple env variables file
```
TOKEN_LIST_UPTIMES_BOT='unique-bot-token
API_ID='app-id'
API_HASH='app-hash'
REST_API='https://rest.api/enpoint'
PARAMS='{"ordering": "-created_at"}'
```

<!---
# vim: ai et ts=4 sw=4 sts=4 nu
-->
