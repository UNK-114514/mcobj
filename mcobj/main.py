from mcobj.command.commands import CMD_MGR, initialization

initialization()

while True:
    command = input("")

    if command == "/exit":
        break
    elif len(command) > 0 and command[0] == "/":
        try:
            CMD_MGR.run(command[1:])
        except Exception as e:
            print(e)

    print()
