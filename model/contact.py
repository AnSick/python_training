class Contact():
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None,
                       title=None, company=None,
                       address=None, home_number=None, mobile_number=None,
                       email=None, website=None, notes=None,
                       work_number=None, fax=None, email2=None, email3=None, day_of_birth=None, month_of_birth=None,
                       birth_year=None, day_of_anniversary=None, month_of_anniversary=None, anniversary_year=None,
                       address2=None, phone2=None, photo=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_number = home_number
        self.mobile_number = mobile_number
        self.email = email
        self.website = website
        self.notes = notes
        self.work_number = work_number
        self.fax = fax
        self.email2 = email2
        self.email3 = email3
        self.day_of_birth = day_of_birth
        self.month_of_birth = month_of_birth
        self.birth_year = birth_year
        self.day_of_anniversary = day_of_anniversary
        self.month_of_anniversary = month_of_anniversary
        self.anniversary_year = anniversary_year
        self.address2 = address2
        self.phone2 = phone2
        self.photo = photo
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return self.id == other.id and self.first_name == other.first_name and self.last_name == other.last_name