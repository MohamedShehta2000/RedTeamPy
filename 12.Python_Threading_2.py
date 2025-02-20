
import threading 
import time
# Function that greets the user by name
def hi(name):
    print(f"welcome mr {name}")

# Ask for the user's name
yourname = input("Enter your name: ")

# Create a thread to run the hi() function with the user's name as an argument
thread1 = threading.Thread(target=hi, args=(yourname,))

# Start the thread
thread1.start()

# Wait for the thread to finish before continuing
thread1.join()


#from threading import thread
import threading

# This function loops from 0 to 9 and prints each number
def loop1():
    for i in range(10):
        print(i)

# Main block to create and manage threads
if __name__ == "__main__":
    threads = []         # List to store threads
    threads_num = 10     # Number of threads to create

    # Create and start threads
    for i in range(threads_num):
        t = threading.Thread(target=loop1)  # Create a thread to run loop1()
        threads.append(t)                   # Add thread to the list
        t.start()                           # Start the thread

    # Wait for all threads to complete
    for t in threads:
        t.join()  # Ensures main program waits for all threads to finish

        t.join()