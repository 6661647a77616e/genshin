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
    # print(scenarios)

    # Get top lineups
    lineups = await client.get_lineups(scenarios.abyss.spire, limit=20)
    print(f"Fetched {len(lineups)} lineups.")

    print("Spiral Abyss Structure:")
    print_scenario_tree(scenarios.abyss)

    print("\nWorld Exploration Structure:")
    print_scenario_tree(scenarios.world)

    print("\nImaginarium Theater Structure:")
    print_scenario_tree(scenarios.children[-2])  # or access by name if available



def print_scenario_tree(scenario, indent=0):
    print("  " * indent + f"- {scenario.name} (id={scenario.id})")
    for child in scenario.children:
        print_scenario_tree(child, indent + 1)


asyncio.run(main())
