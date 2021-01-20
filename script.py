from decouple import config

from instapy import InstaPy
from instapy import smart_run


USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')

session = InstaPy(username=USERNAME, password=PASSWORD)


with smart_run(session):
    session.set_do_follow(enabled=True, percentage=100)
    session.set_do_like(enabled=True, percentage=100)
    session.follow_likers(["frontendjoe"], photos_grab_amount=1, follow_likers_per_photo=2, randomize=False, sleep_delay=600, interact=True)

    session.join_pods()