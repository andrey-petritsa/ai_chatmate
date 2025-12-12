class LinkGatherer:
    def __init__(self):
        self.platform = None
        self.link_repository = None

    def gather(self):
        chat_links = self.platform.get_chat_links()
        links = [self.__to_link(link) for link in chat_links]
        self.link_repository.save_links(links)

    def __to_link(self, link):
        return {'platform':self.platform.get_name(), 'id':link, 'status':self.platform.get_link_status(link)}
