import unittest
from unittest import mock

# @see https://note.nkmk.me/python-relative-import/
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import md_formatter

import configparser
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

class MdFormatterTest(unittest.TestCase):
  def setUp(self) -> None:
      array = [
        {
          config_ini['DEFAULT']['Repository']: 'https://github.com/ledermann/templatus-hotwire',
          config_ini['DEFAULT']['Star']: 6,
        },
        {
          config_ini['DEFAULT']['Repository']: 'https://github.com/ParamagicDev/rails_starter',
          config_ini['DEFAULT']['Star']: 5
        }
      ]
      self.formatter = md_formatter.MdFormatter(array)

  def tearDown(self) -> None:
      return super().tearDown()

  
  def test_display(self):
    self.assertEqual(self.formatter.display(), 'foo')

if __name__ == "__main__":
  unittest.main()

