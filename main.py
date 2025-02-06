import os
from kindle_parse import Highlights
from notion_push import HighlightPush
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Telegram Bot API Token
TELEGRAM_API_TOKEN = "7275940612:AAGuPFUupXs3Snfq-9L6ZclUx9iNGqxbLME"


async def start(update: Update, context):
    await update.message.reply_text(
        "发送 Kindle 的 HTML 文件，我会解析并上传到 Notion！"
    )


async def handle_document(update: Update, context):
    document = update.message.document
    file = await context.bot.get_file(document.file_id)
    file_path = f"{document.file_name}"

    # 下载文件
    await file.download_to_drive(file_path)

    print(file_path)
    # 解析并上传
    h = Highlights(file_path)
    h.parse()
    p = HighlightPush(h.book_title, h.highlights)
    p.push()
    # parse_html_and_upload(file_path)

    # 删除文件
    os.remove(file_path)

    await update.message.reply_text(
        f"文件 {document.file_name} 处理完成并上传到 Notion！"
    )


def main():
    # 初始化应用
    application = Application.builder().token(TELEGRAM_API_TOKEN).build()

    # 添加命令处理器
    application.add_handler(CommandHandler("start", start))

    # 处理文档消息
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    # 启动应用
    application.run_polling()


if __name__ == "__main__":
    main()


# h = Highlights(html)
# h.parse()
# # p = HighlightPush(h.book_title, h.highlights)
# # p.push()
