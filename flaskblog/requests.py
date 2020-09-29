import urllib.request,json
from .models import Quotes

# base_url = None
base_url = 'http://quotes.stormconsultancy.co.uk/quotes.json'

# def configure_request(app):
#     global base_url
#     base_url = app.config['QUOTES_API_BASE_URL']
    
def get_quotes():

    get_quotes_url = base_url
    
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
        
        quotes_results = None
        if get_quotes_response:
            quotes_results_list = get_quotes_response
            quotes_results = process_results(quotes_results_list)
            
    return quotes_results
    

def process_results(quotes_list):
    
    quote_results = []
    
    for quote_item in quotes_list:
        author = quote_item.get('author')
        id = quote_item.get('id')
        quote = quote_item.get('quote')
        permalink = quote_item.get('permalink')
        
        if quote:
            quote_object = Quotes(author,id, quote, permalink)
            quote_results.append(quote_object)
            
    return quote_results