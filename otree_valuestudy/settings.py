from os import environ



SESSION_CONFIGS = [
    


dict(
        name='cookiebanner', 
        display_name="The cookiebanner shown to participants",
        app_sequence=['cookiebanner', 'WTA_abfrage',  'survey', 'paternalism', 'debriefing'], 
        num_demo_participants=1
    ),

 

    dict(
        name='WTA_abfrage', 
        display_name="The WTA method.",
        app_sequence=['WTA_abfrage'], 
        num_demo_participants=1
    ),

    
    dict(
        name='survey', 
        display_name="The survey about internet usage for participants",
        app_sequence=['survey'], 
        num_demo_participants=1
    ),

    

    dict(
            name='paternalism', 
            display_name="Survey regarding Paternalism",
            app_sequence=['paternalism'], 
            num_demo_participants=1
        ),

    dict(
        name='debriefing', 
        display_name="The last part of the survey.",
        app_sequence=['debriefing'], 
        num_demo_participants=1
    ),

     
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['cookie_choice',  'banner_design']
SESSION_FIELDS = []


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3269395020090'
