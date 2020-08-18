# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : main.py
# @Created  : 2020/8/18 3:04 下午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 运行测试程序
# -------------------------------------------------------------------------------

import chapters.chapter4.auth as auth

class Editor:

    def __init__(self):
        self.logged = False
        self.username = None
        self.default_menu_map = {
            "1": self.login,
            "2": self.add_user,
            "3": self.add_permission,
            "4": self.perm_user,
            "5": self.quit,
        }

        self.logged_menu_map = {
            "1": self.check_permission,
            "2": self.show_user_info,
            "3": self.logout
        }

    def show_default_menu(self):
        print("""
Please choice a command:
1. 登陆
2. 添加用户
3. 添加权限
4. 给用户授权
5. 退出系统
""")

    def show_logged_menu(self):
        print("""
Please choice a command:
1. 检查授权
2. 显示用户信息
3. 退出登录
""")

    def login(self):
        username = input("username:")
        password = input("password:")
        try:
            auth.authenticator.login(username, password)
        except auth.InvalidUsername:
            print("username does not exist!")
        except auth.InvalidPassword:
            print("password was wrong")
        else:
            self.logged = True
            self.username = username
            print("Success. Welcome back {}.".format(username))

    def logout(self):
        try:
            auth.authenticator.logout(self.username)
        except auth.InvalidUsername:
            print("username does not exist!")
        else:
            print("Bye {}.".format(self.username))
            self.logged = False
            self.username = None

    def show_user_info(self):
        user = auth.authenticator.user_info(self.username)
        print("username:{} ,is_logging:{},  password:{}".format(user.username,user.is_logged_in ,user.password))

    def add_user(self):

        username = input("username:")
        password = input("password:")
        try:
            auth.authenticator.add_user(username, password)
        except auth.InvalidUsername:
            print("username cannot be null!")
        except auth.UserAreadyExist:
            print("username exist!")
        except auth.PasswordTooShort:
            print("password len must > 6")
        else:
            print("Success Add User.")

    def add_permission(self):
        perm_name = input("permission name:")
        try:
            auth.authorizor.add_permission(perm_name)
        except PermissionError as e:
            print(str(e))
        else:
            print("Success Add Permission {}.".format(perm_name))

    def perm_user(self):
        username = input("username:")
        perm_name = input("permission name:")
        try:
            auth.authorizor.permit_user(perm_name, username)
        except PermissionError as e:
            print(str(e))
        except auth.InvalidUsername:
            print("username does not exist!")
        else:
            print("Success Add Permission {} to User {}.".format(perm_name,username))

    def is_permitted(self,perm_name):
        try:
            auth.authorizor.check_permission(perm_name,self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} does have {}".format(e.username,perm_name))
            return False
        except PermissionError as e:
            print(str(e))
            return False
        else:
            return True

    def check_permission(self):
        perm_name = input("permission name:")
        if self.is_permitted(perm_name):
            print("user {} has permission {}".format(self.username , perm_name))

    def quit(self):
        # 可以用 sys 退出。
        # 为了演示异常，用SystemExit 错误。该错误 和 KeyboardInterrupt 一样不是继承自 Exception 是继承自 BaseException 。
        # except 默认是捕获 Exception ，所以无法捕获KeyboardInterrupt，SystemExit 所以抛出这 2 个异常程序就终止了。
        # 如果要捕获 SystemExit 可以 except BaseException
        # import sys
        # sys.exit()
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                func = None
                try:
                    if not self.logged:
                        self.show_default_menu()
                    else:
                        self.show_logged_menu()

                    answer = input("Your choice:")

                    if not self.logged:
                        func = self.default_menu_map[answer]
                    else:
                        func = self.logged_menu_map[answer]

                except KeyError:
                    print("Invalid choice [{}]".format(answer))
                else:
                    func()
        except:
            import sys
            print("something was wrong : ",sys.exc_info())
        finally:
            print("Thank you for testing the auth module")

Editor().menu()