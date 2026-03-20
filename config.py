TOKEN = 'insert your token'

# button's text
button_text = {
    'main_menu': "🏘️Главное меню",
    'help': "Помощь",
    'info': 'О нас...'
}
main_menu = button_text['main_menu']
help = button_text['help']
info = button_text['info']



# prices in Russian Rubles
price_test = 20
price_mouth = 150
price_three_mouth = 400
price_half_year = 600
price_permanently = 2000

# welcome text (/start command reply)
def welcome_text(user_name = 'unknown'):
    return (
        f'Привет, {user_name}!\n\n'
        f'Цены на vpn:\n'
        f'Проба: ₽{price_test}\n'
        f'Месяц: ₽{price_mouth}\n'
        f'Три месяца ₽{price_three_mouth}\n'
        f'Полгода: ₽{price_half_year}'
    )

info_text = (
    "<u>...Наша Команда</u> — <i>ООО <b>УЁБКИ</b></i>\n" +
    "<i>Наша задача = </i> <u>Продавать </u> <b>V - P - N</b>......\n" +
    "и получать за <b><i>ЭТО</i></b> БАБКИ"
)
