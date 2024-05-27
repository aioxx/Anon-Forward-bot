from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nSend me anything and I'll send it back after removing the forwarded tag. \n\nBy @NXDDUpdates ♥"

    # About Message
    ABOUT = """
**About This Bot** 

Developer : @NXDDUpdates
    """

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Remove Caption Button
    remove_button = [InlineKeyboardButton("� Remove Caption �", callback_data="remove")]

    # Add caption button
    add_button = [InlineKeyboardButton("💬 Re-Add Caption 💬", callback_data="add")]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🎪 About The Bot 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/NXDDUpdates")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/vipscraper")],
    ]
