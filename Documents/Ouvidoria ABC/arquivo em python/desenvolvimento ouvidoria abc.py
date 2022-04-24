#abc ombudsman menu
options = 0
all_manifestations = ["001#Weslley#Complaints#no water in the drinking fountains", "002#Felipe#Suggestion#add more computers in the class rom"]
list_suggestion = ["002#Felipe#Suggestion#add more computers in the class rom"]
list_complaints = ["001#Weslley#Complaints#no water in the drinking fountains"]
list_praise = []
broken_manifestation = []
blue = '\033[34m'
red = '\033[31m'
normal = '\033[m'
type = 0

print(f"{blue}Hello, my name is Tron. I am your virtual assistant.{normal}")
while options != 7:
  print(f"{blue}What do you want? {normal}")
  print()
  print("1) List all manifestations: \n2) List all suggestions: \n3) List all complaints: \n4) List all praise: \n5) Create a new manifestation: \n6) Search protocol by number: \n7) Leave")
  options = int(input("Enter the number you want: "))
  print()

  while options < 1 or options > 7:
    print(f"{red}Number invalid. Please enter a new number between 1 and 7{normal}")
    print()
    break

  if options == 1:
    print(f"{blue}List of all manifestations:{normal}")
    for manifestation in all_manifestations:
      list_exit = manifestation.replace("#", " - ")
      print(list_exit)
    print()

  if options == 2:
    print(f"{blue}List of all suggestions:{normal}")
    for suggestion in list_suggestion:
      list_exit = suggestion.replace("#", " - ")
      print(list_exit)
    print()

  if options == 3:
    print(f"{blue}List of all complaints:{normal}")
    for complaint in list_complaints:
      list_exit = complaint.replace("#", " - ")
      print(list_exit)
    print()

  if options == 4:
    print(f"{blue}List of all praise:{normal}")
    if not list_praise:
      print("Empty list")
    else:
      for praise in list_praise:
        list_exit = praise.replace("#", " - ")
        print(list_exit)
    print()

  if options == 5:
    protocol = len(all_manifestations) + 1
    replace_protocol = str(protocol).zfill(3)
    # I put 2 zeros on the left in the variable.
    print(f"{blue}To make a new manifestation I need some information{normal}")
    name = input("Enter your name: ").capitalize()
    type = int(input("1) For complaints \n2) For suggestions \n3) For praise \nEnter the type: "))

    while type < 1 or type > 3:
      print (f"{red}Number invalid. Please enter one new number between 1 and 3.{normal}")
      type = int(input("1) For complaints \n2) For suggestions \n3) For praise \nEnter the type: "))
    if type == 1:
      type = "Complaints"
    elif type == 2:
      type = "Suggestions"
    elif type == 3:
      type = "Praise"
    # I converted the answer to string
    description = input("Enter description: ").capitalize()
    protocol_complet = (f"{replace_protocol}#{name}#{type}#{description}")
    # I converted all variables in one string.
    print(f"{blue}The number of your protocol is: {str(protocol).zfill(3)} {normal}")
    broken_manifestation = protocol_complet.split("#")
    print()
    # And now I will put the protocol in the list it belongs to.
    if type == "Complaints":
      all_manifestations.append(protocol_complet)
      list_complaints.append(protocol_complet)
    elif type == "Suggestions":
      all_manifestations.append(protocol_complet)
      list_suggestion.append(protocol_complet)
    elif type == "Praise":
      all_manifestations.append(protocol_complet)
      list_praise.append(protocol_complet)
      protocol += 1
    print(f"{blue}request accepted!!{normal} ")

  if options == 6:
    number_protocol = int(input("Enter the your number of procol: "))
    # now I'm checking if there is a protocol with that number.
    if (number_protocol > len(all_manifestations)) or (number_protocol < 1):
      print(f"{red}There is no protocol with this number{normal}")
    else:
      string_protocol = str(number_protocol).zfill(3)
      search_protocol = all_manifestations[number_protocol - 1]
      broken_manifestation = search_protocol.split("#")
      print(f"{blue}Details of protocol {normal}")
      print(f"Number of protocol: {broken_manifestation[0]}")
      print(f"Name: {broken_manifestation[1]}")
      print(f"Type: {broken_manifestation[2]}")
      print(f"Description: {broken_manifestation[3]}")
      print()
print(f"{blue}Thanks for visiting our website! {normal} ")