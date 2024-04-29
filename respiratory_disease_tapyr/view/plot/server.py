from shiny import module, reactive
from shinywidgets import (
    render_widget,
)

from respiratory_disease_tapyr.helpers.plot_utils import create_figure
from respiratory_disease_tapyr.logic.data_loading import plot_data_oecd, plot_data_world_bank

country_choices = [*plot_data_oecd["Entity"].unique().tolist(), "World"]


@module.server
def plot_server(input, output, session, is_wb_data):
    @reactive.Calc
    def data():
        if is_wb_data():
            return plot_data_world_bank
        return plot_data_oecd

    @reactive.Calc
    def fig_one():
        return create_figure(
            data=data(),
            year_range=input.years_value(),
            country=input.country_select(),
            y_from="Death.Rate",
            title="Death Rate From Respiratory Diseases",
            labels={
                "Year": "Year",
                "Death.Rate": "Deaths per 100,000",
            },
        )

    @reactive.Calc
    def fig_two():
        return create_figure(
            data=data(),
            year_range=input.years_value(),
            country=input.country_select(),
            y_from="PM2.5",
            title="PM2.5 Measure",
            labels={
                "Year": "Year",
                "PM2.5": "PM2.5",
            },
        )

    @output(suspend_when_hidden=False)
    @render_widget
    def dr_plot():
        return fig_one()

    @output(suspend_when_hidden=False)
    @render_widget
    def pm_plot():
        return fig_two()
