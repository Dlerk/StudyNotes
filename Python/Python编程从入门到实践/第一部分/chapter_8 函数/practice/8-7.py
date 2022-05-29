# practice 8-7

def make_album(singer, album_name, num=''):
    album={
        'singer': singer,
        'Name': album_name
    }
    if num != '':
        album['num'] = num
    return album

A = make_album("Hatsune Miku", "Chimera")
print(A)
B = make_album("洛天依", "与光同尘", 8)
print(B)