import json
import time
import requests
work_url = "https://deckofcardsapi.com/"
site_ext1 = "api/deck/new/shuffle/?deck_count=1"
new_number = ""

def main_script():
    url = (work_url + site_ext1)
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    your_file = (response.text.encode('utf8'))

    data_dict = json.loads(your_file)
    num_cards = data_dict.get("remaining")
    current_id = data_dict.get("deck_id")
    new_vlaues = (num_cards, current_id)
    return new_vlaues

class Calls_APIs:
    def __init__(self, num_cards1, current_id1):
        self.num_cards1 = num_cards1
        self.current_id1 = current_id1
        
    def pull_cards(self):
        global new_number
        number_cards = float(self.num_cards1)
        var_1 = ("Remember that you have ")
        var_2 = (" cards!")
        while number_cards > 0:
            banner1 = ('Please, enter how many cards you want to pull from your deck.')
            print(banner1)
            time.sleep(2)
            banner2 = var_1, number_cards ,var_2
            print(banner2)
            time.sleep(2)
            pulled_car = input('Enter the number here: ')
            new_number = pulled_car
            break
            
    def cards_left(self):
        new_line = (self.current_id1 + "/draw/?count=" + new_number)
        new_url = (work_url + new_line)
        payload = {}
        headers= {}
        response = requests.request("GET", new_url, headers=headers, data = payload)
        print(response.text.encode('utf8'))            

if __name__ == '__main__':
    value1, value2 = main_script()
    script_values = Calls_APIs(value1, value2)
    script_values.pull_cards()
    script_values.cards_left()


    
