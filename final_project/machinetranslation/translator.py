import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(
    apikey=apikey,
)

translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=auth,
)
translator.set_service_url(url)


def english_to_french(english_text: str) -> str:
    """
    Translate a string from English to French.
    :param english_text: str
    :return:
    """
    res = translator.translate([english_text], source="en", target="fr")
    french_text = res.result["translations"][0]["translation"]
    return french_text


def french_to_english(french_text: str) -> str:
    """
    Translate a string from French to English.
    :param french_text:
    :return:
    """
    res = translator.translate([french_text], source="fr", target="en")
    english_text = res.result["translations"][0]["translation"]
    return english_text
