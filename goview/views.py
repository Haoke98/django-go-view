import json
import os

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    resp = {
        "msg": "操作成功",
        "code": 200,
        "data": {
            "userinfo": {
                "id": "1",
                "username": "admin",
                "password": "21232f297a57a5a743894a0e4a801fc3",
                "nickname": "管理员",
                "depId": None,
                "posId": None,
                "depName": None,
                "posName": None
            },
            "token": {
                "tokenName": "satoken",
                "tokenValue": "8a40083d-1aa3-43f2-9e31-b1912dedfadb",
                "isLogin": None,
                "loginId": "1",
                "loginType": "login",
                "tokenTimeout": 2592000,
                "sessionTimeout": 2592000,
                "tokenSessionTimeout": 2591893,
                "tokenActivityTimeout": -1,
                "loginDevice": "default-device",
                "tag": None
            }
        }
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


def index(request):
    # 指向Vue项目编译后的index.html的文件路径
    index_file_path = os.path.join(os.path.dirname(__file__), 'frontend', 'index.html')
    with open(index_file_path, 'r', encoding='utf-8') as f:
        index_file_content = f.read()
    return HttpResponse(index_file_content)
