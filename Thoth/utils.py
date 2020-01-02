# -*- coding: utf-8 -*-

import os
import logging
import configparser

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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

        # Log Path
        self.log_path = config.get('log', 'path')


config = Config()


def load_logger():
    """
    load logger for print log to logfile.
    :return: logger
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler(config.log_path)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
