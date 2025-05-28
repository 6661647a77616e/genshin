import asyncio
import genshin

async def main():
    # Initialize the client
    client = genshin.Client()

    # If you need to authenticate, add cookies or other login here
    cookies = await client.login_with_password('', "")

    # Required to load character names and metadata
    await genshin.utility.update_characters_any()

    # --- Get all characters ---
    characters = await client.get_calculator_characters()
    print(f"Total characters found: {len(characters)}")

    # --- Get all 5★ and 4★ weapons ---
    weapons = await client.get_calculator_weapons(rarities=[5, 4])
    print(f"Total weapons found (4★ and 5★): {len(weapons)}")

    # --- Get all artifacts ---
    artifacts = await client.get_calculator_artifacts()
    print(f"Total artifacts found: {len(artifacts)}")

    # --- Search for character "Xi" (e.g. Xingqiu or Xiao) ---
    xi_characters = await client.get_calculator_characters(query="Xi")
    print("Matching characters for query 'Xi':", [c.name for c in xi_characters])

    # --- Get all talents of Hu Tao ---
    talents = await client.get_character_talents(10000046)  # Hu Tao ID
    print("Hu Tao talents:", talents)

    # --- Calculate required materials for Hu Tao (level 1 → 90), Staff of Homa (20 → 70) ---
    cost = await (
        client.calculator()
        .set_character(10000046, current=1, target=90)
        .set_weapon(13501, current=20, target=70)  # Staff of Homa
    ).calculate()

    print("\n--- Hu Tao + Homa Upgrade Cost ---")
    for item in cost:
        print(f"{item.name}: {item.amount}")

    # --- Optional: calculate for full Gladiator set (ID: 7554) from 0 → 20 ---
    artifact_set_id = 7554
    artifact_cost = await (
        client.calculator()
        .set_artifact_set(artifact_set_id, current=0, target=20)
    ).calculate()

    print("\n--- Gladiator's Set Upgrade Cost ---")
    for item in artifact_cost:
        print(f"{item.name}: {item.amount}")

asyncio.run(main())
