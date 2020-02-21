import base64
import gzip
import json
import logging
from pathlib import Path
import os


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [b'{"status": "ok"}']


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    log.info(f"Server running on port {port} ...")
    with make_server('', port, app) as httpd:
        httpd.serve_forever()
