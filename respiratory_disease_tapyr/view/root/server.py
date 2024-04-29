from shiny import Inputs, Outputs, Session, reactive

from respiratory_disease_tapyr.helpers.helper_text import info_modal
from respiratory_disease_tapyr.view import map, plot


def server(input: Inputs, output: Outputs, session: Session):
    info_modal()

    @reactive.Effect
    @reactive.event(input.info_icon)
    def _():
        info_modal()

    @reactive.Calc
    def is_wb_data():
        return input.dataset()

    map.map_server("map", is_wb_data)
    plot.plot_server("plot", is_wb_data)

    @reactive.Effect
    @reactive.event(input.tab_map)
    async def _():
        await session.send_custom_message("toggleActiveTab", {"requestedTab": "map"})

    @reactive.Effect
    @reactive.event(input.tab_plot)
    async def _():
        await session.send_custom_message("toggleActiveTab", {"requestedTab": "plot"})
