from datetime import datetime
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from mixer.backend.django import mixer
from mixer.factory import GenFactory

from project.factory import *

from django.test import TestCase
from django.db import IntegrityError
from project.models import *

pytestmark = pytest.mark.django_db


class TestCategory(TestCase):
    def test_create(self):
        title = '分类1'
        category = Category.objects.create(title=title)
        assert title == category.title

    def test_unique(self):
        title = '分类1'
        Category.objects.create(title=title)
        with self.assertRaisesMessage(IntegrityError, 'UNIQUE constraint failed: project_category.title'):
            category = Category.objects.create(title=title)


class TestProject(TestCase):
    def test_delete(self):
        user = mixer.blend('auth.User')
        p = ProjectFactory.create()
        assert p.deleted_by is None
        assert p.deleted_at is None
        assert p.state == 'new'
        p.do_delete(user)
        assert p.state == 'deleted'
        assert p.deleted_by == user
        assert isinstance(p.deleted_at, type(now()))

    def test_active(self):
        p = ProjectFactory.create()
        assert p.state == 'new'
        p.active()
        assert p.state == 'active'

    def test_create(self):
        user = mixer.blend('auth.User', is_superuser=True)
        title = '测试项目抬头1'
        description = '描述'
        project = Project.objects.create(
            title=title, owner=user, description=description)
        assert project.title == title
        assert project.owner == user
        assert project.description == description
        assert project.category is None
        project.delete()

        p2 = Project.objects.create(
            title=title, owner=user, description=description)
        assert p2.title == title
        assert p2.owner == user
        assert p2.description == description
        p2.delete()

        title = '分类1'
        category = Category.objects.create(title=title)

        p3 = Project.objects.create(
            category=category,
            title=title, owner=user, description=description)
        assert p3.category is category
        p3.delete()

    def test_unique(self):
        user = mixer.blend('auth.User', is_superuser=True)
        title = '测试项目抬头1'
        p2 = Project.objects.create(title=title, owner=user)
        with self.assertRaisesMessage(IntegrityError, 'UNIQUE constraint failed: project_project.title'):
            Project.objects.create(title=title, owner=user)

    def test_tags(self):
        user = mixer.blend('auth.User', is_superuser=True)
        title = '测试项目抬头1'
        n = 10
        tags = mixer.cycle(n).blend('core.tag')
        p = Project.objects.create(title=title, owner=user)
        [p.tags.add(i) for i in tags]
        assert p.tags.all().count() == n
        assert Project.objects.filter(
            tags__name__in=[i.name for i in tags]).distinct().count() == 1


class TestFolder(TestCase):
    def test_create(self):
        p = ProjectFactory.create()
        assert p.owner
        assert p.title

        name = '主目录'
        folder = Folder.objects.create(project=p, name=name)
        assert folder.name == name
        assert folder.parent is None
        assert folder.project is p

        name = '子目录1'
        subfolder = Folder.objects.create(
            project=p, name=name, parent=folder)
        assert subfolder.name == name
        assert subfolder.parent is folder
        assert subfolder.project is p


class TestFile(TestCase):

    def test_create(self):
        p = ProjectFactory.create()
        folder = FolderFactory.create()
        fn = 'abc.ext'
        content = b'this is just content'
        doc = File.objects.create(
            project=p, folder=folder, file=SimpleUploadedFile(fn, content))
        assert doc.name == fn
        assert doc.file_type == 'text/plain'
        assert doc.ext == '.ext'
        assert doc.file.file.read() == content

        fn = 'abc.ext'
        nw = 'axxj我 ‘，'
        doc = File.objects.create(
            name=nw,
            project=p, folder=folder, file=SimpleUploadedFile(fn, content))
        assert doc.name == nw
        assert doc.file_type == 'text/plain'
        assert doc.ext == '.ext'
        assert doc.file.file.read() == content