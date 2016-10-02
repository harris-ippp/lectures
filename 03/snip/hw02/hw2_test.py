#!/usr/bin/env python3

import unittest

import q1, q2, q3, q4, q4, q5 

class TestHW2(unittest.TestCase):

  def test_q1(self):
    self.assertEqual(q1.solution, 81900)

  def test_q2(self):
    self.assertEqual(q2.solution, 15129388)

  def test_q3(self):
    self.assertEqual(q3.solution, 6)

  def test_q4(self):
    self.assertEqual(q4.solution, 2257403904)

  def test_q5(self):
    self.assertEqual(q5.solution, 31875000)


if __name__ == '__main__':
  unittest.main()



