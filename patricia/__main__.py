import patricia.utils  # pylint:disable=E0602
from patricia import TOKEN, bot

bot.start(bot_token=TOKEN)

bot.run_until_disconnected()
