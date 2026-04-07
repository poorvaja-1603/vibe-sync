import httpx
import random

EMOTION_TO_QUERIES = {
    "sad": [
        "levitating dua lipa",
        "good life onerepublic",
        "happy pharrell williams",
        "on top of the world imagine dragons",
        "count on me bruno mars",
        "roar katy perry",
        "pasoori ali sethi",
        "sunflower post malone",
    ],
    "angry": [
        "fix you coldplay",
        "someone like you adele",
        "let her go passenger",
        "the scientist coldplay",
        "channa mereya arijit singh",
        "tujhe kitna chahne lage arijit singh",
        "drivers license olivia rodrigo",
        "stay rihanna",
    ],
    "happy": [
        "shape of you ed sheeran",
        "dance monkey tones and i",
        "blinding lights weeknd",
        "dynamite bts",
        "as it was harry styles",
        "watermelon sugar harry styles",
        "kesariya arijit singh",
        "bad guy billie eilish",
    ],
    "fear": [
        "heat waves glass animals",
        "perfect ed sheeran",
        "hall of fame the script",
        "stronger kelly clarkson",
        "brave sara bareilles",
        "believer imagine dragons",
        "kabira arijit singh",
        "thunder imagine dragons",
    ],
    "neutral": [
        "lovely billie eilish",
        "save your tears weeknd",
        "golden jungkook",
        "peaches justin bieber",
        "anti hero taylor swift",
        "starboy weeknd",
        "khairiyat arijit singh",
        "beautiful in white charlie puth",
    ],
    "surprise": [
        "uptown funk bruno mars",
        "cant stop the feeling justin timberlake",
        "shake it off taylor swift",
        "havana camila cabello",
        "senorita shawn mendes",
        "7 rings ariana grande",
        "ghungroo war hrithik roshan",
        "stay the kid laroi",
    ],
}

def get_youtube_url(name: str, artist: str) -> str:
    q = f"{name} {artist} official audio".replace(" ", "+")
    return f"https://www.youtube.com/results?search_query={q}"

async def search_deezer(query: str) -> dict | None:
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(
                "https://api.deezer.com/search",
                params={"q": query, "limit": 5},
                timeout=8.0
            )
        data = r.json().get("data", [])
        if not data:
            return None

        # pick first track that has a preview
        for track in data:
            if track.get("preview"):
                return track
        return None

    except Exception as e:
        print(f"Deezer error for '{query}': {e}")
        return None

async def get_songs(emotion: str, limit: int = 5) -> list:
    queries = EMOTION_TO_QUERIES.get(emotion, EMOTION_TO_QUERIES["neutral"])
    pool    = queries[:]
    random.shuffle(pool)

    songs = []
    for query in pool:
        if len(songs) >= limit:
            break

        track = await search_deezer(query)
        if not track:
            continue

        name    = track["title"]
        artist  = track["artist"]["name"]
        preview = track["preview"]           # always 30s mp3
        art     = track["album"]["cover_medium"]
        deezer  = track["link"]

        songs.append({
            "name":        name,
            "artist":      artist,
            "preview_url": preview,
            "youtube_url": get_youtube_url(name, artist),
            "deezer_url":  deezer,
            "album_art":   art,
            "has_preview": True,
        })

    print(f"Songs returned: {len(songs)} for {emotion}")
    return songs