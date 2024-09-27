from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)  # e.g., Beginner, Intermediate, Expert
    icon = models.URLField(blank=True, null=True)  # Optional URL to an icon/image

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.ManyToManyField(Skill, related_name='projects')  # Many-to-many relationship
    url = models.URLField(blank=True, null=True)  # Live project link
    repository_url = models.URLField(blank=True, null=True)  # GitHub repo link
    image = models.URLField(blank=True, null=True)  # URL to a project image
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='educations')

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # End date can be null if currently employed
    responsibilities = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences')

    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"