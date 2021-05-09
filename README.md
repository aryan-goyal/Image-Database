<p float="left">
   <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?&style=for-the-badge&logo=pythonlogoColor=white"/>
   <img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white"/>
   <img alt="Firebase" src="https://img.shields.io/badge/firebase-%23039BE5.svg?&style=for-the-badge&logo=firebase"/>
   <img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?&style=for-the-badge&logo=docker&logoColor=white"/>

</p>

# ShopifyCodingChallenge

[Fall 2021 - Shopify Developer Intern Challenge](https://docs.google.com/document/d/1ZKRywXQLZWOqVOHC4JkF3LqdpO3Llpfk_CkZPR8bjak/edit#)

## Development

This is the application was developed using [Flask](https://flask.palletsprojects.com/en/1.1.x/) (a microframework for Python) and [Firebase](https://firebase.google.com/) (a flexible, scalable database for mobile, web, and server development), and deployed to Cloud Run (a serverless environment to run containers on Google Cloud).

## Local Setup

- On linux or macOS, run `source setup.sh`. This will create a python virutal enviroment with all of the packages required to execute the application.

- If there is an issue related to packaging dependency, then the `pip3 -r requirements.txt` can be used to install the same package version used for development.

- The file `env.py` contains the enviroment variables used in the Flask app. However, for security reasons this file has been added to .gitignore. A tempeleate version, `env.py.template` has been included for format purposes.

## Deployment
