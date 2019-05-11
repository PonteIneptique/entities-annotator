from typing import Iterator, Tuple, List, Optional
import glob
import csv
from annotator.results import Match


_Textname = str

class Reader:
    def get_kwic(self, word: str, window: Tuple[int, int]) -> Iterator[Tuple[Match, _Textname]]:
        return []


class CsvReader(Reader):
    def __init__(self, glob_path: str):
        self.files: List[str] = glob.glob(glob_path)

    def get_kwic(self, word: str, window: Tuple[int, int] = (5, 5)):
        before, after = window
        for file in self.files:
            with open(file) as f:
                last = []
                current: Optional[str] = None
                reader = csv.DictReader(f, delimiter="\t")
                for line in reader:
                    if not line:
                        if current:
                            yield Match(last, current)
                        last = []
                        current = None
                        continue
                    last.append(line.get("form"))

                    if line.get("lemma") == word:
                        current = line.get("form")

                    try:
                        if current\
                            and current in last\
                                and last.index(current) <= before \
                                and len(last) >= before+after+1:
                            yield Match(last, current)
                            current = None
                    except:
                        print(current, last)
                        raise
                    if len(last) >= before+after+1:
                        last = last[1:]

                if current:
                    yield Match(last, current)
                    current = None


class LemmatizedCsvReader(CsvReader):
    def get_kwic(self, word: str, window: Tuple[int, int] = (5, 5)):
        yield from super(LemmatizedCsvReader, self).get_kwic(word.lower(), window)


if __name__ == "__main__":
    reader = LemmatizedCsvReader("/home/thibault/dev/LASLA/output/*.tsv")
    for match in reader.get_kwic("TREBELLENVS"):
        print(repr(match))
