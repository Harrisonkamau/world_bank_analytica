# Installation instructions
## NOTE:
This project uses Python2

Make sure you have `virtualenv` and `pip` installed on your PC
Please note that `pip` should be `pip2` if you're running `python3` as the default on your PC.

Create virtualenv:
Navigate into the cloned folder of this repo and run:

`virtualenv venv`

Activate the virtualenv environment:

`source ./venv/bin/activate`

Install application's dependencies:

`pip install -r requirements.txt`

Run:
`./setup.sh` then run: `flask run` to start the app

Or run the server with:
`python run.py server`
