# Create your views here.
from django.views.generic.list_detail import object_list
from show.models import *
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template import loader
from show.models import *
from RhythmDB import *
from django.views.decorators.cache import cache_page
import cPickle as pickle
from django.contrib.auth.decorators import login_required
from rb.settings import *
import os
import socket
import paramiko

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

@login_required
def player(request):
    ip = socket.gethostbyaddr(REMOTE_HOST)[-1][0]
    ip = socket.gethostbyaddr('secpewt.local')[-1][0]
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(
                paramiko.AutoAddPolicy())
    ssh.connect(ip,
                key_filename=IDENTITY_FILE,
                username=USER,
                password='')
    a,b,c = ssh.exec_command(
        'source init_dbus.sh 2&>/dev/null; rhythmbox-client --print-playing')

    t = loader.get_template('rb/player.html')
    c  = RequestContext(request,
            {
                'current_track': b.read().strip(),
            })
    return HttpResponse(t.render(c))
