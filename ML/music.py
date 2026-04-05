import random

EMOTION_TO_SONGS = {
    "angry": [
        {"name": "Love You Zindagi",        "artist": "Jasleen Royal",    "album_art": "https://c.saavncdn.com/369/Dear-Zindagi-Hindi-2016-500x500.jpg"},
        {"name": "Ilahi",                   "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/174/Yeh-Jawaani-Hai-Deewani-2013-500x500.jpg"},
        {"name": "On Top of the World",     "artist": "Imagine Dragons",  "album_art": "https://c.saavncdn.com/307/Night-Visions-2013-500x500.jpg"},
        {"name": "Blinding Lights",         "artist": "The Weeknd",       "album_art": "https://c.saavncdn.com/258/After-Hours-2020-20200320130000-500x500.jpg"},
        {"name": "Agar Tum Saath Ho",       "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/175/Tamasha-2015-500x500.jpg"},
    ],
    "fear": [
        {"name": "Fix You",                 "artist": "Coldplay",         "album_art": "https://c.saavncdn.com/309/X-Y-2005-500x500.jpg"},
        {"name": "Kabira",                  "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/174/Yeh-Jawaani-Hai-Deewani-2013-500x500.jpg"},
        {"name": "Phir Se Ud Chala",        "artist": "Mohit Chauhan",    "album_art": "https://c.saavncdn.com/641/Rockstar-2011-500x500.jpg"},
        {"name": "Somewhere Only We Know",  "artist": "Keane",            "album_art": "https://c.saavncdn.com/292/Hopes-And-Fears-2004-500x500.jpg"},
        {"name": "Raahi",                   "artist": "Pritam",           "album_art": "https://c.saavncdn.com/291/Jab-Harry-Met-Sejal-Hindi-2017-20170802135040-500x500.jpg"},
    ],
    "sad": [
        {"name": "Love You Zindagi",        "artist": "Jasleen Royal",    "album_art": "https://c.saavncdn.com/369/Dear-Zindagi-Hindi-2016-500x500.jpg"},
        {"name": "Levitating",              "artist": "Dua Lipa",         "album_art": "https://c.saavncdn.com/396/Future-Nostalgia-2020-20200327185020-500x500.jpg"},
        {"name": "Good Life",               "artist": "OneRepublic",      "album_art": "https://c.saavncdn.com/316/Native-2013-500x500.jpg"},
        {"name": "Ilahi",                   "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/174/Yeh-Jawaani-Hai-Deewani-2013-500x500.jpg"},
        {"name": "Raabta",                  "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/895/Agent-Vinod-2012-500x500.jpg"},
    ],
    "happy": [
        {"name": "Dynamite",                "artist": "BTS",              "album_art": "https://c.saavncdn.com/718/Dynamite-English-2020-20200821065806-500x500.jpg"},
        {"name": "Kesariya",                "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/871/Brahmastra-Original-Motion-Picture-Soundtrack-Hindi-2022-20221006155213-500x500.jpg"},
        {"name": "Gangnam Style",           "artist": "PSY",              "album_art": "https://c.saavncdn.com/032/Gangnam-Style--English-2012-20200421073139-500x500.jpg"},
        {"name": "Shape of You",            "artist": "Ed Sheeran",       "album_art": "https://c.saavncdn.com/286/WMG_190295851286-English-2017-500x500.jpg"},
        {"name": "Naal Nachna",             "artist": "Shashwat Sachdev", "album_art": "https://c.saavncdn.com/570/Naal-Nachna-From-Dhurandhar-Hindi-2025-20251211114255-500x500.jpg"},
    ],
    "neutral": [
        {"name": "Raataan Lambiyan",        "artist": "Jubin Nautiyal",   "album_art": "https://c.saavncdn.com/955/Shershaah-Hindi-2021-20210810131909-500x500.jpg"},
        {"name": "Sunflower",               "artist": "Post Malone",      "album_art": "https://c.saavncdn.com/441/Spider-Man-Into-The-Spider-Verse-2018-500x500.jpg"},
        {"name": "Heat Waves",              "artist": "Glass Animals",    "album_art": "https://c.saavncdn.com/045/Dreamland-2020-20200807060909-500x500.jpg"},
        {"name": "Kho Gaye Hum Kahan",      "artist": "Jasleen Royal",    "album_art": "https://c.saavncdn.com/981/Kho-Gaye-Hum-Kahan-Hindi-2023-20231215062829-500x500.jpg"},
        {"name": "Tum Hi Ho",               "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/159/Aashiqui-2-2013-500x500.jpg"},
    ],
    "surprise": [
        {"name": "Happy",                   "artist": "Pharrell Williams","album_art": "https://c.saavncdn.com/877/G-I-R-L-English-2014-20250924204116-500x500.jpg"},
        {"name": "Butter",                  "artist": "BTS",              "album_art": "https://c.saavncdn.com/723/Butter-English-2021-20210521065809-500x500.jpg"},
        {"name": "Ilahi",                   "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/174/Yeh-Jawaani-Hai-Deewani-2013-500x500.jpg"},
        {"name": "Love You Zindagi",        "artist": "Jasleen Royal",    "album_art": "https://c.saavncdn.com/369/Dear-Zindagi-Hindi-2016-500x500.jpg"},
        {"name": "Namo Namo",               "artist": "Amit Trivedi",     "album_art": "https://c.saavncdn.com/324/Kedarnath-Hindi-2018-20181207070829-500x500.jpg"},
    ]
}

def get_youtube_url(song_name: str, artist: str) -> str:
    query = f"{song_name} {artist} official audio".replace(" ", "+")
    return f"https://www.youtube.com/results?search_query={query}"

async def get_songs(emotion: str, limit: int = 5) -> list:
    songs_data = EMOTION_TO_SONGS.get(emotion, EMOTION_TO_SONGS["neutral"])
    selected   = random.sample(songs_data, min(limit, len(songs_data)))

    songs = []
    for s in selected:
        songs.append({
            "name":        s["name"],
            "artist":      s["artist"],
            "youtube_url": get_youtube_url(s["name"], s["artist"]),
            "album_art":   s["album_art"],
        })

    print(f"Songs returned: {len(songs)}")
    return songs