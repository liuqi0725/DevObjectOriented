# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : menu.py
# @Created  : 2020/8/14 4:47 下午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 目的?
# -------------------------------------------------------------------------------

import sys
from chapter2.notebook import Notebook

class Menu:

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1" : self.show_notes,
            "2" : self.search_notes,
            "3" : self.add_note,
            "4" : self.modify_note,
            "5" : self.quit
        }

    def display_menu(self):
        '''
        显示菜单
        :return:
        '''

        # """ 包括中的数据可以换行，任然是字符串 , 移动到最左边，在控制台也会在最左边 """
        print(
"""
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
""")

    def run(self):
        """
        执行菜单程序，显示菜单，返回选择项
        :return:
        """
        while True:
            self.display_menu()
            choice = input("请选择:")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{} 选择不正确，没有该选项!".format(choice))

    def show_notes(self , notes=None):
        '''
        显示该笔记本，所有备注
        :return:
        '''
        if not notes:
            notes = self.notebook.notes

        if not notes:
            print("您尚未录入 Note ！")

        for note in notes:
            print("{} : {}\n{}".format(note.id , note.tags, note.memo))

    def search_notes(self):
        '''
        搜索备注
        :return:
        '''
        filter = input("搜索备注内容:")
        notes = self.notebook.search(filter)
        if notes:
            self.show_notes(notes)
        else:
            print("没有找到对应备注.")


    def add_note(self):
        memo = self.__get_user_memo()
        tags = self.__get_user_tags()
        note = self.notebook.new_note(memo,tags)
        print("Add Note Success! ID:{}".format(note.id))

    def __get_user_memo(self):
        memo = input("输入内容:")
        if not memo:
            print("内容不能为空!")
            memo = self.__get_user_memo()
        return memo

    def __get_user_tags(self):
        '''
        添加标签
        :return:
        '''
        tags = input("请输入标签,多个用','号分割[选填]:")
        return tags

    def modify_note(self):
        '''
        修改 note
        :return:
        '''
        note_id = input("输入 Note ID:")
        note = self.notebook.find_note(note_id)
        if not note:
            print("Note ID [{}] 不存在.".format(note_id))
            # 回到开始
            return

        memo = self.__get_user_memo()
        tags = self.__get_user_tags()

        self.notebook.modify_memo(note_id , memo)
        self.notebook.modif_tags(note_id, tags)

        print("修改 Note Success! ID:{}".format(note.id))

    def quit(self):
        print("下次再见!")
        sys.exit()

Menu().run()