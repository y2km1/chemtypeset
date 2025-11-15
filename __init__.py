import re
from aqt import gui_hooks

# Match \chem{ ... } blocks
chem_pattern = re.compile(r'\\chem\{(.*?)\}', re.DOTALL)

# Digits that should go to subscript (H2, SO4, (OH)2 etc.)
sub_pattern = re.compile(r'(?<=[A-Za-z\)\]])(\d+)')

# Superscripts via ^ notation (e.g. Fe^3+, SO4^2-)
sup_pattern = re.compile(r'\^([0-9]+[+-]?|[+-])')

# Standalone electrons (e-, e+)
electron_pattern = re.compile(r'(?<![A-Za-z0-9])e([+-])\b')

# Standalone protons (H+, H-)
proton_pattern = re.compile(r'(?<![A-Za-z0-9])H([+-])\b')

# Physical state symbols
state_pattern = re.compile(r'\((aq|g|l|s)\)')


def format_chem_inner(inner: str) -> str:
    """Convert \chem{} content into HTML-formatted chemistry."""

    # Reaction arrows (handles escaped HTML too)
    inner = inner.replace('<=>', '⇌').replace('&lt;=&gt;', '⇌')
    inner = inner.replace('->', '→').replace('-&gt;', '→')
    inner = inner.replace('<-', '←').replace('&lt;-', '←')

    # Hydrate dot
    inner = inner.replace('*', '·')

    # Subscripts
    inner = sub_pattern.sub(r'<sub>\1</sub>', inner)

    # e- / e+ 
    inner = electron_pattern.sub(r'e<sup>\1</sup>', inner)

    # H+ / H-
    inner = proton_pattern.sub(r'H<sup>\1</sup>', inner)

    # Superscripts via ^
    inner = sup_pattern.sub(r'<sup>\1</sup>', inner)

    # Smaller state symbols
    inner = state_pattern.sub(r'<span style="font-size: 80%;">(\1)</span>', inner)

    # Use a consistent font
    return f'<span style="font-family: Arial;">{inner}</span>'


def replace_chem(match: re.Match) -> str:
    return format_chem_inner(match.group(1))


def on_card_will_show(text: str, card, kind: str) -> str:
    # Replace all \chem{} occurrences in the card
    return chem_pattern.sub(replace_chem, text)


gui_hooks.card_will_show.append(on_card_will_show)