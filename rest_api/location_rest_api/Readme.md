### Example commands.
* List (user_id randomized) geolocation data with the token that allows `can_view_randomized_data_only`
```
http localhost:8000/api/v1/geolocations/ \  
    "Authorization: Token 10605f6df2cd886feb45e2bffcc1f21447d15399" \  
```

* Post geolocation data with the token that allows `can_post_geolocation`
```
http localhost:8000/api/v1/geolocations/ 
    "Authorization: Token d173dcdbbf5d31882d8b1c1e5d199239f7dd4c47" \  
    telegram_user:=222222 longitude:=4.5 latitude:=2.0
```

* Viewing all the data with a token that allows `can_view_all_data`
```
``` 