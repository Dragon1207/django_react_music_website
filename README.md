# README

## Introduction

[![Build Status](https://travis-ci.org/osya/music_website.svg)](https://travis-ci.org/osya/music_website) [![Coverage Status](https://coveralls.io/repos/github/osya/music_website/badge.svg?branch=master)](https://coveralls.io/github/osya/music_website?branch=master)

Django-based Music website created during the video serie [Django Tutorials for Beginners](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK)

Used technologies:

- Python & Django
- Testing: Selenium & PhantomJS & Factory Boy
- Assets management: NPM & Webpack
- Travis CI
- Deployed at [Heroku](https://django-music-website.herokuapp.com)

## Installation

```shell
    git clone https://github.com/osya/music_website
    cd music_website
    pip install -r requirements.txt
    npm install
    node node_modules/webpack/bin/webpack.js
    python manage.py collectstatic
    python manage.py runserver
```

## Usage

## Tests

To run all tests, run

```shell
    python manage.py test
```
