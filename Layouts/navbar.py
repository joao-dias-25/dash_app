import dash_bootstrap_components as dbc
def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/index")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Page 2(not available)", href="#"),
                    dbc.DropdownMenuItem("Page 3(not available)", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="pages",
            ),
        ],
        brand="A Dashboard on crypto currencies",
        color="black",
        dark=True,
    )
    return navbar