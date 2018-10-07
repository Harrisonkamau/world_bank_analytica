"""
Utilities file
"""
import ast

# List of keys to filter from the datacatalog payload
ID_ENUMS = [ 'name', 'acronym', 'description', 'lastrevisiondate', 'contactdetails', 'popularity', 'coverage' ]

# Return 'metatype' lists from 'datacatalog'
def metatype_data(obj):
    filtered_payload = _filter_payload(obj)
    for item in filtered_payload:
        return _object_filter(item, 'metatype')


def metatype_filter(array):
    """
     metatype_data(obj) contains an array of:
     [{ id: '1', metatype: [{}] }]
     Get the metatype array from the datacatalog
     - only return objects with the fields in ID_ENUMS
    """
    new_list = list(filter(lambda x: x['id'] in ID_ENUMS, array))
    return new_list



"""
HELPER FUNCTIONS
"""

def _string_decoder(string):
    """
    The DATA from the API comes in a unicode string:
    params: unicode string (u'{''})
    returns: decoded string: '{}'
    """
    new_str = ast.literal_eval(string)
    return new_str

def _object_filter(obj, key):
    """
    Filter an object:
    params: Dictionary and filter key
    returns the value of the filtered key
    For Example
    dict = { 'name': 'Nelson', 'age': 23 }
    _object_filter(dict, 'age') # returns 23
    """
    new_obj = obj.get(key)
    return new_obj


def _list_contains(lst, item):
    """
    Params: List of items & item
    Return: boolean if item exists in List
    """
    boolean = True if item in lst else False
    return boolean


def _filter_payload(obj):
    new_obj = _string_decoder(obj)
    catalog = _object_filter(new_obj, 'datacatalog')
    return catalog
