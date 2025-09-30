import sys
from bank_account import BankAccount
from robust_division_calculator import safe_divide


def main():
    # Create a bank account with an initial balance of 100
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<params>")
        print("Commands:")
        print("  deposit:<amount>   - Deposit money into account")
        print("  withdraw:<amount>  - Withdraw money from account")
        print("  display            - Show account balance")
        print("  divide:<num>,<den> - Divide two numbers safely")
        sys.exit(1)

    command, *params = sys.argv[1].split(":")

    # --- BankAccount commands ---
    if command == "deposit" and params:
        amount = float(params[0])
        account.deposit(amount)
        print(f"Deposited: ${amount}")

    elif command == "withdraw" and params:
        amount = float(params[0])
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    elif command == "display":
        account.display_balance()

    # --- Robust Division command ---
    elif command == "divide" and params:
        try:
            numerator, denominator = params[0].split(",")
            result = safe_divide(numerator, denominator)
            print(result)
        except ValueError:
            print("Usage for division: divide:<numerator>,<denominator>")

    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
