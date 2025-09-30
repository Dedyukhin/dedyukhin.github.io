---
layout: default
title: Teaching
permalink: /teaching/
---

<h2>Undergraduate</h2>

<div class="pub-card">
  <div class="pub-header">
    <span class="pub-title"><strong>Fundamentals Of Economics For Business I</strong></span>
    <div class="publication-info">Undergraduate course</div>

    <div class="button-group">
      <button class="abstract-button" aria-expanded="false" aria-controls="course_foebi" onclick="toggleAbstract('course_foebi', this)">View details</button>
      <!-- Add/Remove adjacent buttons as needed -->
      <a class="mini-btn" href="#" target="_blank" rel="noopener">Syllabus</a>
      <a class="mini-btn" href="#" target="_blank" rel="noopener">Schedule</a>
      <a class="mini-btn" href="#" target="_blank" rel="noopener">Slides</a>
      <a class="mini-btn" href="#" target="_blank" rel="noopener">Assignments</a>
      <a class="mini-btn" href="#" target="_blank" rel="noopener">Evaluations</a>
    </div>
  </div>

  <div id="course_foebi" class="abstract-container" hidden>
    <p><strong>Offerings:</strong> Fall 2023; Spring 2024; Fall 2024; Spring 2025; Fall 2025.</p>
    <!-- Optional short description; edit or remove -->
    <p>This course introduces core microeconomic tools for business decision-making: supply &amp; demand, elasticities, consumer/producer surplus, market efficiency, and market failures with business applications.</p>
  </div>
</div>

<script>
function toggleAbstract(id, btn) {
  const el = document.getElementById(id);
  const isHidden = el.hasAttribute('hidden');
  if (isHidden) {
    el.removeAttribute('hidden');
    el.style.display = 'block';
    btn.setAttribute('aria-expanded', 'true');
    el.scrollIntoView({ behavior: "smooth", block: "nearest" });
  } else {
    el.setAttribute('hidden', '');
    el.style.display = 'none';
    btn.setAttribute('aria-expanded', 'false');
  }
}
</script>

<style>
/* --- Reuse the same style as the Research page --- */

/* Card/box container */
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

/* Title & meta */
.pub-title{ text-decoration: none; }
.publication-info{
  font-style: italic;
  opacity: 0.85;
}

/* Tight inline button row directly under meta */
.button-group{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 2px; /* keeps buttons very close to text */
}

/* Abstract/details toggle button */
.abstract-button{
  background: transparent;
  border: none;
  padding: 4px 8px;
  font-size: 14px;
  cursor: pointer;
  text-decoration: underline;
  color: #dc143c;
  line-height: 1.2;
}
.abstract-button:hover{ color:#0056b3; }

/* Extra small link-buttons that sit next to the toggle */
.mini-btn{
  display: inline-block;
  font-size: 12px;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid #ddd;
  text-decoration: none;
  line-height: 1.2;
}
.mini-btn:hover{ background:#f3f4f6; }

/* Details/abstract box inside the same card */
.abstract-container{
  border-top: 1px dashed #e5e7eb;
  margin-top: 10px;
  padding-top: 10px;
}
</style>
