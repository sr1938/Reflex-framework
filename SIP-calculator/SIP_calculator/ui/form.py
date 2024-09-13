import reflex as rx
from ..calc import calculate  # Import the calculate function from the calculator module

class State(rx.State):
    form_data: dict = {}
    future_value: str = ""  # For storing formatted future value
    invested: str = ""      # For storing invested amount
    returns: str = ""       # For storing returns over the period
    datapie01: list = []  # Explicitly annotate the data type
    dataarea01: list = []  # Explicitly annotate the data type

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        self.future_value, self.invested, self.returns, self.dataarea01, self.datapie01 = calculate(form_data)
        print("Data for Area Chart:", self.dataarea01)  # Debug: Print area chart data
        print("Data for Pie Chart:", self.datapie01)    # Debug: Print pie chart data

    @staticmethod
    def pie_simple(datapie01):
        return rx.recharts.pie_chart(
            rx.recharts.pie(
                data=datapie01, 
                data_key="value",
                name_key="name",
                stroke = rx.color("blue"),
                fill = rx.color("crimson"),
                inner_radius="60%",
                label = True,
            ),
            rx.recharts.pie(
                data=datapie01, 
                data_key="percent",
                name_key="name",
                stroke = rx.color("blue"),
                fill = rx.color("indigo"),
                outer_radius="50%",  # Adjust the radius as needed
                label = True,
            ),
            rx.recharts.graphing_tooltip(),
            width="100%",
            height=300,
        )
    
    @staticmethod
    def area_stack(dataarea01):
        return rx.recharts.composed_chart(
            rx.recharts.line(
                data_key="future value",
                stroke="#8884d8",
                fill="#8884d8",
                stack_id="1",
            ),
            rx.recharts.line(
                data_key="investment",
                stroke="#ff7300",
                fill="#ff7300",
                stack_id="1",
            ),
            rx.recharts.x_axis(data_key="year"),
            rx.recharts.y_axis(),
            rx.recharts.legend(),
            rx.recharts.graphing_tooltip(),
            data=dataarea01,
            stack_offset="none",
            margin={
                "top": 20,
                "right": 30,
                "bottom": 5,
                "left": 30,
            },
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
                        justify="space",
                        width="100%",
                    ),
                    rx.section(
                        rx.hstack(
                            rx.text("Time period (Years): "),
                            rx.spacer(),
                            rx.input(placeholder="Insert Duration in Years", name="tenure", max_length=70),
                        ),
                        justify="space",
                        width="100%",
                    ),
                    rx.section(
                        rx.hstack(
                            rx.text("Annual Growth Rate (%): "),
                            rx.spacer(),
                            rx.input(placeholder="Insert ROI p.a.", name="AGR", max_length=100),
                        ),
                        justify="space",
                        width="100%",
                    ),
                    rx.button("Calculate", type="submit", color_scheme="ruby"),
                    spacing="10",
                    justify="space-evenly",
                    width="100%",
                ),
                background_color="var(--tomato-3)",
                border_radius="10px",
                width="100%",  # Adjusted width to fit well with pie chart
                margin="1px",
                padding="8px",
                align= "flex-start",
            ),
            # Pie Chart Box
            rx.box(
                State.pie_simple(State.datapie01),
                background_color="var(--plum-3)",
                border_radius="10px",
                width="100%",  # Adjust width to fit well with form
                margin="1px",
                padding="8px",
            ),
            # Area Chart Box
            rx.box(
                State.area_stack(State.dataarea01),
                background_color="var(--plum-3)",
                border_radius="10px",
                width="100%",  # Adjust width to fit well with form
                margin="1px",
                padding="8px",
            ),
            bg=rx.color("accent", 6),
            spacing="2",
            padding="8px",
            border_radius="10px",
            flex_direction=["column","column","row"],
            height="auto",  # Adjusted to auto to fit the content
            width="100%",
        ),
        on_submit=State.handle_submit,
        reset_on_submit=True,
        width="100%",  # Adjusted width of the form to better fit in the view
        spacing="2",
        justify="space-evenly",
        align="stretch",
        )