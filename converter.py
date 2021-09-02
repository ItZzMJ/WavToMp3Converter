import os
from pydub import AudioSegment


dest_path = "/home/jannik/Musik/NeueTracks"
wav_path = os.path.join(dest_path, "wavs")

toConvert = os.listdir(wav_path)

for file_name in toConvert:
    print("Loading " + file_name)
    file_path = os.path.join(wav_path, file_name)

    song = AudioSegment.from_wav(file_path)

    dest_file = os.path.join(dest_path, file_name.replace(".wav", ".mp3"))
    print("Exporting " + dest_file)
    if " - " in file_name:
        songData = file_name.split(" - ")
        trackname = songData[0]
        artist = songData[1]
        song.export(dest_file, format="mp3", bitrate="320k", tags={"artist": artist, "title": trackname})

    else:
        song.export(dest_file, format="mp3", bitrate="320k")

print("Finished!")
