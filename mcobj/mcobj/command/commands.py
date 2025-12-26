from mcobj.command.command_manager import CommandManager

CMD_MGR = CommandManager()


def initialization():
    CMD_MGR.register("debug", lambda x: print(x), True)
    CMD_MGR.register("add", lambda a, b: print(int(a) + int(b)), True)
