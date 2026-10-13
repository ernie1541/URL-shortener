import random
import math

def main():
    short_URLS = {}
    randlets = "abcdefghijklmnopqrstuvwxyz123456789"
    choice = int(input(("""Welcome to the URL shortener!
    What will you do?
    1.generate shortened URL.
    2.get original URL.
    3. view shortened URLS and Their Original.""")))
    match choice:
        case 1:
            for i in range(6):
                the_URL += randlets[random.randint(0,len(randlets)-1)]
            target_URL = input("What URL do you want to shorten?")
            short_URLS[the_URL] = target_URL
