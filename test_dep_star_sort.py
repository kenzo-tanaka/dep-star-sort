import unittest
import dep_star_sort

class DepStarSortTest(unittest.TestCase):
  def setUp(self) -> None:
      pass

  def tearDown(self) -> None:
      pass

  def test_dep_url(self):
      executor = dep_star_sort.DepStarSort()
      self.assertEqual(executor.dep_url("https://github.com/github/view_component"), "https://github.com/github/view_component/network/dependents")

  def test_get_html(self):
      executor = dep_star_sort.DepStarSort()
      self.assertIn(executor.get_html(), "<!DOCTYPE html>")



if __name__ == "__main__":
    unittest.main()
