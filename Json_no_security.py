import json
import sys

import requests



def value_euro():
    try:
        #Get Json from url
        response=requests.get('https://api.frankfurter.app/latest?from=EUR&to=USD')
        response_json = json.loads(response.text)
    except Exception:
        print("Error")
        sys.exit()



    return response_json

def randon_joke():
    try:
        #Get random joke from url
        response=requests.get('https://simple-joke-api.deno.dev/random')
        response_json = json.loads(response.text)
    except Exception:
        print("Error in connection")
        sys.exit()
    return response_json

def dog_pic():
    try:
        #Get dog pic (Json format) from url
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response_json = json.loads(response.text)
    except Exception:
        print("Error in connection")
        sys.exit()
    return response_json




#Main program start here with welcome
print("Welcome to use some Json messages.\n ")
while True:
    try:
        choice=int(input(" 1) One € value in $  \n 2) Get random Joke \n 3) Get link to Dog picture \n 0) Quit program \n Your choice > "))
    except Exception:
        print("Choice NOT accepted")
        print("Make choice, press 1, 2, 3 or 0\n")
        continue
    if choice==1:
        answer=value_euro()
        print("Today "+str(answer["date"])+":\n")
        print("1.0 € is in USD "+str(answer["rates"]['USD'])+"\n")
    if choice == 2:
        answer = randon_joke()
        print("1.st part of joke:\n" + str(answer["setup"]))

        print("And the punchline: " + str(answer["punchline"])+"\n")

    if choice==3:
        answer=dog_pic()
        print("Click on the link "+answer["message"])
    if choice==0:

        print("Thanks for using program.")
        break