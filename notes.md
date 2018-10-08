# Flask BluePrints
- These are used to created re-usable components
- All related modules are grouped together
- I have created two of such: `auth` for authentication and `main` for functionality other than authentication

# Database
- This app uses SQLite3, be sure to have this installed on your PC


# Models
### User
- Has fields such as: email, username and password (hashed)

### Catalog
- Fields: The data from the API had innumerable fields, but for readability, I used a few of them.
- 'name', 'acronym', 'description', 'lastrevisiondate', 'contactdetails', 'popularity', 'coverage'

# Implementation
- Fetch data from the API
- This returns an unicode string: this method `_string_decoder()` in `utils.py` file decodes it to a normal string
- Filter the data to return only `datacatalog`. That's being handled by `_filter_payload()` method in `utils.py` file
- `datacatalog` is composed of objects of `id` and `metatype`. Filter the `metatype` lists and omit the `ids`
- `metatype` is contains a list of objects in `id` & `value`, key-value pairs respectively.
- Next step was to merge the objects in `metatype` list to generate objects with the chosen fields for creating new `Catalog` model
- However, if you want to add more fields, add them to `ID_ENUMS` list in `utils.py` file.

## Justification
- Merging the data into the respective keys and values would help us save the data in an orderly fashion to db (SQLite3)
- Filtering the api, allows us to have fields to choose from while visualising data.
- Visualisations are the next part of the implementation here [Highcharts.js](https://www.highcharts.com/) would be my library of choice.

## Utils
- All helper methods are stored in the `utils.py` file
