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

{% assign working_papers = site.data.research | where: "category", "working-paper" %}
{% assign publications = site.data.research | where: "category", "publication" %}
{% assign in_progress = site.data.research | where: "category", "work-in-progress" %}

{% comment %} Job market - DISABLED (step 2): featured job-market paper section.
Re-enable this together with the other four steps listed at the top of README.md.
{% assign jmp_id = site.data.profile.job_market.paper_id %}
{% assign jmp = site.data.research | where: "id", jmp_id | first %}

{% if jmp %}
<section class="section section--tight" aria-labelledby="job-market-paper">
  <h2 class="u-visually-hidden" id="job-market-paper">Job market paper</h2>
  <div class="jm-banner">
    {% include research-entry.html entry=jmp heading_level=3 featured=true label="Job Market Paper" %}
  </div>
</section>
{% endif %}
{% endcomment %}

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
    {%- comment -%}
      Job market note: when the section above is re-enabled, wrap this include in an
      "unless entry.id == jmp_id" guard again so the featured paper is not listed twice.
    {%- endcomment -%}
    {% for entry in in_progress %}
      {% include research-entry.html entry=entry heading_level=3 show_label=false %}
    {% endfor %}
  </div>
</section>
{% endif %}
