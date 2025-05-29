import asyncio
import genshin
import sys
import asyncio
import genshin

client = genshin.Client()

async def login():
    # Replace with your actual credentials or prompt user input
    email = input("Email: ")
    password = input("Password: ")
    try:
        await client.login_with_password(email, password)
        print("✅ Login successful.")
    except Exception as e:
        print(f"❌ Login failed: {e}")
        exit()

async def get_characters():
    await genshin.utility.update_characters_any()
    characters = await client.get_calculator_characters()
    print(f"Total characters found: {len(characters)}")
    for c in characters:
        print("-", c.name)

async def claim_daily_reward():
    try:
        reward = await client.claim_daily_reward()
        print(f"🎁 Claimed {reward.amount}x {reward.name}")
    except genshin.AlreadyClaimed:
        print("🔁 Daily reward already claimed.")

async def view_lineups():
    scenarios = await client.get_lineup_scenarios()
    lineups = await client.get_lineups(scenarios.abyss.spire, limit=5)
    for i, lineup in enumerate(lineups, 1):
        print(f"{i}. Lineup ID: {lineup.id}, Characters: {[char.name for char in lineup.characters]}")

async def view_accounts():
    accounts = await client.get_game_accounts()
    for acc in accounts:
        print(f"UID: {acc.uid} | Level: {acc.level} | Nickname: {acc.nickname}")

async def main_menu():
    while True:
        print("\n=== Genshin CLI Menu ===")
        print("1. Get Characters")
        print("2. Claim Daily Reward")
        print("3. View Lineups")
        print("4. View Accounts")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            await get_characters()
        elif choice == "2":
            await claim_daily_reward()
        elif choice == "3":
            await view_lineups()
        elif choice == "4":
            await view_accounts()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

async def main():
    await login()
    client.default_game = genshin.Game.GENSHIN  # ✅ Set the default game otherwise no default game stated
    await main_menu()

if __name__ == "__main__":
    asyncio.run(main())

    # asyncio.run(asyncio.create_task(login()).then(main_menu))

# asyncio.run() expects a courtine , a sync def funtion thats been called.