import random

EMOTION_TO_SONGS = {
    "angry": [
        {"name": "Love You Zindagi",        "artist": "Jasleen Royal",    "album_art": "https://c.saavncdn.com/494/Dear-Zindagi-Hindi-2016-500x500.jpg"},
        {"name": "Ilahi",                   "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/440/Yeh-Jawaani-Hai-Deewani-2013-500x500.jpg"},
        {"name": "On Top of the World",     "artist": "Imagine Dragons",  "album_art": "https://c.saavncdn.com/210/Night-Visions-2013-500x500.jpg"},
        {"name": "Blinding Lights",         "artist": "The Weeknd",       "album_art": "https://c.saavncdn.com/820/Blinding-Lights-English-2020-20200912094411-500x500.jpg"},
        {"name": "Agar Tum Saath Ho",       "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/994/Tamasha-Hindi-2015-500x500.jpg"},
    ],

    "fear": [
        {"name": "Fix You",                 "artist": "Coldplay",         "album_art": "https://c.saavncdn.com/659/X-Y-English-2005-20201104171639-500x500.jpg"},
        {"name": "Kabira",                  "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/440/Yeh-Jawaani-Hai-Deewani-2013-500x500.jpg"},
        {"name": "Phir Se Ud Chala",        "artist": "Mohit Chauhan",    "album_art": "https://c.saavncdn.com/408/Rockstar-Hindi-2011-20221212023139-500x500.jpg"},
        {"name": "Somewhere Only We Know",  "artist": "Keane",            "album_art": "https://c.saavncdn.com/079/Somewhere-Only-We-Know-English-2022-20240824160837-500x500.jpg"},
        {"name": "Hawayein",                   "artist": "Pritam",        "album_art": "https://c.saavncdn.com/584/Jab-Harry-Met-Sejal-Hindi-2017-20170803161007-500x500.jpg"},
    ],

    "sad": [
        {"name": "Love You Zindagi",        "artist": "Jasleen Royal",    "album_art": "https://c.saavncdn.com/494/Dear-Zindagi-Hindi-2016-500x500.jpg"},
        {"name": "Levitating",              "artist": "Dua Lipa",         "album_art": "https://c.saavncdn.com/665/Future-Nostalgia-English-2020-20260306223201-500x500.jpg"},
        {"name": "Good Life",               "artist": "OneRepublic",      "album_art": "https://c.saavncdn.com/110/Waking-Up-English-2009-20251203081546-500x500.jpg"},
        {"name": "Ilahi",                   "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/440/Yeh-Jawaani-Hai-Deewani-2013-500x500.jpg"},
        {"name": "Raabta",                  "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/603/Agent-Vinod-2012-500x500.jpg"},
    ],

    "happy": [
        {"name": "Dynamite",                "artist": "BTS",              "album_art": "https://c.saavncdn.com/918/Dynamite-DayTime-Version-English-2021-20230404202342-500x500.jpg"},
        {"name": "Kesariya",                "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/871/Brahmastra-Original-Motion-Picture-Soundtrack-Hindi-2022-20221006155213-500x500.jpg"},
        {"name": "Gangnam Style",           "artist": "PSY",              "album_art": "https://c.saavncdn.com/032/Gangnam-Style--English-2012-20200421073139-500x500.jpg"},
        {"name": "Shape of You",            "artist": "Ed Sheeran",       "album_art": "https://c.saavncdn.com/126/Shape-of-You-English-2017-500x500.jpg"},
        {"name": "Naal Nachna",             "artist": "Shashwat Sachdev", "album_art": "https://c.saavncdn.com/570/Naal-Nachna-From-Dhurandhar-Hindi-2025-20251211114255-500x500.jpg"},
    ],

    "neutral": [
        {"name": "Raataan Lambiyan",        "artist": "Jubin Nautiyal",   "album_art": "https://c.saavncdn.com/238/Shershaah-Original-Motion-Picture-Soundtrack--Hindi-2021-20210815181610-500x500.jpg"},
        {"name": "Sunflower",               "artist": "Post Malone",      "album_art": "https://c.saavncdn.com/280/Spider-Man-Into-the-Spider-Verse-Deluxe-Edition-Soundtrack-From-Inspired-By-The-Motion-Picture-English-2019-20250805024215-500x500.jpg"},
        {"name": "Heat Waves",              "artist": "Glass Animals",    "album_art": "https://c.saavncdn.com/136/Heat-Waves-Expansion-Pack--English-2022-20220128063818-500x500.jpg"},
        {"name": "Kho Gaye Hum Kahan",      "artist": "Jasleen Royal",    "album_art": "https://c.saavncdn.com/279/Baar-Baar-Dekho-Hindi-2016-20181205114400-500x500.jpg"},
        {"name": "Tum Hi Ho",               "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/430/Aashiqui-2-Hindi-2013-500x500.jpg"},
    ],

    "surprise": [
        {"name": "Happy",                   "artist": "Pharrell Williams","album_art": "https://c.saavncdn.com/877/G-I-R-L-English-2014-20250924204116-500x500.jpg"},
        {"name": "Butter",                  "artist": "BTS",              "album_art": "https://c.saavncdn.com/918/Dynamite-DayTime-Version-English-2021-20230404202342-500x500.jpg"},
        {"name": "Ilahi",                   "artist": "Arijit Singh",     "album_art": "https://c.saavncdn.com/440/Yeh-Jawaani-Hai-Deewani-2013-500x500.jpg"},
        {"name": "Love You Zindagi",        "artist": "Jasleen Royal",    "album_art": "https://c.saavncdn.com/494/Dear-Zindagi-Hindi-2016-500x500.jpg"},
        {"name": "Namo Namo",               "artist": "Amit Trivedi",     "album_art": "https://c.saavncdn.com/367/Kedarnath-Hindi-2019-20190219-500x500.jpg"},
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