from django.test import TestCase
from django.urls import reverse
from products.models import Product, ProductCategory
# Create your tests here.
class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context_data['title'], 'Каталог')
        self.assertTemplateUsed(response, 'products/index.html')

class ProductsListViewTestCase(TestCase):
    fixtures = ['categories.json', 'products.json']

    def test_view(self):
        path = reverse('products:index')
        response = self.client.get(path)
        products = Product.objects.all()
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

        self.assertEquals(list(response.context_data['object_list']), list(products[:3]))

    def test_list_with_category(self):
        category = ProductCategory.objects.firs()
        products = Product.objects.all()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEquals(
            list(response.context_data['object.list']),
            list(products.filter(category_id= category.id))
        )



