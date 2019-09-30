# -*- coding: utf-8 -*-
"""
Updated Sep 29, 2019
The primary goal of this file is to demonstrate a simple unittest implementation
for a triangle classication file called Triangle.py
@author: ruthylevi
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    '''This class tests the Triangle.py file in order to determine if the functions
created to classify triangles hold up to several different inputs'''
    # define multiple sets of tests as functions with names that begin

    def test_right_triangle_a(self):
        """This test determines if a triangle is properly classified as a right triangle"""
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        """This test determines if a triangle is properly classified as a right triangle"""
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def test_equilateral_triangle_a(self):
        """This test determines if a triangle is properly classified as an equilateral triangle"""
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_equilateral_triangle_b(self):
        """This test determines if a triangle is properly classified as an equilateral triangle"""
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral', '5,5,5 should be equilateral')

    def test_scalene_triangle_a(self):
        """This test determines if a triangle is properly classified as a scalene triangle"""
        self.assertEqual(classifyTriangle(6, 8, 11), 'Scalene', '6,8,11 should be scalene')

    def test_scalene_triangle_b(self):
        """This test determines if a triangle is properly classified as a scalene triangle"""
        self.assertEqual(classifyTriangle(12, 16, 22), 'Scalene', '12,16,22 should be scalene')

    def test_isosceles_triangle_a(self):
        """This test determines if a triangle is properly classified as an isosceles triangle"""
        self.assertEqual(classifyTriangle(5, 5, 4), 'Isosceles', '5,5,4 should be isosceles')

    def test_isosceles_triangle_b(self):
        """This test determines if a triangle is properly classified as an isosceles triangle"""
        self.assertEqual(classifyTriangle(10, 10, 8), 'Isosceles', '10,10,8 should be isosceles')

    def test_invalid_triangle_a(self):
        """This test determines if a triangle is an invalid triangle"""
        self.assertEqual(classifyTriangle(250, 250, 300), 'InvalidInput', 'Should be invalid')

    def test_invalid_triangle_b(self):
        """This test determines if a triangle is an invalid triangle"""
        self.assertEqual(classifyTriangle("5", "10", "8"), 'InvalidInput', '"Should be invalid')

    def test_invalid_triangle_c(self):
        """This test determines if a triangle is an invalid triangle"""
        self.assertEqual(classifyTriangle(-5, -5, -5), 'InvalidInput', 'Should be invalid')

    def test_invalid_triangle_d(self):
        """This test determines if a triangle is an invalid triangle"""
        self.assertEqual(classifyTriangle(5, 6, 20), 'NotATriangle', 'Should not be a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
