# -*- coding: utf-8 -*-

import os
import configparser

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_PATH)
class Config(object):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(BASE_PATH, 'conf', 'setting.ini'))

        # MySQL information
        self.db_ip = config.get('db', 'db_ip')
        self.db_port = config.get('db', 'db_port')
        self.db_username = config.get('db', 'db_username')
        self.db_password = config.get('db', 'db_password')
        self.db_name = config.get('db', 'db_name')

        # Files Path
        self.article_path = config.get('article', 'path')
