import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.Button("Sidebar", outline=True, color="secondary", className="mr-1", id="btn_sidebar"),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("DeFi", href="https://defipulse.com/"),
                    dbc.DropdownMenuItem("Top liquidity pools", href="https://pools.fyi/#/"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("stablecoin marketcap", href="http://stablecoinwatch.com/"),
                    dbc.DropdownMenuItem("fiat marketcap", href="https://fiatmarketcap.com/")
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