
#Generate Graphs
genre_song_counts = [ (genre, len(db.get('genre',genre))) for genre in genres]
genre_sorted_by_count = sorted(l, key = lambda a: -a[1])
CairoPlot.dot_line_plot('dot-plot.svg',data,1000,600,h_labels=labels,grid=True)

song_list_by_genre = [ (genre, Playlist(db.get('genre', genre)).duration() ) for
        genre in genres ]
data_sorted = sorted(song_list_by_genre ,key = lambda a: -a[1])

data = [ x[1] for x in data_sorted ]
labels = [ x[0] for x in data_sorted ]

CairoPlot.dot_line_plot('genre-duration-dot-plot.svg',data,1000,600,h_labels=labels,grid=True)

