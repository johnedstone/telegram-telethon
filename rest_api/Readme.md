#### Notes on developement
* Started with sqlite3 and telegram user_id as a PositiveIntegerField.
* In production, with MariaDB, this threw a data error, out-of-range.
* Troubleshooting:
    * edit django settings setting DEBUG = False
    * followed with journalctl -fu geolocation_restapi.service
* Eventually set telegram user_id to BigIntegerField
