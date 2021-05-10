<p float="left">
   <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?&style=for-the-badge&logo=pythonlogoColor=white"/>
   <img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white"/>
   <img alt="Firebase" src="https://img.shields.io/badge/firebase-%23039BE5.svg?&style=for-the-badge&logo=firebase"/>
   <img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?&style=for-the-badge&logo=docker&logoColor=white"/>

</p>

# Shopify Developer Intern Challenge

[Fall 2021 - Shopify Developer Intern Challenge](https://docs.google.com/document/d/1ZKRywXQLZWOqVOHC4JkF3LqdpO3Llpfk_CkZPR8bjak/edit#)

## Development

This application was developed using [Flask](https://flask.palletsprojects.com/en/1.1.x/) (a microframework for Python) and [Firebase](https://firebase.google.com/) (a flexible, scalable database for mobile, web, and server development). The images themselves reside on [Google Cloud Storage](https://cloud.google.com/storage).

The REST API has three main endpoints for adding, deleting, and searching through the image database. The image URLs are returned to the user based on the search criteria if specified, through which the images can be downloaded.

## Usage

### POST /add

Example:

```
curl --location --request POST 'http://0.0.0.0:8080/add' --form 'image=@"/C:/Users/Aryan/Downloads/pictures/car.jpg"'
```

Response body:

```
{
"success": true
}
```

### DEL /delete

Example:

```
curl --location --request DELETE 'http://0.0.0.0:8080/delete?filename=car.jpg'
```

Response body:

```
{
"success": true
}
```

### GET /search

Example:

```
curl --location --request GET 'http://0.0.0.0:8080/search'
```

Response body:

```
[
    {
        "Created": "Mon, 10 May 2021 00:30:51 GMT",
        "Url": "https://storage.googleapis.com/shopifycodingchallenge.appspot.com/dog.jpg",
        "filename": "dog.jpg",
        "size": "3.3 MB",
        "type": "image/jpeg"
    },
    {
        "Created": "Mon, 10 May 2021 00:30:57 GMT",
        "Url": "https://storage.googleapis.com/shopifycodingchallenge.appspot.com/sunrise.jpg",
        "filename": "sunrise.jpg",
        "size": "1.2 MB",
        "type": "image/jpeg"
    },
    {
        "Created": "Mon, 10 May 2021 03:17:18 GMT",
        "Url": "https://storage.googleapis.com/shopifycodingchallenge.appspot.com/car.jpg",
        "filename": "car.jpg",
        "size": "4.0 MB",
        "type": "image/jpeg"
    }
]
```

Example:

```
curl --location --request GET 'http://0.0.0.0:8080/search?filename=sunrise.jpg'
```

```
[
    {
        "Created": "Mon, 10 May 2021 00:30:57 GMT",
        "Url": "https://storage.googleapis.com/shopifycodingchallenge.appspot.com/sunrise.jpg",
        "filename": "sunrise.jpg",
        "size": "1.2 MB",
        "type": "image/jpeg"
    }
]
```

## Testing

The application can be can tested using two different methods. Firstly, using PyTest (framework used for simple unit tests to complex functional tests), which are in the `tests/tests.py`. The second is the Postman Collection which is a group of saved requests organized into a folder. This file can be imported into Postman and used for endpoint testing.

## Local Setup

- On Linux or macOS, run `source setup.sh`. This will create a python virtual environment with all of the packages required to execute the application.

- If there is an issue related to packaging dependency, then the `pip3 -r requirements.txt` can be used to install the same package version used for development.

- The file `env.py` contains the environment variables used in the Flask app. However, for security reasons this file has been added to .gitignore. A template version, `env.py.template` has been included for format purposes.

## Deployment

The following command can be run to build the Docker container and pushed to the container registry Cloud Run, which using the resources mentioned in the `cloudbuild.yaml` file.

```
gcloud builds submit --config cloudbuild.yaml .
```
