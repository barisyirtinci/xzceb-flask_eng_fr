""" Translator Module """
from deep_translator import MyMemoryTranslator



def english_to_french(english_text):
    """ Translates English text to French """
    french_text = MyMemoryTranslator(source='english',target='french').translate(english_text)
    #translated text
    return french_text #return translated


def french_to_english(french_text):
    """ Translates French text to English """
    english_text = MyMemoryTranslator(source='french',target='english').translate(french_text)
    #translated text
    return english_text #return translated
