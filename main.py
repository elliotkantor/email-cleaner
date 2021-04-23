import os
from pathlib import Path
import datetime
from tqdm import tqdm
import concurrent.futures

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


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def delete_msg(email_list):
    for m in email_list:
        m.trash()
        print(f"deleted {m.messages[0].subject}")
    print("finished deleting emails")


def main(run=False):
    if run:
        while all_emails_to_delete := get_emails():
            with concurrent.futures.ProcessPoolExecutor() as executor:
                executor.map(delete_msg, chunks(all_emails_to_delete, 10))
            print("new batch")


if __name__ == "__main__":
    run = input("Run? (y/n) ").lower().strip().startswith("y")
    main(run)
