---
theme: default
title: The Addition Law and Independent Events
info: |
  IB Mathematics HL Core Topics, Chapter 11 (Probability), sections F and G
class: text-center
transition: slide-left
mdc: true
drawings:
  persist: false
---

# Probability

## F The addition law · G Independent events

IB Mathematics HL Core, Chapter 11

---

# Compound events

We consider more than one event in the same sample space $U$.

<div class="grid grid-cols-2 gap-8 mt-6 items-center">
<div>

<v-click>

$A \cap B$: both $A$ and $B$ occur

read: “$A$ intersection $B$”

</v-click>

<v-click>

$A \cup B$: $A$ or $B$ or both occur

read: “$A$ union $B$”

</v-click>

</div>
<div class="text-center">

<v-click at="1">
<Venn shade="intersection" :width="260" />
</v-click>

<v-click at="2">
<Venn shade="union" :width="260" />
</v-click>

</div>
</div>

<!--
Mengennotation aus Kapitel Sets wiederholen: "und" = Schnitt, "oder" = Vereinigung (inklusives oder).
-->

---

# Warm-up: counting

$U = \{x \mid x \text{ is a positive integer less than } 100\}$, $A$ = multiples of 7, $B$ = multiples of 5

<div class="grid grid-cols-2 gap-8 mt-4 items-center">
<div>

<v-clicks>

- $n(A) = 14$, $n(B) = 19$
- $n(A \cap B) = 2$ (35 and 70)
- $n(A \cup B) = 31$, not $14 + 19 = 33$
- 35 and 70 were counted twice

</v-clicks>

<v-click>

$$
n(A \cup B) = n(A) + n(B) - n(A \cap B)
$$

</v-click>

</div>
<div class="text-center">

<v-click at="2">
<Venn :regions="['12', '2', '17', '68']" :width="300" />
</v-click>

</div>
</div>

<!--
Ersetzt die (gestrichene) Investigation 3 in 2 Minuten. Klasse zuerst selbst zählen lassen.
-->

---

# The addition law of probability

Divide by $n(U)$:

<div class="law">

For two events $A$ and $B$:

$$
\P(A \cup B) = \P(A) + \P(B) - \P(A \cap B)
$$

$\P(\text{either } A \text{ or } B \text{ or both}) = \P(A) + \P(B) - \P(\text{both } A \text{ and } B)$

</div>

<v-click>

Example 13: If $\P(A) = 0.6$, $\P(A \cup B) = 0.7$ and $\P(A \cap B) = 0.3$, find $\P(B)$.

</v-click>

<v-click>

$$
\begin{aligned}
0.7 &= 0.6 + \P(B) - 0.3 \\
\P(B) &= 0.4
\end{aligned}
$$

</v-click>

---
layout: two-cols
---

# Mutually exclusive events

$A$ and $B$ are mutually exclusive (disjoint) if they cannot occur at the same time:

$$
A \cap B = \varnothing \quad \Rightarrow \quad \P(A \cap B) = 0
$$

<v-click>

<div class="law">

The addition law becomes

$$
\P(A \cup B) = \P(A) + \P(B)
$$

</div>

</v-click>

::right::

<div class="mt-20 text-center">
<Venn disjoint :width="320" />
</div>

---

# Example 14

30 students write a History test: 7 score an A, 11 score a B. One student is selected at random.

$A$: the student scored an A, $B$: the student scored a B

a) Are $A$ and $B$ mutually exclusive? b) Find $\P(A)$, $\P(B)$, $\P(A \cap B)$ and $\P(A \cup B)$.

<v-click>

a) A student cannot score both an A and a B, so $A$ and $B$ are mutually exclusive.

</v-click>

<v-click>

b) $\P(A) = \frac{7}{30}$, $\P(B) = \frac{11}{30}$, $\P(A \cap B) = 0$

$$
\P(A \cup B) = \frac{7}{30} + \frac{11}{30} = \frac{18}{30} = \frac{3}{5}
$$

</v-click>

---

# Exercise 1

$\P(A) = 0.35$, $\P(B) = 0.5$ and $\P(A \cup B) = 0.6$.

a) Find $\P(A \cap B)$. b) Find the probability that neither $A$ nor $B$ occurs. c) Are $A$ and $B$ mutually exclusive?

<v-click>

a)

$$
\P(A \cap B) = \P(A) + \P(B) - \P(A \cup B) = 0.35 + 0.5 - 0.6 = 0.25
$$

</v-click>

<v-click>

b) $\P((A \cup B)') = 1 - 0.6 = 0.4$

</v-click>

<v-click>

c) No, since $\P(A \cap B) = 0.25 \neq 0$.

</v-click>

---

# Exercise 2

A ticket is drawn at random from tickets numbered 1 to 20.

$A$: multiple of 3, $B$: multiple of 4, $C$: odd number

a) Find $\P(A \cup B)$. b) Are $B$ and $C$ mutually exclusive? Find $\P(B \cup C)$.

<v-click>

