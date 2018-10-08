"""
Utilities file
"""
import ast

# List of keys to filter from the datacatalog payload
ID_ENUMS = [ 'name', 'acronym', 'description', 'lastrevisiondate', 'contactdetails', 'popularity', 'coverage' ]

# Return 'metatype' lists from 'datacatalog'
def metatype_data(obj):
    filtered_payload = _filter_payload(obj)
    m_list = []
    for item in filtered_payload:
        for item in _object_filter(item, 'metatype'):
            m_list.append(item)
    return m_list


def metatype_filter(array):
    """
     metatype_data(obj) contains an array of:
     [{ id: '1', metatype: [{}] }]
     Get the metatype array from the datacatalog
     - only return objects with the fields in ID_ENUMS
    """
    new_list = list(filter(lambda x: x['id'] in ID_ENUMS, array))
    return new_list


def metatype_mapper(array):
    """
    param: list
    returns: refined list (remove 'id' and 'value')
    For Example:
    obj = [
        {'id': 'name', 'value': 'World Development Indicators'},
         {'id': 'acronym', 'value': 'WDI'},
         {'id': 'popularity', 'value': '3765'},
         {'id': 'coverage', 'value': '1960 - 2016'},
        ]
    returned_obj = {
        'name': 'World Development Indicators',
        'acronym': 'WDI',
        'popularity': '3765'
         }

         obj = [
             {
        'name': 'World Development Indicators',
        'acronym': 'WDI',
        'popularity': '3765'
         },
         {
        'name': 'World Development Indicators',
        'acronym': 'WDI',
        'popularity': '3765'
         }
         ]
    """
    final_list = []
    allowed_length = len(ID_ENUMS)
    for i in range(0, len(array), allowed_length):
        new_dict = {}
        for item in array[i:i+allowed_length]:
            new_dict[item['id']] = item['value']
        final_list.append(new_dict)
    return final_list


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
