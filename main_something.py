# i want to feel unstopable for 30 minutes

import genshin 
from typing import Any
import asyncio
import pandas as pd
from io import BytesIO 
from PIL import Image 
from tqdm import tqdm 
import requests
from pathlib import Path

async def main() -> Any: 
    client = genshin.Client()

    cookies = await client.login_with_password('','')

    await genshin.utility.update_characters_any()

    accounts = await client.get_game_accounts()
    for account in accounts:
        print(account.uid, account.level, account.nickname)

    # artifacts = await client.get_calculator_artifacts()
    # print(f'total artifacts found: {len(artifacts)}')

    characters = await client.get_calculator_characters(query='') #query nothing gives all character

    output_dir = Path("images")
    output_dir.mkdir(exist_ok=True)
    all_chacaters_dict = [c.__dict__ for c in characters]
    
    df = pd.DataFrame(all_chacaters_dict)

    for _, row in df.iterrows():
        name = row['name']

        character_id = int(row['id'])

        talents = await client.get_character_talents(character_id)

        talents_ = [t.__dict__ for t in talents]
        df_talents = pd.DataFrame(talents_)
        print(f"\n{name}'s Talents:")
        for _,talent_row  in df_talents.iterrows():
            print(f"- {talent_row['id']}: {talent_row['name']}")


    # get all weapons 
    weapons = await client.get_calculator_weapons(query='')
    all_weapons_dict = [w.__dict__ for w in weapons]
    df_weapons = pd.DataFrame(all_weapons_dict)

    for _, row_weapon in df_weapons.iterrows():
        name = row_weapon['name']
        id_w = int(row_weapon['id'])
        print(f'{id_w} : {name}')

    # diary = await client.get_diary()

    # print(f"Primogems earned this month: {diary.data.current_primogems}")
    # for category in diary.data.categories:
    #     print(f"{category.percentage}% earned from {category.name} ({category.amount} primogems)")
        
    # image_url = df['icon'].tolist()

    #if you want to download the images
    # for url in image_url:
    #     try:
    #         filename = url.split("/")[-1]  # e.g., UI_AvatarIcon_Clorinde.png
    #         filepath = output_dir / filename

    #         if not filepath.exists():  # Skip if already downloaded
    #             response = requests.get(url, timeout=10)
    #             response.raise_for_status()
    #             with open(filepath, "wb") as f:
    #                 f.write(response.content)
    #             print(f"Downloaded: {filename}")
    #         else:
    #             print(f"Already exists: {filename}")
    #     except Exception as e:
    #         print(f"Failed to download {url}: {e}")
    


if __name__ == "__main__":
    asyncio.run(main())