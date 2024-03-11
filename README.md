# Django + GoView

An Django extension for Django and GoView

## Install & Usage

* Install :
  ```pip install django-go-view```
* Optimize the proj setting.py:

```python
INSTALLED_APPS = [
    '......',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'goview',
    '.......',
]
```
* Add the urls
```python
from django.urls import path, include, re_path

urlpatterns = [
  ...
]

urlpatterns += [
    ...
    re_path(r'^goview/', include('goview.urls', namespace='photologue')),
]
```
* Sync Your Database
```shell
python manage.py migrate goview
```

## Contribute & Development

* Admin 页面账号和密码统一都是: `go-view` / `go-view`.

## 友情链接

* [API文档](https://docs.apipost.cn/preview/5aa85d10a59d66ce/ddb813732007ad2b?target_id=dd81da11-9f8c-48ce-a4e8-3647279683fe)
* 前端源代码: [github]() / [gitee](https://gitee.com/dromara/go-view)
* [后端Java版](https://gitee.com/MTrun/go-view-serve)