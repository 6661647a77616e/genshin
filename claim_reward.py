import asyncio
import genshin

async def main():
    client = genshin.Client()

    # Login with email and password

    cookies = await client.login_with_password('', "")

    # Optional: Set the default game (Genshin Impact = "genshin")
    client.default_game = genshin.Game.GENSHIN

    # Try to claim the daily reward
    try:
        reward = await client.claim_daily_reward()
        print(f"Claimed {reward.amount}x {reward.name}")
    except genshin.AlreadyClaimed:
        print("Daily reward already claimed")

    # Get all previously claimed rewards
    print("\nClaimed rewards history:")
    async for reward in client.claimed_rewards():
        print(f"{reward.time} - {reward.amount}x {reward.name}")

    # Get daily sign-in info
    signed_in, claimed_rewards = await client.get_reward_info()
    print(f"\nSigned in: {signed_in} | Total claimed rewards: {claimed_rewards}")

asyncio.run(main())

