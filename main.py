import pyrogram, os
# import dotenv
# dotenv.load_dotenv()
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
CHAT_ID = int(os.environ.get("CHAT_ID"))
PER_USER = os.environ.get("PER_USER")
SESSION_STRING =os.environ.get("SESSION")
import time

app = pyrogram.Client("my_account",api_id=API_ID,api_hash=API_HASH,session_string=SESSION_STRING,sleep_threshold=0)
# app.start()
async def main():
  async with app:
    await app.send_message("me", "Greetings from **Pyrogram**!")
    id=0
    while True:
      async for b in app.get_chat_history(chat_id=CHAT_ID,limit=1):
        print(b.id,b.text)
        if id != b.id:
          latest_id = b.id
          # latest_text=b.text
          await app.copy_message(chat_id=PER_USER, from_chat_id=CHAT_ID, message_id=latest_id)
          id = latest_id
          print("Sent one message")
      time.sleep(10)
app.run(main())
