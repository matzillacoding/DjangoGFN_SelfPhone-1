from django.test import TestCase
from django.contrib.auth.models import User
from .models import Costumer, Smartphone, Manufacturer, Color, Memory_size, Storage_size, Product, CartItem, Order, Address


class SmartphoneStoreTestCase(TestCase):
    def setUp(self):
        # Benutzer und Kunden erstellen
        self.user1, _ = User.objects.get_or_create(username='user1', defaults={
                                                   'email': 'user1@example.com', 'password': 'user1password'})
        self.customer1, _ = Costumer.objects.get_or_create(customer=self.user1, defaults={
                                                           'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com'})

        # Adresse für den Kunden erstellen
        self.address1 = Address.objects.create(
            customer=self.customer1,
            postcode='12345',
            city='Test City',
            street='123 Test St',
            house_number='1'
        )

        # Smartphone-Modelle erstellen oder abrufen
        self.smartphone1, _ = Smartphone.objects.get_or_create(
            manufacturer=Manufacturer.APPLE,
            model='iPhone 13',
            defaults={
                'color': Color.SCHWARZ,
                'memory_size': Memory_size.acht,
                'storage_size': Storage_size.einhundertachtundzwanzig,
                'akku': 3000,
                'basic_price': 799.99,
                'description': "Latest model"
            }
        )
        self.product1, _ = Product.objects.get_or_create(
            smartphone=self.smartphone1, defaults={'name': 'iPhone 13 Schwarz'})

        self.smartphone2, _ = Smartphone.objects.get_or_create(
            manufacturer=Manufacturer.SAMSUNG,
            model='Galaxy S21',
            defaults={
                'color': Color.BLAU,
                'memory_size': Memory_size.zwoelf,
                'storage_size': Storage_size.zweihundertsechsundfunfzig,
                'akku': 4000,
                'basic_price': 999.99,
                'description': "High-end specs"
            }
        )
        self.product2, _ = Product.objects.get_or_create(
            smartphone=self.smartphone2, defaults={'name': 'Galaxy S21 Blau'})

    def test_create_orders_with_different_quantities_and_models(self):
        cart_item1 = CartItem.objects.create(product=self.product1, quantity=2)
        cart_item2 = CartItem.objects.create(product=self.product2, quantity=1)
        order1 = Order.objects.create(
            customer=self.customer1, address=self.address1)
        order1.products.add(cart_item1, cart_item2)

        total_quantity = order1.get_total_quantity
        self.assertEqual(total_quantity, 3,
                         "The total quantity calculated is incorrect.")

    def test_pricing_logic(self):
        self.smartphone1.memory_size = Memory_size.sechzehn
        self.smartphone1.storage_size = Storage_size.terabyte
        self.smartphone1.save()

        expected_price_adjustment = 310  # Korrekte Anpassung nach Überprüfung
        expected_price = 799.99 + expected_price_adjustment
        new_price = self.smartphone1.basic_price

        self.assertEqual(new_price, expected_price,
                         f"Expected price to be {expected_price}, but got {new_price}.")

    def test_user_session_persistence(self):
        # Benutzer einloggen und Produkt zum Warenkorb hinzufügen
        self.client.login(username='user1', password='user1password')
        CartItem.objects.create(product=self.product1, quantity=1)
        items_in_cart_before_logout = CartItem.objects.filter(
            product=self.product1).count()

        # Benutzer ausloggen und wieder einloggen
        self.client.logout()
        self.client.login(username='user1', password='user1password')
        items_in_cart_after_login = CartItem.objects.filter(
            product=self.product1).count()

        self.assertEqual(items_in_cart_before_logout, items_in_cart_after_login,
                         "Cart items do not persist after re-login.")


class PricingLogicTestCase(TestCase):
    def test_update_price_based_on_specs(self):
        # Erstelle ein Smartphone-Objekt
        smartphone = Smartphone(
            manufacturer=Manufacturer.APPLE,
            model='Test iPhone',
            color='Schwarz',
            memory_size=Memory_size.sechzehn,
            storage_size=Storage_size.terabyte,
            basic_price=799.99  # Basispreis setzen
        )

        # Preis aktualisieren
        smartphone.update_price_based_on_specs()

        # Überprüfen, ob der Preis korrekt aktualisiert wurde
        expected_price = 799.99 + 280  # Erwartete Preisanpassung für diese Konfiguration
        self.assertEqual(smartphone.basic_price, expected_price,
                         f"Expected price to be {expected_price}, but got {smartphone.basic_price}.")
