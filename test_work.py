import pytest
import sys
from work import learnings
class Test_learnings:

    ''' 
    This test_math method checks if the biggest number is the one returned 
    by the math method from our work.py file
    '''
    @staticmethod
    def test_math():
        assert learnings.math()  == 7
    
    '''
    This test_user_input method checks if the user enters a positive,neagative or
    nuetral number then the user_input method from work.py will return the True answer
     '''
    def test_user_input(self, monkeypatch):
        def test_positive_input():
            monkeypatch.setattr('builtins.input', lambda : 3)
            output = learnings.user_input()
            assert output == True
        def test_neutral_input():
            monkeypatch.setattr('builtins.input', lambda : 0)
            assert output == False
        def test_negative_input():
            monkeypatch.setattr('builtins.input', lambda : -5)
            assert output == False
