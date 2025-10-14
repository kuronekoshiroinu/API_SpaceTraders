from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button, Static
from textual.containers import HorizontalGroup
from typing import cast

from src.cli_textual.presentation.presenters.contracts import ContractsPresenter
from src.cli_textual.presentation.presenters.ship_purchase import ShipPurchasePresenter
from src.traders.domain.entities.ship_purchase import ShipPurchase
from src.traders.infraestructure.services.space_traders_service import SpaceTradersService


class SpaceActions(HorizontalGroup):
    def compose(self) -> ComposeResult:
        yield Button("Show Contract", id="sc")
        yield Button("Accept contract", id="ac")
        yield Button("View Available ships", id="vs")
        yield Button("Buy ship", id="bs")
        yield Button("Orbit Ship", id="os")
        yield Button("Navigate Ship", id="ns")
        yield Button("Extract Mineral", id="em")
        yield Button("Jettison Mineral", id="jm")
        yield Button("View Cargo", id="vc")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        output_widget = cast(Static, self.app.query_one("#output-text"))
        space = SpaceTradersService()
        match button_id:
            case "sc":
                contracts = space.get_contracts()
                if not contracts:
                    output_widget.update(f"no hay contratos: {button_id}")
                else:
                    presenter = ContractsPresenter(contracts)
                    output_widget.update(presenter.to_str)

            case "ac":
                output_widget.update(f"boton accept contract: {button_id}")
            case "bs":
                contracts = space.get_contracts()
                shipyards_infos = space.find_shipyards(system_symbol=contracts[0].terms.deliver[0].system_symbol)
                available_ships_info = space.view_ship_available(
                    system_symbol=contracts[0].terms.deliver[0].system_symbol,
                    waypoint_symbol=shipyards_infos[2].symbol)
                ship_purchaser = space.purchase_ship(ship_type="SHIP_MINING_DRONE",
                                                     waypoint_symbol=available_ships_info.symbol)
                #TODO formulario de 3 campos + boton de envio , el boton crea un panel

                presenter=ShipPurchasePresenter(ship_purchaser)
                output_widget.update(presenter.to_str)
            case _:
                output_widget.update(f"Último botón defecto: {button_id}")


class MainApp(App):

    # BINDINGS =
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield SpaceActions()
        yield Static(content="mostrando id", id="output-text")


if __name__ == "__main__":
    app = MainApp()
    app.run()
