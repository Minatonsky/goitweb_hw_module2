from Bot import AddBot, ExitBot, SearchBot, EditBot, RemoveBot, SaveBot, LoadBot, CongratulateBot, ViewBot

choice = {
    'add': AddBot(),
    'search': SearchBot(),
    'exit': ExitBot(),
    'edit': EditBot(),
    'remove': RemoveBot(),
    'save': SaveBot(),
    'load': LoadBot(),
    'congratulate': CongratulateBot(),
    'view': ViewBot()
}


class BotFactory:
    @staticmethod
    def create(action):
        if action in choice:
            return choice[action]
        else:
            return None


if __name__ == "__main__":
    while True:
        action = input("Choose an action: ")
        bot = BotFactory.create(action)
        if bot:
            bot.handle()
        else:
            print(f"No bot found for action: {action}")
