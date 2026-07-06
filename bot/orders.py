from bot.client import BinanceClient


class OrderManager:
    def __init__(self, api_key, api_secret):
        self.client = BinanceClient(api_key, api_secret)

    def create_order(self, symbol, side, order_type, quantity, price=None):
        try:
            order = self.client.place_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )
            return order
        except Exception as e:
            return {"error": str(e)}
