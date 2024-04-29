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

    
    banner_design = models.StringField(
        label="Bitte wählen sie aus ob sie Cookies akzeptieren oder ablehnen wollen.",
        choices=[
            ["design1", "1"],
            ["design2", "2"],
            ["design3", "3"],
            ["design4", "4"]
        ],

        blank=True,
    
    )

    cookie_choice = models.StringField(
        label="Bitte wählen sie aus ob sie Cookies akzeptieren oder ablehnen wollen.",
        choices=[
            ["all-accepted", "Alle akzeptiert"],
            ["all-declined", "Alle abgelehnt"]
        ],

        blank=True,
    
    )

    cookie_choice_settings = models.StringField(
        label="Bitte wählen sie aus ob sie Cookies akzeptieren oder ablehnen wollen.",
        

        blank=True,
    )

    cookie_analytics = models.BooleanField(
        label="Stimmen Sie den Analytischen Cookies zu?",
        choices=[
            [True, "Analytische Cookies zugestimmt"],
            [False, "Analytische Cookies abgelehnt"]
        ],

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
    form_fields = [ 'banner_design', 'cookie_choice', 'cookie_choice_settings', 'cookie_analytics', 'cookie_comfort', 'cookie_marketing' ]

  
    
    @staticmethod
    def live_method(player: Player, data):
        if data in ['design1', 'design2', 'design3', 'design4']:
            player.banner_design = data
        elif data in ['all-accepted', 'all-declined', 'all-accepted-settings', 'apply-settings']:
            player.cookie_choice = data



page_sequence = [Index]
