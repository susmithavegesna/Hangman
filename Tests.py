import hangman
import unittest

class TestCasesFlask(unittest.TestCase):
    # test for title content
    def test_title(self):
        tester = hangman.app.test_client(self)
        response = tester.get('/',content_type = 'html/text' )
        #print("resp:",response.data)
        self.assertTrue(b'Hangman game' in response.data)
    
    #test sucessful loading of page
    def test_index(self):
        tester = hangman.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #test for spl char and numbers in guess word
    def test_word(self):
        self.assertNotIn("_",hangman.random_word())
        self.assertNotIn(" ",hangman.random_word())
        self.assertNotIn("*",hangman.random_word())
        self.assertNotIn("!",hangman.random_word())
        self.assertNotIn(".",hangman.random_word())
        self.assertNotIn("9",hangman.random_word())






if __name__ == '__main__':
    unittest.main()
