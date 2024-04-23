class oftolmolog:
    nameO = 'abror'
    ageO = 23
    date_of_birthO = 2000

    def __init__(self):
        self.created = 'aftolmolog obyekti yaratildi'


p = oftolmolog()
print(p.created)


class nevrolog:
    nameN = 'Mark'
    ageN = 22
    date_of_birthN = 1998

    def __init__(self):
        self.created = 'nevrolog obyekti yaratildi'


p1 = nevrolog()
print(p1.created)

class boxer:
    name = 'joha'
    age = 23
    date_of_birth = 1234

    def __init__(self):
        self.created = 'boxer obyekti yaratildi'


p2 = boxer()
print(p2.created)

class soccer:
    name = 'ronaldo'
    age = 23
    date_of_birth = 1334

    def __init__(self):
        self.created = 'ronaldo obyekti yaratildi'


p3 = soccer()
print(p3.created)

class cheif:
    ch1_name = 'anton'
    ch1_age = 22
    ch1_date_of_birth = 1896
    ch2_name = 'mixail'
    ch2_age = 23
    ch2_date_of_birth = 1893

    def __init__(self):
        self.ch1_created = 'Salad shefi obyekti yaratildi'
        self.ch2_created = 'Cake shefi obyekti yaratildi'


p3 = cheif()
print(p3.ch1_created)
print(p3.ch2_created)


class programmers:
    frontender = 'Abbos'
    frontender_age = 20
    frontender_date_of_birth = 2000
    tester_name = 'Rustam'
    tester_age = 19
    tester_date_of_birth = 2003
    backender = 'Javohir'
    backender_age = 15
    backender_date_of_birth = 2008

    def __init__(self):
        self.frontender_created = 'frontender obyekti yaratildi'
        self.tester_created = 'tester obyekti yaratildi'
        self.backender_created = 'backenderlar qandaydir obyektlar emas ular proffesional dasturchilardir😎😂 '


p4 = programmers()

print(p4.tester_created)
print(p4.frontender_created)
print(p4.backender_created)
