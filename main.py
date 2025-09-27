from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button, Static
from textual.containers import HorizontalGroup
from typing import cast

from src.cli_textual.presentation.presenters.contracts import ContractsPresenter
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
        # Actualizar el widget Static con el ID del botón
        output_widget = cast(Static, self.app.query_one("#output-text"))
        space = SpaceTradersService()
        match button_id:
            case "sc":
                contracts = space.get_contracts()
                if not contracts:
                    output_widget.update(f"no hay contratos: {button_id}")
                else:
                    presenter=ContractsPresenter(contracts)
                    output_widget.update(presenter.to_str)

            case "ac":
                output_widget.update(f"boton accept contract: {button_id}")
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
