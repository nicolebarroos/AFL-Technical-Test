from datetime import datetime

class Contract:
    def __init__(self, validity_date, signing_date, fee, company):
        self.validity_date = datetime.strptime(validity_date, '%d-%m-%Y')
        self.signing_date = datetime.strptime(signing_date, '%d-%m-%Y')
        self.fee = fee #porcentafem
        self.services = {
            "Department A": ["BUY", "SELL", "EXCHANGE"],
            "Department B": ["BUY", "SELL", "EXCHANGE"]
        }
        self.company = company

    def list_services(self):
        for dept, services in self.services.items():
            print(f"{dept}: {', '.join(services)}")
