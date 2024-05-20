from django.core.management.base import BaseCommand
from django.conf import settings
from app.models import Users

from telebot import TeleBot

import logging
import telegram 

#  python-telegram-bot 13.15

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger()

bot = telegram.Bot(token=settings.TELEGRAM_API_TOKEN)
updater = Updater(settings.TELEGRAM_API_TOKEN)

# Определяем константы этапов сеанса
ROLE, PHOTO, SECRET, CONFIRM = range(4)

# функция обратного вызова точки входа в сеанс
def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['Тестировщик', 'Служба безопасности', 'Наблюдатель']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем сеанс с вопроса
    update.message.reply_text( 
        'Бот участников практических исследований в рамках ВКР "Разработка системы контроля доступа и уведомления персонала о попытках НСД к сетевым ресурсам предприятия"'
        '\nКоманда /cancel, чтобы прекратить сеанс'
        '\n\nВыберите свою роль в организации',
        reply_markup=markup_key,)
    # переходим к этапу `SET_GROUP`
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `ROLE`
    return ROLE


# Обрабатываем роль пользователя
def alert(update, _):
    
    user = update.message.from_user
    # Пишем в журнал
    logger.info("Зашел злоумышленник %s: %s, user.id: %d", user.first_name, update.message.text, user.id)
    all_users = Users.objects.filter(secure=True).all()
    for v in all_users:        
        bot.send_message(chat_id=v.tg_id, text='Произошел инцидент!')


# Обрабатываем роль пользователя
def role(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал
    logger.info("Зашел %s: %s, user.id: %d", user.first_name, update.message.text, user.id)    
    if update.message.text == 'Наблюдатель':
        update.message.reply_text('сеанс закончен, спасибо!')
        Users.objects.create(tg_fio = user.first_name, tg_id = user.id)
        return ConversationHandler.END
    if update.message.text == 'Служба безопасности':
        update.message.reply_text('введите пароль, в случае успеха придет SMS с кодом подтверждения')
        return SECRET
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    update.message.reply_text(
        'Пришлите фото для электронного пропуска  (/skip - пропустить)',
        reply_markup=ReplyKeyboardRemove(),
    )
    # переходим к этапу `PHOTO`
    return PHOTO

# Обрабатываем фотографию пользователя
def photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем фото 
    photo_file = update.message.photo[-1].get_file()
    # скачиваем фото 
    # photo_file.download(f'{user.id}_photo.jpg')
    # Пишем в журнал
    logger.info("Фотография %s: %s", user.first_name, f'{user.id}_photo.jpg')
    # Отвечаем
    update.message.reply_text('Пропуск будет отправлен личным сообщением\nсеанс закончен, спасибо!')
    return ConversationHandler.END
    # переходим к этапу `LOCATION`
    return SECRET

# Обрабатываем команду /skip для фото
def skip_photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о фото
    logger.info("Пользователь %s не отправил фото.", user.first_name)
    # Отвечаем на сообщение с пропущенной фотографией
    update.message.reply_text(
        'Фото можно будет добавить позже\nсеанс закончен, спасибо!'        
    )
    return ConversationHandler.END

# Обрабатываем секретный код пользователя
def secret(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем секретный код
    secret = update.message.text
    # Пишем в журнал
    logger.info(
        "Секретный код %s: %s", user.first_name, secret)
    # Отвечаем
    update.message.reply_text(
        'Введите код подтверждения'
    )
    # переходим к этапу `COMMENT`
    return CONFIRM

# Обрабатываем команду /skip
def skip_secret(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал
    logger.info("User %s did not send a location.", user.first_name)
    # Отвечаем
    update.message.reply_text(
        'Оставьте комментарий'
    )
    # переходим к этапу `COMMENT`
    return COMMENT

# Обрабатываем сообщение
def confirm(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал
    logger.info("Пользователь %s ввел SMS-код подтверждения: %s", user.first_name, update.message.text)
    Users.objects.create(tg_fio = user.first_name, tg_id = user.id, secure = True)
    # Отвечаем
    update.message.reply_text('Сеанс завершен, спасибо')
    # Заканчиваем сеанс.
    return ConversationHandler.END

# Обрабатываем команду /cancel если пользователь отменил сеанс
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не заполнил данные
    logger.info("Пользователь %s отменил сеанс.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Продолжим в другой раз',
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем сеанс.
    return ConversationHandler.END



# Название класса обязательно - "Command"
class Command(BaseCommand):
    
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик сеансов `ConversationHandler` 
    def handle(self, *args, **kwargs):
        print('Telegram bot завершил свою работу')

    

    conv_handler = ConversationHandler( # здесь строится логика сеанса
        # точка входа
        entry_points=[
            CommandHandler('start', start),
            CommandHandler('alert', alert)
        ],
        # этапы сеанса
        states={
            ROLE: [MessageHandler(Filters.regex('^(Тестировщик|Служба безопасности|Наблюдатель)$'), role)],
            PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            SECRET: [MessageHandler(Filters.text & ~Filters.command, secret)],
            CONFIRM: [MessageHandler(Filters.text & ~Filters.command, confirm)],            
        },
        # точка выхода из сеанса
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)
    # Запуск бота
    updater.start_polling()
    updater.idle()
    
	
