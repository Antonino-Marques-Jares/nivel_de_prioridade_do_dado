# Função calcularPrioridade() define um método mensurável para calcularmos a prioridade dos dados

Ao **mensurarmos os valores de prioridade de cada dado** estamos definindo a **ordem de trabalho**.

Tendo em vista termos muitos dados a serem validados e tratados na gestão de dados, definir a ordem de trabalho é de grande importância.

O valor de prioridade é calculado considerando os **características** e seu **peso** :

* **valoNegocio** : Mede o impacto positivo do dado nos objetivos da empresa — receita, decisões estratégicas, vantagem competitiva, eficiência operacional.
* **risco** : Mede a exposição a danos — financeiros, regulatórios, reputacionais ou operacionais.
* **uso** : Mede a dependência operacional — quantos processos, dashboards, APIs ou áreas dependem dele.
* **compliance** : Mede a obrigação externa — LGPD, GDPR, BACEN, ANS, SOX, contratos, auditorias.
* **sensibilidade** : Mede o grau de restrição de acesso — público, interno, confidencial, restrito.

**O peso representa a importância que a instituição dá a uma característica**, por isso o valor da característica é multiplicado pelo peso.
