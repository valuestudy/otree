from otree.api import *
import random

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
        min=0,  label="How much do you want to give?",
        blank=True
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

    desired_amount = models.FloatField(
        label="Ich wäre für den folgenden Betrag bereit, mich mit meinem Google Konto einzuloggen:",
        min=2,
        blank=True
    )

    assigned_price = models.FloatField(initial=0)
    # Your other page code...



    


# PAGES

class WTA_abfrage(Page):
    pass

class WTA_abfrage1(Page):
    pass

class WTA_abfrage2(Page):

    form_model = 'player'
    form_fields = ['WTA', 'desired_amount']

    @staticmethod
    def js_vars(player: Player):
        return dict(endowment=C.ENDOWMENT)

    @staticmethod
    def vars_for_template(self):
        if 'assigned_price' not in self.session.vars:
            self.session.vars['assigned_price'] = random.uniform(0, 2)
        return {
            'assigned_price': self.session.vars['assigned_price']
        }

    

   






page_sequence = [WTA_abfrage, WTA_abfrage1, WTA_abfrage2]
