from faker import Faker
fake = Faker()

class BaseContact():
  def __init__(self, first_name, last_name, phone_number, email):
    self.first_name = first_name
    self.last_name = last_name
    self.company = phone_number
    self.email = email

  def __str__(self):
    return f'{self.first_name} {self.last_name} {self.phone_number} {self.email}'

  def __repr__(self):
    return f'BaseContact(first_name={self.first_name}, last_name={self.last_name}, phone_number={self.phone_number} email={self.email})'

  def contact(self):
    return f'Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}'

    self._len_adressee = 0

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

    self._len_adressee = 0

  @property
  def len_adressee(self):
    self._len_adressee = len(self.first_name) + len(self.last_name) + 1
    return self._len_adressee

def create_contacts(type, value):
  


if __name__ == '__main__':


  