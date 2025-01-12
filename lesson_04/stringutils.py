class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """

    def capitalize(self, string: str) -> str:
        return string.capitalize()

    def trim(self, string: str) -> str:
        whitespace = " "
        while (string.startswith(whitespace)):
            string = string.removeprefix(whitespace)
        return string

    def to_list(self, string: str, delimeter=",") -> list[str]:
        """
        Принимает на вход текст с разделителем и возвращает список строк. \n
        Параметры: \n
            `string` - строка для обработки \n
            `delimeter` - разделитель строк. По умолчанию запятая (",") \n
        Пример 1: `to_list("a,b,c,d") -> ["a", "b", "c", "d"]`
        Пример 2: `to_list("1:2:3", ":") -> ["1", "2", "3"]`
        """
        if (self.is_empty(string)):
            return []

        return string.split(delimeter)

    def contains(self, string: str, symbol: str) -> bool:
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass

        return res

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки \n
        Параметры: \n
            `string` - строка для обработки \n
            `symbol` - искомый символ для удаления \n
        Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
        Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`
        """
        if (self.contains(string, symbol)):
            string = string.replace(symbol, "")
        return string

    def starts_with(self, string: str, symbol: str) -> bool:
        return string.startswith(symbol)

    def end_with(self, string: str, symbol: str) -> bool:

        return string.endswith(symbol)

    def is_empty(self, string: str) -> bool:

        string = self.trim(string)
        return string == ""

    def list_to_string(self, lst: list, joiner=", ") -> str:

        string = ""
        length = len(lst)

        if length == 0:
            return string

        for i in range(0, length - 1):
            string += str(lst[i]) + joiner

        return string + str(lst[-1])
