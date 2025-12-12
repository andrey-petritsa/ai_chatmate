from chatmate_business.usecases.get_chats_command import GetChatsCommand
from mocks.platform_spy import PlatformSpy
from mocks.spy_link_repository import SpyLinkRepository


class TestGetChatsCommand:
    def test_execute(self):
        cmd = GetChatsCommand()
        cmd.link_repository = SpyLinkRepository()
        cmd.platform = PlatformSpy()
        cmd.link_repository.save_links([{'platform': 'spy', 'id': 1, 'status': 'active'}])
        chats = cmd.execute()
        assert len(chats) != 0
