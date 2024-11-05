from django.core.management.base import BaseCommand
from typing import Any
from django.conf import settings

import helper


STATICFILES_VENDORS_DIR = getattr(settings, "STATICFILES_VENDORS_DIR")

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js",
}


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Download static links")
        completed_url = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDORS_DIR / name
            dl_success = helper.download_file(url, out_path)
            print(name, url)
            if dl_success:
                completed_url.append(url)
                self.stdout.write(self.style.SUCCESS(f"Successfully downloaded {name}"))
            else:
                self.stdout.write(self.style.ERROR(f"Error in downloading {name}"))

            # Check if all downloads were successful
            if set(completed_url) == set(VENDOR_STATICFILES.values()):
                self.stdout.write(self.style.SUCCESS(f"Success fully downloaded {url}"))
            else:
                self.stdout.write(self.style.ERROR(f"Error in downloading {url}"))
