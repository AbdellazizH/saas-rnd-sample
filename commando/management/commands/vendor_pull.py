import helpers
from typing import Any
from django.core.management.base import BaseCommand

from django.conf import settings

STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js",
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Downloading Vendor static files...')
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            # self.stdout.write(f'Downloading {name}')
            dl_success = helpers.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(self.style.ERROR(f'Failed to download {url}'))
            print(name, url, out_path)

        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.style.SUCCESS('Successfully updated Vendor static files.!')
        else:
            self.stdout.write(self.style.ERROR('Some files were not updated.'))
