from typing import Any
import foolbox
import keras

class Attack:
    loops = 10
    model = None
    report = False
    reportDir = "./report"

    def __init__(self, model, loops, report = False, report_dir = "./report") -> None:
        super().__init__()

    def single(self, data, attack):
        return "A"

    def all(self, data):
        return "B"

    def any_of(self,data,attacks):
        return "C"


