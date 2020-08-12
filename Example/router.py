from rest_framework import routers
from . import viewsets

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'colors', viewsets.ColorPalletViewsets, basename='colors')
