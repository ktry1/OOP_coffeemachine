from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
money_counter=MoneyMachine()
coffee_machine=CoffeeMaker()


def coffee():
    answer=input(f"What would you like? ({menu.get_items()})")
    order = menu.find_drink(answer)

    if answer=="off":
        return
    elif answer=="report":
        print(coffee_machine.report(),money_counter.report())
        return coffee()

    elif order.name is not None:

        if coffee_machine.is_resource_sufficient(order):
            if money_counter.make_payment(order.cost):
                coffee_machine.make_coffee(order)
                print(f"Thank you, here is your {order.name} ☕")
                return coffee()
            else:
                print("Sorry, not enough money inserted. Cost refunded")
        else:
                return coffee()




coffee()
