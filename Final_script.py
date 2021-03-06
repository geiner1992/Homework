import json
import time
import requests
import pprint
import sys

work_url = "https://deckofcardsapi.com/"
site_ext1 = "api/deck/new/shuffle/?deck_count=1"
new_number = ""
current_id_deck = ""

class Calls_APIs:
    def __init__(self, num_cards1, current_id1):
        self.num_cards1 = num_cards1
        self.current_id1 = current_id1
        
    def pull_cards(self):
        global new_number
        attemps = 3
        number_cards = int(self.num_cards1)
        while attemps > 0:
            if number_cards > 0:
                try:
                    banner1 = ('Please, enter how many cards you want to pull from your deck: ')
                    print(banner1)
                    time.sleep(2)
                    print(f"(Remember that you have {number_cards} cards!)")
                    time.sleep(2)
                    pulled_card = int(input("Enter the number here: "))
                    if pulled_card <= number_cards:
                        new_number = pulled_card
                        self.cards_left()
                    elif pulled_card > number_cards:
                        time.sleep(2)
                        print("\nNumber higher than the number cards in your deck! Try again...\n")
                        attemps -= 1
                    else:
                        print("\nYou don't have more cards. The game has ended!")
                        time.sleep(2)
                        sys.exit()
                        attemps -= 1
                except ValueError:
                    time.sleep(2)
                    attemps -= 1
                    print ("\nNot a value between 0 and 52!\n")
            elif number_cards == 0:
                print("\nYou don't have more cards. The game has ended!")
                time.sleep(2)
                sys.exit()
                        
        print("You have run out of attemps, bye!")
        sys.exit()
    
    def cards_left(self):
        global current_id_deck
        global new_number
        current_id_deck = str(self.current_id1)
        list_cards = []
        new_line = (f"api/deck/{current_id_deck}/draw/?count=" + str(new_number))
        new_url = (work_url + new_line)
        payload = {}
        headers = {}
        new_response = requests.request("GET", new_url, headers=headers, data = payload)
        file1_json = new_response.json()
        new_number_cards = file1_json["remaining"]
        for card in file1_json["cards"]:
            value = card["value"]
            suit = card["suit"]
            list_cards.append(f"{value} of {suit}")
        time.sleep(2)
        print("\nYour cards are: ", *list_cards, sep="\n")
        new_number = new_number_cards
        information_deck()
        
def information_deck():
       loop_script = Calls_APIs(new_number, current_id_deck)
       loop_script.pull_cards()

def main_script():
    url = (work_url + site_ext1)
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    data_dict = response.json()
    num_cards = data_dict.get("remaining")
    current_id = data_dict.get("deck_id")
    new_vlaues = (num_cards, current_id)
    return new_vlaues

if __name__ == "__main__":
    value1, value2 = main_script()
    script_values = Calls_APIs(value1, value2)
    script_values.pull_cards()
