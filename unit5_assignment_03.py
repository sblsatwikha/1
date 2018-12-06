__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    if first==second:
        return True
    else:
        if(len(first)==len(second)):
            c=0
            for i in range(len(first)):
                s=first[i]
                c=first.count(s)
                h=second.count(s)
                if c==h:
                  c=c+1
            if c==len(first)-1:
                return True
            else:
                return False
        else:
           return False



# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.
    assert True==are_anagrams(None,None)
    assert True==are_anagrams([],[])
# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_are_anagrams(are_anagrams)
