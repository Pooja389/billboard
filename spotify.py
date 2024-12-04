import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import spotipy
from spotipy.oauth2 import SpotifyOAuth  

scope = "playlist-modify-private"
clien_id = "your_client_id"
clien_secrest = "client_secret"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id=clien_id,
                                               client_secret=clien_secrest,redirect_uri="http://localhost:7000/callback",
                                               username="Poojasaini",cache_path="tok.text",show_dialog=True))
user_id = sp.current_user()["id"]

date = input("in which date you want to go to (yyyy-mm-dd):")
url=f"https://www.billboard.com/charts/hot-100/{date}/"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

year = date.split("-")[0]

songs = driver.find_elements(By.CSS_SELECTOR, "li ul li h3")
song_titles = []
i=0
while i < 20:
    song_titles.append(songs[i].text.strip())
    i=i+1
print(song_titles)
song_uris = []
for song in song_titles:
    result = sp.search(q=f"{song}",type="track")
    try:
        song_uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    except IndexError:
        print("not available on spotify",song)   

playlist = sp.user_playlist_create(user=user_id,name=f"billboard top 20 {date},",public=False)

sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)