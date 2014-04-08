import uuid
import string
from django.core.signing import Signer

def get_protect_data():
    hash = get_hash()
    signer = Signer()
    data = { 
            'name' : hash,
            'code' : signer.sign(hash)
    }
        
    return data

def get_hash():
    return string.upper(uuid.uuid1().hex)

def validate_hash(data):
    signer = Signer()
    sign_code = ''
    
    try:
        sign_code = signer.unsign(data['code'])
    except:
        pass
    
    if data and data['name'] and data['code'] and data['name'] == sign_code:
        return True    
    
    return False