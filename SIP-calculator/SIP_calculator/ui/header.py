# header.py
import reflex as rx
from datetime import datetime, timezone

class State(rx.State):
    date_now: datetime = datetime.now(timezone.utc)

def header():
    return rx.box(
        rx.hstack(
            rx.heading("SIP Calculator", size="8"),
            rx.spacer(),
            rx.text("Made by",size="1", color="tomato",weight="light"),
            rx.text(" Shubham Rajput",size="6", color="tomato",weight="medium"),
            rx.link(rx.button("in",size="8"), href="https://www.linkedin.com/in/shubhsmiles/"),
            rx.color_mode.button(position="left"),
            rx.vstack(
                rx.moment(State.date_now, format="YYYY-MM-DD"),
                rx.moment(interval=1000, format="HH:mm:ss"),
            ),
            spacing="2",
            justify="space-between",
            align="center",
        ),
        background_color="var(--plum-3)",
        border_radius="10px",
        width="100%",  # Adjusted width of the form to better fit in the view
        spacing="2",
        justify="between",
        align="stretch",        
        margin="1px auto",  # Centering horizontally
        padding="8px",
    )
