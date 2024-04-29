from typing import cast

from ipyleaflet import basemaps
from shiny import module, ui
from shinywidgets import output_widget

from respiratory_disease_tapyr.helpers.helper_text import (
    about_text,
    dataset_information,
    missing_note,
    slider_text_map,
)

basemap = cast(dict, basemaps)


@module.ui
def map_ui():
    return ui.tags.div(
        ui.tags.div(
            about_text,
            ui.tags.hr(),
            slider_text_map,
            ui.tags.br(),
            ui.input_slider(
                id="years_value",
                label="Select Year",
                min=1990,
                max=2017,
                value=2010,
                sep="",
            ),
            ui.tags.hr(),
            dataset_information,
            ui.tags.hr(),
            missing_note,
            class_="main-sidebar card-style",
        ),
        ui.tags.div(
            output_widget("map", width="auto", height="auto"),
            class_="main-main card-style no-padding",
        ),
        class_="main-layout",
    )
