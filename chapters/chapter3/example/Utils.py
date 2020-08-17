# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : Utils.py
# @Created  : 2020/8/17 8:35 下午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 目的?
# -------------------------------------------------------------------------------

def get_valid_input(input_string, valid_options):
    input_string += "({})".format(",".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response