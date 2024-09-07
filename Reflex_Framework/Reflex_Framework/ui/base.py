import reflex as rx
from .nav import navbar


def base_page(child: rx.Component, hide_navbar=False,*args) -> rx.Component:
    # print([type(x) for x in args])
    if not isinstance(child, rx.Component):
        child = rx.heading("This is not a valid child element")
    if hide_navbar:
        return rx.container(
            child,
            rx.logo(),
            rx.color_mode.button(position="bottom-right"),
    )
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            # bg=rx.color("accent", 3),
            padding="1em",
            width="100%",
        ),

        rx.logo(),
        rx.color_mode.button(position="bottom-right"),
    )
