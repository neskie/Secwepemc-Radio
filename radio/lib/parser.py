from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    count = 0

    def handle_starttag(self, tag, attrs):
        print "Encountered the beginning of a %s tag" % tag

    def handle_endtag(self, tag):
        print "Encountered the end of a %s tag" % tag
