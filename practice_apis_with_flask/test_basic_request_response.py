from flask import Flask, jsonify, request  # Flask library for build apis
from log import log_application as fileLog

logApplication = fileLog.LogApplication(__file__)
log = logApplication.log
app = Flask(__name__)

# log.debug("test %s",12) # all data you want to log have to put %s , <data>

