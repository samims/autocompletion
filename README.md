# Fuzzy Search

## Installation and run

Create virtualenv (Python3.6)
```bash
$ python3.6 -m venv myvenv
```
Activate virtualenv using
```bash
source myvenv/bin/activate
```
Clone this repo
```bash
git clone
```
Install dependencies
```bash
pip install -r requirements.txt
```
Go to the project directory and run migrations files  using this command
```bash
python manage.py migrate
```

To run this project
```bash
python manage.py runserver
```

To run tests
```bash
python manage.py test
```

To test using postman use this endpoint
```bash
GET /search?word=<input>
```
use below code as header to send ajax request
```python
{X-Requested-With: XMLHttpRequest}
```

To test with html. Go to ```'/'``` url and type in the input box