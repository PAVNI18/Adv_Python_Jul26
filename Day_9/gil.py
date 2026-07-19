# Global Interpreter Lock (GIL)
# GIL is a mutex, prevents multiple native threads from executing python bytecode
# GIL like a single key to a room, only one person can be inside the room at 
# any given point of timw
# GIL like a single key to a room, only one person can be inside the room at any given point of time
import time
from threading import Thread
