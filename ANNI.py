import subprocess
import wolframalpha
import pyttsx3
import json
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !") 

	else:
		speak("Good Evening Sir !") 

	assname =("Anni")
	speak("I am your Assistant")
	speak(assname)
	

def usrname():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 0.9
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	
	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('enter your email', '*******')
	server.sendmail('enter your email', to, content)
	server.close()

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any command before execution of this python file
	clear()
	wishMe()
	usrname()
	
	while True:
		
		query = takeCommand().lower()
		
		# All the commands said by user will be stored here in 'query' and will be converted to lower case for easily recognition of command
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)
                 #Youtube is open by this condition
		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")
			
                 #Open google website by this condition in default broswer 
		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")
			
                  #Open stackoverflow website by this condition in default broswer
		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com") 
                  
		#Play music by default which play list you have in your pc   
		elif 'play music' in query or "play song" in query:
			speak("Here you go with music")
			# music_dir = "G:\\Song"
			music_dir = "D:\songs"
			songs = os.listdir(music_dir)
			print(songs) 
			random = os.startfile(os.path.join(music_dir, songs[1]))
                
		#it shows you time 
		elif 'the time' in query:
			strTime =time.strftime("%m-%d-%Y %T:%M%p") 
			speak(f"Sir, the time is {strTime}")

		
               #this will help you to create  mail 
		elif 'mail  ' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				to = "sending email "
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")
                #this will help you to send mail 
		elif 'send a mail' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				speak("whome should i send")
				to = input() 
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")
                  
		#this condition response you like a human talk 
		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")
                
		#this condition response you like a human talk 
		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")
                 
		#this condition will help you to change user name 
		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query
               
	         #this condition will hepl you to change name of your virtual assistant 
		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")
                
		#this condition will return you very friendly answers
		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)
                 
		#this will finish the commands of your program and finish the program 
		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()
                    
		#this condition give you information about developer name 
		elif "who made you" in query or "who created you" in query: 
			speak("I have been created by Anmol .")
		
		#through this condition anni crack a joke for you 
		elif 'joke' in query:
			speak(pyjokes.get_joke())
		
		#this condtion will return you any query answer using AI algo's 
		elif "calculate" in query: 
			
			app_id = 'walform api '
			client = wolframalpha.Client(app_id)
			indx = query.lower().split().index('calculate') 
			query = query.split()[indx + 1:] 
			res = client.query(' '.join(query)) 
			answer = next(res.results).text
			print("The answer is " + answer) 
			speak("The answer is " + answer) 
                
		#this condtion will  help to search
		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "") 
			query = query.replace("play", "")		 
			webbrowser.open(query) 
 
                #this condtion will friendly reslut like human 
		elif "who i am" in query:
			speak("If you talk then definately your human.")
 
                #this condition will result of creating anni
		elif "why you came to world" in query:
			speak("Thanks to Anmol. further It's a secret")

		
                #this condtion will friendly result like human 
                elif 'is love' in query:
                       speak("It is 7th sense that destroy all other senses")
 
                #this condtion will friendly result like human 
                 elif "who are you" in query:
			speak("I am your virtual assistant created by Anmol ")
                
		#this condtion will friendly result like human 
                 elif 'reason for you' in query:
			speak("I was created as a Minor project by Anmol ")

		#this condition will change background of your pc 	
		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20, 
													0, 
													"Location of wallpaper",
													0)
			speak("Background changed succesfully")

		
                #this condition will return you news 
		elif 'news' in query:
			
			try: 
				jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =0a202433323f4644ace82626e2750277''')
				data = json.load(jsonObj)
				i = 1
				
				speak('here are some top news from the times of india')
				print('''=============== TIMES OF INDIA ============'''+ '\n')
				
				for item in data['articles']:
					
					print(str(i) + '. ' + item['title'] + '\n')
					print(item['description'] + '\n')
					speak(str(i) + '. ' + item['title'] + '\n')
					i += 1
			except Exception as e:
				
				print(str(e))

		
		#this condtion willlock window of your pc 
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()
                 
		#this condtion will shutdown system your pc 
		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
		
		#this condtion will empty recycle bin your pc 
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")
			
                #this condtion will stop music  your pc 
		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop anni from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

                 #this condition will gives you location of any where  	
		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")
           
	        #this condtion will turn on camera your pc 
		elif "camera" in query or "take a photo" in query:
			ec.capture(0, "Jarvis Camera ", "img.jpg")

		#this condtion will restart your pc 	
		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
		
		#this condtion will hibernate your pc 
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		#this condtion will log off your pc 	
		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		#this conition will help to create a document 	
		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('new.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = time.strftime("%m-%d-%Y %T:%M%p") 
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		#this condition will gives show you notes that you create 
		elif "show note" in query:
			speak("Showing Notes")
			file = open("new.txt", "r") 
			print(file.read())
			speak(file.read(6))

		
		#this condition will gives you  result that anni is there for you 
		elif "Anni" in query:
			
			wishMe()
			speak("anni in your service Mister")
			speak(assname)

		#this condition gives weather report of any location 	
		elif "weather" in query:
			base_url = "http://api.openweathermap.org/data/2.5/weather?appid=api_id&q="
			speak(" City name ")
			print("City name : ")
			city_name = takeCommand()
			complete_url = base_url  + city_name
			response = requests.get(complete_url) 
			x = response.json() 
			
			if x["cod"] != "404": 
				y = x["main"] 
				current_temperature = y["temp"] 
				current_pressure = y["pressure"] 
				current_humidiy = y["humidity"] 
				z = x["weather"] 
				weather_description = z[0]["description"] 
				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
			
			else: 
				speak(" City Not Found ")
			
		
 
                #this condition is give result of query from wikipedia 
		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		#this condition wishes you when you first intract with anni 	
		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)

		#this will give you very friendly result	
		elif "will you be my gf" in query or "will you be my bf" in query: 
			speak("I'm not sure about, may be you should give me some time")

		#this will give you very friendly result	
		elif "how are you" in query:
			speak("I'm fine, glad you me that")
 
                  #this will give you very friendly result
		elif "i love you" in query:
			speak("It's hard to understand")

	
