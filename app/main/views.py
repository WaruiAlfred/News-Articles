from flask import render_template 
from . import main
from ..api_requests import get_news_sources,get_articles

# Views functions
@main.route('/') 
def index(): 
  '''
  View function that returns index.html template
  '''
  news_sources = get_news_sources()
  return render_template('index.html', sources = news_sources)

@main.route('/article/<source_id>')
def article(source_id): 
  '''
  Function that returns the article details 
  '''
  article_source_name = source_id.split(" ")
  article_name_format = "+".join(article_source_name)
  article = get_articles(article_name_format)
  title = 'Articles'
  
  return render_template('article.html', title = title, articles = article)