from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.CharField(max_length=50)  # e.g., Toyota
    model = models.CharField(max_length=100)  # e.g., Avanza
    year = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Purchase(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Tunai', 'Tunai'),
        ('Kredit', 'Kredit'),
        ('Leasing', 'Leasing'),
    ]

    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='purchases')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='purchases')
    date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f"Pembelian oleh {self.buyer.name} - {self.car}"


class Survey(models.Model):
    SATISFACTION_CHOICES = [(i, str(i)) for i in range(1, 6)]

    purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE, related_name='survey')
    satisfaction_rating = models.IntegerField(choices=SATISFACTION_CHOICES)  # 1 (worst) - 5 (best)
    comments = models.TextField(blank=True)
    would_recommend = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Survey untuk {self.purchase.buyer.name}"
