---
layout: default
title: Research
permalink: /research/
---

Publications
---
- **[Local fiscal health in Russia: An Achilles’ heel of fiscal federalism?](https://www.tandfonline.com/doi/full/10.1080/01900692.2024.2399133)**  
  <div class="publication-info">International Journal of Public Administration</div>  
  <div class="author-names">With Andrey Yushkov and Michael Alexeev</div>  
  <button class="abstract-button" onclick="toggleAbstract('abstract1')">View Abstract</button>
  <div id="abstract1" class="abstract-container">This paper discusses the fiscal health of local governments in Russia, analyzing the implications of fiscal federalism...</div>

Working papers
---
- **[Ownership, Asymmetric Information, and Quality of Care for the Elderly: Evidence From US Nursing Homes During the COVID-19 Pandemic](https://ssrn.com/abstract=4906864)**  
  <div class="publication-info">SSRN Working Paper</div>  
  <div class="author-names">With Michael Alexeev and Leonid Polishchuk</div>  
  <button class="abstract-button" onclick="toggleAbstract('abstract2')">View Abstract</button>
  <div id="abstract2" class="abstract-container">This study examines how ownership structures and asymmetric information affected the quality of care in US nursing homes...</div>

Work in progress
---
- **Endogenous continuation in repeated public good games**  
  <div class="publication-info">Work in Progress</div>  
  <div class="author-names">Ivan Dedyukhin</div>  
  <button class="abstract-button" onclick="toggleAbstract('abstract3')">View Abstract</button>
  <div id="abstract3" class="abstract-container">This project explores endogenous continuation in public good games and its effect on player cooperation...</div>

- **What strategies drive framing effects in repeated games?**  
  <div class="publication-info">Work in Progress</div>  
  <div class="author-names">Ivan Dedyukhin</div>  
  <button class="abstract-button" onclick="toggleAbstract('abstract4')">View Abstract</button>
  <div id="abstract4" class="abstract-container">This research analyzes the strategic decision-making behind framing effects in repeated game scenarios...</div>

<script>
function toggleAbstract(id) {
  var abstract = document.getElementById(id);
  abstract.style.display = abstract.style.display === "none" ? "block" : "none";
}
</script>

<style>
  .abstract-button {
    background-color: transparent;
    color: #007bff;
    border: none;
    padding: 5px 10px;
    font-size: 14px;
    cursor: pointer;
    text-decoration: underline;
    transition: color 0.3s;
  }
  .abstract-button:hover {
    color: #0056b3;
  }
  .abstract-container {
    display: none;
    margin-top: 10px;
  }
  .publication-info {
    font-style: italic;
    margin-bottom: 10px;
  }
  .author-names {
    font-weight: bold;
  }
</style>
