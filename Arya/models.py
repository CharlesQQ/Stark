from django.db import models

# Create your models here.

class Host(models.Model):
    hostname=models.CharField(max_length=123,unique=True)
    key = models.TextField()
    status_choices=((0,'Waiting Approval'),
                    (1,'Accepted'),
                    (2,'Rejected'))

    os_type_choice=(
        ('redhat','Redhat\Centos'),
        ('ubuntu','Ubuntu'),
        ('suse','Suse'),
        ('windows','Windows'),
    )

    os_type = models.CharField(choices=os_type_choice,max_length=64,default='redhat')
    status=models.SmallIntegerField(choices=status_choices,default=0)

    def __str__(self):
        return self.hostname

class HostGroup(models.Model):
    name = models.CharField(max_length=64,unique=64)
    hosts=models.ManyToManyField(Host,blank=True)

    def __str__(self):
        return self.name
