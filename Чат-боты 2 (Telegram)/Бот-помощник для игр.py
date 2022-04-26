from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardRemove
from telegram import ReplyKeyboardMarkup
import random

markup_start = ReplyKeyboardMarkup([['/dice', '/timer']], one_time_keyboard=False)
markup_dice = ReplyKeyboardMarkup([['кинуть один шестигранный кубик', 'кинуть 2 шестигранных кубика одновременн'],
                                   ['кинуть 20-гранный кубик', 'вернуться назад']], one_time_keyboard=False)
markup_timer = ReplyKeyboardMarkup([['30 секунд', '1 минута'],
                                    ['5 минут', 'вернуться назад']], one_time_keyboard=False)
key_message = 'предлагаю новую клавиатуру'


def remove_job_if_exists(name, context):
    """Удаляем задачу по имени.
    Возвращаем True если задача была успешно удалена."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


def alarm(context: CallbackContext):
    """Send the alarm message."""
    global text
    job = context.job
    context.bot.send_message(job.context, text=f'Время {text} истекло')


def echo(update, context):
    global text
    text = update.message.text
    print(update.message.text, context)
    if text == 'вернуться назад':
        start(update, context)
    elif text == 'кинуть один шестигранный кубик':
        update.message.reply_text(f'{random.randint(1, 6)}')
    elif text == 'кинуть 2 шестигранных кубика одновременн':
        update.message.reply_text(f'{random.randint(1, 6)} и {random.randint(1, 6)}')
    elif text == 'кинуть 20-гранный кубик':
        update.message.reply_text(f'{random.randint(1, 20)}')
    else:
        task = text
        if text == '30 секунд':
            due = 30
        if text == '1 минута':
            due = 60
        if text == '5 минут':
            due = 300
        update.message.reply_text(f'засёк {task}')
        chat_id = update.message.chat_id
        job_removed = remove_job_if_exists(
            str(chat_id),
            context
        )
        context.job_queue.run_once(alarm, due, context=chat_id, name=str(chat_id))


def start(update, context):
    update.message.reply_text(key_message,
                              reply_markup=markup_start
                              )


def dice(update, context):
    update.message.reply_text(key_message,
                              reply_markup=markup_dice
                              )


def timer(update, context):
    update.message.reply_text(key_message,
                              reply_markup=markup_timer
                              )


TOKEN = '5156486540:AAH7wejiXRCysVyzTrXY0YEE6m7xKvf22Yg'


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("dice", dice))
    dp.add_handler(CommandHandler("timer", timer))
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
