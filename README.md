# ChemTypeset
Chemical formula formatter for Anki.

A small Anki add-on that formats chemical formulas and reactions inside `\chem{ ... }` blocks.  
It handles common chemistry notation (subscripts, charges, arrows, electrons, hydrate dots, etc.)  
and outputs clean HTML that looks good in Anki's reviewer.

Built for personal study decks, but useful for anyone studying chemistry.

---

## Features

Only text inside `\chem{ ... }` is processed. Everything else is left untouched.

### Subscripts
H2O → H₂O  
SO4 → SO₄  
Ca(OH)2 → Ca(OH)₂  

### Superscripts (charges / oxidation states)
Fe^3+  → Fe³⁺  
SO4^2- → SO₄²⁻  
MnO4^- → MnO₄⁻  

### Reaction arrows
<=> → ⇌  
->  → →  
<-  → ←  

(HTML-escaped forms like &lt;=&gt; are also supported.)

### Electrons & protons
e- → e⁻  
H+ → H⁺  

### Hydrate dot
CuSO4*5H2O → CuSO₄·5H₂O  

### State symbols (smaller)
(aq), (g), (l), (s)

### Consistent font
All formatted chemistry is rendered in **Arial**.

---

## Usage

Wrap expressions in:

**\chem{ ... }**

Examples:

\chem{H2O}  
\chem{SO4^2-}  
\chem{Zn(s) -> Zn^2+ (aq) + 2e-}  
\chem{N2(g) <=> 2NH3(g)}  
\chem{CuSO4*5H2O(s)}  

Expected output:

- H₂O  
- SO₄²⁻  
- Zn(s) → Zn²⁺ (aq) + 2e⁻  
- N₂(g) ⇌ 2NH₃(g)  
- CuSO₄·5H₂O(s)

---

## Example snippet

\chem{H2O}

\chem{SO4^2-}

\chem{[Cu(NH3)4]^2+}

\chem{Zn(s) -> Zn^2+ (aq) + 2e-}

\chem{2H2O(l) + 2e- -> H2(g) + 2OH-(aq)}

\chem{N2(g) + 3H2(g) <=> 2NH3(g)}

\chem{CO(g) + H2O(g) <- CO2(g) + H2(g)}

\chem{CuSO4*5H2O(s)}

---

## Output

<img width="845" height="754" alt="prev" src="https://github.com/user-attachments/assets/14c2160e-7d8f-4c4f-b0e7-26a922b74a1e" />



---
## Installation

1. In Anki: **Tools → Add-ons → View Files**  
2. Create a folder inside `addons21/` (e.g., `chemtypeset`)  
3. Place `__init__.py` into that folder  
4. Restart Anki  

The add-on loads automatically when Anki starts.

---

## License

MIT License. Feel free to use, modify, or fork.
