import time

from mastodon import Mastodon
from rss import get_new_posts

mastodon = Mastodon(
        access_token = 'token.secret',
        api_base_url = 'muenchen.social'
)

#mastodon.status_post('hello world')

if __name__ == '__main__':
    while True:
        # Get posts
        posts = get_new_posts()
        if len(posts) > 0:
            print(time.asctime(time.localtime()), f'Found {len(posts)} new post(s)')
            for post in posts:
                status = f'{post["headline"]}\n\n{post["text"]}\n\n{post["link"]}'
                mastodon.status_post(status, language='de')

        # Wait for two minutes
        time.sleep(2 * 60)
