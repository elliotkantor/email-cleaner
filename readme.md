# Email Cleaner
## Installation
### Python setup
1. Make sure python 3 is installed (and use a virtual environment)
2. Clone the repo with `git clone https://github.com/elliotkantor/email-cleaner.git`
3. `pip install -r requirements.txt` to install everything
### Set up Gmail API
1. Go to [https://developers.google.com/gmail/api/quickstart/python/](https://developers.google.com/gmail/api/quickstart/python/)
2. Create a project and enable the API
3. Make a new project
4. In APIs & Services, Enable APIs and Services
5. Enable Gmail API
6. In Credentials on dashboard, add OAuth 2.0 Client ID
7. Download json and rename it `credentials.json`
8. In OAuth Consent Screen, Publish your app
9. Move json into `email-cleaner` directory and run code, then allow access from a web browser and use the API as normal
### Run the code
1. `python3 main.py` to run
2. You will have to authorize Gmail access to your account the first time you run this
3. When prompted, type `y` or `yes`