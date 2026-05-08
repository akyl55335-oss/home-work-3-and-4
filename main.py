import flet as ft 


def main_page(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    hello_text = ft.Text(value='Helo world')

    greeting_history = []
    history_text = ft.Text('История приветствий: ')


    def on_button_click(_):
        # print(name_input.value)
        # pass
        name = name_input.value.strip()
        

        if name:
            # print(name)
            # hello_text = 'sdfsdfsdf'
            hello_text.color = None
            hello_text.value = f'Hello {name}'
            name_input.value = None

            greeting_history.append(name)
            print(greeting_history)
            history_text.value = 'История приветствий: \n-' + '\n-'.join(greeting_history)
        else:
            # print('Error')
            hello_text.value = 'ОШИБКА Введите имя'
            hello_text.color = ft.Colors.RED

        page.update()


    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    # text_button = ft.TextButton(text='SEND', icon=ft.Icons.SEND)
    # icon_button = ft.IconButton(icon=ft.Icons.SEND)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update()

    clear_button = ft.IconButton(icon=ft.Icons.CLEAR, on_click=clear_history)


    page.add(hello_text, name_input, elevated_button, clear_button, history_text)


ft.app(main_page) 
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)

# GeeksSmm 


import flet as ft
from datetime import datetime


def main_page(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    hello_text = ft.Text(value='Hello world')

    history = []
    history_text = ft.Text()

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            hello_text.color = None
            hello_text.value = f'Hello {name}'

            current_time = datetime.now().strftime("%H:%M:%S")

            text = f"{current_time} - Привет, {name}!"

            history.append(text)

            history[:] = history[-5:]

            history_text.value = "\n".join(history)

            name_input.value = ""

        else:
            hello_text.value = 'ОШИБКА Введите имя'
            hello_text.color = ft.Colors.RED

        page.update()

    name_input = ft.TextField(
        label='Введите имя',
        on_submit=on_button_click
    )

    elevated_button = ft.ElevatedButton(
        'SEND',
        icon=ft.Icons.SEND,
        on_click=on_button_click
    )

    page.add(
        hello_text,
        name_input,
        elevated_button,
        ft.Text("История:"),
        history_text
    )


ft.app(main_page)