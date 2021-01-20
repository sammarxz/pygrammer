from decouple import config

from instapy import InstaPy
from instapy import smart_run


USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')

session = InstaPy(username=USERNAME, password=PASSWORD)


with smart_run(session):
    session.set_do_follow(enabled=True, percentage=100)
    session.set_do_like(enabled=True, percentage=100)

    session.like_by_tags(["designinspiration", "Programming", "UIDesign", 
        "dribbblers", "Programmer", "webprogramming", "development",
        "webdevelopment", "computer", "tech"
    ], 5)

    comments = ["Nice", "Love your posts"]
    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(comments=comments, media="Photo")

    session.join_pods()