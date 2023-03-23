import sys

from src.infrastructure.containers import TelegramHandlerContainer
from src.infrastructure.init import run_telegram_handler

app = TelegramHandlerContainer()
app.config.from_yaml('config.yaml')
app.wire(packages=[
    'src.image',
    'src.infrastructure',
    'src.telegram',
    'src.utils',
])

try:
    run_telegram_handler(sys.argv[1])
    # with open('test', 'a') as f:
    #     f.write(sys.argv[1])

    # print(sys.argv[1])
except (IndexError,):
    raise SystemExit()
