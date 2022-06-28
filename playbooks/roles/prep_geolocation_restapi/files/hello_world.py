"""
https://gunicorn.org/
"""
def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

# vim: ai et ts=4 sw=4 sts=4 nu
