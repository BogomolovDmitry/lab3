from ClientVK import ClientGetID
from ClientVK import ClientGetFriendsAges
from gist import Gist

debug = True
username = "demonBogomolov"

get_id = ClientGetID(username).execute()
friends_ages = ClientGetFriendsAges(get_id).execute()

if debug:
    print("ID: ", get_id)
    print("Ages: ", friends_ages)

mygist = Gist(friends_ages)
mygist.print_hist()