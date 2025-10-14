from typing import cast

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Header, Footer, Input, Log, Static

from src.cli_textual.domain.entities.trader_config import TraderConfig
from src.cli_textual.presentation.presenters.contracts import ContractsPresenter
from src.cli_textual.presentation.presenters.ship_purchase import ShipPurchasePresenter
from src.traders.infraestructure.services.space_traders_service import SpaceTradersService


class HomeScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Button("Ir a Botones", id="go_buttons"),
            Button("Ir a Entrada/Salida", id="go_io"),
            id="home_buttons"
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "go_buttons":
            self.app.push_screen("buttons")
        elif event.button.id == "go_io":
            self.app.push_screen("io")


from textual.containers import Container, Horizontal
from textual.widgets import Button, Footer, Header, Log, Static
from textual.screen import Screen
from textual.app import ComposeResult
from typing import cast

class ButtonScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()

        # Botones divididos en filas de 4 usando Horizontal
        yield Container(
            Horizontal(
                Button("Show Contract", id="sc"),
                Button("Accept contract", id="ac"),
                Button("View Available ships", id="vs"),
                Button("Buy ship", id="bs"),
            ),
            Horizontal(
                Button("Orbit Ship", id="os"),
                Button("Navigate Ship", id="ns"),
                Button("Extract Mineral", id="em"),
                Button("Jettison Mineral", id="jm"),
            ),
            Horizontal(
                Button("View Cargo", id="vc"),
            ),
            Log(id="output-text", highlight=True),
            Button("Volver al inicio", id="go_home"),
            id="button_screen"
        )

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "go_home":
            self.app.pop_screen()
        else:
            button_id = event.button.id
            output_widget = self.query_one("#output-text", Log)
            output_widget.clear()
            space = SpaceTradersService()
            match button_id:
                case "sc":
                    contracts = space.get_contracts()
                    if not contracts:
                        output_widget.write(f"No hay contratos: {button_id}")
                    else:
                        presenter = ContractsPresenter(contracts)
                        output_widget.write(presenter.to_str)

                case "ac":
                    output_widget.write(f"Botón accept contract: {button_id}")

                case "bs":
                    contracts = space.get_contracts()
                    shipyards_infos = space.find_shipyards(system_symbol=contracts[0].terms.deliver[0].system_symbol)
                    available_ships_info = space.view_ship_available(
                        system_symbol=contracts[0].terms.deliver[0].system_symbol,
                        waypoint_symbol=shipyards_infos[2].symbol)
                    ship_purchaser = space.purchase_ship(ship_type="SHIP_MINING_DRONE",
                                                         waypoint_symbol=available_ships_info.symbol)

                    presenter = ShipPurchasePresenter(ship_purchaser)
                    output_widget.write(presenter.to_str)

                case "jm":
                    output_widget.write("test")

                case _:
                    output_widget.write(f"Último botón defecto: {button_id}")



class IOScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            VerticalScroll(
                Static("Entradas:", id="input_title"),
                Input(placeholder="contract_system_symbol", id="input_contract"),
                Input(placeholder="shipyard_waypoint_symbol", id="input_waypoint"),
                Input(placeholder="shipyard_available_system_symbol", id="input_available"),
                Button("Enviar", id="send_btn"),
                id="left_pane"
            ),
            Log(id="right_pane", highlight=True),
            id="io_container"
        )
        yield Button("Volver al inicio", id="go_home_bottom")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "send_btn":
            input_contract = self.query_one("#input_contract", Input).value
            input_waypoint = self.query_one("#input_waypoint", Input).value
            input_available = self.query_one("#input_available", Input).value
            config = TraderConfig(
                contract_system_symbol=input_contract,
                shipyard_waypoint_symbol=input_waypoint,
                shipyard_available_system_symbol=input_available
            )
            text_log = self.query_one("#right_pane", Log)
            text_log.write("Diccionario generado:")
            text_log.write(config.to_str)
            # self.query_one("#input_contract", Input).value = ""
            # self.query_one("#input_waypoint", Input).value = ""
            # self.query_one("#input_available", Input).value = ""
        elif event.button.id == "go_home_bottom":
            self.app.pop_screen()


class MyApp(App):
    CSS_PATH = "styles.css"
    TITLE = "Mi CLI con Textual"

    # ✅ Usamos clases, no instancias
    SCREENS = {
        "home": HomeScreen,
        "buttons": ButtonScreen,
        "io": IOScreen,
    }

    def on_mount(self) -> None:
        self.push_screen("home")  # ✅ Empujamos por nombre, no instancia


if __name__ == "__main__":
    app = MyApp()
    app.run()
