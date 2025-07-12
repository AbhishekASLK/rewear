import os
import gettext
import polib
from pathlib import Path
from typing import Callable

DOMAIN = "messages"

def compile_translations(i18n_root: Path):
    """
    Recursively compile all .po files in a given i18n root dir.
    Expected structure: i18n/<locale>/LC_MESSAGES/messages.po
    """
    if not i18n_root.exists():
        print(f"[i18n] No i18n directory found at {i18n_root}")
        return

    for locale_dir in i18n_root.iterdir():
        po_path = locale_dir / "LC_MESSAGES" / f"{DOMAIN}.po"
        mo_path = locale_dir / "LC_MESSAGES" / f"{DOMAIN}.mo"
        if po_path.exists():
            try:
                po = polib.pofile(str(po_path))
                mo_path.parent.mkdir(parents=True, exist_ok=True)
                po.save_as_mofile(str(mo_path))
                print(f"[i18n] Compiled {po_path} → {mo_path}")
            except Exception as e:
                print(f"[i18n] Error compiling {po_path}: {e}")

def get_translations(i18n_root: Path, locale: str) -> Callable[[str], str]:
    """
    Returns a translation function for the given i18n root and locale.
    """
    try:
        translation = gettext.translation(DOMAIN, localedir=i18n_root, languages=[locale], fallback=True)
        return translation.gettext
    except Exception as e:
        print(f"[i18n] No translation found for locale '{locale}' in {i18n_root}: {e}")
        return lambda s: s