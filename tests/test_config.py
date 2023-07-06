import unittest

import tomli  # you can use toml, json,yaml, or ryo for your config file

import smartpark.config_parser as pc
import json


class TestConfigParsing(unittest.TestCase):
    def test_parse_config_has_correct_location_and_spaces(self):

        parking_lot = pc.parse_config('config.json')
        self.assertEqual(parking_lot['location'], "moondalup")
        self.assertEqual(parking_lot['total-spaces'], 130)