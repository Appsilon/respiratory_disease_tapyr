import sys
from pathlib import Path

from loguru import logger
from shiny import App

from respiratory_disease_tapyr.settings import AppSettings
from respiratory_disease_tapyr.view.root import get_dashboard_ui, server

# Setup settings and logger
app_settings = AppSettings()
logger.remove()
logger.add(sys.stderr, level=app_settings.log_level)

# Combine clean shiny UI with CSS and external resources
# ui_with_css = ui.TagList(ui.tags.link(href="style.css", rel="stylesheet"), get_dashboard_ui())

app_dir = Path(__file__).parent
app = App(get_dashboard_ui(), server, static_assets=app_dir / "www")
