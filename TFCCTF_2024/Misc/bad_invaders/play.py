from ansi_escapes import ansiEscapes as ansi
import sys, tty, termios
import os
import socket
import time
import select
import threading

write = sys.stdout.write
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1.0)

GAME_STATE = "name_entry"
PLAYER_COUNT = 0
PLAYER1_POS = 0
PLAYER2_POS = 0
PLAYER1_NAME = ""
PLAYER2_NAME = ""
LAST_ERROR_TIME = 0
LAST_PING_TIME = 0
PLAYER_ID = -1

def show_game():
    if GAME_STATE == "waiting_for_players":
        show_waiting_for_players()
    elif GAME_STATE == "playing":
        show_playing()

def show_waiting_for_players():
    write(ansi.cursorTo(0,0)+ansi.eraseLines(9))
    print("Welcome to the game!")
    print("Waiting for other players to join...")
    print("Press Ctrl+C to exit")

def show_playing():
    write(ansi.cursorTo(0,0)+ansi.eraseLine)
    print(" "*PLAYER2_POS+"👾"+(" "*(40-PLAYER2_POS-1))+PLAYER2_NAME)
    write(ansi.cursorTo(0,1)+ansi.eraseLine)
    write(ansi.cursorTo(0,2)+ansi.eraseLine)
    write(ansi.cursorTo(0,3)+ansi.eraseLine)
    write(ansi.cursorTo(0,4)+ansi.eraseLine)
    print(" "*3 + "🧱")
    write(ansi.cursorTo(0,5)+ansi.eraseLine)
    write(ansi.cursorTo(0,6)+ansi.eraseLine)
    print(" "*PLAYER1_POS+"🚀"+(" "*(40-PLAYER1_POS-1))+PLAYER1_NAME)

host = sys.argv[1]
port = int(sys.argv[2])
addr = (host, port)

s.connect(addr)

def play():
    global LAST_ERROR_TIME, PLAYER_COUNT, PLAYER1_POS, PLAYER2_POS, GAME_STATE, PLAYER1_NAME, PLAYER2_NAME, LAST_PING_TIME, PLAYER_ID

    write(ansi.eraseScreen+ansi.cursorTo(0,0)+ansi.cursorHide)

    PLAYER1_NAME = input("Enter your name: ")

    write(ansi.eraseScreen)

    s.send(f"N|{PLAYER1_NAME};".encode())

    while True:
        show_game()
        write(ansi.cursorTo(0,15))

        if time.time() - LAST_PING_TIME > 2 and PLAYER_ID != -1:
            s.send(f"{PLAYER_ID}|P;".encode())
            LAST_PING_TIME = time.time()
        
        if LAST_ERROR_TIME > 0 and time.time() - LAST_ERROR_TIME > 2:
            write(ansi.cursorTo(0,10)+ansi.eraseLine)
            LAST_ERROR_TIME = 0

        try:
            data = b""
            while True:
                new_data = s.recv(1)
                if new_data == b";":
                    break
                data += new_data
        except socket.timeout:
            continue
            
        if len(data) == 0:
            continue
        response = data.decode()

        if response[0] == "E":
            write(ansi.cursorTo(0,10)+ansi.eraseLine)
            print("Error: "+response[2:])
            LAST_ERROR_TIME = time.time()
            if response[2:] == "Invalid name":
                print("Invalild name. Please enter a different name")
                break
        elif response[0] == "J":
            parts = response.split("|")
            PLAYER_ID = int(parts[1])
        elif response[0] == "N":
            parts = response.split("|")
            PLAYER_COUNT += 1
            if PLAYER_COUNT < 2:
                GAME_STATE = "waiting_for_players"
            else:
                GAME_STATE = "playing"
            
            if PLAYER1_NAME != parts[1]:
                PLAYER2_NAME = parts[1]
                if len(parts) > 2:
                    PLAYER2_POS = int(parts[2])
        elif response[0] == "R":
            PLAYER_COUNT -= 1
            GAME_STATE = "waiting_for_players"
        elif response[0] == "S":
            write(ansi.cursorTo(0,10)+ansi.eraseScreen)
            print(response[2:])
        elif response[0] == "M":
            parts = response.split("|")
            if parts[1] == PLAYER1_NAME:
                PLAYER1_POS = int(parts[2])
            else:
                PLAYER2_POS = int(parts[2])
        elif response[0] == "F":
            GAME_STATE = "playing"
            write(ansi.cursorTo(0,10)+ansi.eraseScreen)
            print("Game starting soon. You can move until then using the keys A and D")
        elif response[0] == "G":
            write(ansi.cursorTo(0,10)+ansi.eraseScreen)
            print("Game started. You can shoot using the key S")

def get_input():
    while True:
        if GAME_STATE != "playing":
            time.sleep(0.1)
            continue

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setraw(sys.stdin.fileno())

        ch = sys.stdin.read(1)

        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        
        if ch == "q":
            exit()
        elif ch == "a":
            s.send(f"{PLAYER_ID}|M|0;".encode())
        elif ch == "d":
            s.send(f"{PLAYER_ID}|M|1;".encode())
        elif ch == "s":
            s.send(f"{PLAYER_ID}|S;".encode())
            write(ansi.cursorTo(PLAYER1_POS,5)+ansi.eraseScreen)
            print("🔥")


threading.Thread(target=get_input).start()

play()