---
layout: default
title: CV
heading: Curriculum Vitae
permalink: /CV/
description: >-
  Curriculum vitae of Ivan Dedyukhin, PhD candidate in economics at Indiana University
  Bloomington: education, publications, working papers, teaching, awards and service.
---

{% assign profile = site.data.profile %}

<p class="lead prose">
  Education, research, teaching, awards and professional service.
  {% if profile.cv.updated %}Last updated {{ profile.cv.updated }}.{% endif %}
</p>

<div class="cv-actions">
  <a class="btn btn--primary" href="{{ profile.cv.url | relative_url }}" target="_blank" rel="noopener noreferrer">View CV (PDF)</a>
  <a class="btn btn--outline" href="{{ profile.cv.url | relative_url }}" download>Save a copy</a>
</div>

<p class="cv-preview-note note">
  The CV is a two-page PDF. Use one of the buttons above to open or save it.
</p>

<div class="cv-preview">
  <iframe class="cv-preview__frame"
          src="{{ profile.cv.url | relative_url }}#view=FitH"
          title="Curriculum vitae of Ivan Dedyukhin"
          loading="lazy"></iframe>
  <p class="cv-preview__fallback">
    If the preview does not load,
    <a href="{{ profile.cv.url | relative_url }}" target="_blank" rel="noopener noreferrer">open the CV directly</a>.
  </p>
</div>
