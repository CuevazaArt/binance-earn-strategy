from pydantic import BaseModel, Field
from typing import List
from .client import BinanceEarnClient

class AllocationRule(BaseModel):
    product_type: str  # e.g., "flexible_savings", "staking", "dual_investment"
    weight: float = Field(ge=0, le=1, description="Proportion of capital to allocate")

class EarnStrategy(BaseModel):
    name: str
    allocations: List[AllocationRule]
    min_balance: float = 0.0  # Minimum amount to keep in spot wallet

    def execute(self, client: BinanceEarnClient, total_capital: float):
        """Execute the strategy by allocating capital according to the defined weights.
        This simple implementation assumes the product types map to client methods.
        """
        available = total_capital - self.min_balance
        if available <= 0:
            raise ValueError("Insufficient capital after reserving min_balance.")

        for rule in self.allocations:
            amount = available * rule.weight
            if amount <= 0:
                continue
            if rule.product_type == "flexible_savings":
                # Example: purchase USDT flexible savings
                client.purchase_flexible_savings(product_id="USDT", amount=amount)
            elif rule.product_type == "staking":
                client.purchase_staking(product_id="DOT", amount=amount)
            elif rule.product_type == "dual_investment":
                client.purchase_dual_investment(product_id="BTC", amount=amount)
            else:
                raise NotImplementedError(f"Unsupported product_type: {rule.product_type}")
