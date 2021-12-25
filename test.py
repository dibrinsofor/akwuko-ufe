import requests

BASE = "http://127.0.0.1:5000/"

# field={field}, cover_img={cover_img}, audio_url={audio_url}, summary={summary}, addi_img={addi_img})

data = [{"title": "farts", "content": "200000", "likes": 4000000, "field":"history", "cover_img":"https://linkedin.com/in/dibrinsofor", "audio_url":"https://spotify.com", "summary":"still fartual", "date":"2021-11-01"}, 
        {"title": "How to deez nuts", "content": "20000000", "likes": 500000, "field":"folk tale", "cover_img":"https://linkedin.com/in/jamesharden", "audio_url":"spotify.com/artist/drake", "addi_img":"https://photos.com"}, 
        {"title": "How to tie your shoes", "content": "150000000000000", "likes": 100000, "field":"audio lesson", "cover_img":"https://linkedin.com/in/dibrinsofor", "audio_url":"spotify.com/artist/drake", "summary":"still fartual", "addi_img":"https://deeznuts.com"}, 
        {"title": "farts. Part 2", "content": "2000", "likes": 10, "field":"history", "cover_img":"https://linkedin.com/in/dibrinsofor", "audio_url":"spotify.com/artist/drake", "summary":"still fartual", "addi_img":"https://deeznuts.com"}]


# for i in range(len(data)):
#     response = requests.put(BASE + "api/story/" + str(i+1), data[i])
#     print(response.json())
    
# input()

response = requests.get(BASE + "api/story/1")
print(response.json())

# print(requests.get(BASE + "story/").content)