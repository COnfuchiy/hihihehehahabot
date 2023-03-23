from src.infrastructure.containers import AppContainer
from src.infrastructure.init import run_app

app = AppContainer()
app.config.from_yaml('config.yaml')
app.wire(packages=[
    'src.image',
    'src.infrastructure',
    'src.telegram',
    'src.utils',
    'src.vk.api'
])

run_app()
