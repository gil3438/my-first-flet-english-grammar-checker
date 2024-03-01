import flet as ft
from standardEnglish import StandardEnglish


def main(page: ft.Page):
    page.title = "Correcteur Grammatical"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.horizontal_alignment = "center"
    page.theme_mode = "light"

    pr = ft.ProgressRing(width=16, height=16, stroke_width=2, opacity=0)

    logo = ft.Image(src=f"./images/logo.jpg", width=300)

    user_input = ft.TextField(hint_text="enter any sentence...", bgcolor='#52ACDD', border_radius=10)
    outputText = ft.Text("your response will be generated here...", bgcolor='#FCDC12')
    userText = ft.Text()

    def print_result(e):
        answer = []
        pr.opacity = 1
        userText.value = user_input.value
        user_input.value = ""
        outputText.value = "your response will be generated here..."
        userContainer.border = ft.border.all(1, ft.colors.BLACK)
        page.update()
        answer = StandardEnglish(str(userText.value)).convertStandardEnglish()

        outputText.value = answer
        pr.opacity = 0
        print("=>", answer)
        page.update()

    outputContainer = ft.Container(
        content=outputText,
        alignment=ft.alignment.top_left,
        # margin=10,
        padding=20,
        bgcolor="#FCDC12",
        border=ft.border.all(1, ft.colors.BLACK),
        border_radius=10,
    )

    question_container = ft.Container(
        content=ft.Row([user_input, ft.ElevatedButton("Submit", on_click=print_result), pr],
                       alignment=ft.MainAxisAlignment.START),
        alignment=ft.alignment.bottom_center,  # Alignement vertical en bas
        padding=0,  # Espacement intérieur du container
        bgcolor=ft.colors.WHITE,  # Couleur de fond du container
    )

    userContainer = ft.Container(
        content=userText,
        # margin=10,
        alignment=ft.alignment.top_left,
        padding=20,
        bgcolor="#FFFFFF",
        border=ft.border.all(1, ft.colors.WHITE),
        border_radius=10,

    )

    page.add(
        ft.Container(
            content=ft.Row([logo], alignment="center"),
            padding=10
        ),
        ft.Container(
            content=userContainer,
            border_radius=20,
            padding=10,
        ),
        ft.Container(
            content=outputContainer,
            border_radius=20,
            padding=10,
            expand=True,
        ),
        ft.Container(
            question_container,
            padding=10
        )

    )


ft.app(target=main, assets_dir="assets")
