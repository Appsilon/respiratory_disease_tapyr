from shiny import module, ui
from shinywidgets import (
    output_widget,
)

from respiratory_disease_tapyr.helpers.helper_text import (
    about_text,
    dataset_information,
    missing_note,
    slider_text_plot,
)
from respiratory_disease_tapyr.logic.data_loading import plot_data_oecd

country_choices = plot_data_oecd["Entity"].unique().tolist() + ["World"]


@module.ui
def plot_ui():
    return ui.tags.div(
        ui.tags.div(
            about_text,
            ui.tags.hr(),
            slider_text_plot,
            ui.tags.br(),
            ui.input_slider(
                id="years_value",
                label="Select Year",
                min=1990,
                max=2017,
                value=[2010, 2015],
                sep="",
            ),
            ui.input_selectize(
                id="country_select",
                label="Select Countries:",
                choices=country_choices,
                selected="World",
                multiple=True,
            ),
            ui.tags.hr(),
            dataset_information,
            ui.tags.hr(),
            missing_note,
            class_="main-sidebar card-style",
        ),
        ui.tags.div(
            output_widget("dr_plot"),
            ui.tags.hr(),
            output_widget("pm_plot"),
            class_="main-main card-style",
        ),
        class_="main-layout",
    )
