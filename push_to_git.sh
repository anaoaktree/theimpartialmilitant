#!/bin/bash
pip freeze > requirements.txt

git commit -m "updated reqs" requirements.txt
git push heroku master
git push -u origin master
