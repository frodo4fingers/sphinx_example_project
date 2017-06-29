#!/usr/bin/env python

import numpy as np


class Class1FromDirectory():
    """
    This is a docstring describing the class function. Since __init__ functions is left out, any argument passed needs to be planted here.

    Parameters
    ----------
    start : [int]
        means where something starts
    end : [int]
        means where something ends
    """

    def __init__(self, end):
        """
        Minor docstring describing whats initialized.
        """
        self.start = 0
        self.end = end

    def thisIsAModule(self):
        """
        Hi, I am the description of what this module does.

        Returns
        -------
            A list of the numbers between start and end
        """
        return  np.arange(self.start, self.end)


class Class2FromDirectory():
    """
    This is a docstring describing the class function. Since __init__ functions is left out, any argument passed needs to be planted here.

    Parameters
    ----------
    start : [int]
        means where something starts
    end : [int]
        means where something ends
    """

    def __init__(self, varA=None, evil=None):
        """
        Minor docstring describing whats initialized.
        """
        self.varA = 5
        self.evil = 666

    def functionWithNArguments(self, varA, varB, varC, angel=None):
        """
        Gets a few more arguments for no obvious reason at all.

        Parameters
        ----------
        varA : [int]
            Just a random integer number
        varB : [float]
            Just a random number floating through space
        varC : [list]
            List full of.. i don't know
        angel: (optional)
            Removes the evil somehow

        Returns
        -------
            A **list** of the numbers between start and end

        Examples
        --------
            >>> from numpy import arange
            >>> # doesn't make any sense, but...
            >>> ab = self.varA + self.varB
            >>> the_list = arange(0, ab, self.varC)

        """
        return  np.arange(self.varA, self.varC/self.varB)
