# TH3D-Unified-web-GUI

django-admin startproject <project-name>
python manage.py runserver
python manage.py startapp <app-name>
sudo python3 manage.py runserver 0.0.0.0:80

python manage.py makemigrations music
python manage.py sqlmigrate music 0001
python manage.py runserver

python manage.py shell

## Database

from music.models import Album,Song
Album.objects.all()
a = Album(artist="yolo",album_title="wtf",gerne="nah",album_logo="https://github.com/ChipTechno/TH3D-Marlin2-EZBoard-cli-compiler/blob/master//img/img-00.png")
a.save()
a.artist
a.id OR a.pk
>>> b = Album()
>>> b.artist = "nanashi"
>>> b.album_title = "nai"
>>> b.gerne="rock"
>>> b.gerne="punk"
>>> b.album_logo="https://raw.githubusercontent.com/ChipTechno/TH3D-Marlin2-EZBoard-cli-compiler/master/img/img-01.png"
Album.objects.filter(id=1)
>>> Album.objects.filter(artist__startswith="n")
song = Song()
song = Song()
album1.song_set.all()
album1.song_set.create(song_title="another meaningless title",file_type="mp100")
song = album1.song_set.create(song_title="python song",file_type="mp100")
album1.song_set.count()


## admin

python manage.py createsuperuser