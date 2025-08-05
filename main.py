import pyrogram, os
# import dotenv
# dotenv.load_dotenv()
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
CHAT_ID1 = int(os.environ.get("CHAT_ID1"))
CHAT_ID2 = int(os.environ.get("CHAT_ID2"))
PER_USER = os.environ.get("PER_USER")
SESSION_STRING =os.environ.get("SESSION")
import time

app = pyrogram.Client("my_account",api_id=API_ID,api_hash=API_HASH,session_string=SESSION_STRING,sleep_threshold=0)
# app.start()
async def main():
  async with app:
    await app.send_message("me", "Greetings from **Pyrogram**!")
    id1, id2= 0, 0
    while True:
      #1
      async for b in app.get_chat_history(chat_id=CHAT_ID1,limit=1):
        print(b.id,b.text)
        if id1 != b.id:
          latest_id = b.id
          # latest_text=b.text
          await app.copy_message(chat_id=PER_USER, from_chat_id=CHAT_ID1, message_id=latest_id)
          id1 = latest_id
          print("Sent one message")
      #2
      async for b in app.get_chat_history(chat_id=CHAT_ID2,limit=1):
        print(b.id,b.text)
        if id2 != b.id:
          latest_id = b.id
          # latest_text=b.text
          await app.copy_message(chat_id=PER_USER, from_chat_id=CHAT_ID2, message_id=latest_id)
          id2 = latest_id
      
      time.sleep(10)
app.run(main())
