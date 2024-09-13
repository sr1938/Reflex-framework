# SIP-Calculator.py
import reflex as rx
from .ui.header import header  # Import the header component
from .ui.form import form_section, State  # Import the form section and State

def index():
    return rx.vstack(
        header(),  # Use the header component
        form_section(),  # Use the form section component
        # Results Section
        rx.box(
            rx.heading("Results", size="8.5"),
            rx.vstack(
                rx.text(f"Future Value: Rs {State.future_value}"),
                rx.text(f"Invested Amount: Rs {State.invested}"),
                rx.text(f"Returns: Rs {State.returns}"),
                spacing="5",
                padding="1px",
                width="100%",
                align="center",
            ),
            border_radius="10px",
            border_width="medium",
            width="100%",
            margin="1px auto",  # Centering horizontally
            padding="8px",
            background_color="var(--plum-2)",
            justify="center auto",
            align="center",
        ),
        width="100%",
        spacing="5",
        justify="center",
        align="center",
        min_height="65vh",
        padding="8px",
    )

app = rx.App()
app.add_page(index)
