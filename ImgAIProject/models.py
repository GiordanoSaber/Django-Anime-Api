from django.db import models

class AnimeImage(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='anime_imagenes/')
    generated_image = models.ImageField(upload_to='anime_imagenes/generated/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AnimeImage {self.name}"



class NotesAnime(models.Model):
    note_name = models.CharField(max_length=255, blank=True)
    text_note = models.TextField()
    date_note = models.DateField(null=True)
    
    def __str__(self):
        return self.note_name
    