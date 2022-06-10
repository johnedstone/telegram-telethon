### Example commands.
* List randomized geolocation data with permission `can_view_randomized_data_only`
```
http localhost:8000/api/v1/geolocations/ \
    "Authorization: Token 10605f6df2cd886feb45e2bffcc1f21447d15399" \
    telegram_user:=222222 longitude:=4.5 latitude:=2.0
```
