class MainSource: 
  '''
  Class to define news sources url
  '''
  def __init__(self,id,name,description,url):
    self.id = id 
    self.name = name 
    self.description = description
    self.url = url
    
class NewsArticles: 
  '''
  Class to define news articles objects according to sources
  '''
  def __init__(self,title,url,urlToImage,publishedAt):
    self.title = title 
    self.url = url 
    self.urlToImage = urlToImage 
    self.publishedAt = publishedAt
    