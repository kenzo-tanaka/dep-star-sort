import unittest
import dep_star_sort

class DepStarSort:
    def dep_url(self, url):
        return(f"{url}/network/dependents")

class DepStarSortTest(unittest.TestCase):
  def setUp(self) -> None:
      pass

  def tearDown(self) -> None:
      pass

  def test_dep_url(self):
    dep_star_sort = DepStarSort()
    self.assertEqual(dep_star_sort.dep_url("https://github.com/github/view_component"), "https://github.com/github/view_component/network/dependents")


if __name__ == "__main__":
    unittest.main()
