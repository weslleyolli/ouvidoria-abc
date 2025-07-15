class List:
  all_manifestations = ["001#Weslley#Complaints#no water in the drinking fountains", "002#Felipe#Suggestion#add more computers in the class rom"]
  list_suggestion = ["002#Felipe#Suggestion#add more computers in the class rom"]
  list_complaints = ["001#Weslley#Complaints#no water in the drinking fountains"]
  list_praise = []
  broken_manifestation = []

class Colors:
  blue = '\033[34m'
  red = '\033[31m'
  normal = '\033[m'

class Functions:
  options = 0
  type = 0

def printList(list):
  for item in list:
    list_exit = item.replace("#", " - ")
    print(list_exit)