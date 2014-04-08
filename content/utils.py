from settings import SITE_NAMES, SITE_ID

def get_site_name():
    try:
        return SITE_NAMES[SITE_ID]
    except:
        return ''