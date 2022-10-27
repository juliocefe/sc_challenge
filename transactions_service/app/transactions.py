import csv
from statistics import mean
from dataclasses import dataclass, field
from decimal import Decimal


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
class MonthStats:

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


class TransactionsProcessor:

    CREDIT_CARD = "+"
    DEBIT_CARD = "-"

    def __init__(self, file_name):
        self.file_name = file_name
        self.total_balance = Decimal("0.00")
        self.debit_total_balance = Decimal("0.00")
        self.credit_total_balance = Decimal("0.00")
        self.month_stats = {}
        self.process_data()

    def process_transaction(self, raw_data: dict, month: MonthStats):
        sign = raw_data["transaction"][0]
        transaction = {
            "amount": Decimal(raw_data["transaction"][1:]), 
            "date": raw_data["date"],
        }
        if sign == self.CREDIT_CARD:
            month.credit_transactions.append(transaction)
            self.credit_total_balance += transaction["amount"]
        elif sign == self.DEBIT_CARD:
            month.debit_transactions.append(transaction)
            self.debit_total_balance += transaction["amount"]
        self.total_balance += transaction["amount"]

    def process_data(self):
        # TODO delete file after
        with open(self.file_name) as f:
            data = csv.DictReader(f)
            for row in data:
                month, year = row["date"].split("/")[1:]
                month_id = f"{month}-{year}"
                if month_id not in self.month_stats:
                    self.month_stats[month_id] = MonthStats(
                        name=MONTHS[int(month)],
                        month_number=int(month)
                    )
                month_stats: MonthStats = self.month_stats[month_id]
                self.process_transaction(row, month_stats)

    @property
    def data(self):
        return {
            "month_stats": self.month_stats,
            "total_balance": self.total_balance,
            "debit_total_balance": self.debit_total_balance,
            "credit_total_balance": self.credit_total_balance
        }
