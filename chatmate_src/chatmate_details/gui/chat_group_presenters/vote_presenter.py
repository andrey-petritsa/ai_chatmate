class VotePresenter:
    def __init__(self):
        self.options = []

    def set_options(self, options):
        self.options = options

    def present(self, vote_stats):
        if len(vote_stats) == 0:
            return "Никто не голосовал! Победителя нет"

        view_vote_stats = []
        for i, vote_stat in enumerate(vote_stats):
            view_vote_stat = self.__get_view_vote_stat(i, vote_stat)
            view_vote_stats.append(view_vote_stat)
        return '\n'.join(view_vote_stats)

    def __get_view_vote_stat(self, i, vote_stat):
        position = self.__get_position(i)
        option = self.options[vote_stat['option_number'] - 1]
        voters = self.__get_voters(vote_stat)
        message_parts = [position, option, voters]
        view_vote_stat = '\n'.join(message_parts)
        return view_vote_stat

    def __get_voters(self, stat):
        return "Голосовавшие: " + ', '.join(stat['voters'])

    def __get_position(self, i):
        return 'Победитель' if i == 0 else f'{i + 1} место'
