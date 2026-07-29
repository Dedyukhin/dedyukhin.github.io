---
layout: default
title: Job Market
heading: Job Market
permalink: /job-market/
description: >-
  Job-market information for Ivan Dedyukhin, PhD candidate in economics at Indiana
  University Bloomington: job market paper, CV, research fields and contact details.
---

{% assign profile = site.data.profile %}
{% assign jmp_id = profile.job_market.paper_id %}
{% assign jmp = site.data.research | where: "id", jmp_id | first %}

<section class="section section--tight" aria-labelledby="status">
  <h2 class="u-visually-hidden" id="status">Status</h2>
  {%- comment -%}
    TODO(confirm): no job-market year or availability statement exists in this
    repository. The sentence below states only what files/Academic_CV.pdf confirms.
    Set `job_market.status` in _data/profile.yml to add an explicit availability line.
  {%- endcomment -%}
  <p class="lead prose">
    I am a PhD candidate in economics at {{ profile.institution }}, expecting to
    complete my degree in 2027. My research is in experimental economics, game theory
    and behavioral economics.
  </p>
  {% if profile.job_market.status != "" %}
  <p class="profile__status">{{ profile.job_market.status }}</p>
  {% endif %}

  <div class="btn-row">
    <a class="btn btn--primary" href="{{ profile.cv.url | relative_url }}" target="_blank" rel="noopener noreferrer">Download CV (PDF)</a>
    <a class="btn" href="{{ "/research/" | relative_url }}">All research</a>
    <a class="btn" href="mailto:{{ profile.email }}">Email me</a>
  </div>
</section>

{% if jmp %}
<section class="section" aria-labelledby="jmp-heading">
  <h2 class="section__title" id="jmp-heading">Job market paper</h2>
  <div class="jm-banner">
    {% include research-entry.html entry=jmp heading_level=3 featured=true label="Job Market Paper" %}
  </div>
</section>
{% endif %}

<section class="section" aria-labelledby="materials">
  <h2 class="section__title" id="materials">Job market materials</h2>
  <ul class="materials">
    <li class="materials__item">
      <span class="materials__name">
        Curriculum vitae
        <span class="materials__detail">Updated {{ profile.cv.updated }}</span>
      </span>
      <a class="btn btn--quiet" href="{{ profile.cv.url | relative_url }}" target="_blank" rel="noopener noreferrer">Download PDF</a>
    </li>

    {%- comment -%}
      TODO(missing): no job-market paper PDF or slide deck exists in files/. Once the
      draft is ready, add it to files/, list it under the paper's `links:` in
      _data/research.yml, and replace the status text below with the download action.
    {%- endcomment -%}
    <li class="materials__item">
      <span class="materials__name">
        Job market paper
        <span class="materials__detail">{{ jmp.title }}</span>
      </span>
      <span class="materials__status">Draft not yet posted &mdash; available on request</span>
    </li>

    <li class="materials__item">
      <span class="materials__name">
        Working paper
        <span class="materials__detail">Ownership, Asymmetric Information, and Quality of Care for the Elderly</span>
      </span>
      <span>
        <a class="btn btn--quiet" href="{{ "/files/Nursing_Homes_WP_Aug2024.pdf" | relative_url }}" target="_blank" rel="noopener noreferrer">Download PDF</a>
      </span>
    </li>
  </ul>
  {%- comment -%}
    TODO(missing): no research statement, teaching statement or list of references
    exists in this repository. Add each file to files/ and a matching row above.
  {%- endcomment -%}
</section>

<section class="section" aria-labelledby="education">
  <h2 class="section__title" id="education">Education</h2>
  <ul class="facts">
    {% for item in profile.education %}
    <li class="facts__item">
      <span class="facts__label">
        <strong>{{ item.degree }}</strong>
        <span class="facts__detail">{{ item.institution }}</span>
      </span>
      <span class="facts__value">{{ item.year }}</span>
    </li>
    {% endfor %}
  </ul>
  <p class="note">Full academic history, awards, presentations and service are listed in the <a href="{{ "/CV/" | relative_url }}">CV</a>.</p>
</section>

<section class="section" aria-labelledby="jm-contact">
  <h2 class="section__title" id="jm-contact">Contact</h2>
  <p class="prose">
    <a href="mailto:{{ profile.email }}">{{ profile.email }}</a><br>
    {{ profile.department }}, {{ profile.institution }}<br>
    {{ profile.office }}
  </p>
</section>
