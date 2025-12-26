from typing import Any


class CommandNotFoundError(Exception):
    pass


class CommandManager:
    def __init__(self):
        self.commands: list[tuple[str, Any, bool]] = []

    def register(self, command, func, arg: bool = True):
        self.commands.append((command, func, arg))

    def run(self, command: str):
        for cmd, func, arg in self.commands:
            if cmd in command:
                if arg:
                    func(*command[len(cmd) + 1:].split(" "))
                else:
                    func()
                return 0

        raise CommandNotFoundError(f"Invalid Command: {command}")
