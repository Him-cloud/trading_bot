from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

from bot.logging_config import setup_logger

logger = setup_logger()

API_KEY = "eKA1UUPgKMoqZ0LO6NKoh5J9PUMh1iSqMNdft1nkLhRcrhdVvteNLX7BM5ko98Am"
API_SECRET = "ltaBXCvCbc6vt0UoY0Ql8ZSo2cSqGgMJhclbEL30NdybNOYSpQua0rAIVE8LdffL"


def main():
    print("=== Binance Futures Testnet Trading Bot ===")

    symbol = validate_symbol(input("Enter Symbol (e.g. BTCUSDT): "))
    side = validate_side(input("Enter Side (BUY/SELL): "))
    order_type = validate_order_type(input("Enter Order Type (MARKET/LIMIT): "))
    quantity = validate_quantity(input("Enter Quantity: "))

    price = None
    if order_type == "LIMIT":
        price = validate_price(input("Enter Price: "))

    manager = OrderManager(API_KEY, API_SECRET)

    result = manager.create_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price,
    )

    logger.info(f"Order Request: {symbol},{side},{order_type},{quantity},{price}")
    logger.info(f"Order Response:{result}")

    print("\nOrder Result:")
    print(result)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Error:{e}")
        print("Error:",e)