import sys

#empty list 

tasks=[]


# Welcoming users 

def greet_user():
    print('Hello welcome to Get Things Done')

#Display menu options

def options():
    try:
      menu= "\nWould you like to add, view, or delete task?'\nPress'v' to view \nPress 'a' to add \nPress 'd to delete \nPress 'q' to quit program \n"
      press= input(menu)
      if press == 'q':
            print("\nThank you for choosing Get Things Done! \nBy for now.\n")
            sys.exit()
      elif press== ('a'):
           todo()    
      elif press=='v':
           view(tasks)
      elif press == 'd':
           remove_task()
    except TypeError: 
        print('\nCharacter invalid\n')
        options()
    
#To enter task
def todo():
    while True:
      task = input("\nEnter Task (or enter 'done' to stop adding task): \n")
      if task == 'done':
          print("\nReturning to main menu\n")
          options()
          break
      tasks.append(task)

# To view task 
def view(tasks):

    if not tasks:
     print('\nThere are no task to view\n')
    else:
     print(tasks)
    
    options()

#To delete task

def remove_task():
    task = input("Enter the task to be removed: ")
    if task in tasks:
        tasks.remove(task)
    if not task:
        print('\nThere are no task to delete\n')
    
    options()    
    
#Program Start

greet_user()
options()