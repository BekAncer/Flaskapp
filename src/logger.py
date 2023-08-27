import logging
import asyncio
from models import Sneaker, db
from app import app


logger = logging.basicConfig(
    filename='report.log',
    encoding='utf-8',
    level=logging.INFO,
    filemode='a',
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)


def report() -> None:
    summ = 0
    count = 0
    with app.app_context():
        sneakers = db.session.execute(db.select(Sneaker).order_by(Sneaker.name)).scalars()
        for sneaker_info in sneakers:
            summ += sneaker_info.price
            count += 1
    logging.info(f'количество товара:{count} - сумма товара:{summ}')


async def report_timer(tme: int) -> None:
    task = asyncio.create_task(asyncio.to_thread(report))
    await asyncio.sleep(tme)
    await task


while True:
    asyncio.run(report_timer(10))
