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

# SURVEY Knowledge2.html / 1 is true, 0 is false

    question16 = models.IntegerField(
            label="<b>1. Was verbirgt sich hinter dem Begriff 'Browserverlauf'? Im Browserverlauf werden...</b>",
            choices=[
                ['1', '... die Adressen besuchter Websites gespeichert.'],
                ['0', '... Cookies von besuchten Websites abgelegt.'],
                ['0', '... potenziell infizierte Websites separat abgelegt.'],
                ['0', '... je nach Browsertyp unterschiedliche Informationen über den Nutzer gespeichert.']
            ],
            widget=widgets.RadioSelect,
        )

    question17 = models.IntegerField(
            label="<b>2. Was ist ein Cookie?</b>",
            choices=[
                ['1', 'Eine Text-Datei, die es Websites ermöglicht, den Nutzer beim erneuten Besuch wiederzuerekennen'],
                ['0', 'Ein Programm, mit dem man die Datenspeicherung von Webanbietern unterbinden kann.'],
                ['0', 'Ein Computer-Virus, das man sich beim Besuch einer Website einfangen kann.'],
                ['0', 'Ein Browser Plugin, das sicheres Surfen gewährleistet.']
            ],
            widget=widgets.RadioSelect,
        )
    
    question18 = models.IntegerField(
            label="<b>3. Was versteht man unter dem Begriff 'Cache'?</b>",
            choices=[
                ['0', 'Ein Browser-Plug-In, welches den Datentransfer beim Surfen verschlüsselt.'],
                ['0', 'Ein Programm, welches Daten auf eine externe Festplatte kopiert, um diese vor Datenklau zu schützen.'],
                ['0', 'Ein Programm, welches Daten über den Internetnutzer gezielt ausspioniert und dann Dritte weiterleitet.'],
                ['1', 'Einen Puffer-Speicher, der das Surfen im Internet beschleunigt.']
            ],
            widget=widgets.RadioSelect,
        )
    
    question19 = models.IntegerField(
            label="<b>4. Was versteht man unter einem 'Trojaner'?</b>",
            choices=[
                ['0', '... den Rechner vor Viren und anderen Schadprogrammen schützt.'],
                ['1', '... als nützliche Anwendung getarnt ist, im Hintergrund aber eine andere Funktion erfüllt.'],
                ['0', '... nur zum Spaß entwickelt wurde und keine spezifische Funktion hat.'],
                ['0', '... als Computervirus in den 90ern Schaden anrichtete, heute aber nicht mehr existiert.']
            ],
            widget=widgets.RadioSelect,
        )
    
    question20 = models.IntegerField(
        label="<b>5. Was ist eine 'Firewall'?</b>",
        choices=[
            ['0', 'Eine neue technische Entwicklung, die verhindert, dass Daten bei einem Kurzschluss verloren gehen.'],
            ['0', 'Ein Browser-Plugin, das sicheres Surfen ermöglicht.'],
            ['0', 'Ein veraltetes Schutzprogramm gegen Computer-Viren.'],
            ['1', 'Ein Sicherungssystem, das den Computer vor unerwünschten Netzangriffen schützen soll.']
        ],
        widget=widgets.RadioSelect,
    )
# SURVEY Law.html

    question21 = models.StringField(
        label="<b>Die Weiterleitung anonymisierter Nutzerdaten zu Marktforschungszwecken in der EU ist gesetzlich erlaubt.</b>",
        choices=[
            ('1', 'Wahr'),
            ('0', 'Falsch'),
            ('NA', 'Weiß nicht'),
        ],
        widget=widgets.RadioSelect,
    )

    question22 = models.IntegerField(
        label="<b>Die EU-Richtlinien zum Datenschutz (z.B. die ePrivacy Richtlinie)...</b>",
        choices=[
            ('0', '...geben den EU-Ländern lediglich eine unverbindliche Orientierung hinsichtlich ihrer Datenschutzgesetze.'),
            ('0', '...gelten als länderübergreifendes EU-Datenschutzgesetz.'),
            ('1', '...müssen von allen EU-Ländern in das nationale Datenschutzgesetz implementiert werden.'),
            ('0', '...existieren bisher noch nicht.'),
        ],
        widget=widgets.RadioSelect,
    )

    question23 = models.StringField(
        label="<b>Für alle sozialen Netzwerkseiten gelten in Deutschland die gleichen Standard-AGBs. Abweichungen müssen von den Betreibern kenntlich gemacht werden.</b>",
        choices=[
            ('0', 'Wahr'),
            ('1', 'Falsch'),
            ('NA', 'Weiß nicht'),
        ],
        widget=widgets.RadioSelect,
    )

    question24 = models.StringField(
        label="<b>Laut dem deutschen Gesetz haben Nutzer von Online-Anwendungen, die personenbezogene Daten erheben und verarbeiten, einen Anspruch darauf, die über sie gespeicherten Daten einzusehen.</b>",
        choices=[
            ('1', 'Wahr'),
            ('0', 'Falsch'),
            ('NA', 'Weiß nicht'),
        ],
        widget=widgets.RadioSelect,
    )

    question25 = models.IntegerField(
        label="<b>Informationelle Selbstbestimmung ist...</b>",
        choices=[
            ('1', '...ein Grundrecht deutscher Bürger.'),
            ('0', '...ein philosophischer Begriff.'),
            ('0', '...die zentrale Forderung datenverarbeitender Stellen.'),
            ('0', '...die zentrale Aufgabe des Bundesdatenschutzbeauftragten.'),
        ],
        widget=widgets.RadioSelect,
    )

