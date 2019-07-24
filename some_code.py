# unused import
import __future__

SOME_HARDCODED_TOKEN = "dbdff73f-ca51-45f6-b1f1-3631f66164be"


def validate_filename(filename):
    # use of assert
    assert not filename.startswith("/")


def sqlinjection():
    import sqlalchemy

    engine = create_engine("sqlite:///bookstore.db")
    user_name = input("user name?")
    with engine.connect() as con:
        con.execute("SELECT * FROM public.user WHERE user_name=%s" % user_name)


def insecure_download():
    import requests

    return requests.get("https://google.com", verify=False)


def some_hardcoded_password():
    import requests

    password = "1234"
    requests.post("https://example.com", data=password)


def unencrypted_connection():
    import requests

    requests.get("http://example.com")


def unused_variables():
    x = 1
