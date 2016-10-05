from .models import *


def update_profile():
    accounts = Account.objects.all()
    count = 0
    for account in accounts:
        try:
            account.profile
        except Profile.DoesNotExist:
            Profile.objects.create(account=account)
            count += 1
    return (count)
