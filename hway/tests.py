from django.test import TestCase
import models
from datetime import datetime
from django.db import transaction

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

django.setup()


def create_chargebytype():
    create_chargebytype()
