class Person:

    def __init__(self):
        self.age_called = 0

    @property
    def age(self):
        self.age_called += 1

        return self.age_called


p = Person()

for i in range(10):
    print(f"[{i}] => {p.age}")