a) $A = \{3, 6, 9, 12, 15, 18\}$, $B = \{4, 8, 12, 16, 20\}$, $A \cap B = \{12\}$

$$
\P(A \cup B) = \frac{6}{20} + \frac{5}{20} - \frac{1}{20} = \frac{10}{20} = \frac{1}{2}
$$

</v-click>

<v-click>

b) Multiples of 4 are even, so $B \cap C = \varnothing$: mutually exclusive.

$$
\P(B \cup C) = \frac{5}{20} + \frac{10}{20} = \frac{3}{4}
$$

</v-click>

---
layout: center
class: text-center
---

# G Independent events

<div class="law text-left mt-8">

Two events are independent if the occurrence of each event does not affect the occurrence of the other.

</div>

---

# Coin and die

A coin is tossed and a die is rolled. Does the coin affect the die?

<div class="grid grid-cols-2 gap-8 mt-4 items-center">
<div>

<table class="grid-table">
<tr><th></th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr>
<tr><th>H</th><td>·</td><td>·</td><td>·</td><td>·</td><td>·</td><td v-click="1" class="hit">×</td></tr>
<tr><th>T</th><td>·</td><td>·</td><td>·</td><td>·</td><td>·</td><td>·</td></tr>
</table>

12 equally likely outcomes

</div>
<div>

<v-click at="1">

$$
\P(\text{H} \cap 6) = \frac{1}{12}
$$

</v-click>

<v-click at="2">

$$
\P(\text{H}) \cdot \P(6) = \frac{1}{2} \cdot \frac{1}{6} = \frac{1}{12}
$$

</v-click>

</div>
</div>

<v-click at="3">

<div class="law">

$A$ and $B$ are independent $\iff$ $\P(A \cap B) = \P(A) \cdot \P(B)$

</div>

</v-click>

<!--
Ersetzt Investigation 4. Die Produktregel ist zugleich Test für Unabhängigkeit.
-->

---

# Example

$A$ and $B$ are independent with $\P(A) = 0.3$ and $\P(B) = 0.5$. Find $\P(A \cap B)$ and $\P(A \cup B)$.

<v-click>

$$
\P(A \cap B) = 0.3 \cdot 0.5 = 0.15
$$

</v-click>

<v-click>

$$
\P(A \cup B) = 0.3 + 0.5 - 0.15 = 0.65
$$

</v-click>

<v-click>

<div class="warn">

Mutually exclusive $\neq$ independent. If $\P(A), \P(B) > 0$ and $A$, $B$ are mutually exclusive, then $\P(A \cap B) = 0 \neq \P(A) \cdot \P(B)$: if $A$ occurs, $B$ cannot occur. The events are dependent.

</div>

</v-click>

---

# Dependent events

Two events are dependent if the occurrence of one affects the probability of the other.

A bag contains 3 red and 2 blue marbles. Two marbles are drawn.

<div class="grid grid-cols-2 gap-8 mt-4">
<div>

<v-click>

with replacement (independent)

$$
\P(\text{R R}) = \frac{3}{5} \cdot \frac{3}{5} = \frac{9}{25}
$$

</v-click>

</div>
<div>

<v-click>

without replacement (dependent)

$$
\P(\text{R R}) = \frac{3}{5} \cdot \frac{2}{4} = \frac{3}{10}
$$

</v-click>

</div>
</div>

<v-click>

The second factor changes: after a red marble only 2 of 4 marbles are red.

</v-click>

<!--
Nur Ausblick; ausführlich mit Baumdiagramm und bedingter Wahrscheinlichkeit in den nächsten Abschnitten.
-->

---

# Exercise 3

$\P(A) = 0.4$, $\P(B) = 0.5$ and $\P(A \cup B) = 0.7$. Are $A$ and $B$ independent?

<v-click>

$$
\P(A \cap B) = 0.4 + 0.5 - 0.7 = 0.2
$$

</v-click>

<v-click>

$$
\P(A) \cdot \P(B) = 0.4 \cdot 0.5 = 0.2
$$

</v-click>

<v-click>

$\P(A \cap B) = \P(A) \cdot \P(B)$, so $A$ and $B$ are independent.

</v-click>

---

# Exercise 4

Two archers shoot at a target independently. Anna hits with probability 0.7, Ben with probability 0.6.

Find the probability that a) both hit, b) at least one hits, c) neither hits.

<v-click>

a) $\P(A \cap B) = 0.7 \cdot 0.6 = 0.42$

</v-click>

<v-click>

b) $\P(A \cup B) = 0.7 + 0.6 - 0.42 = 0.88$

</v-click>

<v-click>

c) $\P(A' \cap B') = 0.3 \cdot 0.4 = 0.12$ (check: $1 - 0.88 = 0.12$)

</v-click>

---
layout: center
class: text-center
---

# Practice

Exercise 11F: 1, 4, 5

<div class="text-sm opacity-60 mt-8">

Mathematics Core Topics HL, pp. 266–267

</div>
