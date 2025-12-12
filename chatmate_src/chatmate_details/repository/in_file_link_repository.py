from pathlib import Path
import json
from filelock import FileLock

class InFileLinkRepository:
    OUTPUT_DIR = Path('./output')

    def get_links(self, platform):
        self.__ensure_output_dir()
        path = self.OUTPUT_DIR / f"{platform}_links.txt"
        lock = FileLock(str(path) + ".lock")
        with lock:
            if not path.exists():
                return []
            content = path.read_text(encoding='utf-8').strip()
            if not content:
                return []
            data = json.loads(content)
            if isinstance(data, list):
                return data
            return []

    def save_links(self, links):
        self.__ensure_output_dir()
        grouped = {}
        for link in links:
            platform = link.get('platform')
            if not platform:
                continue
            grouped.setdefault(platform, []).append(link)

        for platform, platform_links in grouped.items():
            path = self.OUTPUT_DIR / f"{platform}_links.txt"
            lock = FileLock(str(path) + ".lock")
            with lock:
                data_str = json.dumps(platform_links, ensure_ascii=False, indent=2)
                path.write_text(data_str, encoding='utf-8')

    def __ensure_output_dir(self):
        if not self.OUTPUT_DIR.exists():
            self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
