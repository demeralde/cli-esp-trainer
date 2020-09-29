# cli-esp-trainer 🧙‍♂️️

ESP trainer that runs in your terminal. The idea is inspired by [Russell Targ's ESP trainer](http://www.espresearch.com/iphone/) and is based on sound parapsychological study design.

![Screenshot of cli-esp-trainer](assets/preview.png?raw=true "Screenshot of cli-esp-trainer")

## How it works ✨

1. There's 24 trials.
2. Each trial has four numbers to select from. You guess which number is going to be next.
3. If you're right, you score a hit.
4. If you're wrong, it's a miss. The correct number is displayed.
5. At the end, your results are tallied.

This trains you to distinguish an intuitive hunch from mental noise. True intuition should feel like a magnetic pull towards the correct number.

If your result is statistically significant, this is a clear indication of ESP. The milestones are 6, 8. 10, 12, or 14 hits. Frequently scoring 12 or more is considered highly developed ESP.

### Features 📔

#### Current

- Track your score against milestones of ESP ability
- Fast, minimal UI
- Cross-platform
- Coloured text
- Pretty table to display results

#### Future ideas

- Improved number selection prompt
- Customise amount of trials or or number range to select from
- Ability to skip trials
- Export results into .csv file (or maybe SQLite DB)
- Visualise improvements in results over time with pretty ASCII charts
- Interactive shell (so you can play again without needing to reload the script)
- `--help` command to provide info from the terminal
- Code quality improvements (tests, linting)
- CI/CD
- Info website for the CLI
- Progressive web app
- Public leaderboards
- Plot different variables (such as your meditation experience or a rating on how you're feeling), to see how this correlates with results
- Seamless integration with my upcoming meditation app's API (so some of these variables can be inferred)
- Public statistics for open parapsychology research
- Settings menu
- Ability to abort game and go back to the menu
- Toggle between different themes
- CLI animations
- General ASCII art
- Extra results stats
- 8-bit sound effects
- `cmatrix` Easter egg if you make a shit tonne of hits
- Gamble on your success with crypto
- IRC channel to meet like-minded panpsychists and the like
- Tarot deck CLI app of the same style as this project

### Scientific evidence 🧪

The proof of ESP is out of the scope of this README. The evidence is extremely strong despite the controversy. Look at the work of both Russell Targ and Dean Radin if you're not convinced.

### Improving your score 📈

To improve your score, do consciousness work (especially meditation). Psychedelics also help (but do so at your own risk, I can't recommend it unless you know what you're doing).

## Installation 🚀

### Dependencies

* Python 3.8.2 (lower versions of 3 will probably work, but haven't been tested)

### Instructions

Install the CLI client:

```sh
pip3 install esp-trainer
```

Run the script:

```sh
esp-trainer
```

## Development 👨‍💻

Install dependencies with [Pipenv](https://pipenv.pypa.io/en/latest/):

```sh
pipenv install --dev
```

Then open the project with your preferred editor. If possible, it's also recommended to install the [EditorConfig](https://editorconfig.org) plugin.

Open the Pipenv shell:

```sh
pipenv shell
```

Open the script:

```sh
ipython -m esp_trainer
```

That's it. Start coding.

## Donations ₿

If you like this project and want to support my endeavors, feel free to send Bitcoin to the following address: `148X9eN1Yy287Xn245j7fqLsESnnaNePyU`
