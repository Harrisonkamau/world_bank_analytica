"""
Utilities file
"""

def filter_payload(obj):
    new_obj = string_decoder(obj)
    catalog = obj.get('datacatalog')
    return catalog


def string_decoder(string):
    new_str = string.decode('utf-8')
