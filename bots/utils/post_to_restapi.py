def post_to_restapi(logger_log, logger_error):
    try:
        return 'success'
    except Exception as e:
        return f'{e}'

