from textual.containers import Horizontal
from textual.widget import Widget
from textual.widgets import Button, Input


class CustomFormWidget(Horizontal):
    def __init__(
            self,
            *children: Widget,
            name: str | None = None,
            id: str | None = None,
            classes: str | None = None,
            disabled: bool = False,
            markup: bool = True,
    ) -> None:
        self.input1 = Input(placeholder="Input 1", id="input1")
        self.input2 = Input(placeholder="Input 2", id="input2")
        self.submit_button = Button("Enviar", id="submit_input", classes="button")
        self.change_display_status(False, False, False)
        super().__init__(
            self.input1,
            self.input2,
            self.submit_button,
            *children,
            name=name,
            id=id,
            classes=classes,
            disabled=disabled,
            markup=markup
        )

    def change_display_status(self, show_input1: bool, show_input2: bool, show_button: bool):
        self.input1.display = show_input1
        self.input2.display = show_input2
        self.submit_button.display = show_button
