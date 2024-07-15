#Money class for handling monetary amounts with various currencies

from decimal import Decimal


#Money class revised
class Money(Decimal):

    """Money Class.
    Stores both a Decimal amount and currency units.
    Supports addition, multiplication, and subtraction operations.
    """

    #Exchange rates
    exch_dict = {
        'USDCAD': Decimal('0.75'), 'USDEUR': Decimal('1.16'),
        'CADUSD': Decimal('1.33'), 'CADEUR': Decimal('1.54'),
        'EURUSD': Decimal('0.86'), 'EURCAD': Decimal('0.65')
    }

    #Default currency
    default_curr = 'USD'

    #Constructor
    def __new__(cls, v, units=''):
        return super(Money, cls).__new__(cls, Decimal(v))

    #Initializer
    def __init__(self, v='0', units=''):
        if not units:
            self.units = Money.default_curr
        else:
            self.units = units

    #Representations
    def __str__(self):
        return super().__str__() + ' ' + self.units

    def __repr__(self):
        return 'Money(' + super().__str__() + ' ' + self.units + ')'

    #Addition
    def __add__(self, other):
        if self.units != other.units:
            r = Money.exch_dict[self.units + other.units]
            m1 = Decimal(self)
            m2 = Decimal(other) * r
            m = Money(m1 + m2, self.units)
        else:
            m = Money(Decimal(self) + Decimal(other), self.units)
        m = round(m, 2)
        return m

    #Subtraction
    def __sub__(self, other):
        if self.units != other.units:
            r = Money.exch_dict[self.units + other.units]
            m1 = Decimal(self)
            m2 = Decimal(other) * r
            m = Money(m1 - m2, self.units)
        else:
            m = Money(Decimal(self) - Decimal(other), self.units)
        m = round(m, 2)
        return m

    #Multiplication
    def __mul__(self, other):
        m = Money(Decimal(self) * Decimal(other), self.units)
        m = round(m, 2)
        return m


#Test function
def testMoneyClass():

    """Test function for Money class."""

    #Money objects
    m1 = Money('1.05', 'USD')
    m2 = Money('2.00', 'CAD')
    m3 = Money('1.50', 'EUR')
    m4 = Money('2.00', 'USD')

    #Testing addition
    print(m1 + m2)  # USD + CAD
    print(m1 + m3)  # USD + EUR
    print(m1 + m4)  # USD + USD

    #Testing subtraction
    print(m1 - m2)  # USD - CAD
    print(m1 - m3)  # USD - EUR
    print(m1 - m4)  # USD - USD

    #Testing multiplication
    print(m1 * 2)  # USD * 2
    print(m2 * 3)  # CAD * 3
    print(m3 * 4)  # EUR * 4


#Call for test start
testMoneyClass()
