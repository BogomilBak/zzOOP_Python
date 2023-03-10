class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.remaining_memory = self.memory
        self.apps = []
        self.is_on = False

    def install(self, app, app_memory):
        if self.remaining_memory < app_memory:
            return f"Not enough memory to install {app}"
        elif not self.is_on:
            return f"Turn on your phone to install {app}"
        self.remaining_memory -= app_memory
        self.apps.append(app)
        return f"Installing {app}"

    def power(self):
        self.is_on = not self.is_on

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.remaining_memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
