import os
from pathlib import Path
import datetime
from tqdm import tqdm

os.chdir(Path("/Users/elliotkantor/Documents/python_personal/GoogleAPI/eli_gmail"))

# ezgmail docs: https://ezgmail.readthedocs.io/en/latest/
import ezgmail

assert ezgmail.LOGGED_IN, "Must be logged in"


def get_emails():
    # get date to start from
    before_date = (datetime.datetime.now() - datetime.timedelta(weeks=25)).strftime(
        "%m/%d/%Y"
    )
    # search queries: https://support.google.com/mail/answer/7190?hl=en
    emails_to_delete = ezgmail.search(
        f"before:{before_date} AND is:unread", maxResults=5000
    )
    return emails_to_delete


def main(run=False):
    emails_to_delete = get_emails()
    if run:
        batches = 0
        while emails_to_delete := get_emails():
            for thread in tqdm(emails_to_delete):
                thread.trash()
                # print(f"Deleted {thread.messages[0].subject}")
            batches += 1
            print(f"Deleted {len(emails_to_delete)} in batch {batches}\n")
    else:
        print("Cancelled")


if __name__ == "__main__":
    run = input("Run? (y/n) ").lower().strip().startswith("y")
    main(run)