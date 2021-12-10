import sys
import time
import telepot
import RPi.GPIO as GPIO
from dotenv import load_dotenv
import os

load_dotenv()

CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

chat_id=0
ledPin=6
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, GPIO.HIGH)

def on():
        GPIO.output(ledPin,GPIO.HIGH)

def off():
        GPIO.output(ledPin,GPIO.LOW)

def dot():
	on()
	bot.sendMessage(chat_id, '.')
	time.sleep(0.2)
	off()
	time.sleep(0.2)

def dash():
	on()
	bot.sendMessage(chat_id, '-')
	time.sleep(0.5)
	off()
	time.sleep(0.2)

def morseLetter(letter):
	for symbol in CODE[letter.upper()]:
		if symbol == '-':
			dash()
		elif symbol == '.':
			dot()
		else:
			time.sleep(0.5)
		time.sleep(0.5)

def handle(msg):

	if 'text' in msg:
		global chat_id
		chat_id = msg['chat']['id']
		command = msg['text']

		print('Got command: %s' % command)

		if command == 'on':
			on()
			bot.sendMessage(chat_id, 'Dune lüchtets💡')
		elif command =='off':
			off()
			bot.sendMessage(chat_id, 'Dune lüchtets nüm 🕯')
		elif "morse:" in command.lower():
			for letter in command.replace("morse: ", ''):
				morseLetter(letter)
	else:
		print(msg)
try:
    token = os.getenv('BOT_TOKEN')
    bot = telepot.Bot(token)
    print(bot.getMe())
    bot.message_loop(handle)
    print('I am listening...')
except KeyboardInterrupt:
    print('\n Program interrupted')
    GPIO.cleanup()
    exit()
except:
    print("some error") 
while 1:
    try:
        time.sleep(10)
    
    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()
    
    except:
        print('Other error or exception occured!')
        GPIO.cleanup()
