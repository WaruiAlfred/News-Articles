from instance.config import NEWS_API_KEY
import os

class Config:
  '''
  General configuration parent class
  '''
  NEWS_ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
  NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class DevConfig(Config):
  '''
  Development  configuration child class
  '''
  DEBUG = True
  
config_options = {
  'development':DevConfig
}