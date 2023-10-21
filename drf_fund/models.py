from django.db import models


class Profile(models.Model):
    tg_id = models.IntegerField(null=False, unique=True)
    tg_name = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.pk} {self.name} {self.surname}'


class Group(models.Model):
    group_tg = models.IntegerField(null=False, unique=True)
    group_name = models.CharField(max_length=255, null=False)
    week_limit = models.FloatField(default=0)
    leak = models.FloatField(default=0)

    def __str__(self):
        return f'id:{self.pk} {self.group_name}'


class Transaction(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    amount = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now=True)

    def formatted_date(self):
        return self.transaction_date.strftime('%d.%m.%Y %H:%M')

    def __str__(self):
        return f'id: {self.pk} by: {self.profile_id.name} {self.profile_id.surname} date: {self.formatted_date()} ' \
               f'amount: {self.amount}'


class ProfileGroup(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'id: {self.pk} : {self.profile_id.name} {self.profile_id.surname} - {self.group_id.group_name}'


class RegisteredGroup(models.Model):
    group_tg_id = models.IntegerField(null=False, unique=True)
    is_active = models.BooleanField(default=False)
    comment = models.TextField(null=True)

    def __str__(self):
        return f'id:{self.pk} tg_id:{self.group_tg_id} Comment: {self.comment}'
