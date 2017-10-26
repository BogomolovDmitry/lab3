class Gist ():
    # данные гистаграммы
    _data = None
    _data_sorting = dict()

    def __init__(self, date):
        self._data = date
        for number in date:
            self._data_sorting.update({number: self._data_sorting.get(number, 0) + 1})

    def print_hist(self):
        str_out = ""
        for age, stat in self._data_sorting.items():
            str_out += str(age).ljust(4) + str().ljust(stat, '#') + '\n'
        print( str_out)
