import asyncio
import genshin

async def main():
    client = genshin.Client()

    # Login with username and password
    cookies = await client.login_with_password('', "")

    accounts = await client.get_game_accounts()
    for account in accounts:
        print(account.uid, account.level, account.nickname)

asyncio.run(main())

