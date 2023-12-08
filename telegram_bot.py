from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import json

# Configuration for the bot
TOKEN = ''  # bot's token

# Function to read and format product data
def read_and_format_product_data():
    """
Reads the merged product data from 4_result.json.
Formats each product into a message string including name, base price, sale price, and link.
    """
    with open('data/4_result.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    messages = []
    for page, items in data.items():
        for item in items['body']['products']:
            name = item.get('name', 'No name')
            price_base = item.get('item_basePrice', 'No price')
            price_sale = item.get('item_salePrice', 'No price')
            link = item.get('item_link', 'No link')
            message = f"{name}\nBase Price: {price_base}\nSale Price: {price_sale}\nLink: {link}\n"
            messages.append(message)
    
    return messages

# Global dictionary to keep track of user pagination
user_pagination = {}
"""
user_pagination dictionary to track each user's position in the product list.
send_product_info initializes the pagination for a user and calls send_next_products.
send_next_products sends a limited number of product messages and provides a "More" button for additional products.
button function handles the callback from the "More" button.
"""
def send_product_info(update, context):
    chat_id = update.message.chat_id
    product_messages = read_and_format_product_data()
    # Set initial state for new user or reset if already exists
    user_pagination[chat_id] = {
        'current_index': 0,
        'messages': product_messages
    }

    send_next_products(update, context)
def send_next_products(update, context, chat_id=None):
    if chat_id is None:
        chat_id = update.effective_chat.id

    pagination = user_pagination.get(chat_id, None)
    if pagination:
        start_index = pagination['current_index']
        end_index = start_index + 3  # Adjust the number of products per page here
        messages = pagination['messages'][start_index:end_index]

        for message in messages:
            context.bot.send_message(chat_id=chat_id, text=message)

        # Update the current index
        pagination['current_index'] = end_index

        # Check if there are more products to show
        if end_index < len(pagination['messages']):
            button = InlineKeyboardMarkup([[InlineKeyboardButton("More", callback_data='more')]])
            context.bot.send_message(chat_id=chat_id, text='Show more products?', reply_markup=button)

"""
start function to handle the /start command.
send_product_info for the /products command.
button for handling pagination.
"""
def button(update, context):
    query = update.callback_query
    query.answer()

    chat_id = query.message.chat_id

    if query.data == 'more':
        send_next_products(update, context, chat_id=chat_id)


def start(update, context):
    update.message.reply_text('Welcome to the Product Info Bot! Use /products to view products.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("products", send_product_info))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()