# -*- coding: utf-8 -*-

from django.conf import settings
if 'localeurl' in settings.INSTALLED_APPS:
    from localeurl.models import patch_reverse
    patch_reverse()

from django.core.urlresolvers import reverse
from coop_cms.models import BaseArticle
from coop_cms.settings import get_article_class
from coop_cms.tests import BaseArticleTest, AUTH_LOGIN_NAME


class PermissionMiddlewareTest(BaseArticleTest):
    
    def setUp(self):
        super(PermissionMiddlewareTest, self).setUp()
        self._MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES
        if not 'coop_cms.middleware.PermissionsMiddleware' in settings.MIDDLEWARE_CLASSES:
            settings.MIDDLEWARE_CLASSES += ('coop_cms.middleware.PermissionsMiddleware',)
        
    def tearDown(self):
        super(PermissionMiddlewareTest, self).tearDown()
        self.MIDDLEWARE_CLASSES = self._MIDDLEWARE_CLASSES
        
    def test_view_draft_anonymous(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.DRAFT)
        self.assertEqual(article.is_draft(), True)
        url = article.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(302, response.status_code)
        auth_url = reverse(AUTH_LOGIN_NAME)
        self.assertRedirects(response, auth_url+'?next='+url)
        
    def test_edit_anonymous(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.DRAFT)
        self.assertEqual(article.is_draft(), True)
        url = article.get_edit_url()
        response = self.client.get(url)
        self.assertEqual(302, response.status_code)
        auth_url = reverse(AUTH_LOGIN_NAME)
        self.assertEqual(response["Location"], "http://testserver"+auth_url+'?next='+url)
        #self.assertRedirects(response, auth_url+'?next='+url)
        
    def test_view_published_anonymous(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)
        self.assertEqual(article.is_draft(), False)
        url = article.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        
    def test_view_draft_not_allowed(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.DRAFT)
        self.assertEqual(article.is_draft(), True)
        
        self._log_as_non_editor()
        
        url = article.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(403, response.status_code)