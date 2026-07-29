---
layout: default
title: Research
heading: Research
permalink: /research/
description: >-
  Working papers, publications and work in progress by Ivan Dedyukhin on cooperation
  under strategic uncertainty, repeated games, perceptions of AI assistance, and
  public economics.
intro: >-
  My work is primarily experimental: I design laboratory experiments to test how
  strategic incentives and beliefs about opponents shape cooperation and
  sophistication. Abstracts are available for each project below.
---

{% assign jmp_id = site.data.profile.job_market.paper_id %}
{% assign jmp = site.data.research | where: "id", jmp_id | first %}
{% assign working_papers = site.data.research | where: "category", "working-paper" %}
{% assign publications = site.data.research | where: "category", "publication" %}
{% assign in_progress = site.data.research | where: "category", "work-in-progress" %}

{% if jmp %}
<section class="section section--tight" aria-labelledby="job-market-paper">
  <h2 class="u-visually-hidden" id="job-market-paper">Job market paper</h2>
  <div class="jm-banner">
    {% include research-entry.html entry=jmp heading_level=3 featured=true label="Job Market Paper" %}
  </div>
</section>
{% endif %}

{% if working_papers.size > 0 %}
<section class="section" aria-labelledby="working-papers">
  <h2 class="section__title" id="working-papers">Working papers</h2>
  <div class="research-list">
    {% for entry in working_papers %}
      {% include research-entry.html entry=entry heading_level=3 show_label=false %}
    {% endfor %}
  </div>
</section>
{% endif %}

{% if publications.size > 0 %}
<section class="section" aria-labelledby="publications">
  <h2 class="section__title" id="publications">Publications</h2>
  <div class="research-list">
    {% for entry in publications %}
      {% include research-entry.html entry=entry heading_level=3 show_label=false %}
    {% endfor %}
  </div>
</section>
{% endif %}

{% if in_progress.size > 0 %}
<section class="section" aria-labelledby="work-in-progress">
  <h2 class="section__title" id="work-in-progress">Work in progress</h2>
  <div class="research-list">
    {% for entry in in_progress %}
      {% unless entry.id == jmp_id %}
        {% include research-entry.html entry=entry heading_level=3 show_label=false %}
      {% endunless %}
    {% endfor %}
  </div>
</section>
{% endif %}
