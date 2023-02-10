
from rasa_sdk import Action, Tracker
#from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

# class for check balance in the account

class ActionCheckBalance(Action):

    def name(self):
        return "check_balance"
                        
    def run(self, dispatcher, tracker, domain):
        account_number = tracker.get_slot("account_number")
        name = tracker.get_slot("name")

        user_db = {
            "12345": {"name": "mukesh jayswal", "balance": 1000},       # dict of account data
            "54321": {"name": "ram thapa", "balance": 2000},
        } 
        if account_number in user_db:                                   #check account number in the data
            user_info = user_db[account_number]
            if name == user_info["name"]:                                #check name in given data
                response = (
                    f"Dear {name}, your account number {account_number} has a balance of Rs. {user_info['balance']}"    # account number and name matched then showing balance of account
                )
            else:
                response = "The name does not match the account number. Please try again."                          # if name not matched then show this message
        else:
            response = "Sorry, the account number does not exits in our records."                                   # if account not matched then show this message

        dispatcher.utter_message(text=response)
        return []


# class for check transaction history of account

class ActionCheckTransactionHistory(Action):
    def name(self):
        return "check_transaction_history"

    def run(self, dispatcher, tracker, domain):
        account_number = tracker.get_slot("account_number")
        name = tracker.get_slot("name")
        user_db = {
            "12345": {"name": "mukesh jayswal", "transaction": ["transaction 1", "transaction 2"]},
            "54321": {"name": "ram thapa", "transaction": ["transaction 3", "transaction 4"]},
        }

        if account_number in user_db:
            user_info = user_db[account_number]
            if name == user_info["name"]:
                transactions = ", ", join(user_info["transactions"])
                response = (
                    f"Dear {name}, your account number {account_number} has the following transactions: {transactions}"
                )
            else:
                response = "The name does not match the account number. please try again."
        else:
            response = "Sorry, the account number does not exits in our records."

        dispatcher.utter_message(text=response)
        return []
