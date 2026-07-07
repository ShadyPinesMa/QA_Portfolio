from dataclasses import dataclass

@dataclass()
class CheckoutData:
    first_name: str
    last_name: str
    email: str
    address1: str
    address2: str = ""
    country: str = ""
    city: str = ""
    zip: str = ""
    cc_name: str = ""
    cc_number: str = ""
    exp_date: str = ""
    cvv: str = ""