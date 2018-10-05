from django.apps import AppConfig

class ImagesConfig(AppConfig):
    """docstring for ImageConfig."""
    name = 'images'
    verbose_name = 'Image bookmarks'

    def ready(self):
        # import signal handlers
        import images.signals
