"""
*TL;DR
Separates data in GUIs from the ways it is presented, and accepted.
"""

import model
import view
import controller


def main():
    mod = model.ProductModel()
    viw = view.ConsoleView()
    contr = controller.Controller(mod, viw)

    contr.show_item_information("cheese")
    contr.show_item_information("eggs")
    contr.show_item_information("eggs")
    contr.show_item_information("arepas")


if __name__ == "__main__":
    main()
