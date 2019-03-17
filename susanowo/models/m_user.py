from django.db import models

class M_User(models.Model):
    user_id = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    create_date = models.TimeField()
    create_pg_id = models.CharField(max_length=30)
    create_user_id = models.CharField(max_length=6)
    update_date = models.TimeField()
    update_pg_id = models.CharField(max_length=30)
    update_user_id = models.CharField(max_length=6)
