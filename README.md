# Les Grecques — sensibilités et bornes d'arbitrage

Bibliothèque Python des sensibilités analytiques de Black-Scholes, accompagnée d'une
interface graphique PyQt et d'une note sur les bornes de non-arbitrage des prix
d'options.

## Contenu

| Fichier | Description |
|---|---|
| `black_scholes.py` | Formule fermée de Black-Scholes (call / put) |
| `Bornes et grecques/les_grecques.py` | Delta, Gamma, Theta, Rho, Vega analytiques |
| `Bornes et grecques/grecques_app.py` | Interface graphique PyQt (`Ui_MainWindow`) |
| `Bornes et grecques/bornes et grecques.pdf` | Note théorique : bornes d'arbitrage et démonstration des grecques |

## Formules implémentées

Avec
$d_1 = \dfrac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$ et
$d_2 = d_1 - \sigma\sqrt{T}$ :

| Grecque | Call | Put |
|---|---|---|
| Prix | $S\Phi(d_1) - Ke^{-rT}\Phi(d_2)$ | $Ke^{-rT}\Phi(-d_2) - S\Phi(-d_1)$ |
| Delta | $\Phi(d_1)$ | $\Phi(d_1) - 1$ |
| Gamma | $\dfrac{\varphi(d_1)}{S\sigma\sqrt{T}}$ | idem |
| Vega | $S\varphi(d_1)\sqrt{T}$ | idem |
| Theta | $-\dfrac{S\varphi(d_1)\sigma}{2\sqrt{T}} - rKe^{-rT}\Phi(d_2)$ | $-\dfrac{S\varphi(d_1)\sigma}{2\sqrt{T}} + rKe^{-rT}\Phi(-d_2)$ |
| Rho | $KTe^{-rT}\Phi(d_2)$ | $-KTe^{-rT}\Phi(-d_2)$ |

Gamma et Vega sont identiques pour le call et le put, ce qui découle directement de la
parité call-put.

## Signature commune

```python
black_scholes(S, K, T, r, sigma, style)   # style = "call" ou "put"
delta(S, K, T, r, sigma, style)
gamma(S, K, T, r, sigma, style)
theta(S, K, T, r, sigma, style)
rho(S, K, T, r, sigma, style)
vega(S, K, T, r, sigma)
```

- `S` : prix spot du sous-jacent
- `K` : prix d'exercice
- `T` : maturité en années
- `r` : taux sans risque continu
- `sigma` : volatilité annualisée

## Bornes d'arbitrage

Le PDF joint établit les bornes que tout prix d'option doit respecter sous peine
d'arbitrage, notamment

$$\max(S - Ke^{-rT},\, 0) \le C \le S,
\qquad \max(Ke^{-rT} - S,\, 0) \le P \le Ke^{-rT}$$

ainsi que la monotonie et la convexité du prix par rapport au strike. Ces bornes
servent de test de cohérence pour tout pricer numérique développé par ailleurs
(arbres, Monte Carlo, différences finies).

## Interface graphique

`grecques_app.py` fournit une fenêtre PyQt (`Ui_MainWindow`) où l'utilisateur saisit
les paramètres du contrat et lit le prix ainsi que les cinq sensibilités.

```bash
pip install PyQt6 numpy scipy matplotlib
python "Bornes et grecques/grecques_app.py"
```

## Dépendances

```
numpy scipy matplotlib PyQt6
```

## Voir aussi

- [`binomial_-_trinomial_model`](https://github.com/Cklmens/binomial_-_trinomial_model) — mêmes grecques par arbres, pour comparaison numérique
- [`Pricing-des-options-par-simulation-de-Monte-Carlo`](https://github.com/Cklmens/Pricing-des-options-par-simulation-de-Monte-Carlo) — approche Monte Carlo
