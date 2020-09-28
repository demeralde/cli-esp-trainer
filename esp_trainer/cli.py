import random
from typing import List

from colorama import Fore, Style
from tabulate import tabulate


class CLI:
    ANSWER_RANGE_START: int = 1
    ANSWER_RANGE_END: int = 5  # 4
    ALL_MILESTONES = (6, 8, 10, 12, 14)

    total_trials: int = 24
    current_trial: int = 0
    hits: int = 0
    hit_milestones: List[int] = []

    def __init__(self):
        print(Style.DIM + "\nStarting game...")
        self._reset_styles()
        print(f"Total trials: {self.total_trials}\n\n")

    def _check_number(self, selected_number: int, correct_number: int) -> bool:
        return selected_number == correct_number

    def _print_milestone(self):
        for milestone in reversed(self.ALL_MILESTONES):
            if self.hits == milestone and milestone not in self.hit_milestones:
                print(Fore.LIGHTMAGENTA_EX +
                      f"\n> Well done! You've hit milestone #{milestone}.")
                self.hit_milestones.append(milestone)

    def _print_trial_result(self, result: bool, correct_number: int):
        if result == True:
            print("Hit.")
        else:
            print("Miss. " + Fore.LIGHTYELLOW_EX +
                  f"(correct number: {correct_number})")
        self._print_milestone()
        print("\n")
        self._reset_styles()

    def _tally_result(self, result):
        if result == True:
            self.hits = self.hits + 1

    def _print_final_result(self):
        misses: int = self.total_trials - self.hits
        hit_ratio_decimal: int = self.hits / self.total_trials
        hit_ratio_percentage = round(hit_ratio_decimal * 100, 2)
        milestones_comma_list = ", ".join(map(str, self.hit_milestones))
        milestones_formatted = f"[{milestones_comma_list}]"

        table = (
            ("Hits", self.hits),
            ("Misses", misses),
            ("Hit ratio", f"{hit_ratio_percentage}%"),
            ("Total trials", f"{self.total_trials}"),
            ("Milestones", milestones_formatted)
        )
        print("RESULTS:")
        print(tabulate(table, tablefmt="psql"))

    def _reset_styles(self):
        print(Style.RESET_ALL, end="")

    def _prompt_selected_number(self) -> str:
        trial_fraction: str = f"{self.current_trial}/{self.total_trials}"
        input_message: str = f"[{trial_fraction}] Which number is it? (1-4) "
        selected_number = input(Style.DIM + input_message + Style.BRIGHT)
        self._reset_styles()
        return selected_number

    def _validate_selected_number(self):
        pass

    def _get_selected_number(self):
        selected_number: int

        while True:
            try:
                selected_number = int(self._prompt_selected_number())
                if selected_number in range(self.ANSWER_RANGE_START, self.ANSWER_RANGE_END):
                    break
            except Exception:
                print("Invalid number entered.\n")

        return selected_number

    def _update_current_trial(self):
        self.current_trial = self.current_trial + 1

    def run_trainer(self):
        while self.current_trial < self.total_trials:
            self._update_current_trial()
            selected_number: int = self._get_selected_number()
            correct_number: int = random.randrange(
                self.ANSWER_RANGE_START, self.ANSWER_RANGE_END,
            )

            result = self._check_number(selected_number, correct_number)
            self._tally_result(result)
            self._print_trial_result(result, correct_number)

        self._print_final_result()
