from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# some variables 
LIKERT_CHOICES = [
        [1, 'Stimme gar nicht zu'],
        [2, 'Stimme eher nicht zu'],
        [3, 'Neutral'],
        [4, 'Stimme eher zu'],
        [5, 'Stimme voll zu'],
    ]

KNOWLEDGE_CHOICES = [

            ['Wahr', 'Wahr'],
            ['Falsch', 'Falsch'],
            ['Weiß nicht', 'Weiß nicht'],
        ]
    


class Player(BasePlayer):


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


# SURVEY Preferences.html
    question1 = models.IntegerField(
        label="Es ist wichtig für mich, meine Privatsphäre im Internet zu schützen.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    question2 = models.IntegerField(
        label="Wenn ich Websites besuche, versuche ich normalerweise, so wenig Daten wie möglich preiszugeben.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    question3 = models.IntegerField(
        label="Ich schätze personalisierte Werbung, die auf meinen vorherigen Online-Aktivitäten zugeschnitten sind.",
        choices=LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

# SURVEY Preferences2.html

    question4 = models.IntegerField(
            label="...dass Online-Organisationen nicht sind, wer sie vorgeben zu sein?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

    question5 = models.IntegerField(
            label="...dass bei der Anmeldung oder bei Online-Einkäufen viele persönliche Informationen angeben werden müssen?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

    question6 = models.IntegerField(
            label="...dass Personen, die Sie nicht kennen, durch Ihre Online-Aktivitäten persönliche Informationen über Sie erhalten?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

    question7 = models.IntegerField(
            label="...über Online-Identitätsdiebstahl?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

    question8 = models.IntegerField(
            label="...dass eine Nachricht, die Sie jemandem online schicken, unberechtigterweise an andere weitergeleitet werden könnte?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

    question9 = models.IntegerField(
            label="...dass Informationen über Sie auf einem alten Computer gefunden werden könnten?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

    question10 = models.IntegerField(
            label="...dass Nachrichten, die Sie online erhalten, nicht von der Person stammen, die diese vorgibt zu sein?",
            choices=LIKERT_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )
    
# SURVEY Knowledge.html

    question11 = models.StringField(
            label="Die National Security Agency (NSA) greift nur auf Nutzerdaten zu, die öffentlich und für jedermann zugänglich sind.",
            choices=KNOWLEDGE_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )
    
    question12 = models.StringField(
            label="Betreiber sozialer Netzwerke (z.B. Facebook) sammeln und verarbeiten auch Informationen von Personen, die dieses Netzwerk gar nicht nutzen.",
            choices=KNOWLEDGE_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )
    
    question13 = models.StringField(
            label="Daten, die Betreiber sozialer Netzwerke (z.B. Facebook) über die Nutzer sammlen, werden nach 5 Jahren gelöscht.",
            choices=KNOWLEDGE_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )
    
    question14 = models.StringField(
            label="Unternehmen kombinieren Daten, die auf verschiedenen Websites im Internet hinterlassen werden und stellen daraus Nutzerprofile zusammen.",
            choices=KNOWLEDGE_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )
    
    question15 = models.StringField(
            label="E-Mails werden häufig über mehrere Rechner weitergeleitet, bevor sie bei ihrem eigentlichen Empfänger ankommen.",
            choices=KNOWLEDGE_CHOICES,
            widget=widgets.RadioSelectHorizontal,
        )

# SURVEY Knowledge2.html

    question16 = models.StringField(
            label="1. Was verbirgt sich hinter dem Begriff 'Browserverlauf'?",
            choices=[
                ['A', '... die Adressen besuchter Websites gespeichert.'],
                ['B', '... Cookies von besuchten Websites abgelegt.'],
                ['C', '... potenziell infizierte Websites separat abgelegt.'],
                ['D', '... je nach Browsertyp unterschiedliche Informationen über den Nutzer gespeichert.']
            ],
            widget=widgets.RadioSelect,
        )

    question17 = models.StringField(
            label="2. Was ist ein Cookie?",
            choices=[
                ['A', 'Eine Text-Datei, die es Websites ermöglicht, den Nutzer beim erneuten Besuch wiederzuerekennen'],
                ['B', 'Ein Programm, mit dem man die Datenspeicherung von Webanbietern unterbinden kann.'],
                ['C', 'Ein Computer-Virus, das man sich beim Besuch einer Website einfangen kann.'],
                ['D', 'Ein Browser Plugin, das sicheres Surfen gewährleistet.']
            ],
            widget=widgets.RadioSelect,
        )
    
    question18 = models.StringField(
            label="3. Was versteht man unter dem Begriff 'Cache'?",
            choices=[
                ['A', 'Ein Browser-Plug-In, welches den Datentransfer beim Surfen verschlüsselt.'],
                ['B', 'Ein Programm, welches Daten auf eine externe Festplatte kopiert, um diese vor Datenklau zu schützen.'],
                ['C', 'Ein Programm, welches Daten über den Internetnutzer gezielt ausspioniert und dann Dritte weiterleitet.'],
                ['D', 'Einen Puffer-Speicher, der das Surfen im Internet beschleunigt.']
            ],
            widget=widgets.RadioSelect,
        )
    
    question19 = models.StringField(
            label="4. Was versteht man unter einem 'Trojaner'?",
            choices=[
                ['A', '... den Rechner vor Viren und anderen Schadprogrammen schützt.'],
                ['B', '... als nützliche Anwendung getarnt ist, im Hintergrund aber eine andere Funktion erfüllt.'],
                ['C', '... nur zum Spaß entwickelt wurde und keine spezifische Funktion hat.'],
                ['D', '... als Computervirus in den 90ern Schaden anrichtete, heute aber nicht mehr existiert.']
            ],
            widget=widgets.RadioSelect,
        )
    
    question20 = models.StringField(
        label="5. Was ist eine 'Firewall'?",
        choices=[
            ['A', 'Eine neue technische Entwicklung, die verhindert, dass Daten bei einem Kurzschluss verloren gehen.'],
            ['B', 'Ein Browser-Plugin, das sicheres Surfen ermöglicht.'],
            ['C', 'Ein veraltetes Schutzprogramm gegen Computer-Viren.'],
            ['D', 'Ein Sicherungssystem, das den Computer vor unerwünschten Netzangriffen schützen soll.']
        ],
        widget=widgets.RadioSelect,
    )

# FUNCTIONS


# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['education', 'age', 'gender']


class Preferences(Page):
    form_model = 'player'
    form_fields = ['question1', 'question2', 'question3']

class Preferences2(Page):
    form_model = 'player'
    form_fields = ['question4', 'question5', 'question6', 'question7', 'question8', 'question9', 'question10']

class Knowledge(Page):
    form_model = 'player'
    form_fields = ['question11', 'question12', 'question13', 'question14', 'question15']

class Knowledge2(Page):
    form_model = 'player'
    form_fields = ['question16', 'question17', 'question18', 'question19', 'question20']


page_sequence = [Demographics, 
                 Preferences,
                   Preferences2,
                    Knowledge,
                     Knowledge2 ]
