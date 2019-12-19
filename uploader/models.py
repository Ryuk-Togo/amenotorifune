from django.db import models

# Create your models here.
class UploadFile(models.Model):
    """アップロードされたファイルを表すモデル"""
    file = models.FileField('画像ファイル')  # これが重要

    def __str__(self):
        """ファイルのURLを返す"""
        return self.file.url
