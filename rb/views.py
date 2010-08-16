# Create your views here.
from django.views.generic.list_detail import object_list
from show.models import *
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from show.models import *
from RhythmDB import *
from django.views.decorators.cache import cache_page
import cPickle as pickle
from django.contrib.auth.decorators import login_required
from rb.settings import *
import os


f = open(DB_FILE)

db = pickle.load(f)
@cache_page(60 * 15)
def genres(request):
    genres = db.genres()
    counts_by_genre = [ (genre,len(Playlist(db.get('genre',genre)))) for genre in genres ]
    counts_by_genre = sorted(counts_by_genre,key=lambda a: -a[1])

    context= {
        'genres': counts_by_genre,
            }

    return object_list(request,
            queryset=Show.objects.none(),template_name='rb/genres.html',
            extra_context=context)

@cache_page(60 * 15)
def artists(request):
    genres = db.artists()
    counts_by_genre = [ (genre,len(Playlist(db.get('artist',genre)))) for genre in genres ]
    counts_by_genre = sorted(counts_by_genre,key=lambda a: -a[1])

    context= {
        'artists': counts_by_genre,
            }

    return object_list(request,
            queryset=Show.objects.none(),template_name='rb/artists.html',
            extra_context=context)

@cache_page(60 * 15)
def artists_detail(request, slug):
    artist_songs = db.get('artist', slug)

    context= {
        'artist_songs': artist_songs,
        'slug': slug
            }

    return object_list(request,
            queryset=Show.objects.none(),template_name='rb/artists_detail.html',
            extra_context=context)

@cache_page(60 * 15)
def albums(request):
    albums = set([song['album'] for song in db ])

    context= {
        'albums': albums,
            }

    return object_list(request,
            queryset=Show.objects.none(),template_name='rb/albums.html',
            extra_context=context)

@cache_page(60 * 15)
def album_detail(request, slug):
    album = db.get('album', slug)

    context= {
        'album': album,
        'slug': slug
            }

    return object_list(request,
            queryset=Show.objects.none(),template_name='rb/album_detail.html',
            extra_context=context)

@login_required
def play(request):
    os.system("ssh -i %s -p %s %s@%s 'source init_dbus.sh; rhythmbox-client --play'" % (IDENTITY_FILE, PORT, USER, REMOTE_HOST))
    return HttpResponseRedirect('/rb/player/')

@login_required
def pause(request):
    os.system("ssh -i %s -p %s %s@%s 'source init_dbus.sh; rhythmbox-client --pause'" % (IDENTITY_FILE, PORT, USER, REMOTE_HOST))
    return HttpResponseRedirect('/rb/player/')

@login_required
def next(request):
    os.system("ssh -i %s -p %s %s@%s 'source init_dbus.sh; rhythmbox-client --next'" % (IDENTITY_FILE, PORT, USER, REMOTE_HOST))
    return HttpResponseRedirect('/rb/player/')

