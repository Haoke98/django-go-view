import json
import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Project


# Create your views here.
def get_oss_info(request):
    resp = {
        "msg": "返回成功",
        "code": 200,
        "data": {
            "BucketName": "v2-cloud",
            "bucketURL": "http://127.0.0.1:9000/v2-cloud"
        }
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def create_project(request):
    if request.method == "POST":
        data = json.loads(request.body)
        project_name = data["projectName"]
        index_image = data["indexImage"]
        remarks = data["remarks"]
        obj = Project(name=project_name, cover=index_image, remarks=remarks)
        obj.save()
        resp = {
            "msg": "创建成功",
            "code": 200,
            "data": obj.serialize()
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def edit_project(request):
    if request.method == "POST":
        data: dict = json.loads(request.body)
        projectId = data["id"]

        projectName = data["projectName"]
        qs = Project.objects.filter(id=projectId)

        qs.update(name=projectName)
        if data.__contains__("indexImage"):
            qs.update(indexImage=data["indexImage"])
        if data.__contains__("remarks"):
            qs.update(remarks=data["remarks"])

        resp = {
            "msg": "操作成功",
            "code": 200
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def publish_project(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        projectId = data["id"]
        state = data["state"]
        Project.objects.filter(id=projectId).update(state=state)
        resp = {
            "msg": "操作成功",
            "code": 200
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")


def get_project_data(request):
    resp = {
        "msg": "获取成功",
        "code": 200,
        "data": "11111111111"
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


def delete_project(request):
    if request.method == "DEL":
        ids = request.GET.getlist("ids")
        Project.objects.filter(id__in=ids).delete()



def get_project_list(request):
    objs = Project.objects.all()
    data = []
    for obj in objs:
        data.append(obj.serialize())
    resp = {
        "code": 0,
        "msg": "获取成功",
        "count": len(objs),
        "data": data
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


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
