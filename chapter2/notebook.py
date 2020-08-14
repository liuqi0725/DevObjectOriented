# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : notebook.py
# @Created  : 2020/8/14 4:47 下午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 目的?
# -------------------------------------------------------------------------------

import datetime

# 为所有新的备注存储下一个可用的 id
last_id = 0

class Note:
    '''
    每台笔记本都应该有的备注
    '''

    def __init__(self , memo, tags=''):
        '''
        使用 memo 初始化一个备注。 并创建 note 创建时间 creation_date
        :param memo:
        :param tags:
        '''

        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id +=1 # id 自增
        self.id = last_id

    def match(self, filter):
        '''
        查找 filter 是否在 memo 或 tags 中存在，如果找到返回 True
        :param filter:
        :return:
        '''
        return filter in self.memo or filter in self.tags


class Notebook:

    '''笔记本 ，可以增删改 存储的 memos '''

    def __init__(self):
        '''初始化笔记本'''
        self.notes = []

    def new_note(self, memo , tags=""):
        '''
        新建 备忘
        :param memo:
        :param tags:
        :return:
        '''
        note = Note(memo, tags)
        self.notes.append(note)
        return note

    def modify_memo(self,note_id, memo):
        '''
        根据 note_id 修改备忘 的 memo 信息
        :param note_id:
        :param memo:
        :return:
        '''
        note = self.find_note(note_id)
        if note:
            note.memo = memo

    def modif_tags(self, note_id, tags):
        '''
        根据 note_id 修改备忘标签
        :param note_id:
        :param tags:
        :return:
        '''
        note = self.find_note(note_id)
        if note:
            note.tags = tags

    def find_note(self, note_id):
        '''
        根据 note_id 获取 note
        :param note_id:
        :return:
        '''
        for note in self.notes:
            # 数据为 int 但是用户输入获取到的是 str，所以用 str 比较
            if str(note.id) == str(note_id):
                return note
        return None

    def search(self , filter):
        '''
        根据 filter 查找 note 的 memo，tags，如果找到，返回 notes 集合
        :param filter:
        :return:
        '''
        return [note for note in self.notes if note.match(filter)]