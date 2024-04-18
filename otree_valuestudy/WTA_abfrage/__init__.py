from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'WTA_abfrage'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Your other page code...

    # Define the question

    WTA = models.FloatField(
        min=0, max=C.ENDOWMENT, label="How much do you want to give?"
    )

    login_option = models.StringField(
    choices=[
            ["option1", "Ich das grundsätzlich nicht möchte."],
            ["option2", "Ich dafür nur bereit wäre für einen Betrag, der über 5 EUR liegt."],
            ["option3", "Ich kein Google Konto habe."]
        ],
    label="Ich bin nicht bereit, mich für eine Zusatzvergütung mit meinem Google Konto einzuloggen, weil",
    widget=widgets.RadioSelect
    )

    amount = models.FloatField(
        label="Ich wäre für den folgenden Betrag bereit, mich mit meinem Google Konto einzuloggen:",
        min=5,
        blank=True
    )
    # Your other page code...



    


# PAGES

class WTA_abfrage(Page):
    pass

class WTA_abfrage2(Page):

    form_model = 'player'
    form_fields = ['WTA']
    @staticmethod
    def js_vars(player: Player):
        return dict(endowment=C.ENDOWMENT)




   






page_sequence = [WTA_abfrage, WTA_abfrage2]
