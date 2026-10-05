import os
import sys

def quit_app():
    print("Exiting...\n")
    raise SystemExit(0)

def undo_command():
    print("**Undo**")

def new_command():
    print("new")

def reload_command():
    os.execv(sys.executable, [sys.executable] + sys.argv)

commands = {
    "/exit": quit_app,
    "/undo": undo_command,
    "/new": new_command,
    "/reload": reload_command,
}