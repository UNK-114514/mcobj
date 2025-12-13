from util.lang import Lang
from util.translation_key import TranslationKey


class Translation:
    def __init__(self, lang: Lang = Lang()):
        self.lang = lang

    def get_translation(self, translation_key: TranslationKey):
        return self.lang.get_content()[translation_key.key]