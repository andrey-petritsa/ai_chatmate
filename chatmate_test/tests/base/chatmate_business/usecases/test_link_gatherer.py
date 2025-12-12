from mocks.platform_spy import PlatformSpy
from mocks.spy_link_repository import SpyLinkRepository
from chatmate_business.usecases.link_gatherer import LinkGatherer


class TestLinkGatherer:
    def setup_method(self):
        pass

    def test_gather(self):
        gatherer = LinkGatherer()
        gatherer.link_repository = SpyLinkRepository()
        gatherer.platform = PlatformSpy()

        gatherer.gather()

        links = gatherer.link_repository.get_links('spy')
        e_links = [
            {'platform': 'spy', 'id': 1, 'status': 'active'}
        ]
        assert links == e_links
