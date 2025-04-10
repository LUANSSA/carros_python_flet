import flet as ft
from dao.database import cars

def main(page: ft.Page):
    # Título da página
    page.title="Carros"
    # Largura inicial da página
    page.window.width=400
    # Altura inicial da página
    page.window.height=800
    

    # Função checked
    def chek_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    # Função para mostrar descrição do carro
    def show_car_description(e):
        # Obtem o primeiro item que satisfaz a condição ou None. Busca ID de carro
        car = next((car for car in cars if car["id"] == e.control.parent.key), None)

        dlg = ft.AlertDialog(
            title=ft.Text(car["descricao"]),
            actions=[
                ft.TextButton("Fechar", on_click=lambda e: page.close(dlg))
            ]
        )
        page.open(dlg)


    # Menu de navegação
    app_bar = ft.AppBar(
        # Icone
        leading=ft.Icon(ft.icons.DIRECTIONS_CAR_FILLED),
        leading_width=40,
        # Título
        title=ft.Text("Carros"),
        center_title=True,
        # Beckground color
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            # Botão de navegação
            ft.IconButton(
                icon=ft.icons.NOTIFICATIONS
            ),
            # Pop Menu
            ft.PopupMenuButton(
                icon=ft.icons.MENU,
                # Lista de itens do menu
                items=[
                    # Perfil
                    ft.PopupMenuItem(
                        icon=ft.icons.PERSON,
                        text="Perfil",
                    ),
                    #Cadastrar
                    ft.PopupMenuItem(
                        icon=ft.icons.ADD_CARD,
                        text="Cadastrar"
                    ),
                    # Configurações
                    ft.PopupMenuItem(
                        icon=ft.icons.SETTINGS,
                        text="Configuração",
                    ),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(
                        text="Mostrar todos",
                        checked=False,
                        on_click=chek_item_clicked,
                    )
                ]
            )
        ]
    )

    # Lista de carros
    car_list = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        expand=True
    )

    for car in cars:
        car_component = ft.ListTile(
            leading=ft.Image(
                src=car["foto"],
                height=100,
                width=100,
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=5,
            ),
            title=ft.Text(f'{car['modelo']} - {car["marca"]} ({car["ano"]})'),
            subtitle=ft.Text(f'{car['tipo']}'),
            trailing=ft.PopupMenuButton(
                key=car["id"],
                icon=ft.icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(
                        icon=ft.icons.REMOVE_RED_EYE_SHARP,
                        text="Ver descrição",
                        on_click=show_car_description,
                    ),
                    ft.PopupMenuItem(
                        icon=ft.icons.DELETE,
                        text="Deletar",
                        # on_click=delete_car
                    )
                ]

            )
        )
        car_list.controls.append(ft.Row(
            controls=[
                car_component,
            ],
            wrap=True

        ))

    # Navegação do rodapé
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.DIRECTIONS_CAR_FILLED_OUTLINED,
                label="Antigos"
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.CAR_RENTAL,
                label="Novos"
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.ELECTRIC_CAR,
                label="Elétricos"
            )
        ]
    )

    page.add(
        app_bar,
        car_list,
        nav_bar
    ) 



ft.app(main)
