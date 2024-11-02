from django.db import models

from root.utils import BaseModel
from users.models import User
# Create your models here.

class Poll(BaseModel):
    question = models.CharField(max_length=100, unique = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_created")
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.question}"
    


class Choice(BaseModel):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.choice_text}"
    


class Vote(BaseModel):
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name = "user_polls")
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name  = "user_voted_by")


    class Meta:
        unique_together = ("poll", "voted_by")

    def __str__(self):
        return f"{self.choice}"