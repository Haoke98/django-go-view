import datetime
import json
import os

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.core.files.storage import default_storage

from .models import Project

BUCKET_NAME = "goview"
MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT', 'media')
MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')


# Create your views here.
def get_oss_info(request):
    resp = {
        "msg": "返回成功",
        "code": 200,
        "data": {
            "BucketName": BUCKET_NAME,
            "bucketURL": "/goview/media/{}/".format(BUCKET_NAME)
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

        qs = Project.objects.filter(id=projectId)
        if data.__contains__("projectName"):
            qs.update(name=data["projectName"])
        if data.__contains__("indexImage"):
            qs.update(cover=data["indexImage"])
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


@require_http_methods(["GET"])
def get_project_data(request):
    projectId = request.GET.get("projectId")
    proj = Project.objects.filter(id=projectId).get()
    resp = {
        "msg": "获取成功",
        "code": 200,
        "data": proj.serialize(with_content=True)
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


def delete_project(request):
    if request.method == "DEL":
        ids = request.GET.getlist("ids")
        Project.objects.filter(id__in=ids).delete()


@csrf_exempt
@require_http_methods(["POST"])
def project_upload(request):
    # 要实现保存图片的逻辑
    in_mem_upload_f: InMemoryUploadedFile = request.FILES.get("object")
    fp = os.path.join(MEDIA_ROOT, BUCKET_NAME, in_mem_upload_f.name)
    result = default_storage.save(fp, in_mem_upload_f)
    f_name = os.path.basename(result)
    resp = {
        "code": 200,
        "data": {
            "id": "859313657253859328",
            "fileName": f_name,
            "bucketName": BUCKET_NAME,
            "fileSize": in_mem_upload_f.size,
            "fileSuffix": "image/png",
            "createUserId": "-",
            "createUserName": "-",
            "createTime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updateUserId": None,
            "updateUserName": None,
            "updateTime": None
        }
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
@require_http_methods(['POST'])
def save_project(request):
    projectId = request.POST.get("projectId", None)
    content = request.POST.get("content", None)
    if projectId is None or projectId == "undefined" or content is None:
        resp = {
            "msg": "字段异常/字段缺失",
            "code": 500
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")
    Project.objects.filter(id=projectId).update(content=content)
    resp = {"msg": "数据保存成功", "code": 200}
    return HttpResponse(json.dumps(resp), content_type="application/json")


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


@csrf_exempt
def login(request):
    # TODO: 实现实际鉴权操作
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
