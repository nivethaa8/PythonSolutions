from datetime import datetime
import time
import pytz
from pytz import timezone
#

# return PhaseTrigger.is_phrase_in(self, story.get_description())
#
# class Trigger(object):
#     def evaluate(self, story):
#         """
#         Returns True if an alert should be generated
#         for the given news item, or False otherwise.
#         """
#         # DO NOT CHANGE THIS!
#         raise NotImplementedError
#
#  y = NotTrigger(self.ft)
#         self.assertTrue(y.evaluate(b)
#
#
# T.evaluate(x)
#
# class PhaseTrigger(Trigger):
#     def __init__(self, phrase):
#         self.phrase = phrase
#
#     def is_phrase_in(self, text):
#         class DescriptionTrigger(PhaseTrigger):
#             def __init__(self, phrase):
#                 PhaseTrigger.__init__(self, phrase)
#
#             def evaluate(self, story):
#                 # STORY IS AN INSTANCE OF NEWSOBJECT
#                 """
#                 Returns True if an alert should be generated
#                 for the given news item, or False otherwise.
#                 """
#                 return PhaseTrigger.is_phrase_in(self, story.get_description())


text = "hello this is purple cow"
phrase = "purple cow"

if phrase not in text:
    print ("True")
else:
    print("false")

