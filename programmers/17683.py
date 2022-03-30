
from datetime import datetime

def replace_sharp(string):
    string = string.replace('C#', 'c')
    string = string.replace('D#', 'd')
    string = string.replace('F#', 'f')
    string = string.replace('G#', 'g')
    string = string.replace('A#', 'a')
    return string


def solution(m, musicinfos):
    candidate = []
    for musicinfo in musicinfos:
        start_time, end_time, title, melody = musicinfo.split(",")
        music_length = datetime.strptime(end_time, "%H:%M") - datetime.strptime(start_time, "%H:%M")
        music_length = music_length.seconds // 60
        
        melody = replace_sharp(melody)
        all_melody = ''
        while len(all_melody) < music_length:
            all_melody += melody
        all_melody = all_melody[:music_length]
        
        if replace_sharp(m) in all_melody:
            candidate.append((music_length, title))
                
    if candidate:
        _max = candidate[0]
        for c in candidate:
            if _max[0] < c[0]:
                _max = c
        
        return _max[1]
    
    return "(None)"
