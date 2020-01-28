# Minsk lombards scrapper

## About

[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/manti-by/Apollo/master/LICENSE)

Author: Alexander Chaika <manti.by@gmail.com>

Source link: https://github.com/manti-by/lmscraper/

Requirements: Python 3.6+, Scrapy


## Setup development environment  

1. Install, create and activate virtualenv

        $ sudo pip install virtualenv  
        $ virtualenv -p python3 --no-site-packages --prompt=lms- venv  
        $ source venv/bin/activate  

3. Clone sources and install pip packages

        $ mkdir lmscraper/ && cd lmscraper/  
        $ git clone https://github.com/manti-by/lmscraper.git src && cd src/  
        $ pip install -r requirements.txt  

4. Run local dev server or prod server

        $ cd lmscraper  
        $ scrapy crawl reallombard

