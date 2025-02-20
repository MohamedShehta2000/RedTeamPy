# Code for Python Threading

# Example 1
import threading

# This function prints "Hello World"
def hi():
    print("Hello World")

# Create two threads that will both run the hi() function
thread1 = threading.Thread(target=hi)
thread2 = threading.Thread(target=hi)

# Start both threads
thread1.start()
thread2.start()

# Both threads will print "Hello World" concurrently


# Example 2
import threading

# This function prints "Hello World" five times
def hi():
    for i in range(5):
        print("Hello World")

# Create a thread to run the hi() function
thread1 = threading.Thread(target=hi)

# Start the thread
thread1.start()

# Wait for thread1 to finish before moving on
thread1.join()

# Using join() ensures the main program waits for the thread to complete



# Example 3
import threading
import time

# This function prints the current time five times with an index
def hi():
    for i in range(5):
        # Print the index and the current time
        print(str(i) + " => " + time.ctime())

# Create a thread to run the hi() function
thread1 = threading.Thread(target=hi)

# Start the thread
thread1.start()

# Wait for thread1 to finish before continuing
thread1.join()

# Using join() ensures that all output is printed before the program exits
