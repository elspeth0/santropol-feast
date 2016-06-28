import aldjemy.core as ac
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import func, or_, and_

import datetime
import io
import sys

from meal.models import Component, Restricted_item, Ingredient
from meal.models import Component_ingredient, Incompatibility
from meal.models import Menu, Menu_component
from member.models import Member, Client, Contact, Address, Note, Referencing
from member.models import Route, Note, Option, Client_option, Restriction
from member.models import Client_avoid_ingredient, Client_avoid_component
from notification.models import Notification
from order.models import Order, Order_item


def print_all_cols(q):
    pass
    # print("\n---------------------------------------------------------\n", q)
    # for row in q:
    #     d = row.__dict__
    #     # filter out SQLAlchemy "internal" columns to get "result" dict
    #     fd = { k:v for (k,v) in d.items()
    #            if not str(k).startswith("_") }
    #     print("Row ", fd)


def print_rows(q, heading=""):
    pass
    # print("\n-----------------------------------------------------\n",
    #       # q, "\n",
    #       heading)
    # for row in q.all():
    #     print(row)


def run():
    print("START dataload")
    engine = ac.get_engine()
    Session = sessionmaker(bind=engine)
    db = Session()

    # meal app
    Ingredient.objects.all().delete()
    Component.objects.all().delete()
    Component_ingredient.objects.all().delete()
    Restricted_item.objects.all().delete()
    Incompatibility.objects.all().delete()
    Menu.objects.all().delete()
    Menu_component.objects.all().delete()

    # member app
    Member.objects.all().delete()
    Address.objects.all().delete()
    Contact.objects.all().delete()
    Client.objects.all().delete()
    Referencing.objects.all().delete()
    Note.objects.all().delete()
    Option.objects.all().delete()
    Client_option.objects.all().delete()
    Restriction.objects.all().delete()
    Client_avoid_ingredient.objects.all().delete()
    Client_avoid_component.objects.all().delete()
    Route.objects.all().delete()

    # notification app
    Notification.objects.all().delete()

    # order app
    Order.objects.all().delete()
    Order_item.objects.all().delete()

    exec(open('datafull.py').read())

run()
print("END dataload")
