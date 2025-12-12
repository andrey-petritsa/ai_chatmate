from chatmate_details.gui.chat_group_presenters.vote_presenter import VotePresenter


class TestVotePresenter:
    def test_present(self):
        presenter = VotePresenter()
        presenter.set_options(['оп1', 'оп2'])
        vote_stats = [
            {'vote_count': 2, 'option_number': 1, 'voters': ['Андрей Петрица', 'Александр Пушкин']},
            {'vote_count': 1, 'option_number': 2, 'voters': ['Николай Николаевич']}
        ]

        e_view_vote_stat = ('Победитель\nоп1\nГолосовавшие: Андрей Петрица, Александр Пушкин'+
                            '\n2 место\nоп2\nГолосовавшие: Николай Николаевич')

        assert presenter.present(vote_stats) == e_view_vote_stat

    def test_present_no_options(self):
        presenter = VotePresenter()
        presenter.set_options(['оп1', 'оп2'])
        vote_stats = []

        e_view_vote_stat = "Никто не голосовал! Победителя нет"

        assert presenter.present(vote_stats) == e_view_vote_stat

