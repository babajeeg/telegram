from telethon import TelegramClient

api_id = API_ID
api_hash = 'API HASH'
client = TelegramClient('anon', api_id, api_hash)
tlist = []
async def main():
    me = await client.get_me()
    i=0
    async for dialog in client.iter_dialogs():
        print(str(i), " ",  dialog.name, 'has ID', dialog.id)
        i+=1
        tlist.append(dialog.id)
    target = input("Enter a Number: ")
    target_group=tlist[int(target)]
    print(target_group)
    async for message in client.iter_messages(target_group):
        try:
            if message.sender.username:
                username=message.sender.username
            else:
                username = "No_userName"
            if message.text:
                msg=message.text
            else:
                msg = "No_msg"
            print(username, msg)
        except Exception as e:
            print("Exception")
            pass
        if message.photo:
            path = await message.download_media()
            print('File saved to', path)

with client:
    client.loop.run_until_complete(main())
