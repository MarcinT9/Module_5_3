from faker import Faker
fake = Faker()

class BusinessCard():
  def __init__(self, first_name, last_name, company, position, email):
    self.first_name = first_name
    self.last_name = last_name
    self.company = company
    self.position = position
    self.email = email

  def __str__(self):
    return f'{self.first_name} {self.last_name} {self.email}'

  def __repr__(self):
    return f'BusinessCard(first_name={self.first_name}, last_name={self.last_name}, email={self.email})'

  def contact(self):
    return f'Kontaktuję się z {self.first_name} {self.last_name} {self.position} {self.email}'

    self._len_adressee = 0

  @property
  def len_adressee(self):
    self._len_adressee = len(self.first_name) + len(self.last_name) + 1
    return self._len_adressee


if __name__ == '__main__':
  contact1 = BusinessCard(first_name = fake.first_name(), last_name = 'Reyes', company = 'Pauls Record Hut', position = 'Manager', email = 'AlmaRReyes@jourrapide.com')

  contact2 = BusinessCard(first_name = 'Kristi', last_name = 'Jaquez', company = 'Omni Tech Solutions', position = 'Personal attendant', email = 'KristiDJaquez@teleworm.us')

  contact3 = BusinessCard(first_name = 'Erick', last_name = 'Jackson', company = 'Linens n Things', position = 'Mechanical door repairer', email = 'ErickMJackson@armyspy.com')

  business_card_list = [contact1, contact2, contact3]

  for person in business_card_list:
     print(person)

  print()
  print('-' * 20)
  print()

  by_first_name = sorted(business_card_list, key=lambda card: card.first_name)
  for person1 in by_first_name:
     print(person1)

  print()
  print('-' * 20)
  print()

  print(contact1.contact())

  print()
  print('-' * 20)
  print()

  print(contact1.len_adressee)
  print(contact2.len_adressee)
  print(contact3.len_adressee)