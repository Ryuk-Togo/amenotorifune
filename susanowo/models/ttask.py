from django.db import models

class TTask(models.Model):
    # task_id = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    todo_id = models.CharField(max_length=30)
    task_date_time = models.DateTimeField()
    task_discription = models.TextField()
    create_date = models.TimeField()
    create_pg_id = models.CharField(max_length=30)
    create_user_id = models.CharField(max_length=6)
    update_date = models.TimeField()
    update_pg_id = models.CharField(max_length=30)
    update_user_id = models.CharField(max_length=6)
