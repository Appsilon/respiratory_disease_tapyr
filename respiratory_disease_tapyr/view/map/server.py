from typing import cast

from ipyleaflet import LayerGroup, Map, basemaps
from ipywidgets import Layout
from pandas import DataFrame
from shiny import module, reactive
from shinywidgets import register_widget

from respiratory_disease_tapyr.helpers.map_utils import add_circles, add_polygons, filter_data
from respiratory_disease_tapyr.logic.data_loading import map_data_oecd, map_data_world_bank, polygon_data

basemap = cast(dict, basemaps)


@module.server
def map_server(input, output, session, is_wb_data):
    # Initialize and display when the session starts (1)
    map = Map(
        basemap=basemap["CartoDB"]["Positron"],
        center=(50, 10),
        zoom=5,
        scroll_wheel_zoom=True,
        min_zoom=3,
        max_zoom=18,
        no_wrap=True,
        layout=Layout(width="100%", height="100%"),
    )
    map.panes = {"circles": {"zIndex": 650}, "choropleth": {"zIndex": 750}}
    register_widget("map", map)

    # Circles Layer will later be filled with circleMarkers
    circle_markers_layer = LayerGroup()
    circle_markers_layer.pane = "circles"
    map.add_layer(circle_markers_layer)

    # Polygon layer will later be filled reactively
    choropleth_layer = LayerGroup()
    choropleth_layer.pane = "choropleth"
    map.add_layer(choropleth_layer)

    @reactive.Calc
    def point_data() -> DataFrame:
        if is_wb_data():
            return filter_data(map_data_world_bank, input.years_value())
        return filter_data(map_data_oecd, input.years_value())

    @reactive.Effect
    def _() -> None:
        add_circles(point_data(), circle_markers_layer)

    @reactive.Effect()
    def _() -> None:
        add_polygons(polygon_data, point_data(), choropleth_layer)
