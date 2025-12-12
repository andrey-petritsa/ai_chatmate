class SpyLinkRepository:
    def __init__(self):
        self.links = []

    def get_links(self, platform):
        return self.links

    def save_links(self, links):
        self.links = links
