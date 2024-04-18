from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'cookiebanner'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    cookie_choice = models.StringField(
        label="Bitte wählen sie aus ob sie Cookies akzeptieren oder ablehnen wollen.",
        choices=[
            ['1', "Alle Cookies Akzeptieren"],
            ['2', "Alle Cookies Ablehnen"],
            ['3', "Marke"]
        ]
    
    )

    cookie_analytics = models.BooleanField(
        label="Stimmen Sie den Analytischen Cookies zu?",
        choices=[
            [True, "Analytische Cookies zugestimmt"],
            [False, "Analytische Cookies abgelehnt"]
        ],
        widget=widgets.RadioSelectHorizontal,
        blank=True,
    )

    cookie_marketing = models.BooleanField(
        label="Stimmen Sie den Marketings Cookies zu?",
        choices=[
            [True, "Marketing Cookies zugestimmt"],
            [False, "Marketing Cookies abgelehnt"]
        ],
        blank=True,
    )

    cookie_comfort = models.BooleanField(
        label="Stimmen Sie den Komfort Cookies zu?",
        choices=[
            [True, "Komfort Cookies zugestimmt"],
            [False, "Komfort Cookies abgelehnt"]
        ],
        blank=True,
    )

    


# PAGES
class Index(Page):

    form_model = 'player'
    form_fields = [ 'cookie_analytics', 'cookie_comfort', 'cookie_marketing' ]


    def vars_for_template(self):
        return {}



page_sequence = [Index]
