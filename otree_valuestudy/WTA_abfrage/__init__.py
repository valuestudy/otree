from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'WTA_abfrage'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    slider = models.FloatField(
        label='Choose a value between 0 and 5 EUR:',
        min=0,
        max=5
    )


    


# PAGES
class WTA_abfrage4(Page):
    pass


class WTA_abfrage2(Page):

    form_model = 'player'
    form_fields = ['slider']


   






page_sequence = [WTA_abfrage4, WTA_abfrage2]
