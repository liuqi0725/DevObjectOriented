# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @File     : example.py
# @Created  : 2020/8/18 2:14 下午
# @Software : PyCharm
# 
# @Author   : Liu.Qi
# @Contact  : liuqi_0725@aliyun.com
# 
# @Desc     : 案例，完成一个身份识别授权的系统
# -------------------------------------------------------------------------------

import hashlib

# =======================
# 用户对象
# =======================
class User:

    def __init__(self , username, password):
        '''
        创建一个用户，密码需要在持久化之前加密
        :param username:
        :param password:
        '''
        self.username = username
        self.password = self.__encrypt_pw(password)
        self.is_logged_in = False

    def __encrypt_pw(self,password):
        '''
        用username 加密密码，并返回 sha 值
        :param password:
        :return:
        '''
        hash_string = (self.username + password)
        hash_code = hash_string.encode("utf8")
        return hashlib.sha256(hash_code).hexdigest()

    def check_pw(self, password):
        '''
        验证密码
        :param password:
        :return:
        '''
        en_pw = self.__encrypt_pw(password)
        return en_pw == self.password



# =======================
# 自定义异常
# =======================
class AuthException(Exception):
    def __init__(self , username, user=None):
        super().__init__(username,user)
        self.username = username
        self.user = user

class UserAreadyExist(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class NotLoggedInError(AuthException):
    pass

class NotPermittedError(AuthException):
    pass


# =======================
# 身份验证器
# =======================
class Authenticator:

    def __init__(self):
        '''
        构造一个身份验证器来管理登录/退出用户
        '''
        self.users = {}

    def add_user(self, username,password):
        '''
        添加一个用户
        :param username:
        :param password:
        :return:
        '''
        if not username:
            raise InvalidUsername(username)
        if username in self.users:
            raise UserAreadyExist(username)
        if len(password) < 6:
            raise PasswordTooShort(username)

        self.users[username] = User(username,password)

    def login(self,username,password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        # 判断用户是否存在，还可以用如下方式
        # if username not in self.users:
        #     raise InvalidUsername(username)

        if not user.check_pw(password):
            raise InvalidPassword(username , user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        '''
        是否登陆
        :param username:
        :return:
        '''
        if username in self.users:
            return self.users[username].is_logged_in
        return False



# =======================
# 授权决策器
# =======================
class Authorizor:

    def __init__(self , authenticator):
        '''
        构建一个授权决策器，决策根据认证器[authenticator]来执行
        :param authenticator:
        '''
        self.authenticator = authenticator
        self.permissions = {} # 权限，保存了以权限为 key 用户列表为 val 的键值对

    def add_permission(self, perm_name):
        '''
        创建一个用户可以添加的权限
        :param perm_name:
        :return:
        '''
        try:
            if not perm_name:
                raise PermissionError("Permission name cannot be null")

            # 获取 perm_name 的权限集合，该集合保存了获取该授权的用户列表
            perm_set = self.permissions[perm_name]
        except KeyError:
            # 如果没有创建一个以 perm_name 为 key 的用户集合 set【不用 list，set 只允许一个用户出现一次】
            self.permissions[perm_name] = set()
        else:
            # 如果已存在，则抛出一个权限集合已存在的异常 PermissionError
            raise PermissionError("Permission Exists")

        # 只是为了演示异常，更推荐通过  if perm_name not in self.permissions: 来决策

    def permit_user(self, perm_name, username):
        '''
        给用户授权
        :param perm_name:
        :param username:
        :return:
        '''
        try:
            # 获取 perm_name 的权限集合，该集合保存了获取该授权的用户列表
            perm_set = self.permissions[perm_name]
        except KeyError:
            # 抛出 perm_name 的权限集合不存在的异常
            raise PermissionError("Permission does not exist")
        else:
            # 如果获取到 perm_name 的权限集合
            # 查看用户是否在 认证器中存在
            # 不存在 抛出异常
            # 存在 添加用户到这个权限集合中
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self,perm_name , username):
        '''
        检查用户是否有权限
        :param perm_name:
        :param username:
        :return:
        '''
        # 检查用户是否登陆
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)

        try:
            # 获取 perm_name 的权限集合，该集合保存了获取该授权的用户列表
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            # 如果用户在 set 中，表示该用户有权限，反之抛出没有权限异常
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True


# 创建一个认证器实例
authenticator = Authenticator()
# 创建一个授权器的实例
authorizor = Authorizor(authenticator)
