class Company:
    def __init__(self, nickname, trade_name, legal_name, cnpj, uf, city, logo):
        self.nickname = nickname
        self.trade_name = trade_name
        self.legal_name = legal_name
        self.cnpj = cnpj
        self.uf = uf
        self.city = city
        self.logo = logo
        self.contracts = []

    def add_contract(self, contract):
        self.contracts.append(contract)
