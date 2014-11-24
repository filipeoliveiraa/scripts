from UglyCipher import *

class UglyCipherTester:

    def testBuildCipher(self):
        # init
        uc   = UglyCipher()
        word = "this is test words."
        key    = 5
        c      = 'x'
        a      = 4
        expect = ['nmy', '3', 'iwt|%y', 'jy%', 'n%']

        # run 
        actual = uc.buildCipher(word,key,c,a)
        
        # test
        assert actual == expect

        return actual
    
test = UglyCipherTester()
print test.testBuildCipher()
