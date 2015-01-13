#--source files directory
src_dir = '/myStuff/videos/musicVideos'
#--destination files directory
dst_dir = '/myStuff/videos/musicMP3'
#--ffmpeg.exe directory
exe_dir = '/myStuff/ffmpeg/bin'
#--media types to include in source
media = ['.flv', '.mp4', '.mkv']

import os as os

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

all_stuff =  os.listdir(src_dir)
for each in all_stuff:
    fq_name = '%s/%s' % (src_dir, each)
    if media.count(each[-4:]) > 0 and os.path.isfile(fq_name):
        #ffmpeg -i video.mp4 -vn -ab 256 audio.mp3
        fq_out = '%s/%s.mp3' % (dst_dir, each[:-4])
        if os.path.isfile(fq_out):
            print 'exists'
            continue
        cmd = '%s/ffmpeg.exe -i "%s" -vn -ab 320000 "%s"' % (exe_dir, fq_name, fq_out)
        print cmd
        os.system(cmd)

