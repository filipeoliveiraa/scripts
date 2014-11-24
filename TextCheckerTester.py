from TextChecker import *
class TextCheckerTester:
        def input_by_string(self):
                text = TextChecker()
                input1 = "this is test words."
                input2 = "this is test apples"
                expect = {'count': {'this': 1, 'test': 1, 'is': 2, 'apples': 0}, 'len': 19}
                actual = text.tc(source=input1,words=input2)
                assert actual == expect
                return actual

test = TextCheckerTester()
test.input_by_string()
