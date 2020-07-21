from django.db import models


class Project(models.Model):
    WebDevelopment = 'Web Development'
    MachineLearning = 'Machine Learning'
    CHOICES = [
        (WebDevelopment, 'Web Development'),
        (MachineLearning, 'Machine Learning'),
    ]
    tag = models.CharField(
        max_length=20,
        choices=CHOICES,
        default=WebDevelopment,
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    technologies = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    cover_image = models.ImageField(upload_to='portfolio/image/', blank=True)
    github = models.URLField(blank=True)
    def __str__(self):
        return self.title

class Image(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    img1 = models.ImageField(upload_to='portfolio/image/', blank=True)
    img2 = models.ImageField(upload_to='portfolio/image/', blank=True)
    img3 = models.ImageField(upload_to='portfolio/image/', blank=True)
    img4 = models.ImageField(upload_to='portfolio/image/', blank=True)
    img5 = models.ImageField(upload_to='portfolio/image/', blank=True)
    img6 = models.ImageField(upload_to='portfolio/image/', blank=True)
    img7 = models.ImageField(upload_to='portfolio/image/', blank=True)


class Certification(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    issue_date = models.DateField()
    certificate_id = models.CharField(max_length=50)


class Profile(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dob = models.DateField()
    resume = models.FileField(upload_to='portfolio/resume', blank=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    

