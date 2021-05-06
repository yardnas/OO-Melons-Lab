"""Classes for melon orders."""


class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.shipped = False
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == 'Christmas':
            base_price = base_price * 1.5
            
        total = (1 + self.tax) * self.qty * base_price
        
        if self.order_type == 'international' and self.qty < 10:
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """Remove tax and inspect for the Government"""

    def __init__(self, species, qty):
        super().__init__(species, qty, 'government', 0.00)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Checks whether inspection passed or not"""

        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 'domestic', 0.08)

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.order_type = "domestic"
        # self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 'international', 0.17)

        # self.species = species
        # self.qty = qty
        self.country_code = country_code
        # self.shipped = False
        # self.order_type = "international"
        # self.tax = 0.17
  

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
