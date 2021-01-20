from decouple import config

from instapy import InstaPy
from instapy import smart_run


USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')

session = InstaPy(username=USERNAME, password=PASSWORD)


with smart_run(session):
    session.follow_user_followers(["frontendjoe", amount=3, randomize=False])

    session.join_pods()