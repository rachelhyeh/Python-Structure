# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:52:14 2020

@author: rache
"""

class Artist(object):
    def __init__(self, name):
        self._name = name
        self._songs = []
        self._albums = []
        
    @property
    def name(self):
        return self._name
    
    @property
    def songs(self):
        return self._songs

    @property
    def albums(self):
        return self._albums
        
    def add_song(self, song):
        self._songs.append(song)
        
    def add_album(self, album):
        self._albums.append(album)


class Song(Artist):
    def __init__(self, title, artist, album, track_number):
        self._title = title
        self._artist = artist
        self._album = album
        self._track_number = track_number
        artist.add_song(self)
    
        
class Album(Artist):
    def __init__(self, title, artist, year):
        self._title = title
        self._artist = artist
        self._year = year
        self._tracks = []
        artist.add_album(self)
        
    def add_track(self, title, artist):
        track_number = len(self._tracks)
        song = Song(title, artist, self, track_number)
        self._tracks.append(song)
    
    @property
    def get_tracks(self):
        return self._tracks
    
        
        
class Playlist(object):
    def __init__(self, list_name):
        self._list_name = list_name
        self._songs = []
    
    def add_song(self, song):
        self._songs.append(song)
    
    def get_list(self):
        print('Playlist of %s: %s' %(self._list_name, self._songs))


def main():
    art = Artist('Rachel')
    alb = Album('First Album', art, 2020)
    print(art.albums)
    alb.add_track('Track1', art)
    alb.add_track('Track2', art)
    alb.add_track('Track3', art)
    #print(alb.get_tracks)
    
    playlist = Playlist('My favoriate songs')
    for song in alb.get_tracks:
        playlist.add_song(song)
    #playlist.get_list()   
        
if __name__ == '__main__':
    main()