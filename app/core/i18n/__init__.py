from app.core.config.config import settings
from app.core.i18n.locale import compile_translations

'''
This method will orchestrate translation compilation across all enabled modules.

'''

def compile_all_translations():
    for module in settings.ENABLED_MODULES:
        i18n_path = settings.MODULES_DIR / module / "i18n"
        if i18n_path.exists():
            compile_translations(i18n_path)
