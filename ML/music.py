import httpx
import random

EMOTION_TO_SONGS = {
    "angry": [
        "Love You Zindagi",
        "Ilahi Yeh Jawaani Hai Deewani",
        "On Top of the World Imagine Dragons",
        "Blinding Lights The Weeknd",
        "Agar Tum Saath Ho Tamasha"
    ],
    "fear": [
        "Fix You Coldplay",
        "Kabira Yeh Jawaani Hai Deewani",
        "Phir Se Ud Chala Rockstar",
        "Somewhere Only We Know Keane",
        "Raahi Jab Harry Met Sejal"
    ],
    "sad": [
        "Love You Zindagi",
        "Levitating Dua Lipa",
        "Good Life OneRepublic",
        "Ilahi Yeh Jawaani Hai Deewani",
        "Raabta Agent Vinod"
    ],
    "happy": [
        "Dynamite BTS",
        "Naal Nachhna Dhurandhar",
        "Kesariya Brahmastra",
        "Gangnam Style",
        "Shape of You Ed Sheeran"
    ],
    "neutral": [
        "Raataan Lambiyan Shershaah",
        "Blinding Lights The Weeknd",
        "Sunflower Post Malone",
        "Heat Waves Glass Animals",
        "Kho Gaye Hum Kahan"
    ],
    "surprise": [
        "Happy Pharrell Williams",
        "Butter BTS",
        "Ilahi Yeh Jawaani Hai Deewani",
        "Love You Zindagi",
        "Namo Namo Kedarnath"
    ]
}

def get_youtube_url(song_name: str, artist: str) -> str:
    query = f"{song_name} {artist} official audio".replace(" ", "+")
    return f"https://www.youtube.com/results?search_query={query}"

async def get_one_song(query: str) -> dict | None:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://www.jiosaavn.com/api.php",
                params={
                    "__call":      "search.getResults",
                    "q":           query,
                    "p":           1,
                    "n":           1,
                    "_format":     "json",
                    "_marker":     "0",
                    "api_version": "4",
                    "ctx":         "web6dot0"
                },
                timeout=10.0,
                headers={"User-Agent": "Mozilla/5.0"}
            )
        data = response.json()
        tracks = data.get("results", [])
        if not tracks:
            return None

        track      = tracks[0]
        more_info  = track.get("more_info", {})
        artist_map = more_info.get("artistMap", {})
        song_name  = track.get("title") or "Unknown"

        primary_artists  = artist_map.get("primary_artists", [])
        featured_artists = artist_map.get("featured_artists", [])

        if primary_artists:
            artist = primary_artists[0]["name"]
            if featured_artists:
                artist += f" ft. {featured_artists[0]['name']}"
        else:
            artist = more_info.get("music", "Unknown")

        album_art   = track.get("image", "").replace("150x150", "500x500")
        youtube_url = get_youtube_url(song_name, artist)

        return {
            "name":        song_name,
            "artist":      artist,
            "youtube_url": youtube_url,
            "album_art":   album_art,
        }
    except Exception as e:
        print(f"Song fetch error: {e}")
        return None

async def get_songs(emotion: str, limit: int = 5) -> list:
    queries = EMOTION_TO_SONGS.get(emotion, EMOTION_TO_SONGS["neutral"])
    random.shuffle(queries)

    songs = []
    for query in queries[:limit]:
        song = await get_one_song(query)
        if song:
            songs.append(song)

    print(f"Songs returned: {len(songs)}")
    return songs