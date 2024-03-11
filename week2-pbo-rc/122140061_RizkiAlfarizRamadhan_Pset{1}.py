import random

class Person:
    def __init__(self, blood_type):
        self.blood_type = blood_type

    def get_allele(self):
        return random.choice(self.blood_type)

class Father(Person):
    def __init__(self, blood_type):
        super().__init__(blood_type)

class Mother(Person):
    def __init__(self, blood_type):
        super().__init__(blood_type)

class Child(Person):
    def __init__(self, father, mother):
        father_allele = father.get_allele()
        mother_allele = mother.get_allele()
        super().__init__([father_allele, mother_allele])
        self.father_allele = father_allele
        self.mother_allele = mother_allele

    def determine_blood_type(self):
        alleles = [self.father_allele, self.mother_allele]
        alleles.sort()
        if alleles == ['A', 'A']:
            return 'Blood Type A'
        elif alleles == ['A', 'B']:
            return 'Blood Type AB'
        elif alleles == ['A', 'O']:
            return 'Blood Type A'
        elif alleles == ['B', 'B']:
            return 'Blood Type B'
        elif alleles == ['B', 'O']:
            return 'Blood Type B'
        elif alleles == ['O', 'O']:
            return 'Blood Type O'


mother_blood_type = input("Enter mother's blood type (A, B, AB, or O): ").upper()
father_blood_type = input("Enter father's blood type (A, B, AB, or O): ").upper()
father = Father(father_blood_type)
mother = Mother(mother_blood_type)
child = Child(father, mother)
print("Child's alleles:", child.blood_type)
print("Child's blood type:", child.determine_blood_type())
