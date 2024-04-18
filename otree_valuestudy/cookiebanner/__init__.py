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
    form_fields = [ 'cookie_choice', 'cookie_choice_settings', 'cookie_analytics', 'cookie_comfort', 'cookie_marketing' ]

    @staticmethod
    def vars_for_template(self):
        return {}
    
    @staticmethod
    def live_method(player: Player, data): #as it is not possible to send data via a button without submitting the form, the live method is used which sends data directly to the server on a click
        if data == 'all-accepted':
            player.cookie_choice = 'all-accepted'
        if data == 'all-declined':
            player.cookie_choice = 'all-declined'
        if data == 'all-accepted-settings':
            player.cookie_choice = 'all-accepted-settings'
        if data == 'apply-settings':
            player.cookie_choice = 'apply-settings'



page_sequence = [Index]
