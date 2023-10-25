from django.conf import settings
import hashlib
from datetime import datetime

class UrlSecutity:
    
    @staticmethod
    def get_today_formatted():
        return datetime.today().strftime('%d%m%Y')
        
        
    @staticmethod
    def get_url_hashcode(url):
        
        value_to_encode = url + settings.SECRET_KEY + UrlSecutity.get_today_formatted()
        hashcode = value_to_encode.encode('UTF-8')
        hashcode = hashlib.sha256(hashcode).hexdigest()
        return f"{settings.URL_HASH_PARAM_NAME}={hashcode}"
    
    @staticmethod
    def is_valid_url(request):
        
        url = request.path
        if settings.URL_HASH_PARAM_NAME in url:
            return False
        
        url_hash_param_value = request.GET.get(settings.URL_HASH_PARAM_NAME)
        
        if not url_hash_param_value:
            return False
        
        value_to_encode = url + settings.SECRET_KEY + UrlSecutity.get_today_formatted()
        hashcode_calculated = value_to_encode.encode('UTF-8')
        hashcode_calculated = hashlib.sha256(hashcode_calculated).hexdigest()
        
        return ( str(hashcode_calculated) != str(url_hash_param_value) )
            
        
        
        
        
        
        