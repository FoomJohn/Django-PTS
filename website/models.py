from django.db import models
from django.contrib.auth.models import User 

# models are the database stuff for django



class Candidate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='website/images/', default='static/images/placeholder_image.jpg')

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    

class Status(models.Model):
    judge = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    

class ScoreEverything(models.Model):

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    judge = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    pn_performance = models.IntegerField()
    pn_elegance = models.IntegerField()
    pn_beauty = models.IntegerField()
    pn_audience = models.IntegerField()
    sw_poise = models.IntegerField()
    sw_body = models.IntegerField()
    sw_beauty = models.IntegerField()
    sw_audience = models.IntegerField()
    eg_poise = models.IntegerField()
    eg_elegance = models.IntegerField()
    eg_beauty = models.IntegerField()
    eg_audience = models.IntegerField()
    fq_wisdom = models.IntegerField()
    fq_charisma = models.IntegerField()
    fq_intelligence = models.IntegerField()
    fq_persuasion = models.IntegerField()
    pn_total = models.IntegerField(default=0, blank=False)
    sw_total = models.IntegerField(default=0, blank=False)
    eg_total = models.IntegerField(default=0, blank=False)
    fq_total = models.IntegerField(default=0, blank=False)
    t_avg = models.IntegerField(default=0, blank=False)

class ScoreCard(models.Model):

    #basically what we want to print
    #also err... what we show for scores scores final??

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    pn_all_total = models.IntegerField(default=0, blank=False)
    sw_all_total = models.IntegerField(default=0, blank=False)
    eg_all_total = models.IntegerField(default=0, blank=False)
    fq_all_total = models.IntegerField(default=0, blank=False)
    t_all_avg = models.IntegerField(default=0, blank=False)
    ranking = models.IntegerField(default=0)

