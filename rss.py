import pickle
import time
import feedparser

from os.path import exists

sz_feed = 'https://rss.sueddeutsche.de/rss/Topthemen'
last_post_path = 'last_post.pickle'

def load_last_post_time():
    if not exists(last_post_path):
        last_post_time = time.gmtime(0) # Return January 1st, 1970
        with open(last_post_path, 'wb') as f:
            # Create file
            pickle.dump(last_post_time, f) 
    else:
        with open(last_post_path, 'rb') as f:
            last_post_time = pickle.load(f)

    return last_post_time

def get_new_posts():

    # Load time of last posted entry
    last_post_time = load_last_post_time()

    # Get articles
    feed_obj = feedparser.parse(sz_feed)
    entries = feed_obj['entries']

    # Only select important attributes:
    #   'title'            : Title
    #   'published_parsed' : Publishing date as obj
    #   'dcterms_abstract' : Teaser text
    #   'link'             : URL to article
    cleaned_entries = []
    for entry in entries:
        cleaned_entries.append({
            'headline': entry['title'],
            'date': entry['published_parsed'],
            'text': entry['dcterms_abstract'],
            'link': entry['link'],
        })

    # Reverse posts (oldest first)
    entries = cleaned_entries[::-1]

    # Return all entries to post
    entries_to_post = []
    for entry in entries:
        if entry['date'] > last_post_time:
            last_post_time = entry['date']
            entries_to_post.append(entry)

    # Save last post time, in case of update
    with open(last_post_path, 'wb') as f:
        pickle.dump(last_post_time, f)

    return entries_to_post

