class Bank:
    def __init__(self, balance: list[int]):
        self.bal = balance
        self.n = len(balance)

    def valid(self, acc: int) -> bool:
        return 1 <= acc <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.valid(account1) or not self.valid(account2) or self.bal[account1 - 1] < money:
            return False
        self.bal[account1 - 1] -= money
        self.bal[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.valid(account):
            return False
        self.bal[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.valid(account) or self.bal[account - 1] < money:
            return False
        self.bal[account - 1] -= money
        return True


# Simple tests consistent with repository style (print + assert)
def test_bank():
    # Test 1: Basic deposit
    bank1 = Bank([10, 100, 20, 50, 30])
    result1 = bank1.deposit(3, 10)
    print("Test 1: Deposit(3, 10) ->", result1, "Balance:", bank1.bal)
    assert result1 is True
    assert bank1.bal == [10, 100, 30, 50, 30]

    # Test 2: Basic withdraw
    bank2 = Bank([10, 100, 20, 50, 30])
    result2 = bank2.withdraw(3, 10)
    print("Test 2: Withdraw(3, 10) ->", result2, "Balance:", bank2.bal)
    assert result2 is True
    assert bank2.bal == [10, 100, 10, 50, 30]

    # Test 3: Invalid account
    bank3 = Bank([10, 100, 20, 50, 30])
    result3_1 = bank3.deposit(6, 100)
    result3_2 = bank3.withdraw(0, 10)
    print("Test 3: Invalid account (deposit, withdraw) ->", result3_1, result3_2)
    assert result3_1 is False
    assert result3_2 is False

    # Test 4: Withdraw insufficient funds
    bank4 = Bank([10, 100, 20, 50, 30])
    result4 = bank4.withdraw(3, 30)
    print("Test 4: Withdraw insufficient funds ->", result4)
    assert result4 is False
    assert bank4.bal == [10, 100, 20, 50, 30]

    # Test 5: Basic transfer
    bank5 = Bank([10, 100, 20, 50, 30])
    result5 = bank5.transfer(5, 1, 20)
    print("Test 5: Transfer(5, 1, 20) ->", result5, "Balance:", bank5.bal)
    assert result5 is True
    assert bank5.bal == [30, 100, 20, 50, 10]

    # Test 6: Transfer insufficient funds
    bank6 = Bank([10, 100, 20, 50, 30])
    result6 = bank6.transfer(5, 1, 40)
    print("Test 6: Transfer insufficient funds ->", result6)
    assert result6 is False
    assert bank6.bal == [10, 100, 20, 50, 30]

    # Test 7: Transfer to invalid account
    bank7 = Bank([10, 100, 20, 50, 30])
    result7 = bank7.transfer(3, 6, 10)
    print("Test 7: Transfer to invalid account ->", result7)
    assert result7 is False

    # Test 8: Multiple operations
    bank8 = Bank([0, 100])
    bank8.deposit(1, 50)
    bank8.withdraw(2, 30)
    bank8.transfer(2, 1, 10)
    print("Test 8: Multiple operations -> Balance:", bank8.bal)
    assert bank8.bal == [60, 60]

    # Test 9: Large amounts
    bank9 = Bank([1000, 2000, 3000])
    result9 = bank9.transfer(3, 2, 500)
    print("Test 9: Large amounts ->", result9, "Balance:", bank9.bal)
    assert result9 is True
    assert bank9.bal == [1000, 2500, 2500]

    # Test 10: Edge case - transfer exact balance
    bank10 = Bank([10, 20, 30, 40, 50])
    result10 = bank10.transfer(1, 2, 10)
    print("Test 10: Transfer exact balance ->", result10, "Balance:", bank10.bal)
    assert result10 is True
    assert bank10.bal == [0, 30, 30, 40, 50]

    print("All tests passed!")


if __name__ == "__main__":
    test_bank()