import unittest
from unittest import mock

# @see https://note.nkmk.me/python-relative-import/
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import md_formatter

class MdFormatterTest(unittest.TestCase):
  def setUp(self) -> None:
      array = [
        {
          'repo': 'https://github.com/ledermann/templatus-hotwire',
          'star': 6,
        },
        {
          'repo': 'https://github.com/ParamagicDev/rails_starter',
          'star': 5
        }
      ]
      self.formatter = md_formatter.MdFormatter(array)

  def tearDown(self) -> None:
      return super().tearDown()

  
  def test_display(self):
    self.assertEqual(self.formatter.display(), 'foo')

if __name__ == "__main__":
  unittest.main()

