import fbchat
from getpass import getpass
import codecs
import lyricsgenius
import time
import sys


def initSpamm():
	print("JUMPING ON THE HYPE TRAIN!")
	time.sleep(1)
	print("3")
	time.sleep(1)
	print("2")
	time.sleep(1)
	print("1")
	time.sleep(1)
	print("HERE WE GO!!! TO STOP SENDING MESSAGES PRESS CTRL+C")
	

def sendMessageUser(message, friend):	
		sent = client.sendMessage(message,thread_id = friend.uid)
		if sent:
			print("Message Sent!")
		time.sleep(0.1)


def sendMessageGroup(message, groupid):
	sent = client.sendMessage(message,thread_id = groupid)
	if sent:
		print("Message Sent!")
		time.sleep(0.1)

def fetchSong():
	genius = lyricsgenius.Genius("Genius_Access_Token_Goes_here")
	artist_name = input("Give me an artist/band name to look for: ").encode("utf-8","strict")
	song_name = input("Give me a song of him to look for: ").encode("utf-8","strict")
	song = genius.search_song(song_name.decode("utf-8","strict"),artist_name.decode("utf-8","strict"))
	song_buffer = song.lyrics
	print (song.lyrics)
	tokenizedBuffer = []
	tokenized_buffer = song_buffer.split()
	return tokenized_buffer


print("I need to connect to your facebook to send messages!")

username = input("Facebook Username: ").encode("utf-8","strict")
client = fbchat.Client(username.decode("utf-8","strict"), getpass())
while(1):
	print(
	" _____       _               	\n"
	"/  ___|     | |              	\n"
	"\\ `--. _ __ | |    _   _ _ __ \n"
	" `--. | '_ \\| |   | | | | '__|\n"
	"/\\__/ | |_) | |___| |_| | |  	\n"
	"\\____/| .__/\\_____/\\__, |_|	\n"  
	"      | |           __/ |     	\n"
	"      |_|          |___/      	\n"
	"--------made by Shad3-----------"
	"\n\n\n")
	print("Now do you want to spamm a [G]roup, [U]ser or [E]xit")
	ans = input("[G]/[U]/[E]: ").upper().strip()

	if ans == "G" or ans == "[G]":
		gname = input("Group's name you want to spamm: ").encode("utf-8","strict")
		print("Group's Name Given:" + gname.decode("utf-8","strict"))
		groups = client.searchForGroups(gname.decode("utf-8","strict"))
		group = groups[0]
		tokenisedSong = fetchSong()
		initSpamm()
		for i in range(len(tokenisedSong)):
			sendMessageGroup(tokenisedSong[i],group.uid)
		sys.stdout.flush()

	elif ans == "U" or ans == "[U]":
		
		name = input("Facebook name of your friend you want spamm : ").encode("utf-8","strict")
		print(name.decode("utf-8","strict"))
		friends = client.searchForUsers(name.decode("utf-8","strict"))
		friend = friends[0]
		tokenisedSong = fetchSong()
		initSpamm()
		for i in range(len(tokenisedSong)):
			sendMessageUser(tokenisedSong[i],friend)
		sys.stdout.flush()
	
	elif ans == "E" or ans == "[E]":
		exit(0)
	
	else:
		print("Wrong input!")
		sys.stdout.flush()

	




