import argparse
from src.client import BinanceEarnClient
from src.strategy import EarnStrategy, AllocationRule

def main():
    parser = argparse.ArgumentParser(description="Run Binance Earn strategy")
    parser.add_argument("--capital", type=float, required=True, help="Total capital to allocate (in base asset, e.g., USDT)")
    args = parser.parse_args()

    client = BinanceEarnClient()
    # Example strategy – allocate all capital to flexible savings
    strategy = EarnStrategy(
        name="AllFlexibleSavings",
        allocations=[AllocationRule(product_type="flexible_savings", weight=1.0)],
        min_balance=0.0,
    )
    strategy.execute(client, args.capital)
    print("Strategy execution completed.")

if __name__ == "__main__":
    main()
