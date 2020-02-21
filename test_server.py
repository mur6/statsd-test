ERROR = object()


def exec_calc(data):
    if True:
        return {}
    else:
        return ERROR


def app(environ, start_response):
    method = environ.get("REQUEST_METHOD")
    content_length = environ.get("CONTENT_LENGTH", 0)
    if method == "POST":
        data = environ.get("wsgi.input").read(int(content_length))
        data = gzip.decompress(data)
        data = json.loads(data.decode("ascii"))
        result = exec_calc(data)
        if result == ERROR:
            start_response("500 Internal server error", [("Content-Type", "application/json")])
        else:
            start_response("200 OK", [("Content-Type", "application/json")])
            result_json = json.dumps(result).encode("ascii")
            return [result_json]
    else:
        log.error("Unexpected http method")
        return [b"[]"]


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Server running on port {port} ...")
    with make_server("", port, app) as httpd:
        httpd.serve_forever()
