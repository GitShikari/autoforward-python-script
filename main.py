import pyrogram, os
# import dotenv
# dotenv.load_dotenv()
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
CHAT_ID1 = int(os.environ.get("CHAT_ID1"))
CHAT_ID2 = int(os.environ.get("CHAT_ID2"))
PER_USER = os.environ.get("PER_USER")
SESSION_STRING =os.environ.get("SESSION")
# import time

app = pyrogram.Client("my_account",api_id=API_ID,api_hash=API_HASH,session_string=SESSION_STRING,sleep_threshold=0)
# app.start()

@app.on_message(pyrogram.filters.chat(CHAT_ID1) | pyrogram.filters.chat(CHAT_ID2))
async def message_handler(client,message):
  print(message)
  app.send_message(PER_USER,message.text)
    
      
      # time.sleep(10)
app.run()
