import dash_bootstrap_components as dbc
def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/index")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("DeFi", href="https://defipulse.com/"),
                    dbc.DropdownMenuItem("Top liquidity pools", href="https://pools.fyi/#/"),
                    dbc.DropdownMenuItem("stablecoin marketcap", href="http://stablecoinwatch.com/"),
                    dbc.DropdownMenuItem("fiat marketcap", href="https://fiatmarketcap.com/")
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