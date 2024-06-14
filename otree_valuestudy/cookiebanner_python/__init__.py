from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'cookiebanner_python'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):

    

    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    consent = models.BooleanField(
        label="Ich akzeptiere die Teilnahme und Datenschutzbestimmungen und bin mit der beschriebenen Datenverarbeitung einverstanden. ",
        choices=[
            [True, "Ja"],
            [False, "Nein"],
        ],

    
    )

    banner_design = models.StringField(
        label="Bitte wählen sie aus ob sie Cookies akzeptieren oder ablehnen wollen.",
        choices=[
            ["design1", "1"],
            ["design2", "2"],
            ["design3", "3"],
            ["design4", "4"]
        ],

        blank=True, initial=0,
    
    )

    cookie_choice = models.StringField(
        label="Bitte wählen sie aus ob sie Cookies akzeptieren oder ablehnen wollen.",
        choices=[
            ["all-accepted", "Alle akzeptiert"],
            ["all-declined", "Alle abgelehnt"],
            ["apply-settings", "Einstellungen anwenden"],
        ],
        initial="0",
        blank=True,
    
    )

    

    cookie_analytics = models.BooleanField(
        label="Stimmen Sie den Analytischen Cookies zu?",
        choices=[
            [True, "Analytische Cookies zugestimmt"],
            [False, "Analytische Cookies abgelehnt"]
        ],

        blank=True, initial=False,
    )

    cookie_marketing = models.BooleanField(
        label="Stimmen Sie den Marketings Cookies zu?",
        choices=[
            [True, "Marketing Cookies zugestimmt"],
            [False, "Marketing Cookies abgelehnt"]
        ],
        blank=True, initial=False,
    )

    cookie_comfort = models.BooleanField(
        label="Stimmen Sie den Komfort Cookies zu?",
        choices=[
            [True, "Komfort Cookies zugestimmt"],
            [False, "Komfort Cookies abgelehnt"]
        ],
        blank=True, initial=False,
    )

    education = models.StringField(
        label="Was ist Ihr höchster Bildungsabschluss?",
        choices=[
            ('NoDegree', 'Kein Abschluss'),
            ('MittlereReife', 'Mittlere Reife'),
            ('Abitur', 'Abitur'),
            ('University', 'Bachelor'),
            ('Master', 'Master'),
            ('Promotion', 'Promotion'),
        ],
        widget=widgets.RadioSelect,
    )

    age = models.IntegerField(
        label='What is your age?', min=13, max=125
        )

    gender = models.StringField(
        label="Geschlecht",
        choices=[
            ('männlich', 'männlich'),
            ('weiblich', 'weiblich'),
            ('divers', 'divers'),
            ('NA', 'möchte ich nicht angeben'),
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    


# PAGES
class Index(Page):

    form_model = 'player'
    form_fields = [ 'consent', 'banner_design', 'cookie_choice', 'cookie_analytics', 'cookie_comfort', 'cookie_marketing' ]


    def vars_for_template(self):
        if 'random_design' not in self.session.vars:
            designs = ["design1", "design2", "design3", "design4"]
            self.session.vars['random_design'] = random.choice(designs)
        return {
            'random_design': self.session.vars['random_design']
        }

    @staticmethod
    def live_method(player: Player, data):
        if data in ['design1', 'design2', 'design3', 'design4']:
            player.banner_design = data
        elif data in ['all-accepted', 'all-declined', 'all-accepted-settings', 'apply-settings']:
            player.cookie_choice = data

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant 
        participant.banner_design = player.banner_design
        participant.cookie_choice = player.cookie_choice

class Demographics(Page):
    form_model = 'player'
    form_fields = ['education', 'age', 'gender']



page_sequence = [Index, Demographics]
