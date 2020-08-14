class CoffeeMachine:
    def __init__(self):
        self.water = int(400)
        self.milk = int(540)
        self.beans = int(120)
        self.cups = int(9)
        self.money = int(550)


    def take(self):
        print('I gave you ' + str(self.money))
        self.money = 0
        print(self.water)
    def buy(self, choice):
        if choice == '1':
            if self.water >= 250 and self.beans >= 16 and self.cups > 0:
                print('I have enough resources, making you have coffee')
                self.water -= 250
                self.beans  -= 16
                self.money += 4
                self.cups -= 1
            else:
                if self.water < 250:
                    print('Sorry, not enough water!')
                if self.beans < 16:
                    print('Sorry, not enough coffee beans!')
                elif self.cups <= 0:
                    print('Sorry, not enough cups')
        if choice == '2':
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups > 0:
                print('I have enough resources, making you have coffee')
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
            else:
                if self.water < 350:
                    print('Sorry, not enough water!')
                elif self.milk < 75:
                    print('Sorry, not enough milk')
                elif self.beans < 16:
                    print('Sorry, not enough coffee beans!')
                elif self.cups <= 0:
                    print('Sorry, not enough cups')
        if choice == '3':
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups > 0:
                print('I have enough resources, making you have coffee')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
            else:
                if self.water < 200:
                    print('Sorry, not enough water!')
                elif self.milk < 100:
                    print('Sorry, not enough milk')
                elif self.beans < 12:
                    print('Sorry, not enough coffee beans!')
                elif self.cups <= 0:
                    print('Sorry, not enough cups')
        else:
            return

    def fill(self):
        a_water = int(input('Write how many ml of water do you want to add:'))
        self.water = self.water +  a_water
        a_milk = int(input('Write how many ml of milk do you want to add:'))
        self.milk = self.milk + a_milk
        a_beans = int(input('Write how many grams of coffee beans do you want to add:'))
        self.beans = self.beans + a_beans
        a_cups = int(input('Write how many disposable cups of coffee do you want to add:'))
        self.cups = self.cups + a_cups

    def exit(self):
        exit()
    def remaining(self):
        print('The coffee machine has: ')
        print(str(self.water) + ' of water')
        print(str(self.milk) + ' of milk')
        print(str(self.beans) + ' of coffee beans')
        print(str(self.cups)+' of dispossable cups')
        print(str(self.money) + ' of money')
act = CoffeeMachine()
while True:
    action = input('Write action (buy, fill, take, remaining, exit):')

    if action == 'buy':
        choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        act.buy(choice)
    elif action == 'fill':
        act.fill()
    elif action == 'take':
        act.take()
    elif action == 'remaining':
        act.remaining()
    elif action == 'exit':
        act.exit()
