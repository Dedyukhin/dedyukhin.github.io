---
layout: default
title: Research
permalink: /research/
---

<h1>Research</h1>

<h2>Publications</h2>
<ul class="publication-list">
  <li>
    <strong><a href="https://www.tandfonline.com/doi/full/10.1080/01900692.2024.2399133">Local Fiscal Health in Russia: An Achilles’ Heel of Fiscal Federalism?</a></strong>
    <div class="publication-info">International Journal of Public Administration</div>
    <div class="author-names">With Andrey Yushkov and Michael Alexeev</div>
    <button class="abstract-button" onclick="toggleAbstract('abstract_local_fiscal_health')">View Abstract</button>
    <div id="abstract_local_fiscal_health" class="abstract-container">
      This article is the first attempt to systematically study local public finance in contemporary Russia. We document that local governments do not have sufficient own-source revenues, are increasingly dependent on intergovernmental fiscal aid, lack access to market borrowing, and suffer from structural flaws in intergovernmental fiscal relations. We also present the results of the modified Brown’s 10-point test to compare local fiscal health across Russian regions, and assess the strength of local fiscal incentives in 2012–2021, demonstrating that local governments in Russia lack the capacity to foster local economic growth through the tax code.
    </div>
  </li>
</ul>

<h2>Working Papers</h2>
<ul class="publication-list">
  <li>
    <strong><a href="https://ssrn.com/abstract=4906864">Ownership, Asymmetric Information, and Quality of Care for the Elderly: Evidence From US Nursing Homes During the COVID-19 Pandemic</a></strong>
    <div class="publication-info">SSRN Working Paper</div>
    <div class="author-names">With Michael Alexeev and Leonid Polishchuk</div>
    <button class="abstract-button" onclick="toggleAbstract('abstract_nursing_homes')">View Abstract</button>
    <div id="abstract_nursing_homes" class="abstract-container">
      A common cause of market failures is asymmetric information. In such environments, nonprofit providers can offer additional quality assurance compared to for-profit entities. When quality becomes more observable and verifiable, market incentives align more closely with social welfare and the expected quality gap narrows. We explore this theoretically and empirically, using US nursing homes during the COVID-19 pandemic as a case study. The pandemic introduced new publicly observable measures (infection and death rates), revealing previously hidden aspects of care quality. We find significant initial gaps between for-profit and nonprofit facilities in infection rates, but these gaps declined as transparency increased, eventually reaching statistical parity. We also analyze local market structure, the reliability of the official ranking system, and potential learning-by-doing effects.
    </div>
  </li>
</ul>

<h2>Work in Progress</h2>
<ul class="publication-list">
  <li>
    <strong>When Cooperation Drives Continuation</strong>
    <button class="abstract-button" onclick="toggleAbstract('abstract_WCDC')">View Abstract</button>
    <div id="abstract_WCDC" class="abstract-container">
      This paper introduces a novel variant of the Indefinitely Repeated Prisoner’s Dilemma in which the probability of game continuation is endogenously determined by players’ actions. Theoretical analysis shows that the cooperation reward and continuation probability following mutual cooperation function as substitutes in sustaining cooperation. To test this, I conduct a laboratory experiment varying both parameters. Results suggest that while both mechanisms promote cooperation, increasing the reward is a more effective lever than conditioning future interaction on mutual cooperation.
    </div>
  </li>
</ul>

<script>
function toggleAbstract(id) {
  var abstract = document.getElementById(id);
  abstract.style.display = abstract.style.display === "block" ? "none" : "block";
}
</script>

<style>
  h1 {
    font-size: 2em;
    margin-bottom: 0.5em;
  }
  h2 {
    font-size: 1.5em;
    margin-top: 2em;
    margin-bottom: 0.5em;
  }
  .publication-list {
    list-style: none;
    padding-left: 0;
  }
  .publication-list li {
    margin-bottom: 1.5em;
  }
  .publication-info {
    font-style: italic;
    margin: 0.25em 0;
  }
  .author-names {
    font-weight: 500;
    margin-bottom: 0.25em;
  }
  .abstract-button {
    background-color: transparent;
    color: #b22222;
    border: none;
    padding: 3px 0;
    font-size: 14px;
    cursor: pointer;
    text-decoration: underline;
    transition: color 0.3s ease;
  }
  .abstract-button:hover {
    color: #0056b3;
  }
  .abstract-container {
    display: none;
    margin-top: 0.5em;
    padding-left: 0.5em;
    border-left: 2px solid #eee;
    color: #444;
    line-height: 1.4;
  }
</style>

