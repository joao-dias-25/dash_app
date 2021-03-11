import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.Button("Sidebar", outline=True, color="secondary", className="mr-1", id="btn_sidebar"),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("USD tokens on Ethereum", href="https://duneanalytics.com/johnz/first"),
                    dbc.DropdownMenuItem("Gold tokens on Ethereum", href="https://duneanalytics.com/johnz/assets-on-ethereum"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("DeFi", href="https://defipulse.com/"),
                    dbc.DropdownMenuItem("Top liquidity pools", href="https://pools.fyi/#/")
                ],
                nav=True,
                in_navbar=True,
                label="pages",
            ),
            dbc.NavItem(dbc.NavLink("Home", href="/index")),
        ],
        brand="Dashboard on crypto currencies",
        color="#E5EEFD",
        #dark=True,
        sticky="top",
        fluid=True,

    )
    return navbar