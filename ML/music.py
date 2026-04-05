import httpx
import random

EMOTION_TO_SONGS = {
    "angry": [
        "Love You Zindagi Dear Zindagi",
        "Ilahi Arijit Singh",
        "Imagine Dragons On Top of the World",
        "The Weeknd Blinding Lights",
        "Agar Tum Saath Ho Arijit Singh"
    ],
    "fear": [
        "Coldplay Fix You",
        "Kabira Arijit Singh",
        "Mohit Chauhan Phir Se Ud Chala",
        "Keane Somewhere Only We Know",
        "Raahi Pritam Jab Harry Met Sejal"
    ],
    "sad": [
        "Love You Zindagi Dear Zindagi",
        "Dua Lipa Levitating",
        "OneRepublic Good Life",
        "Ilahi Arijit Singh",
        "Raabta Arijit Singh"
    ],
    "happy": [
        "BTS Dynamite",
        "Arijit Singh Kesariya",
        "PSY Gangnam Style",
        "Ed Sheeran Shape of You",
        "Naal Nachna Dhurandhar"
    ],
    "neutral": [
        "Jubin Nautiyal Raataan Lambiyan",
        "Post Malone Sunflower",
        "Glass Animals Heat Waves",
        "Jasleen Royal Kho Gaye Hum Kahan",
        "Arijit Singh Tum Hi Ho"
    ],
    "surprise": [
        "Pharrell Williams Happy",
        "BTS Butter",
        "Arijit Singh Ilahi",
        "Love You Zindagi",
        "Amit Trivedi Namo Namo"
    ]
}

SKIP_KEYWORDS = [
    "karaoke", "cover", "remix", "instrumental",
    "tribute", "originally performed", "melody",
    "zzang", "boostereo", "revolt", "version"
]

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
                    "n":           5,
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

        best_track = None
        for track in tracks:
            title = track.get("title", "").lower()
            if not any(kw in title for kw in SKIP_KEYWORDS):
                best_track = track
                break

        if not best_track:
            best_track = tracks[0]

        more_info        = best_track.get("more_info", {})
        artist_map       = more_info.get("artistMap", {})
        song_name        = best_track.get("title") or "Unknown"
        primary_artists  = artist_map.get("primary_artists", [])
        featured_artists = artist_map.get("featured_artists", [])

        if primary_artists:
            artist = primary_artists[0]["name"]
            if featured_artists:
                artist += f" ft. {featured_artists[0]['name']}"
        else:
            artist = more_info.get("music", "Unknown")

        return {
            "name":        song_name,
            "artist":      artist,
            "youtube_url": get_youtube_url(song_name, artist),
            "album_art":   best_track.get("image", "").replace("150x150", "500x500"),
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