import unittest 
from app.designs import NewsArticles
 
class MovieTest(unittest.TestCase): 
  '''
  Test class to test the behaviour of the Movie class
  '''
  
  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_article = NewsArticles("A python ate a gorilla","https://www.theverge.com/2021/9/12/22670072/apple-iphone-13-pro-models-1tb-storage-kuo","https://cdn.vox-cdn.com/thumbor/gAXVb_WhDgd8U9o2cbzjPVtCrx8=/0x146:2040x1214/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/21973520/vpavic_4243_20201017_0077.0.jpg","2021-09-12T17:29:44Z")
  
  def test_instance(self): 
    '''
    Testing whether the object instantiated from NewsArticles class exists
    '''
    self.assertTrue(isinstance(self.new_article,NewsArticles))
    
  def test_init(self): 
    '''
    Test to check whether the object is instantiated properly
    '''
    self.assertEqual(self.new_article.title,"A python ate a gorilla")
    self.assertEqual(self.new_article.url,"https://www.theverge.com/2021/9/12/22670072/apple-iphone-13-pro-models-1tb-storage-kuo")
    self.assertEqual(self.new_article.urlToImage,"https://cdn.vox-cdn.com/thumbor/gAXVb_WhDgd8U9o2cbzjPVtCrx8=/0x146:2040x1214/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/21973520/vpavic_4243_20201017_0077.0.jpg")
    self.assertTrue(self.new_article.publishedAt,"2021-09-12T17:29:44Z")