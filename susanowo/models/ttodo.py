from django.db import models

class TTodo(models.Model):
    # todo_id = models.AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    title = models.CharField('タイトル',max_length=30)
    discription = models.CharField('タスクの詳細',max_length=200)
    should_action = models.BooleanField('行動を起こす必要があるか？')
    action_selection = models.CharField(max_length=1,null=True)
    single_action = models.BooleanField('アクションは１つ？')
    can_do_tow_minite = models.BooleanField('２分以内で終わる？')
    should_myself = models.BooleanField('自分でやるべき')
    should_do_than_2min = models.BooleanField('特定の日にやるべき？')
    user_id = models.CharField(max_length=6)
    category = models.CharField(max_length=6)
    create_date = models.TimeField()
    create_pg_id = models.CharField(max_length=30)
    create_user_id = models.CharField(max_length=6)
    update_date = models.TimeField()
    update_pg_id = models.CharField(max_length=30)
    update_user_id = models.CharField(max_length=6)
