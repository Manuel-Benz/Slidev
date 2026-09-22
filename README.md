# Slidev

Slidev-Präsentationen für den Mathematikunterricht.

## Start

```bash
npm install
npm run dev      # Präsentation im Browser, http://localhost:3030
npm run export   # PDF-Export
```

## Inhalt

- `slides.md`: Probability, Kapitel 11 F (addition law) und G (independent events), Mathematics Core Topics HL
- `components/Venn.vue`: Venn-Diagramm für zwei Ereignisse (`shade`, `disjoint`, `regions`)
- `setup/katex.ts`: KaTeX-Makro `\P` für die Wahrscheinlichkeit
