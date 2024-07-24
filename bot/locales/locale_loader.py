import logging
from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader

logger = logging.getLogger(__name__)

def get_fluent_localization(language: str) -> FluentLocalization:
    """
    A function that retrieves the FluentLocalization for a specific language based on the provided language parameter.
    """
    locale_dir = Path(__file__).resolve().parent / language.lower()
    logger.debug(f"Language: {language}; " \
                 f"Locales directory: {locale_dir}")

    if not locale_dir.exists():
        raise FileNotFoundError(f'Directory for "{language}" locale not found')

    locale_files = [str(file) for file in locale_dir.glob("*.ftl")]

    l10n_loader = FluentResourceLoader(str(locale_dir.joinpath("{locale}")))
    logger.debug("Locale set successfully.")
    return FluentLocalization([language], locale_files, l10n_loader)
