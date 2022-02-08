import unittest
from squares_of_sorted_array import Solution

class TestSortedSquares(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

        return super().setUp()

    def test_is_sorted(self):
        input = [-4,-1,0,3,10]

        output = self.solution.sortedSquares(input)

        expected = [pow(x, 2) for x in input]
        expected.sort()

        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
