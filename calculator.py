from textual.app import App
from textual.widgets import Placeholder, ScrollView, Dock, DockEdge, Button, ButtonLayout
from textual.reactive import Reactive

class Calculator(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.display = Placeholder()
        self.result = Reactive(0)

    async def on_mount(self, event):
        await self.view.dock(Dock(self.display, edge=DockEdge.TOP, size=3))
        buttons = ScrollView()
        await self.view.dock(buttons, edge=DockEdge.BOTTOM, size=9)
        layout = ButtonLayout()
        buttons.add(layout)

        for text in [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
        ]:
            if text == '=':
                button = Button(text, name=text, disabled=True)
            else:
                button = Button(text, name=text)
            layout.add(button)

    async def on_click(self, event):
        button = self.sender
        if button.name == '=':
            self.result = eval(self.display.content)
            self.display.update(str(self.result))
        else:
            self.display.update(self.display.content + button.name)

    async def on_startup(self, event):
        await self.bind('click', self.on_click, Button)

    async def on_shutdown(self, event):
        pass