# Survey Law2.html

    question26 = models.StringField(
            label="Das Nachverfolgen der eigenen Internetnutzung kann durch das regelmäßige Löschen von Browserinformationen (Cookies, Cache, Browserverlauf) nicht erschwert werden.",
            choices=[
                ('1', 'Wahr'),
                ('0', 'Falsch'),
                ('NA', 'Weiß nicht'),
            ],
            widget=widgets.RadioSelect,
    )

    question27 = models.StringField(
            label="Durch das Surfen im 'Private Browsing'-Modus kann die Rekonstruktion des eigenen Surfverhaltens erschwert werden, da keine Browserinformationen gespeichert werden.",
            choices=[
                ('1', 'Wahr'),
                ('0', 'Falsch'),
                ('Weiß nicht', 'Weiß nicht'),
            ],
            widget=widgets.RadioSelect,
    )

    question28 = models.StringField(
            label="Durch die Nutzung von falschen Namen oder Pseudonymen kann die Identifizierung der eigenen Person im Internet zumindest erschwert werden.",
            choices=[
                ('1', 'Wahr'),
                ('0', 'Falsch'),
                ('NA', 'Weiß nicht'),
            ],
            widget=widgets.RadioSelect,
        )

    question29 = models.StringField(
            label="Auch wenn selbst schwere Passwörter von IT-Profis geknackt werden können, ist es sinnvoll, Passwörter zu verwenden, die aus einer Kombination von Buchstaben, Zahlen und Sonderzeichen bestehen und keine Wörter, Namen oder einfache Zahlenkombinationen enthalten.",
            choices=[
                ('1', 'Wahr'),
                ('0', 'Falsch'),
                ('NA', 'Weiß nicht'),
            ],
            widget=widgets.RadioSelect,
        )

    question30 = models.StringField(
            label="Um den Zugang zu eigenen Daten zu erschweren, sollte man verschiedene Passwörter und Benutzernamen für unterschiedliche Anwendungen nutzen und diese häufig ändern.",
            choices=[
                ('1', 'Wahr'),
                ('0', 'Falsch'),
                ('NA', 'Weiß nicht'),
            ],
            widget=widgets.RadioSelect,
        )
    

# Survey Usage.html

    internet_hours = models.StringField(
        label="<b>Wie viele Stunden verbringen Sie täglich im Internet?</b>",
        choices=[
            ('0-2h', '0 - 2 Stunden'),
            ('2-4h', '2 - 4 Stunden'),
            ('4-6h', '4 - 6 Stunden'),
            ('6-8h', '6 - 8 Stunden'),
            ('more-than-8h', 'Mehr als 8 Stunden'),
        ],
        widget=widgets.RadioSelect,
    )

    browser = models.StringField(
        label="<b>Welchen Browser benutzen Sie am meisten um im Internet zu surfen?</b>",
        choices=[
            ('Chrome', 'Chrome'),
            ('Microsoft Edge', 'Microsoft Edge'),
            ('Mozilla Firefox', 'Mozilla Firefox'),
            ('Safari', 'Safari'),
            ('Brave', 'Brave'),
        ],
        widget=widgets.RadioSelect,
    )

    other_browser = models.StringField(
        label="Andere Browser:",
        blank=True,
    )

    mobile_os = models.StringField(
        label="<b>Welches mobile Betriebssystem benutzen Sie auf Ihrem Smartphone?</b>",
        choices=[
            ('noSmartphone', 'Ich habe kein Smartphone'),
            ('iOS', 'iOS'),
            ('Android', 'Android'),
            ('unknown', 'Weiß nicht'),
        ],
        widget=widgets.RadioSelect,
    )

    email_provider = models.StringField(
        label="<b>Welchen E-Mail-Provider benutzen Sie?</b>",
        choices=[
            ('Gmail', 'Gmail'),
            ('GMX', 'GMX'),
            ('Outlook', 'Outlook'),
            ('T-Online', 'T-Online'),
            ('Web.de', 'Web.de'),
            ('ProtonMail', 'ProtonMail'),
        ],
        widget=widgets.RadioSelect,
    )

    other_email_provider = models.StringField(
        label="<b>Anderer Provider:</b>",
        placeholder='Anderer Provider eingeben...',
        blank=True,
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

class Law(Page):
    form_model = 'player'
    form_fields = ['question21', 'question22', 'question23', 'question24', 'question25']


class Law2(Page):
    form_model = 'player'
    form_fields = ['question26', 'question27', 'question28', 'question29', 'question30']

class Usage(Page):
    form_model = 'player'
    form_fields = ['internet_hours', 'browser', 'other_browser', 'mobile_os', 'email_provider', 'other_email_provider']



page_sequence = [ Demographics, 
                 Preferences,
                   Preferences2,
                    Knowledge,
                     Knowledge2,
                      Law,
                       Law2,
                       Usage
                        ]
