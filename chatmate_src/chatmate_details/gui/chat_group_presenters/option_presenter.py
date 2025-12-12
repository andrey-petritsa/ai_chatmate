class OptionPresenter:
    def present(self, options):
        numbered_options = []
        for i, opt in enumerate(options, 1):
            numbered_options.append(f"{i}.{opt}")
        return "Выберите следующую фразу\n" + "\n\n".join(numbered_options)
