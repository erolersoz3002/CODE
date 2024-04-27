import pytube


url =input("url gir:")
path=""
pytube.YouTube(url).streams.get_highest_resolution().download(path)