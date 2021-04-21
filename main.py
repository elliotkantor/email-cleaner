import os
from pathlib import Path
import datetime

os.chdir(Path("/Users/elliotkantor/Documents/python_personal/GoogleAPI/eli_gmail"))

# ezgmail docs: https://ezgmail.readthedocs.io/en/latest/
import ezgmail

ezgmail.init(tokenFile="token.json", credentialsFile="credentials.json")
assert ezgmail.LOGGED_IN, "Must be logged in"


def get_emails():
    # get date to start from
    before_date = (datetime.datetime.now() - datetime.timedelta(weeks=25)).strftime(
        "%m/%d/%Y"
    )
    # search queries: https://support.google.com/mail/answer/7190?hl=en
    emails_to_delete = ezgmail.search(f"before:{before_date} OR is:unread")
    return emails_to_delete


def main():
    emails_to_delete = get_emails()
    if (
        input(f"Delete {len(emails_to_delete)} emails? (y/n) ")
        .lower()
        .strip()
        .startswith("y")
    ):
        ezgmail.delete(emails_to_delete)
        print("Deleted")
    else:
        print("Cancelled")


if __name__ == "__main__":
    main()
