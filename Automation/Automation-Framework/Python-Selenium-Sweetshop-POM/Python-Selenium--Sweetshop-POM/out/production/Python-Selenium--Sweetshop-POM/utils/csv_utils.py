import csv
from models.checkout_data import CheckoutData

def load_checkout_data(filename):
    data = []

    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data.append(
                CheckoutData(
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    email=row["email"],
                    address1=row["address1"],
                    address2=row["address2"],
                    country=row["country"],
                    city=row["city"],
                    zip=row["zip"],
                    cc_name=row["cc_name"],
                    cc_number=row["cc_number"],
                    exp_date=row["exp_date"],
                    cvv=row["cvv"],
                )
            )

    return data