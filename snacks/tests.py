from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse

class Snakstest(TestCase):
    def test_home_page_status(self):
        url=reverse('snack_list')
        respones=self.client.get(url)
        self.assertEqual(respones.status_code,200)
    
    def test_home_page_template(self):
        url=reverse('snack_list')
        respones=self.client.get(url)
        self.assertTemplateUsed(respones,'snack_list.html')

    def test_snack_create_template(self):
        url=reverse('create_list')
        respones=self.client.get(url)
        self.assertTemplateUsed(respones,'snack_create.html')
      
    
    def setUp(self):
        self.user=get_user_model().objects.create_user(
        username='test',
        email='test@test.com',
        password='test'
        )

        self.snack=Snack.objects.create(
            title='test',
            purchaser=self.user,
            description='hi',
            image_url='image_url'
        )
    
    def test_str_method(self):
        self.assertEqual(str(self.snack),'test')

    

    def test_update_detail_view(self):
        url=reverse('detail_list',args=[self.snack.id])
        response=self.client.get(url)
        self.assertTemplateUsed(response,'snack_detail.html')


    def test_create_view(self):
        data={
            'title':'test',
            'purchaser':self.user.id,
            'description':'hi',
            'image_url':'image_url'
        } 
        url=reverse('create_list')
        response=self.client.post(path=url,data=data,follow=True)  
        self.assertEqual(len(Snack.objects.all()),2) 
        self.assertTemplateUsed(response,'snack_list.html')
        self.assertRedirects(response,reverse('snack_list'))