#!/bin/sh -e

RESOLUTION=1280:720
VIDEO_CODEC=libx264
AUDIO_CODEC=aac
SAMPLE_RATE=44100

SCALE_OPTION="scale=$RESOLUTION:force_original_aspect_ratio=decrease,pad=$RESOLUTION:(ow-iw)/2:(oh-ih)/2"

reencode_demux () {
    ffmpeg -y -i "$1" -vf "$SCALE_OPTION" \
            -ar $SAMPLE_RATE \
            -c:a $AUDIO_CODEC \
            -c:v $VIDEO_CODEC \
            "$2"
}

reencode () {
    ffmpeg -y  -i "$1" -t 00:00:05.000 -ss 00:00:00.000  -vf "$SCALE_OPTION" \
            -ar $SAMPLE_RATE \
            -c:a $AUDIO_CODEC \
            -c:v $VIDEO_CODEC \
            -bsf:v h264_mp4toannexb \
            -f mpegts \
            "$2"
}


stitch_demux () {
    out="$1"; shift

    for file; do
        echo "file '$file'"
    done | ffmpeg -y -f concat -safe 0 -i - -c copy "$out"
}

stitch () {
    out="$1"; shift

    input="concat:$1"; shift
    for file; do
        input="$input|$file"
    done

    ffmpeg -y -i "$input" -c copy -bsf:a aac_adtstoasc "$out"
}


reencode Grapplers.mp4 1.ts
#reencode DressWisely.mp4 2.ts
#stitch out1.mp4 1.ts 2.ts
#stitch out2.mp4 2.ts 1.ts
