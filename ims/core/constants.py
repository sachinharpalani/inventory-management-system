from django.db.models import TextChoices


class OrderStatus(TextChoices):
    PENDING = "PENDING", "PENDING"
    COMPLETED = "COMPLETED", "COMPLETED"
    INVALID = "INVALID", "INVALID"


class TransactionStatus(TextChoices):
    PENDING = "PENDING", "PENDING"
    SUCCESS = "SUCCESS", "SUCCESS"


class TransactionMode(TextChoices):
    CASH = "CASH", "CASH"
    UPI = "UPI", "UPI"
    CARD = "CARD", "CARD"
    NEFT = "NEFT", "NEFT"
    GIFT = "GIFT", "GIFT"