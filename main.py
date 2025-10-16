from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Log

from src.cli_textual.domain.widgets.custom_form import CustomFormWidget
from src.cli_textual.presentation.presenters.contracts import ContractsPresenter
from src.cli_textual.presentation.presenters.ship_purchase import ShipPurchasePresenter
from src.traders.application.use_cases.contract_accepter import ContractAccepter
from src.traders.domain.interfaces import TradersService
from src.traders.infraestructure.services.space_traders_service import SpaceTradersService


class SpaceActions(Screen):
    def __init__(
            self,
            traders_service: TradersService,
            name: str | None = None,
            id: str | None = None,
            classes: str | None = None,
    ) -> None:
        self.traders_service = traders_service
        super().__init__(name=name, id=id, classes=classes)

    def compose(self) -> ComposeResult:
        action_pending: str | None = None
        yield Header()
        yield Container(
            Vertical(
                # Parte superior: botones de acciones
                Horizontal(
                    Button("Show Contract", id="sc", classes="button"),
                    Button("Accept contract", id="ac", classes="button"),
                    Button("View Available ships", id="vs", classes="button"),
                    Button("Buy ship", id="bs", classes="button"),
                    Button("Orbit Ship", id="os", classes="button"),
                    Button("Navigate Ship", id="ns"),
                    Button("Extract Mineral", id="em"),
                    Button("Jettison Mineral", id="jm"),
                    # classes="top-buttons",
                ),
                Horizontal(
                    Button("View Cargo", id="vc"),
                    # classes="top-buttons",
                ),
                CustomFormWidget(id="custom_form_widget"),

                # Área de salida
                Log(id="output-text", highlight=True,
                    # classes="log-area"
                    ),
                # Footer con botón Exit
                Horizontal(
                    Button("Exit App", id="exit_app", variant="error", classes="exit-button"),
                    classes="footer-bar"
                ),
            ),
            id="main-container"
        )

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        output_widget = self.query_one("#output-text", Log)
        output_widget.clear()

        if button_id == "exit_app":
            self.app.exit()
            return

        match button_id:
            case "sc":
                contracts = self.traders_service.get_contracts()
                if not contracts:
                    output_widget.write("No hay contratos disponibles.")
                else:
                    presenter = ContractsPresenter(contracts)
                    output_widget.write(presenter.to_str)

            case "ac":
                contracts = self.traders_service.get_contracts()
                id_contracts = contracts[0].id
                if contracts[0].accepted == False:
                    accept = ContractAccepter(contract_id=id_contracts).execute()
                    output_widget.write("Aceptado")
                else:
                    output_widget.write("Ya fue aceptado")

            case "bs":
                contracts = self.traders_service.get_contracts()
                shipyards_infos = self.traders_service.find_shipyards(
                    system_symbol=contracts[0].terms.deliver[0].system_symbol)
                available_ships_info = self.traders_service.view_ship_available(
                    system_symbol=contracts[0].terms.deliver[0].system_symbol,
                    waypoint_symbol=shipyards_infos[2].symbol)
                ship_purchaser = self.traders_service.purchase_ship(
                    ship_type="SHIP_MINING_DRONE",
                    waypoint_symbol=available_ships_info.symbol)

                presenter = ShipPurchasePresenter(ship_purchaser)
                output_widget.write(presenter.to_str)
            case "os":
                custom_form_widget: CustomFormWidget = self.query_one("#custom_form_widget")
                if custom_form_widget.input1.display:
                    custom_form_widget.change_display_status(False, False, False)
                    self.action_pending = None
                    output_widget.write("Cancelado Orbit Ship.")
                else:
                    custom_form_widget.change_display_status(True, False, True)
                    self.action_pending = "orbit_ship"
                    output_widget.write("Ingresa el símbolo del barco para orbitar:")
            case "jm":
                output_widget.write("Test - Jettison Mineral")

            case "submit_input":
                input1 = self.query_one("#input1")
                input2 = self.query_one("#input2")
                submit_button = self.query_one("#submit_input")

                value = input1.value  # El valor ingresado

                if self.action_pending == "orbit_ship":
                    # Aquí haces la lógica para orbitar
                    result = self.traders_service.orbit_ship(ship_symbol=value)
                    output_widget.write(f"Orbitando nave {value}: {result}")

                else:
                    output_widget.write("Acción desconocida o no establecida.")

                # Oculta los inputs y limpia acción pendiente
                input1.display = False
                input2.display = False
                submit_button.display = False
                self.action_pending = None

            case _:
                output_widget.write(f"Último botón por defecto: {button_id}")


class MainApp(App):
    CSS_PATH = "styles.tcss"

    def on_mount(self) -> None:
        self.push_screen(SpaceActions(traders_service=SpaceTradersService()))


if __name__ == "__main__":
    app = MainApp()
    app.run()
