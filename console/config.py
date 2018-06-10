# coding=utf-8

import os
import ConfigParser
from console.common import logger


log = logger.getLogger()

BASE_PATH = os.path.abspath(os.path.dirname(__name__))
CONFIG_PATH = os.path.join(BASE_PATH, 'conf', 'setting.ini')


def setup_config(config_file=CONFIG_PATH):
    parser = ConfigParser.SafeConfigParser()
    parser.read(config_file)
    return parser
