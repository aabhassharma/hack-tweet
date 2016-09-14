import os
import sys
import twitter

def get_twitter_creds():
    '''
    Get credentials as set in env because you're not an idiot and don't want to
    commit those
    '''
    creds_dict = {}
    creds_dict['consumer_key'] = os.environ['twitter_consumer_key']
    creds_dict['consumer_secret'] = os.environ['twitter_consumer_secret']
    creds_dict['access_token_key'] = os.environ['twitter_access_token_key']
    creds_dict['access_token_secret'] = os.environ['twitter_access_token_secret']
    return creds_dict


def get_twitter_api(twitter_creds):
    '''
    Reusable instance of the API wrapper
    '''
    api = twitter.Api(
        consumer_key=twitter_creds['consumer_key'],
        consumer_secret=twitter_creds['consumer_secret'],
        access_token_key=twitter_creds['access_token_key'],
        access_token_secret=twitter_creds['access_token_secret'])
    return api


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


if __name__ == "__main__":
    try:
        twitter_creds = get_twitter_creds()
    except KeyError:
        print "You fool you didn't set the env vars"
        sys.exit(1)
    api = get_twitter_api(twitter_creds=twitter_creds)
    trending_articles = api.GetTrendsCurrent()
    # Now we have the trends
    for trend in trending_articles:
        # I don't want the bullshit that has any promoted content with it
        if trend.promoted_content:
            continue
        # There's some unsanitized data in here
        # Simple sanitation
        if "\\" in trend.name:
            continue
        if not is_ascii(trend.name):
            continue
        # Find the most popular tweets that are mentioning this trend
        # But I also want to limit it to within 100 miles of my location
        searched_tweets = api.GetSearch(
            term=trend.name,
            geocode="37.774929,-122.419416,100mi",
            result_type="popular")
        # Got empty list, skip
        if not searched_tweets:
            continue
        # VOILA! You have the most popular tweets within 100 miles of my location
        # that are referencing the most popular trending hashtags right Now
        print searched_tweets
