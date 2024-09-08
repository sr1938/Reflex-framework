import reflex as rx
from ..calculator import calculate  # Import the calculate function from the calculator module

class State(rx.State):
    form_data: dict = {}
    future_value: str = ""  # For storing formatted future value
    invested: str = ""      # For storing invested amount
    returns: str = ""       # For storing returns over the period
    data01: list = []

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.future_value, self.invested, self.returns, self.data01 = calculate(form_data)

    @staticmethod
    def pie_simple(data01):
        return rx.recharts.pie_chart(
            rx.recharts.pie(
                data=data01,
                data_key="value",
                name_key="name",
                label=True,
                fill=rx.color("indigo"), 
            ),
            rx.recharts.legend(),
            width="100%",
            height=300,
        )

def form_section():
    return rx.form(
        rx.flex(
            # Form Box
            rx.box(
                rx.vstack(
                    rx.section(
                        rx.hstack(
                            rx.text("SIP amount: "),
                            rx.spacer(),
                            rx.input(placeholder="Insert SIP Amount", name="sip_amount", max_length=70),
                        ),
                        justify="space-between",
                        width="100%",
                    ),
                    rx.section(
                        rx.hstack(
                            rx.text("Time period (Years): "),
                            rx.spacer(),
                            rx.input(placeholder="Insert time period in Years", name="tenure", max_length=70),
                        ),
                        justify="space-between",
                        width="100%",
                    ),
                    rx.section(
                        rx.hstack(
                            rx.text("Annual Growth Rate (%): "),
                            rx.spacer(),
                            rx.input(placeholder="Insert rate of interest p.a.", name="AGR", max_length=100),
                        ),
                        justify="space-between",
                        width="100%",
                    ),
                    rx.button("Calculate", type="submit", color_scheme="ruby"),
                    spacing="10",
                    justify="center",
                    width="100%",
                ),
                background_color="var(--tomato-3)",
                border_radius="10px",
                width="30%",  # Adjusted width to fit well with pie chart
                margin="16px",
                padding="16px",
            ),
            # Pie Chart Box
            rx.box(
                State.pie_simple(State.data01),
                background_color="var(--plum-3)",
                border_radius="10px",
                width="70%",  # Adjust width to fit well with form
                margin="16px",
                padding="16px",
            ),
            bg=rx.color("accent", 6),
            spacing="2",
            padding="1em",
            border_radius="10px",
            flex_direction=["row", "row"],
            height="500px",
            width="100%",
        ),
        on_submit=State.handle_submit,
        reset_on_submit=True,
        width="80%",  # Adjusted width of the form to better fit in the view
        spacing="2",
        justify="between",
        align="stretch",
    )
