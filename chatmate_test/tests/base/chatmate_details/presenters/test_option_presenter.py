from chatmate_details.gui.chat_group_presenters.option_presenter import OptionPresenter

class TestOptionPresenter:
    def test_present(self):
        presenter = OptionPresenter()
        options = ['опция1', 'опция2']
        
        view_options = "Выберите следующую фразу\n1.опция1\n\n2.опция2"
        
        assert presenter.present(options) == view_options