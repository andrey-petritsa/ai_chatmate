from chatmate_details.repository.in_file_link_repository import InFileLinkRepository


class TestInFileLinkRepository:
    def setup_method(self):
        pass

    def test_repository(self):
        rep = InFileLinkRepository()
        links = [{'platform': 'test', 'id': 1, 'status': 'active'}]
        rep.save_links(links)
        links = rep.get_links('test')

        assert links == [{'platform': 'test', 'id': 1, 'status': 'active'}]
