import urllib.request,json 
from .designs import MainSource,NewsArticles

# Getting the news api key
apiKey = None

# Getting the news sources&articles base urls
sources_base_url = None
articles_base_url = None

def configure_api_requests(app): 
  '''
  Function to help gain access to application configuration objects
  '''
  global apiKey,sources_base_url,articles_base_url
  apiKey = app.config['NEWS_API_KEY']
  sources_base_url = app.config['NEWS_SOURCES_BASE_URL']
  articles_base_url = app.config['NEWS_ARTICLES_BASE_URL']
  

# Actual API requests

def get_news_sources(): 
  '''
  Function the gets the json response
  '''
  get_news_sources_url = sources_base_url.format(apiKey) 
  
  with urllib.request.urlopen(get_news_sources_url) as url: 
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)
    
    news_sources_outcomes = None
    
    if get_sources_response['sources']: 
      sources_list = get_sources_response['sources']
      news_sources_outcomes = process_results(sources_list)
      
  return news_sources_outcomes

def process_results(sources_list):
  '''
  Function  that processes the news sources outcomes and transform them to a list of Objects
  '''
  sources_results = []
  for sources in sources_list:
    id = sources.get('id')
    name = sources.get('name')
    description = sources.get('description')
    url = sources.get('url')
    
    sources_object = MainSource(id,name,description,url)
    sources_results.append(sources_object)

  return sources_results

def get_articles(source_id): 
  '''
  Function to get news articles according to news sources
  '''
  get_articles_details_url = articles_base_url.format(source_id,apiKey)
  
  with urllib.request.urlopen(get_articles_details_url) as url: 
    articles_details_data = url.read()
    articles_details_response = json.loads(articles_details_data)
    
    articles_details = None
    
    if articles_details_response['articles']: 
      articles_list = articles_details_response['articles']
      articles_details = process_articles(articles_list)
    
  return articles_details

def process_articles(articles_list):
  '''
  Function  that processes the articles list and transform them to a list of Objects
  '''
  articles_results = []
  for articles in articles_list:
    title = articles.get('title')
    url = articles.get('url')
    urlToImage = articles.get('urlToImage')
    publishedAt = articles.get('publishedAt')
    
    articles_object = NewsArticles(title,url,urlToImage,publishedAt)
    articles_results.append(articles_object)

  return articles_results