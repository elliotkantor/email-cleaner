import os
from pathlib import Path

os.chdir(
    Path("/Users/elliotkantor/Documents/python_personal/GoogleAPI/eli.kant03 Sheets")
)

# ezgmail docs: https://ezgmail.readthedocs.io/en/latest/
import ezgmail

ezgmail.init(tokenFile="token.json", credentialsFile="credentials.json")
assert ezgmail.LOGGED_IN, "Must be logged in"

# search queries: https://support.google.com/mail/answer/7190?hl=en
emails_to_delete = ezgmail.search("")
