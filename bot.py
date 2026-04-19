from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔑 YAHAN APNI DETAILS DAALO
BOT_TOKEN = "8642124237:AAFcULXgReezhcq6vZEKb3cH8Ce3mlb2aoA"
CHANNEL_USERNAME = "@Darkhck_zone"   # force join ke liye
CHANNEL_ID = -1003976428034  # private channel id (video storage)

# 🎬 VIDEO MESSAGE IDs (channel se)
VIDEO_IDS = list(range(51,73))



# 🚀 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME.replace('@','')}")],
        [InlineKeyboardButton("✅ Verify", callback_data="verify")]
    ]
    await update.message.reply_text(
        "🔥 Welcome!\n\n📌 Pehle channel join karo phir verify karo",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


# ✅ VERIFY
async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

        if member.status in ["member", "administrator", "creator"]:
            buttons = [
                [InlineKeyboardButton("🎓 Course Videos", callback_data="course")]
            ]
            await query.message.edit_text(
                "✅ Verified Successfully!\n\n👇 Ab course open karo",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        else:
            await query.answer("❌ Pehle channel join karo!", show_alert=True)

    except:
        await query.answer("❌ Channel join nahi kiya!", show_alert=True)


# 🎓 COURSE BUTTON
async def course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    # 🎬 VIDEO 1
async def course(update, context):
    query = update.callback_query
    user_id = query.from_user.id

    for vid in VIDEO_IDS:
        await context.bot.copy_message(
            chat_id=user_id,
            from_chat_id=CHANNEL_ID,
            message_id=vid,
            protect_content=True
        )

    await query.answer()


# 🚀 RUN BOT
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(verify, pattern="verify"))
app.add_handler(CallbackQueryHandler(course, pattern="course"))

print("🤖 Bot chal raha hai...")
app.run_polling()