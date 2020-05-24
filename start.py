from rampage import Process, MatchManager
mm = MatchManager()

print("Welcome to Rampage. To target a game process, find its pid.")
print("One way of doing so is running Process.find(<name>) where <name>")
print("is partial name of your game. Numbers printed afterwards are ")
print("the process pid numbers.")
print()
print("After that, create a process obect by running")
print(">>> p = Process(pid)")
print()
print("Once the process object is created, you can read Rampage's manual by running")
print(">>> help(p)")
print()
print("You can also run help() on methods of p, e.g.")
print(">>> help(p.scan)")
print("Or on objects returned by p, or on methods of those objects")
print()
print("Finally, MatchManager object is already created for you in the `mm` variable")
print("Don't forget to call mm.join() before quitting Rampage. After that you can")
print("Exit using exit() or Ctrl-D")