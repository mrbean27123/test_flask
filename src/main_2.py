import flet as ft
import time
from datetime import datetime


class CurrentTime(ft.Text):
    def __init__(self, page: ft.Page, strf_time: str = "%H:%M:%S", time_sleep: int | float = 1, size: int | float = 20):
        super().__init__(size=size)
        self.strf_time = strf_time
        self.time_sleep = time_sleep
        self.page = page
        self.page.run_thread(self.update_time)

    def update_time(self):
        while True:
            now = datetime.now()
            self.value = now.strftime(self.strf_time)
            self.update()
            time.sleep(self.time_sleep)


def main(page: ft.Page):
    # Настройки
    scale = 1 # Размер текста
    page.title = "Steel app"
    page.padding = 0
    page.margin = 0
    page.window.min_width = 500 * scale
    page.window.min_height = 400 * scale
    page.window.width = 700 * scale
    page.window.height = 500 * scale
    page.window.center()

    # AppBar
    time_display = CurrentTime(page, size=20 * scale)
    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            icon=ft.Icons.TABLE_ROWS,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=0),
            ),
            on_click=lambda e: page.open(drawer)
        ),
        leading_width=70 * scale,
        toolbar_height=40 * scale,
        title=ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.PERSON),
                    ft.Text("Петро Петренко", weight=ft.FontWeight.BOLD, size=16 * scale),
                    ft.Icon(ft.Icons.WORK),
                    ft.Text("Сталевар", size=16 * scale),
                ]
            ),
            margin=ft.margin.symmetric(vertical=0, horizontal=0)
        ),
        center_title=False,
        bgcolor="#17212b",
        actions=[
            ft.Container(
                content=time_display,
                padding=ft.padding.only(
                    right=10
                ),
                margin=ft.margin.symmetric(vertical=0, horizontal=0)
            )
        ]
    )

    def handle_dismissal(e):
       print("Drawer dismissed")

    def handle_change(e):
        selected_index = int(e.data)
        print(f"Selected Index changed: {selected_index}")
        sidebar.selected_index = selected_index
        sidebar_click(e)
        page.close(drawer)
        page.update()

    page.theme = ft.Theme(
        navigation_drawer_theme=ft.NavigationDrawerTheme(
            label_text_style=ft.TextStyle(size=16 * scale),
        )
    )

    # Drawler
    drawer = ft.NavigationDrawer(
        bgcolor="#0e1621",
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        controls=[
            ft.Container(height=12 * scale),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.THERMOSTAT,
                label="Температура у пічі",
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.THERMOSTAT_AUTO,
                label="Температура у ківшу",
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.HEAT_PUMP,
                label="Температура ківша",
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.AIR_OUTLINED,
                label="Температура повітря",
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.ACCESS_TIME_OUTLINED,
                label="Час аргону",
            ),
        ],
    )

    # SideBar
    sidebar = ft.NavigationRail(
        label_type=ft.NavigationRailLabelType.NONE,
        bgcolor="#0e1621",
        selected_index=0,
        indicator_shape=ft.RoundedRectangleBorder(radius=0),
        min_width=70  * scale,
        width=70 * scale,
        group_alignment=-1,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.THERMOSTAT, size=24 * scale)
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.THERMOSTAT_AUTO, size=24 * scale)
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.HEAT_PUMP, size=24 * scale)
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.AIR, size=24 * scale)
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.ACCESS_TIME, size=24 * scale)
            ),
        ]
    )

    def sidebar_click(e: ft.ControlEvent) -> None:
        selected_index = int(e.data)
        print("Current page:", selected_index)
        if selected_index == 0:
            content.content = main_page
        elif selected_index == 1:
            content.content = input_data_page
        drawer.selected_index = selected_index
        content.update()

    sidebar.on_change = sidebar_click

    # Content
    main_page = ft.Column(
        controls=[
            ft.Text("Головна сторінка", size=20 * scale, weight=ft.FontWeight.BOLD),
            ft.Text("Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.", size=16 * scale, text_align=ft.TextAlign.JUSTIFY)
        ],
        expand=True,
    )

    input_data_page = ft.Column(
        controls=[
            ft.Text("Ввод показників", size=20 * scale, weight=ft.FontWeight.BOLD),
            ft.TextField(
                label="Температура у пічі",
                label_style=ft.TextStyle(size=16 * scale),
                text_size=16 * scale
            ),
            ft.TextField(
                label="Температура у ківшу",
                label_style=ft.TextStyle(size=16 * scale),
                text_size=16 * scale
            ),
            ft.TextField(
                label="Температура ківша",
                label_style=ft.TextStyle(size=16 * scale),
                text_size=16 * scale
            ),
            ft.TextField(
                label="Температура повітря",
                label_style = ft.TextStyle(size=16 * scale),
                text_size = 16 * scale
            ),
            ft.TextField(
                label="Час аргону",
                label_style=ft.TextStyle(size=16 * scale),
                text_size=16 * scale
            ),
            ft.ElevatedButton(
                text="Відправити",
                icon=ft.Icons.SEND,
                width=200 * scale,
                height=40 * scale,
                color=ft.Colors.WHITE,
                style=ft.ButtonStyle(
                    shadow_color=ft.Colors.TRANSPARENT,
                    bgcolor="#0e1621",
                ),
            )
        ],
        expand=True,
    )

    content = ft.Container(
        expand=True,
        padding=10 * scale,
        bgcolor="#202b36",
        content=main_page,
    )

    # Navbar + Content
    right_panel = ft.Column(
        controls=[
            content,
        ],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )

    # Page
    layout = ft.Row(
        controls=[
            #sidebar,
            right_panel,
        ],
        expand=True,
        spacing=0,
    )

    page.add(
        layout
    )


if __name__ == '__main__':
    ft.app(main)
