class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions_by_name = defaultdict(list)
        invalid_indices = set()
      
        for index, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)

            transactions_by_name[name].append((index, time, city))

            if amount > 1000:
                invalid_indices.add(index)

            for prev_index, prev_time, prev_city in transactions_by_name[name]:
                if prev_city != city and abs(time - prev_time) <= 60:
                    invalid_indices.add(index)
                    invalid_indices.add(prev_index)
      
        return [transactions[i] for i in invalid_indices]