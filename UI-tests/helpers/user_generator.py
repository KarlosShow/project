import random
import string

class UserGenerator:
    @staticmethod
    def generate_text(length=8):
        alphabet = string.ascii_lowercase + string.digits
        return ''.join(
            random.choice(alphabet)
            for _ in range(length)
        )
    @classmethod
    def create_credentials(cls):
        random_part = cls.generate_text()

        return {
            'email': f'autotest_{random_part}@yandex.ru',
            'password': f'Qa_{cls.generate_text(10)}',
            'name': f'user_{cls.generate_text(6)}'
        }
