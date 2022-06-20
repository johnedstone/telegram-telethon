### Running in development mode
From this directory:
```
python manage.py runserver
```

### Example commands to consume data from this REST API
#### Geolocation

* __List__ (user_id randomized) geolocation data with the token that allows `can_view_randomized_data_only`
```
http localhost:8000/api/v1/geolocations/  "Authorization: Token 10605f6df2cd886feb45e2bffcc1f21447d15399"
```

* __Post__ geolocation data with the token that allows `can_post_geolocation`
```
http localhost:8000/api/v1/geolocations/  "Authorization: Token d173dcdbbf5d31882d8b1c1e5d199239f7dd4c47"  telegram_user:=222222 longitude:=4.5 latitude:=2.0
```

* __Patching__ username with the token that allows `can_post_geolocation`
```
http patch localhost:8000/api/v1/telegram-users/2/ "Authorization: Token d173dcdbbf5d31882d8b1c1e5d199239f7dd4c47" username=thursday-afternoon
```

* __List__ all the geolocation data with a token that allows `can_view_all_data`
```
http localhost:8000/api/v1/geolocations/ "Authorization: Token 049915526c2ccc56852b0a556789b5f7a21f5c14"

``` 

* __Filter__ geolocation data for `telegram_user=23` which is its (url/id of telegram_user), created on 09-Jun-2022, and `ordering=-created_at`
```
http localhost:8000/api/v1/geolocations/?ordering=-created_at\&telegram_user=23\&created_at_after="2022-06-09"\&created_at_before="2022-06-09" "Authorization: Token 049915526c2ccc56852b0a556789b5f7a21f5c14"
```

* __Filter__ geolocation data by `telegram_user_username=thursday`
```
http localhost:8000/api/v1/geolocations/?ordering=-created_at\&telegram_user_username=thursday "Authorization: Token 049915526c2ccc56852b0a556789b5f7a21f5c14"
```

* __Filter__ geolocation data by `telegram_user_user_id=222222` and `ordering=-created_at`
```
http localhost:8000/api/v1/geolocations/?ordering=-created_at\&telegram_user_user_id=222222 "Authorization: Token 049915526c2ccc56852b0a556789b5f7a21f5c14"
```

* __Filter__ geolocation data by `telegram_user_randomized_id=5W4VBULEB4MLDS4S`
```
http localhost:8000/api/v1/geolocations/?telegram_user_randomized_id=5W4VBULEB4MLDS4S "Authorization: Token 049915526c2ccc56852b0a556789b5f7a21f5c14"
```

#### Telegram Users
* __List__ telegram_users data with `ordering=user_id`
```
http localhost:8000/api/v1/telegram-users/?ordering=user_id "Authorization: Token 049915526c2ccc56852b0a556789b5f7a21f5c14"
```

<!---
# vim: ai et ts=4 sw=2 sts=4 nu
!>
