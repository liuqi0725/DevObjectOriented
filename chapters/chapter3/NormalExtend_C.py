# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : NormalExtends.py
# @Created  : 2020/8/17 10:12 上午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 继承基本类型
# -------------------------------------------------------------------------------

# 调用不同的子类会有不同结果。
# 例如
# 播放不同的音频格式文件，需要不同解码器
import sys

class AudioFile:

    def __init__(self , filename):
        # 根据子类的 ext 判断文件名，不支持的类型则抛出异常
        if not filename.endswith(self.ext):
            raise Exception("Invalid file type")
        self.filename = filename

    def play(self):
        pass

class Mp3File(AudioFile):

    ext = "mp3"

    def play(self):
        # 重写
        print("play {} with MP3 decoder".format(self.filename))


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        # 重写
        print("play {} with WAV decoder".format(self.filename))

class FlacFile(AudioFile):
    ext = "flac"

    def play(self):
        # 重写
        print("play {} with Flac decoder".format(self.filename))


Mp3File("My_heart_will_go_on.mp3").play()
WavFile("Hero.wav").play()

# 此处抛出异常，因为 wav 子类不支持 mp3类型
try:
    Mp3File("Hero.wav").play()
except:
    print(str(sys.exc_info()))