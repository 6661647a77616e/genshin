import asyncio
import genshin

async def main():
    client = genshin.Client()
    
    # Login with email and password
    cookies = await client.login_with_password("", "")

    await genshin.utility.update_characters_any()

# Set default game (optional but safe)
    client.default_game = genshin.Game.GENSHIN

    # Get lineup scenarios
    scenarios = await client.get_lineup_scenarios()
    print("Scenarios fetched.")

    # Get top lineups
    lineups = await client.get_lineups(scenarios.abyss.spire, limit=20)
    print(f"Fetched {len(lineups)} lineups.")

    # Get details of first lineup
    if lineups:
        lineup = await client.get_lineup_details(lineups[0].id)
        print(f"Lineup ID: {lineup.id}")
        print(f"Characters: {[char.name for char in lineup.characters]}")
    else:
        print("No lineups available.")

    # Get lineup fields info
    fields = await client.get_lineup_fields()
    print("Lineup field info:")
    for field in fields:
        print(f"{field.name}: {field.options}")

asyncio.run(main())
