# Median Price

## Create virtual Environment
install virtualenv
`python -m pip install virtualenv`

init virtualenv
`python -m venv env`

activate virtualenv
* Linux and macOS
`source env/bin/activate`

* Windows
`.\env\Scripts\activate`

install dependencies
`pip install -r requirement.txt`

## Config Environment Variables
rename from .env.template to .env
```
coinmarketcap_api_key = <api-key>
```

## Run server (activate virtualenv first)
`uvicorn main:app`