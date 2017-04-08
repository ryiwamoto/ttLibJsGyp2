{
  "variables": {
    # このタイミングでpkg-configを利用して、ライブラリの有無を確認する
    # mp3lame faac jpegあたりはどうするかね。__has_includeで確認するか・・・
    "libavcodec": "<!(pkg-config --exists libavcodec && echo yes || echo no)",
    "openh264":   "<!(pkg-config --exists openh264   && echo yes || echo no)",
    "opus":       "<!(pkg-config --exists opus       && echo yes || echo no)",
    "speex":      "<!(pkg-config --exists speex      && echo yes || echo no)",
    "theora":     "<!(pkg-config --exists theora     && echo yes || echo no)",
    "vorbis":     "<!(pkg-config --exists vorbis     && echo yes || echo no)",
    "vorbisenc":  "<!(pkg-config --exists vorbisenc  && echo yes || echo no)",
    "x264":       "<!(pkg-config --exists x264       && echo yes || echo no)",
    "x265":       "<!(pkg-config --exists x265       && echo yes || echo no)",
    "soundtouch": "<!(pkg-config --exists soundtouch && echo yes || echo no)",
    "speexdsp":   "<!(pkg-config --exists speexdsp   && echo yes || echo no)",
    "mp3lame": "yes"
  },
  "targets": [{
    "conditions":[
      [
        'libavcodec=="yes"', {
          "defines": ["__ENABLE_AVCODEC__"],
          "libraries": [
            '<!@(pkg-config --libs libavcodec)'
          ],
          "include_dirs": [
            "<!@(pkg-config --cflags-only-I libavcodec | sed -e 's/\-I//g')"
          ]
        }
      ],
      [
        'openh264=="yes"', {
          "defines": ["__ENABLE_OPENH264__"],
          "libraries": [
            '<!@(pkg-config --libs openh264)'
          ],
          "include_dirs": [
            "<!@(pkg-config --cflags-only-I openh264 | sed -e 's/\-I//g')"
          ]
        }
      ],
      [
        'mp3lame=="yes"', {
          "defines": ["<!@(node test.js)"]
        }
      ]
    ],
    "target_name": "ttLibJsGyp",
    "sources": [
      "csrc/ttLibJsGyp.cpp",
      "csrc/frame.cpp",
      "csrc/reader.cpp",
      "csrc/writer.cpp",
      "csrc/decoder.cpp",
      "csrc/decoder/avcodec.cpp",
      "csrc/encoder.cpp",
      "csrc/encoder/openh264.cpp",
      "csrc/resampler.cpp",
      "csrc/resampler/audio.cpp",

      "ttLibC/ttLibC/ttLibC.c",
      "ttLibC/ttLibC/allocator.c",
      "ttLibC/ttLibC/container/container.c",
      "ttLibC/ttLibC/container/misc2.c",
      "ttLibC/ttLibC/container/flv/flvReader.c",
      "ttLibC/ttLibC/container/flv/flvTag.c",
      "ttLibC/ttLibC/container/flv/flvWriter.c",
      "ttLibC/ttLibC/container/flv/type/audioTag.c",
      "ttLibC/ttLibC/container/flv/type/headerTag.c",
      "ttLibC/ttLibC/container/flv/type/metaTag.c",
      "ttLibC/ttLibC/container/flv/type/videoTag.c",
      "ttLibC/ttLibC/container/mkv/mkvReader.c",
      "ttLibC/ttLibC/container/mkv/mkvTag.c",
      "ttLibC/ttLibC/container/mkv/mkvWriter.c",
      "ttLibC/ttLibC/container/mkv/type/simpleBlock.c",
      "ttLibC/ttLibC/container/mp4/mp4Atom.c",
      "ttLibC/ttLibC/container/mp4/mp4Reader.c",
      "ttLibC/ttLibC/container/mp4/mp4Writer.c",
      "ttLibC/ttLibC/container/mp4/type/ctts.c",
      "ttLibC/ttLibC/container/mp4/type/elst.c",
      "ttLibC/ttLibC/container/mp4/type/stco.c",
      "ttLibC/ttLibC/container/mp4/type/stsc.c",
      "ttLibC/ttLibC/container/mp4/type/stsz.c",
      "ttLibC/ttLibC/container/mp4/type/stts.c",
      "ttLibC/ttLibC/container/mp4/type/trun.c",
      "ttLibC/ttLibC/container/mpegts2/mpegtsPacket.c",
      "ttLibC/ttLibC/container/mpegts2/mpegtsReader.c",
      "ttLibC/ttLibC/container/mpegts2/mpegtsWriter.c",
      "ttLibC/ttLibC/container/mpegts2/type/pat.c",
      "ttLibC/ttLibC/container/mpegts2/type/pes.c",
      "ttLibC/ttLibC/container/mpegts2/type/pmt.c",
      "ttLibC/ttLibC/container/mpegts2/type/sdt.c",
      "ttLibC/ttLibC/decoder/avcodecDecoder.c",
      "ttLibC/ttLibC/encoder/openh264Encoder.cpp",
      "ttLibC/ttLibC/frame/frame.c",
      "ttLibC/ttLibC/frame/audio/aac.c",
      "ttLibC/ttLibC/frame/audio/adpcmImaWav.c",
      "ttLibC/ttLibC/frame/audio/audio.c",
      "ttLibC/ttLibC/frame/audio/mp3.c",
      "ttLibC/ttLibC/frame/audio/nellymoser.c",
      "ttLibC/ttLibC/frame/audio/opus.c",
      "ttLibC/ttLibC/frame/audio/pcmAlaw.c",
      "ttLibC/ttLibC/frame/audio/pcmf32.c",
      "ttLibC/ttLibC/frame/audio/pcmMulaw.c",
      "ttLibC/ttLibC/frame/audio/pcms16.c",
      "ttLibC/ttLibC/frame/audio/speex.c",
      "ttLibC/ttLibC/frame/audio/vorbis.c",
      "ttLibC/ttLibC/frame/video/bgr.c",
      "ttLibC/ttLibC/frame/video/flv1.c",
      "ttLibC/ttLibC/frame/video/h264.c",
      "ttLibC/ttLibC/frame/video/h265.c",
      "ttLibC/ttLibC/frame/video/jpeg.c",
      "ttLibC/ttLibC/frame/video/theora.c",
      "ttLibC/ttLibC/frame/video/video.c",
      "ttLibC/ttLibC/frame/video/vp6.c",
      "ttLibC/ttLibC/frame/video/vp8.c",
      "ttLibC/ttLibC/frame/video/vp9.c",
      "ttLibC/ttLibC/frame/video/wmv1.c",
      "ttLibC/ttLibC/frame/video/wmv2.c",
      "ttLibC/ttLibC/frame/video/yuv420.c",
      "ttLibC/ttLibC/resampler/audioResampler.c",
      "ttLibC/ttLibC/resampler/imageResampler.c",
      "ttLibC/ttLibC/resampler/imageResizer.c",
      "ttLibC/ttLibC/resampler/soundtouchResampler.c",
      "ttLibC/ttLibC/resampler/speexdspResampler.c",
      "ttLibC/ttLibC/util/amfUtil.c",
      "ttLibC/ttLibC/util/beepUtil.c",
      "ttLibC/ttLibC/util/byteUtil.c",
      "ttLibC/ttLibC/util/crc32Util.c",
      "ttLibC/ttLibC/util/dynamicBufferUtil.c",
      "ttLibC/ttLibC/util/flvFrameUtil.c",
      "ttLibC/ttLibC/util/hexUtil.c",
      "ttLibC/ttLibC/util/ioUtil.c",
      "ttLibC/ttLibC/util/stlListUtil.cpp",
      "ttLibC/ttLibC/util/stlMapUtil.cpp"
    ],
    "include_dirs": [
      "<!(node -e \"require('nan')\")",
      "ttLibC/",
      "./",
      "/usr/local/lib"
    ]
  }]
}
