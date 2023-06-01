# Suggestion-Box-Page - Project 6
The Suggestion Box Page is a web-based application developed to facilitate the submission, management, and review of suggestions from employees within an organization.


# Project 6
Suggestion Box Page

## Description
The Suggestion-Box-Page is a web application that allows employees to submit suggestions and resolutions. The system stores the suggestions and resolutions in a backend database and provides a user interface to view and manage the submitted suggestions.

## Features
Submit suggestions with corresponding employee ID and resolution.
View submitted suggestions in a table format.
Responsive user interface.
Thank you page after submitting a suggestion.
Easy navigation between pages.
Technologies Used
Django: Python web framework for backend development.
HTML: Markup language for creating web pages.
CSS: Styling language for web pages.
SQLite: Database for storing suggestion data.
Setup and Installation
Follow these steps to run the project locally:


## Clone the repository:

```
git clone https://github.com/dpmaharathy/Suggestion-Box-Page.git
```
## Change into the project directory:

```
cd Suggestion-Box-Page/suggestionbox
```

## Create a virtual environment:
```
python3 -m venv venv
```

## Activate the virtual environment:

### For Linux/macOS:

```
source venv/bin/activate
```
### For Windows (Command Prompt):
```
venv\Scripts\activate
```

## Install the dependencies:
```
pip install -r requirements.txt
```
## Run database migrations:

```
python manage.py migrate
```

## Start the development server:
```
python manage.py runserver
```
Now you can run the development server and access the form page at http://localhost:8000/suggestion/form/. After submitting the form, it will redirect to the thank you page and display the suggestions in a table at http://localhost:8000/suggestion/table/.

## Deleting all the entries from the database
Step 1:Open the Django shell
```
python manage.py shell
```
Step 2:Import the models from the app

```
from suggestion_app.models import Suggestion
```

Step 3:Run the following command to delete all objects from the model
```
Suggestion.objects.all().delete()
```
You can also delete selective responses by removing the all() method.
