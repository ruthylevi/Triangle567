# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 should be equilateral')

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(6,8,11),'Scalene','6,8,11 should be scalene')

    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(12,16,22),'Scalene','12,16,22 should be scalene')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(5,5,4),'Isosceles','5,5,4 should be isosceles')

    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(10,10,8),'Isosceles','10,10,8 should be isosceles')

    def testInvalidTriangleA(self): 
        self.assertEqual(classifyTriangle(250,250,300),'InvalidInput','250,250,300 should be an invalid triangle')

    def testInvalidTriangleB(self): 
        self.assertEqual(classifyTriangle("5","10","8"),'InvalidInput','"5","10","8" should be an invalid triangle')

    def testInvalidTriangleC(self): 
        self.assertEqual(classifyTriangle(-5, -5, -5),'InvalidInput','-5, -5, -5 should be an invalid triangle')

    def testInvalidTriangleD(self): 
        self.assertEqual(classifyTriangle(5, 6, 20),'NotATriangle','5, 6, 20 should not be a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

