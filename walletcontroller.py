from tronpy import Tron
import json
from tronpy.keys import PrivateKey
import os
from tronpy import Tron
from tronpy.providers import HTTPProvider


# client = Tron()
#start tron import as a variable
#input your api key here, https://www.trongrid.io/
provider = HTTPProvider(api_key="86f36a9d-c8e8-41cb-a8aa-3bbe7b66d0a5")
#if it returns ": Exceed the user daily usage (100000), the maximum query frequency is 1 time per second"
# while querying acount balance, please get your api key  https://www.trongrid.io/
# Pass the provider to the Tron object
client = Tron(provider=provider)

def retrive_user_credential():
    if os.path.isfile("wallet-crendetials.json"):
        with open('wallet-crendetials.json', 'r') as file:
         data = json.load(file)
    else:
        print("Please Create a new wallet")
        actdosmth()
    return data;

def receive_trx():
    print("Send your TRX to this address: "+ retrive_user_credential()['base58check_address'])

def get_trx_balance():
   client = Tron()

   try:
      balance = client.get_account_balance(retrive_user_credential()['base58check_address'])
      print(balance + "TRX");
   except Exception as e:
       print("Wallet Not Activated!")


def create_wallet():
    if os.path.isfile("wallet-crendetials.json"):
        print("Wallet Already Exists")
    else:
        wallet = client.generate_address()
        with open('wallet-crendetials.json', 'w') as fp:
            json.dump(wallet, fp)

        print("Wallet address: ", wallet['base58check_address'])
        print("Private Key: ", wallet['private_key'])

        print(wallet);


def send_tron():
    recipient_address = input('Input RECIPIENT_ADDRESS : ')
    amount = input("Amount you wish to send : ")
    send_tron(recipient_address, int(amount))
    try:
        priv_key = PrivateKey(bytes.fromhex(retrive_user_credential()['private_key']))
        txn = (
            client.trx.transfer(recipient_address, amount, retrive_user_credential()['public_key'])
            .memo("Transaction Description")
            .build()
            .inspect()
            .sign(priv_key)
            .broadcast()
        )
        print(txn.txid)
        print("TRX Sucessfully Sent")
    except Exception as ex:
        print("Exception: ", ex)



print("Hello, welcome to your Commandline Python Wallet Built by JerryDev\n")
print("You can request any action by entering a number.\n")
def actdosmth():
    action = input(" 0. CREATE New Wallet\n 1. Check Balance\n 2. Receive TRX\n 3. Send TRX\n 4. See Wallet Address \n 5. See your wallet's public/private keys\n 6. Exit the program\n")

    if(int(action) == 0):
        create_wallet();
        pr = input("do you want to perform another transaction ? yes/no (y/n) : ")
        if (pr == 'y' or pr == 'Y' or pr == 'yes' or pr == 'Yes' or pr == 'YES'):
            actdosmth();
        else:
            print("Thanks for Using this program. Don't forget to give me a STAR!")
    elif(int(action) == 1):
        get_trx_balance();
        pr = input("do you want to perform another transaction ? yes/no (y/n) : ")
        if (pr == 'y' or pr == 'Y' or pr == 'yes' or pr == 'Yes' or pr == 'YES'):
            actdosmth();
        else:
            print("Thanks for Using this program. Don't forget to give me a STAR!")
    elif(int(action) == 2):
        receive_trx();
        pr = input("do you want to perform another transaction ? yes/no (y/n) : ")
        if (pr == 'y' or pr == 'Y' or pr == 'yes' or pr == 'Yes' or pr == 'YES'):
            actdosmth();
        else:
            print("Thanks for Using this program. Don't forget to give me a STAR!")
    elif(int(action) == 3):
        send_tron();
        pr = input("do you want to perform another transaction ? yes/no (y/n) : ")
        if (pr == 'y' or pr == 'Y' or pr == 'yes' or pr == 'Yes' or pr == 'YES'):
            actdosmth();
        else:
            print("Thanks for Using this program. Don't forget to give me a STAR!")
    elif(int(action) == 4):
        print("this is your wallet address " + retrive_user_credential()['base58check_address']);
        pr = input("do you want to perform another transaction ? yes/no (y/n) : ")
        if (pr == 'y' or pr == 'Y' or pr == 'yes' or pr == 'Yes' or pr == 'YES'):
            actdosmth();
        else:
            print("Thanks for Using this program. Don't forget to give me a STAR!")
    elif(int(action) == 5):
        print("Public key: ", retrive_user_credential()['public_key'])
        print("Private Key: ", retrive_user_credential()['private_key'])
        pr = input("do you want to perform another transaction ? yes/no (y/n) : ")
        if (pr == 'y' or pr == 'Y' or pr == 'yes' or pr == 'Yes' or pr == 'YES'):
            actdosmth();
        else:
            print("Thanks for Using this program. Don't forget to give me a STAR!")
    elif(int(action) == 6):
        print("Thanks for Using this program. Don't forget to give me a STAR!");
    else:
        print("Invalid Input !!!")
        actdosmth();

actdosmth();