import flet as ft

def main(page: ft.Page):
    page.title = "Seus Hábitos"
    page.padding = ft.padding.all(20)
    page.bgcolor = ft.colors.BLUE_GREY_900

    habits_list = [
        {'title': 'Estudar Inglês', 'done': False},
        {'title': 'Estudar Violão', 'done': False},
        {'title': 'Academia', 'done': False}
    ]

    def change(e):
        for hl in habits_list:
            if hl['title'] == e.control.label:
                hl['done'] = e.control.value
            
        done = list(filter(lambda x: x['done'], habits_list))
        total = len(done) / len(habits_list)

        progess_bar.value = f'{total:.2f}'
        progress_text.value = f'{total:.0%}'
        progess_bar.update()
        progress_text.update()

    def add_habit(e):
        texto = e.control.value
        habits_list.append({"title": texto, "done": False})
        habits.content.controls = [ft.Checkbox(
                            label=hl["title"],
                            label_style = ft.TextStyle(
                                color=ft.colors.BLACK
                            ),
                            value=hl["done"],
                            on_change=change,
                        ) for hl in habits_list
                    ] 
        habits.update()
        texto = ""
        e.control.update()



    layout = ft.Column(
        expand=True,
        controls=[
            ft.Text(value="Que bom tê-lo aqui!", size=30, color=ft.colors.WHITE),
            ft.Text(value="Como estão seus hábitos hoje?", size=20, color=ft.colors.GREY),
            ft.Container(
                padding=ft.padding.all(30),
                bgcolor=ft.colors.INDIGO,
                border_radius=ft.border_radius.all(20),
                margin=ft.margin.symmetric(vertical=30),
                content=ft.Column(
                    controls=[
                        ft.Text(value="Sua evolução hoje", size=20, color=ft.colors.WHITE),
                        progress_text := ft.Text(value="0%", size=50, color=ft.colors.WHITE),
                        progess_bar := ft.ProgressBar(
                            value=0.5,
                            color=ft.colors.BLUE_GREY_500,
                            bgcolor=ft.colors.INDIGO_900,
                            height=20,
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ),
            ft.Text(value="Hábitos de Hoje", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text(value="Marcar suas tarefas como conluídas te motiva a continuar!", size=16, color=ft.colors.WHITE),
            habits := ft.Container(
                bgcolor = ft.colors.BLUE_GREY_500,
                padding=ft.padding.all(30),
                expand=True,
                border_radius=ft.border_radius.all(20),
                margin=ft.margin.symmetric(vertical=20),
                content=ft.Column(
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    spacing = 20,
                    controls=[
                        ft.Checkbox(
                            label=hl["title"],
                            label_style = ft.TextStyle(
                                color=ft.colors.BLACK
                            ),
                            on_change = change,
                            value=hl["done"],
                        ) for hl in habits_list
                    ] 
                )
                
            ),
            ft.Text(value="Adicionar novo hábito", size=20, color=ft.colors.WHITE),
            ft.TextField(
                hint_text="Tarefas",
                border=ft.InputBorder.UNDERLINE,
                border_color=ft.colors.BLUE_GREY_500,
                ### ENTER
                on_submit=add_habit
            )
        ]
    )

    page.add(layout)
if __name__ == "__main__":
    ft.app(target=main)