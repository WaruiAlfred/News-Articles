import unittest 
from app.designs import MainSource
 
class NewsSourcesTest(unittest.TestCase): 
  '''
  Test class to test the behaviour of the MainSource class
  '''
  
  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_source = MainSource("abc-news","ABC News","Worldwide trusted news source", "https://abcnews.go.com")
  
  def test_instance(self): 
    '''
    Testing whether the object instantiated from MainSource class exists
    '''
    self.assertTrue(isinstance(self.new_source,MainSource))
    
  def test_init(self): 
    '''
    Test to check whether the object is instantiated properly
    '''
    self.assertEqual(self.new_source.id,"abc-news")
    self.assertEqual(self.new_source.name,"ABC News")
    self.assertEqual(self.new_source.description,"Worldwide trusted news source")
    self.assertTrue(self.new_source.url, "https://abcnews.go.com")