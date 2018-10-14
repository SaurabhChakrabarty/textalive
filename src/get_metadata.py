#!/usr/bin/env python
import ConfigParser

class GetMetadata(object):
    def __init__(self, CONFIG_FILE='../.metadata'):
        self._config = ConfigParser.ConfigParser()
        self._config.read(CONFIG_FILE)
    def get_consumer_key(self):
        return self._config.get('Consumer', 'Key')
    def get_consumer_secret(self):
        return self._config.get('Consumer', 'Secret')
    def get_access_token(self):
        return self._config.get('Access', 'Token')
    def get_access_secret(self):
        return self._config.get('Access', 'Secret')
