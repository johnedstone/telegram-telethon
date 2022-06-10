### Example commands
* List (user_id randomized) geolocation data with the token that allows `can_view_randomized_data_only`
```
http localhost:8000/api/v1/geolocations/  "Authorization: Token 10605f6df2cd886feb45e2bffcc1f21447d15399"
```

* Post geolocation data with the token that allows `can_post_geolocation`
```
http localhost:8000/api/v1/geolocations/  "Authorization: Token d173dcdbbf5d31882d8b1c1e5d199239f7dd4c47"  telegram_user:=222222 longitude:=4.5 latitude:=2.0
```

* Patching username with the token that allows `can_post_geolocation`
```
http patch localhost:8000/api/v1/telegram-users/2/ "Authorization: Token d173dcdbbf5d31882d8b1c1e5d199239f7dd4c47" username=thursday-afternoon
```

* Viewing all the geolocation data with a token that allows `can_view_all_data`
```
http localhost:8000/api/v1/geolocations/ "Authorization: Token 049915526c2ccc56852b0a556789b5f7a21f5c14"

``` 

* Viewing the geolocation data with `ordering=-created_at`  and filtering on `telegram_user=23`
```
http localhost:8000/api/v1/geolocations/?ordering=-created_at\&telegram_user=23 "Authorization: Token 049915526c2ccc56852b0a556789b5f7a21f5c14"
```

* Viewer telegram_users data with `ordering=user_id`
```
http localhost:8000/api/v1/telegram-users/?ordering=user_id "Authorization: Token 049915526c2ccc56852b0a556789b5f7a21f5c14"
```

<!---
# vim: ai et ts=4 sw=2 sts=4 nu
!>
