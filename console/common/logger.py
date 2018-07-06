# coding=utf-8

import logging

LOG_FILE = '/var/log/online.log'


class Logger(object):

    def __init__(self, level='DEBUG'):
        self.level = level

    def get_logger(self):
        logger = self.create_log()
        return logger

    def create_log(self):
        logger = logging.getLogger(LOG_FILE)
        logger.setLevel(self.level)

        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] '
            '[%(name)s:%(funcName)s %(lineno)d] - %(message)s'
        )
        handle = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024*1024, backupCount=5)
        handle.setFormatter(formatter)

        logger.addHandler(handle)

        return logger


def getLogger(level='DEBUG'):
    log = Logger(level)
    logger = log.get_logger()
    return logger

