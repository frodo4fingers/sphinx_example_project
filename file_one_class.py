#!/usr/bin/env python

import numpy as np


class TestClass2():
    """
    This is a class docstring from a file that just lays around somewhere.

    Parameters
    ----------
    start : [int]
        means where something starts
    end : [int]
        means where something ends

    Returns
    -------
    Nothing at all
    """

    def __init__(self, end):
        """
        Minor docstring describing whats initialized.
        """
        self.start = 0
        self.end = end

        self.thisIsAModule()

    def thisIsAModule(self):
        """
        Hi, I am the description of what this module does.

        Returns
        -------
        A list of the numbers between start and end
        """
        return  np.arange(self.start, self.end)
