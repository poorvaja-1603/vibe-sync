import asyncio
import httpx

async def test_saavn():
    async with httpx.AsyncClient() as client:
        r = await client.get(
            "https://saavn.dev/api/search/songs",
            params={"query": "happy pop", "limit": 5, "page": 1},
            timeout=10.0
        )
    print(f"Status: {r.status_code}")
    data = r.json()
    results = data["data"]["results"]
    print(f"Songs found: {len(results)}")
    for s in results:
        print(f"{s['name']} — {s['artists']['primary'][0]['name']}")

asyncio.run(test_saavn())