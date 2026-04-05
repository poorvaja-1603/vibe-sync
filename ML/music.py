import httpx
import random

EMOTION_TO_SONGS = {
    "angry": [
        "Love You Zindagi Dear Zindagi original",
        "Ilahi Yeh Jawaani Hai Deewani Arijit Singh",
        "Imagine Dragons On Top of the World original",
        "The Weeknd Blinding Lights original",
        "Agar Tum Saath Ho Arijit Singh Tamasha"
    ],
    "fear": [
        "Coldplay Fix You original",
        "Kabira Arijit Singh Yeh Jawaani Hai Deewani",
        "Mohit Chauhan Phir Se Ud Chala Rockstar",
        "Keane Somewhere Only We Know original",
        "Anushka Shaikh Raahi Jab Harry Met Sejal"
    ],
    "sad": [
        "Love You Zindagi Dear Zindagi original",
        "Dua Lipa Levitating original",
        "OneRepublic Good Life original",
        "Ilahi Arijit Singh Yeh Jawaani Hai Deewani",
        "Raabta Arijit Singh Agent Vinod original"
    ],
    "happy": [
        "BTS Dynamite original",
        "Naal Nachna Dhurandhar original",
        "Arijit Singh Kesariya Brahmastra",
        "PSY Gangnam Style original",
        "Ed Sheeran Shape of You original"
    ],
    "neutral": [
        "Jubin Nautiyal Raataan Lambiyan Shershaah",
        "The Weeknd Blinding Lights original",
        "Post Malone Sunflower original",
        "Glass Animals Heat Waves original",
        "Jasleen Royal Kho Gaye Hum Kahan"
    ],
    "surprise": [
        "Pharrell Williams Happy original",
        "BTS Butter original",
        "Arijit Singh Ilahi Yeh Jawaani Hai Deewani",
        "Love You Zindagi Dear Zindagi original",
        "Amit Trivedi Namo Namo Kedarnath"
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