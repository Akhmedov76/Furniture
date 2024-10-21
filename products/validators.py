from django.core.exceptions import ValidationError


class MinimumValidator:
    def __init__(self, min_value):
        self.min_value = min_value

    def __call__(self, value):
        if value < self.min_value:
            raise ValidationError(f'{value} must be at least {self.min_value}')

