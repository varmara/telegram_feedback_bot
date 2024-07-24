from pathlib import Path
import logging.config
import yaml

def setup_logging(config_path: Path|None=None):
    """
    Sets up logging configuration from a YAML file.

    Args:
        config_path (Path, optional): Path to the YAML configuration file. 
            Defaults to 'bot/logging/config_log.yaml'.
    """
    if not config_path:
        config_path = Path(__file__).parent / "config_log.yaml"
    with open(config_path, "rt") as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
