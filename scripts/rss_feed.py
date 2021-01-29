#!/usr/bin/python3

import feedparser
NO_OF_FEEDS = 5


def get_feeds_from(url, desc):
    news_feed = feedparser.parse(url)
    top_k = news_feed.entries[:NO_OF_FEEDS]
    i = 0
    print("${font Inconsolata:pixelsize=16}${color gold}%s:" % desc)
    for entry in top_k:
        i += 1
        print("$font $color %s: %s" % (i, entry.title))
        print("${font Inconsolata:pixelsize=12}${color grey}\t%s" % entry.summary)


def main():
    get_feeds_from("http://feeds.feedburner.com/NDTV-LatestNews", "NDTV news")
    print("")
    get_feeds_from("https://news.ycombinator.com/rss", "Y-Combinator")


if __name__ == '__main__':
    main()
