# Splyr
Splyr is a small piece of python code that spamms the lyrics of a song to a facebook friend or group. This was a friend's idea and I implemented, just for fun. 

By analysing the piece of code it's easy to understand that all it does is that it connects to a facebook account using the account **USERNAME** and password. Then it looks up for the song's lyrics that you want using the Genius API.
### You can find the username by following the steps below
- Log in to your account
- Go to Settings from the drop-down menu on the top-right area of the window
- It should appear in front of you.

## Desclaimer

The creator of the script carries **no responsibility for any outcome event which may occur** such as getting blocked by a friend or Facebook's actions. the one and only responsible is the one who runs the script.


## Installation

1) Create an account on Genius
Go to https://genius.com/api-clients
Create a client with the characteristics that you want.
Generate an access token and paste it in the code part in Splyr.py that says clearly "Access_token_goes_here".

2) Follow the instructions below typing them on terminal to be able to run the program

```
git clone https://github.com/0xShad3/Splyr.git
cd Splyr
pip3 install -r requirements.txt
python3 Splyr.py
```
Enjoy !

## Shout out
- @annatolia1 for the idea.
- fbchat https://fbchat.readthedocs.io/en/stable/
- LyricsGenius https://github.com/johnwmillr/LyricsGenius
