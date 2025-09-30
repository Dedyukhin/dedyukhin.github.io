---
layout: default
title: Research
permalink: /research/
---

<h2>Publications</h2>

<div class="pub-card">
  <div class="pub-header">
    <a class="pub-title" href="https://www.tandfonline.com/doi/full/10.1080/01900692.2024.2399133"><strong>Local fiscal health in Russia: An Achilles’ heel of fiscal federalism?</strong></a>
    <div class="publication-info">International Journal of Public Administration</div>
    <div class="author-names">With Andrey Yushkov and Michael Alexeev</div>
    <div class="button-group">
      <button class="abstract-button" onclick="toggleAbstract('abstract_local_fiscal_health')">View abstract</button>
      <!-- Example extra buttons kept close; add/remove as needed -->
      <a class="mini-btn" href="https://www.tandfonline.com/doi/pdf/10.1080/01900692.2024.2399133" target="_blank" rel="noopener">PDF</a>
      <a class="mini-btn" href="#" target="_blank" rel="noopener">Data</a>
      <a class="mini-btn" href="#" target="_blank" rel="noopener">Slides</a>
    </div>
  </div>

  <div id="abstract_local_fiscal_health" class="abstract-container">
    This article is the first attempt to systematically study local public finance in contemporary Russia. We document that local governments do not have sufficient own-source revenues, are increasingly more dependent on intergovernmental fiscal aid, lack access to market borrowing, and suffer from structural flaws in the design of intergovernmental fiscal relations. Additionally, we present the results of the modified Brown’s 10-point test to compare local fiscal health across the Russian regions. Finally, we assess the strength of local fiscal incentives in 2012–2021 and demonstrate that local governments in Russia lack capacity to foster local economic growth through the tax code.
  </div>
</div>

<h2>Working papers</h2>

<div class="pub-card">
  <div class="pub-header">
    <a class="pub-title" href="https://ssrn.com/abstract=4906864"><strong>Ownership, Asymmetric Information, and Quality of Care for the Elderly: Evidence From US Nursing Homes During the COVID-19 Pandemic</strong></a>
    <div class="publication-info">SSRN Working Paper</div>
    <div class="author-names">With Michael Alexeev and Leonid Polishchuk</div>
    <div class="button-group">
      <button class="abstract-button" onclick="toggleAbstract('abstract_nursing_homes')">View abstract</button>
      <a class="mini-btn" href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4906864" target="_blank" rel="noopener">SSRN</a>
      <a class="mini-btn" href="#" target="_blank" rel="noopener">Slides</a>
    </div>
  </div>

  <div id="abstract_nursing_homes" class="abstract-container">
    A common cause of market failures is asymmetric information. For this reason, the reliance on market incentives and signals requires that quality of goods and services is properly observable and verifiable. This requirement is hard to meet in the case of credence goods, including most social services. In such environment, nonprofit providers can offer additional quality assurance compared to for-profit entities. When quality becomes better observable and verifiable, and hence could earn a market premium, market incentives are closer aligned with social welfare, and the quality gap expected between nonprofit and for-profit provision is likely to narrow. We explore this conjecture theoretically and empirically, using in the empirical part the case of US nursing homes during the COVID-19 pandemic. The pandemic supplied new tangible and publicly observable nursing home performance measures such as infection and death rates among residents. These measures could serve as care quality indicators, revealing aspects and attributes of the nursing home care that remained hidden before the pandemic. The data reveal significant initial gaps between for-profit and nonprofit nursing homes in COVID-19 infection rates. However, in the ensuing catching-up process triggered by increased transparency, these gaps steadily declined, eventually leading to statistical parity between two types of ownership. We explore the role of local market structure in the adjustment of nursing home industry to the pandemic; retroactively evaluate the reliability of the official ranking system in predicting nursing homes' performance; and look for evidence of sustainable learning-by-doing effect of the pandemic.
  </div>
</div>

<h2>Work in progress</h2>

<div class="pub-card">
  <div class="pub-header">
    <span class="pub-title"><strong>When Cooperation Drives Continuation</strong></span>
    <div class="button-group">
      <button class="abstract-button" onclick="toggleAbstract('abstract_WCDC')">View abstract</button>
      <a class="mini-btn" href="#" target="_blank" rel="noopener">Design</a>
      <a class="mini-btn" href="#" target="_blank" rel="noopener">Slides</a>
    </div>
  </div>

  <div id="abstract_WCDC" class="abstract-container">
    This paper introduces a novel variant of the Indefinitely Repeated Prisoner’s Dilemma in which the probability of game continuation is endogenously determined by players’ actions. Theoretical analysis demonstrates that the cooperation reward and the probability of continuation following mutual cooperation function as substitutes when cooperation can be sustained as equilibrium - different combinations of these parameters can yield the same expected value from cooperation. To test the behavioral relevance of these dynamics, I conduct a laboratory experiment that varies both the reward from mutual cooperation and the continuation probability but only following mutual cooperation. The experimental results suggest that while both mechanisms promote cooperation, increasing the reward is likely a more effective lever than conditioning future interaction on mutual cooperation.
  </div>
</div>

<script>
function toggleAbstract(id) {
  var el = document.getElementById(id);
  el.style.display = (el.style.display === "block") ? "none" : "block";
  // Optional: scroll into view when opened
  if (el.style.display === "block") { el.scrollIntoView({ behavior: "smooth", block: "nearest" }); }
}
</script>

<style>
/* Card/box for each entry */
.pub-card{
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 14px 16px;
  margin: 14px 0 18px;
  background: #fafafa;
}

/* Header area keeps buttons close to the text */
.pub-header{
  display: flex;
  flex-direction: column;
  gap: 4px;
}

/* Title and meta */
.pub-title{
  text-decoration: none;
}
.publication-info{
  font-style: italic;
  opacity: 0.85;
}
.author-names{
  font-weight: 600;
}

/* Tight inline button row directly under meta */
.button-group{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 2px; /* keeps buttons very close to text */
}

/* Abstract toggle button */
.abstract-button{
  background: transparent;
  border: none;
  padding: 4px 8px;
  font-size: 14px;
  cursor: pointer;
  text-decoration: underline;
  color: #dc143c;
}
.abstract-button:hover{ color:#0056b3; }

/* Extra small link-buttons that sit next to the abstract button */
.mini-btn{
  display: inline-block;
  font-size: 12px;
  padding: 4px 8px;
  border-radius: 999px;
  border: 1px solid #ddd;
  text-decoration: none;
  line-height: 1.2;
}
.mini-btn:hover{ background:#f3f4f6; }

/* Abstract sits inside the same box */
.abstract-container{
  display: none;
  border-top: 1px dashed #e5e7eb;
  margin-top: 10px;
  padding-top: 10px;
}
</style>
