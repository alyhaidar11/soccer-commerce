from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
            name="BURHAN Jersey",
            price=150000,
            quantity=10,
            description="Baju kebanggaan BURHAN FC",
            category="cloth",
            is_featured=True
        )
        self.assertEqual(product.name, "BURHAN Jersey")
        self.assertEqual(product.category, "cloth")
        self.assertTrue(product.is_featured)

    def test_product_default_values(self):
        product = Product.objects.create(
            name="Sepatu BURHAN",
            price=250000,
            quantity=5,
            description="Sepatu pemain BURHAN FC"
        )
        # Mengecek default category = 'update'
        self.assertEqual(product.category, "update")
        # Mengecek default is_featured = False
        self.assertFalse(product.is_featured)

    def test_str_method(self):
        product = Product.objects.create(
            name="Kaos BURHAN",
            price=100000,
            quantity=15,
            description="Kaos casual BURHAN FC"
        )
        # __str__ harus mengembalikan nama produk
        self.assertEqual(str(product), product.name)
