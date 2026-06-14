from binance.client import Client
from .config import API_KEY, API_SECRET

class BinanceEarnClient:
    """Wrapper around python‑binance Client for Earn endpoints."""
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)

    # Flexible Savings
    def get_flexible_savings_products(self):
        """Return list of flexible savings products (e.g., USDT)."""
        return self.client.savings_flexible_product_list()

    def purchase_flexible_savings(self, product_id: str, amount: float):
        """Purchase a flexible savings product.
        ``product_id`` is the Binance product identifier (e.g., "USDT").
        ``amount`` is the amount in the asset currency.
        """
        return self.client.savings_flexible_purchase(productId=product_id, amount=amount)

    # Staking (placeholder – add more wrappers as needed)
    def get_staking_products(self):
        return self.client.staking_product_list()

    def purchase_staking(self, product_id: str, amount: float):
        return self.client.staking_purchase(productId=product_id, amount=amount)

    # Dual Investment (placeholder)
    def get_dual_investment_products(self):
        return self.client.dual_investment_product_list()

    def purchase_dual_investment(self, product_id: str, amount: float, direction: str = "BUY"):
        return self.client.dual_investment_purchase(productId=product_id, amount=amount, direction=direction)
