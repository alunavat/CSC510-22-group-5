#! /usr/bin/env python

import numpy
class Addition:
  def __init__(self, num1, num2, decimalPoints=0) -> None:
    self.num1 = num1
    self.num2 = num2
    self.decimalPoints = decimalPoints
    pass
  def main(self) -> float:
    print(self.num1+self.num2)
    return self.num1+self.num2
