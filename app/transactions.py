import csv
from statistics import mean
from dataclasses import dataclass, field
from decimal import Decimal


CREDIT_CARD = "+"
DEBIT_CARD = "-"
MONTHS = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}


@dataclass
class MonthResume:

    name: str
    month_number: int
    debit_transactions: list = field(default_factory=list)
    credit_transactions: list = field(default_factory=list)

    @property
    def debit_average(self):
        return mean([t["amount"] for t in self.debit_transactions])

    @property
    def credit_average(self):
        return mean([t["amount"] for t in self.credit_transactions])
    
    @property
    def transactions_count(self):
        return len(self.debit_transactions + self.credit_transactions)

    def store_transaction(self, sign, amount, date):
        transaction_ = {"amount": amount, "date": date}
        if sign == CREDIT_CARD:
            self.credit_transactions.append(transaction_)
        elif sign == DEBIT_CARD:
            self.debit_transactions.append(transaction_)


def process_transactions():
    # improve this name
    month_states = {}  # TODO type this
    with open("transactions.csv") as f:
        reader = csv.DictReader(f)
        total_balance = Decimal("0.00")
        debit_total_balance = Decimal("0.00")
        credit_total_balance = Decimal("0.00")
        for row in reader:
            month, year = row["date"].split("/")[1:]
            mont_year = f"{month}-{year}"
            if mont_year not in month_states:
                month_states[mont_year] = MonthResume(
                    name=MONTHS[int(month)],
                    month_number=int(month)
                )
            month_resume: MonthResume = month_states[mont_year]
            amount = Decimal(row["transaction"][1:])
            sign = row["transaction"][0]
            transaction_ = {"amount": amount, "date": row["date"]}
            if sign == CREDIT_CARD:
                month_resume.credit_transactions.append(transaction_)
                credit_total_balance += amount
            elif sign == DEBIT_CARD:
                month_resume.debit_transactions.append(transaction_)
                debit_total_balance += amount
            total_balance += amount
    return {
        "month_states": month_states,
        "total_balance": total_balance,
        "debit_total_balance": debit_total_balance,
        "credit_total_balance": credit_total_balance
    }