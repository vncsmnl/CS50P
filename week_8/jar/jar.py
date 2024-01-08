class Jar:
    def __init__(self, capacity=12):
        self._validate_positive_integer(capacity)
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def _validate_positive_integer(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Invalid positive integer.")

    def _validate_non_negative_withdrawal(self, n):
        if n < 0 or self.cookies - n < 0:
            raise ValueError("Invalid withdrawal amount.")

    def _validate_deposit(self, n):
        if n < 0 or self.cookies + n > self._capacity:
            raise ValueError("Invalid deposit amount.")

    def deposit(self, n):
        self._validate_positive_integer(n)
        self._validate_deposit(n)
        self.cookies += n

    def withdraw(self, n):
        self._validate_positive_integer(n)
        self._validate_non_negative_withdrawal(n)
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
