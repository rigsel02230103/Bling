from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

#visit function
NoOfVisits = int(input("Enter the number of url history: "))
print("Enter URLS to visit:")
for i in range(NoOfVisits):
    url = input("URL: ")
    print(f"Visiting {url}")
    backward_history.put(current_page)
    current_page = url

#Display current page
print(f"Current page: {current_page}")

#Go back
while input("Do you want to go back? (yes/no): ").lower() == 'yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get
        print(f"Going back to {current_page}")
    else: 
        print("No previous page available")
