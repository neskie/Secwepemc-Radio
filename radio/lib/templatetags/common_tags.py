import feedparser #feedparser.org
import datetime
from django import template
from django.utils.html import strip_tags, escape
register = template.Library()

@register.inclusion_tag('feedreader.html')
def pull_feed(feed_url, posts_to_show=5):
    feed = feedparser.parse(feed_url)
    posts = []
    for i in range(posts_to_show):
        try:
            pub_date = feed['entries'][i].updated_parsed
            published = datetime.date(pub_date[0], pub_date[1], pub_date[2] )

            if 'news.google' in feed['entries'][i].link:
                st = feed['entries'][i].title.replace(' - ', '')
                posts.append({
                    'title': feed['entries'][i].title,
                    'summary': strip_tags(feed['entries'][i].summary).replace(st,''),
                    'link': feed['entries'][i].link.split('url=')[1],
                    'date': published,
                    })
            elif 'feedproxy.google.com' in feed['entries'][i].link:
                posts.append({
                    'title': feed['entries'][i].title,
                    'link': feed['entries'][i].link,
                    'summary': (strip_tags(feed['entries'][i].content[0].value)[0:].replace('";" alt="" />','')),
                    'date': published,
                    })
            else:
                posts.append({
                    'title': feed['entries'][i].title,
                    'summary': feed['entries'][i].summary,
                    'link': feed['entries'][i].link,
                    'date': published,
                    })
        except:
            pass
    return {'posts': posts}
