from faker import Faker
fake = Faker()

class BaseContact():
  def __init__(self, first_name, last_name, phone_number, email):
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email

  def __str__(self):
    return f'{self.first_name} {self.last_name} {self.phone_number} {self.email}'

  def __repr__(self):
    return f'BaseContact(first_name={self.first_name}, last_name={self.last_name}, phone_number={self.phone_number} email={self.email})'

  def contact(self):
    return f'Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}'

  @property
  def len_adressee(self):
    self._len_adressee = len(self.first_name) + len(self.last_name) + 1
    return self._len_adressee

class BusinessContact(BaseContact):
  def __init__(self, position, company, business_phone, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.position = position
    self.company = company
    self.business_phone = business_phone

  def __str__(self):
    return f'{self.first_name} {self.last_name} {self.phone_number} {self.email} {self.position} {self.company} {self.business_phone}'

  def __repr__(self):
    return f'BaseContact(first_name={self.first_name}, last_name={self.last_name}, phone_number={self.phone_number}, email={self.email}, position={self.position}, company={self.company}, business_phone={self.business_phone})'
  
  def contact(self):
    return f'Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name}'

def create_contacts(choice, choice2):
  
  for i in range(choice2):
    if choice == 1:
      fake_card = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_number=fake.phone_number(), email=fake.email())
      print(fake_card.contact())
      print(f'Długość imienia i nazwiska wynosi {fake_card.len_adressee} znaków.')

    elif choice == 2:
      fake_card2 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), phone_number=fake.phone_number(), email=fake.email(), position=fake.job(), company=fake.company(), business_phone=fake.phone_number())
      print(fake_card2.contact())
      print(f'Długość imienia i nazwiska wynosi {fake_card2.len_adressee} znaków.')

if __name__ == '__main__':
  choice = int(input('Wybierz rodzaj wyzytówki: 1 - Prywatna, 2 - Biznesowa: '))
  if choice not in {1, 2}:
    print('Niepoprawny wybór!')
  else:  
    choice2 = int(input('Podaj ilość wizytówek: '))

    create_contacts(choice, choice2)



  