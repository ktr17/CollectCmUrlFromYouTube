#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():

    print("入ったよ")
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
