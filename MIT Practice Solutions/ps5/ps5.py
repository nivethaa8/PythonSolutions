import feedparser
import string
from time import time
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


# -----------------------------------------------------------------------
# ======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
# ======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
        #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
        #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret


# ======================
# Data structure design
# ======================

# Problem 1

class NewsStory(object):

    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


# ======================
# Triggers
# ======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger

class PhaseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def is_phrase_in(self, text):
        # return True if whole phrase is in the text
        # return False if whole phrase is not in the text
        # method is not case-sensitive
        # This is abstract class, not instantiating any PhaseTriggers
        # PhaseTrigger inherits evaluate method from Trigger
        # Can create subclasses of PhaseTrigger and use is_phase_in function

        positions = []
        text = text.lower()
        text_without_punc_list = []
        phrase_split = self.phrase.lower().split()
        punc = string.punctuation
        punc = list(punc)
        text_list = list(text)

        for index, element in enumerate(text_list):
            if element in punc:
                text_without_punc_list.insert(index, ' ')
            else:
                text_without_punc_list.append(element)

        text_without_punc = ''.join(text_without_punc_list)
        text_without_punc_split = text_without_punc.split()

        for (element_phrase) in phrase_split:
            for (index_text, element_text) in enumerate(text_without_punc_split):
                if element_phrase == element_text:
                    positions.append(index_text)

        if len(positions) <= 1:
            for i in positions:
                if self.phrase == (text_without_punc_split[i]):
                    return True
        else:
            for index in range(len(positions) - 1):
                if (positions[index + 1]) == positions[index] + 1:
                    return True
                else:
                    return False


# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhaseTrigger):

    def __init__(self, phrase):
        PhaseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        # STORY IS AN INSTANCE OF NEWSOBJECT
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        if PhaseTrigger.is_phrase_in(self, story.get_title):
            return True
        return False


# An instance of this type of trigger could be used to generate an
# alert whenever the phrase 'intel processors' occured in the title of news item
# Once implement TitleTrigger, unit tests should pass
# Subclasses inherit from Trigger interface
# should include a working evaluate method
# FAIL -> code runs but produces wrong answer
# Error -> means code crashes due to some error

# Problem 4

class DescriptionTrigger(PhaseTrigger):
    def __init__(self, phrase):
        PhaseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        # STORY IS AN INSTANCE OF NEWSOBJECT
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return PhaseTrigger.is_phrase_in(self, story.get_description)


# TIME TRIGGERS

# Problem 5
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, str_time):
        # Convert string to 'datetime' object, set timezone to EST
        time = datetime.strptime(str_time, "%d %b %Y %H:%M:%S")
        # time = time.replace(tzinfo=pytz.timezone("EST"))

        self.time = time

# Problem 6

# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        try:
            condition = story.get_pubdate() < self.time
        except:
            self.time = self.time.replace(tzinfo=pytz.timezone("EST"))
            condition = story.get_pubdate() < self.time

        if condition:
            return True
        else:
            return False


class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        try:
            condition = story.get_pubdate() > self.time
        except:
            self.time = self.time.replace(tzinfo=pytz.timezone("EST"))
            condition = story.get_pubdate() > self.time

        if condition:
            return True
        else:
            return False


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

class NotTrigger(Trigger):
    def __init__(self, T):
        self.T = T

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """

        return not self.T.evaluate(story)


# Problem 8
# TODO: AndTrigger

class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """

        return self.T1.evaluate(story) and self.T2.evaluate(story)


# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """

        return self.T1.evaluate(story) or self.T2.evaluate(story)


# ======================
# Filtering
# ======================
# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.
    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    filtered_stories = []
    for story in stories:
        if any([T.evaluate(story) for T in triggerlist]):
            filtered_stories.append(story)
    return filtered_stories

# ======================
# User-Specified Triggers
# ======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file
    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # 'lines' is the list of lines that you need to parse and for which you need
    # to build triggers

    # Initialize trigger mapping dictionary
    t_map = {"TITLE": TitleTrigger,
             "DESCRIPTION": DescriptionTrigger,
             "AFTER": AfterTrigger,
             "BEFORE": BeforeTrigger,
             "NOT": NotTrigger,
             "AND": AndTrigger,
             "OR": OrTrigger
             }

    # Initialize trigger dictionary, trigger list
    trigger_dict = {}
    trigger_list = []

    # Helper function to parse each line, create instances of Trigger objects,
    # and execute 'ADD'
    def line_reader(line):
        data = line.split(',')
        if data[0] != "ADD":
            if data[1] == "OR" or data[1] == "AND":
                trigger_dict[data[0]] = t_map[data[1]](trigger_dict[data[2]],
                                                       trigger_dict[data[3]])
            else:
                trigger_dict[data[0]] = t_map[data[1]](data[2])
        else:
            trigger_list[:] += [trigger_dict[t] for t in data[1:]]

    for line in lines:
        line_reader(line)

    return trigger_list


SLEEPTIME = 10  # seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("COVID-19")
        t2 = DescriptionTrigger("Trudeau")
        t3 = DescriptionTrigger("virus")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica", 14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title() + "\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:
            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stori   es RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
