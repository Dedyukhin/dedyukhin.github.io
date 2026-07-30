---
layout: default
title: Home
permalink: /
description: >-
  Ivan Dedyukhin is a PhD candidate in economics at Indiana University Bloomington
  working in experimental economics, game theory and behavioral economics. Research
  papers, teaching experience and CV.
---

{%- comment -%}
  ===========================================================================
  Job market - DISABLED

  Every piece of job-market content on the site is commented out for now.
  To switch it all back on:

    1. this file - uncomment the two `jmp` assigns below, the "Job market
       paper" button in the profile actions, the job-market status line, and
       the job-market banner section that follows the profile
    2. Research.md - uncomment the job-market paper section at the top
    3. _data/profile.yml - uncomment the `job_market:` block and set
       `paper_id` (and optionally `status`)
    4. _data/navigation.yml - uncomment the "Job Market" nav item
    5. job-market.md - remove `published: false` from the front matter

  Nothing else needs to change: the CSS and the research-entry include
  already handle the featured job-market treatment.
  ===========================================================================
{%- endcomment -%}

{% assign profile = site.data.profile %}

{% comment %} Needed only by the Selected research and Teaching blocks below,
both of which are currently commented out.
{% assign selected = site.data.research | where: "featured", true %}
{% assign teaching = site.data.teaching.summary %}
{% endcomment %}

{% comment %} Job market - DISABLED (step 1)
{% assign jmp_id = profile.job_market.paper_id %}
{% assign jmp = site.data.research | where: "id", jmp_id | first %}
{% endcomment %}

<section class="profile" aria-labelledby="profile-name">
  <figure class="profile__figure">
    <img class="profile__photo"
         src="{{ profile.photo.src | relative_url }}"
         alt="{{ profile.photo.alt | strip_newlines | escape }}"
         width="{{ profile.photo.width }}" height="{{ profile.photo.height }}">
  </figure>

  <div class="profile__body">
    <h1 class="profile__name" id="profile-name">{{ profile.name }}</h1>
    <p class="profile__role">{{ profile.role }}</p>
    <p class="profile__affiliation">
      {{ profile.department }},
      <a class="inline-link" href="{{ profile.institution_url }}" target="_blank" rel="noopener noreferrer">{{ profile.institution }}</a>
    </p>
    <p class="profile__fields">{{ profile.fields | join: " · " }}</p>

    {% comment %} Job market - DISABLED (step 1): availability line
    {% if profile.job_market.status != "" %}
    <p class="profile__status">{{ profile.job_market.status }}</p>
    {% endif %}
    {% endcomment %}

    <p class="profile__summary">{{ profile.bio_research }}</p>

    <p class="meta">
      My advisors are
      {% for advisor in profile.advisors %}<a class="inline-link" href="{{ advisor.url }}" target="_blank" rel="noopener noreferrer">{{ advisor.name }}</a>{% unless forloop.last %} and {% endunless %}{% endfor %}.
    </p>

    <div class="btn-row">
      <a class="btn btn--primary" href="{{ profile.cv.url | relative_url }}" target="_blank" rel="noopener noreferrer">Download CV (PDF)</a>
      <a class="btn btn--outline" href="{{ "/research/" | relative_url }}">Research</a>
      <a class="btn" href="mailto:{{ profile.email }}">Email me</a>
      {% comment %} Job market - DISABLED (step 1): strongest action after the CV
      <a class="btn btn--outline" href="{{ "/job-market/" | relative_url }}">Job market paper</a>
      {% endcomment %}
    </div>
  </div>

  <dl class="profile-details">
    <div class="profile-details__row">
      <dt class="profile-details__term">Email</dt>
      <dd class="profile-details__value"><a href="mailto:{{ profile.email }}">{{ profile.email }}</a></dd>
    </div>
    <div class="profile-details__row">
      <dt class="profile-details__term">Office</dt>
      <dd class="profile-details__value">{{ profile.office }}</dd>
    </div>
    <div class="profile-details__row">
      <dt class="profile-details__term">CV</dt>
      <dd class="profile-details__value">
        <a href="{{ profile.cv.url | relative_url }}" target="_blank" rel="noopener noreferrer">Academic CV (PDF)</a>
      </dd>
    </div>
    <div class="profile-details__row">
      <dt class="profile-details__term">Profiles</dt>
      <dd class="profile-details__value">
        <a href="https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=6914508" target="_blank" rel="noopener noreferrer">SSRN</a> ·
        <a href="https://www.linkedin.com/in/ivan-dedyukhin/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
      </dd>
    </div>
  </dl>
</section>

{% comment %} Job market - DISABLED (step 1): featured job-market paper banner
{% if jmp %}
<section class="jm-banner" aria-labelledby="jmp-heading">
  <h2 class="u-visually-hidden" id="jmp-heading">Job market paper</h2>
  {% include research-entry.html entry=jmp heading_level=3 featured=true label="Job Market Paper" prefix="home-abstract" %}
  <p class="jm-banner__footer">
    Full job-market details and materials:
    <a href="{{ "/job-market/" | relative_url }}">Job Market page</a>.
  </p>
</section>
{% endif %}
{% endcomment %}

{% comment %} Selected research - removed from the homepage by request.
The Research page is the single home for papers; the profile actions and the nav
both link to it. To bring this block back, uncomment it and restore the
`selected` assign near the top of this file. If the job-market banner is also
re-enabled, wrap the include in an "unless entry.id == jmp_id" guard so the
featured paper is not listed twice.
<section class="section" aria-labelledby="selected-research">
  <h2 class="section__title" id="selected-research">Selected research</h2>

  <div class="research-list">
    {% for entry in selected %}
      {% include research-entry.html entry=entry heading_level=3 prefix="home-abstract" %}
    {% endfor %}
  </div>

  <a class="more-link" href="{{ "/research/" | relative_url }}">View all research</a>
</section>
{% endcomment %}

<section class="section" aria-labelledby="research-interests">
  <h2 class="section__title" id="research-interests">Research interests</h2>
  <ul class="interests">
    {% for interest in profile.interests %}
    <li>{{ interest }}</li>
    {% endfor %}
  </ul>
</section>

{% comment %} Teaching summary - removed from the homepage by request.
The Teaching page carries the full record and is linked from the nav. To bring
this block back, uncomment it and restore the `teaching` assign near the top of
this file.
<section class="section" aria-labelledby="teaching-summary">
  <h2 class="section__title" id="teaching-summary">Teaching</h2>
  <p class="prose">
    {{ teaching.role }} for <em>{{ teaching.course }}</em> at {{ teaching.institution }},
    a required course for Kelley School of Business students, across
    {{ teaching.terms_count }} terms since {{ teaching.first_term }} &mdash;
    {{ teaching.enrollment }}, {{ teaching.students_total }}.
  </p>
  <a class="more-link" href="{{ "/teaching/" | relative_url }}">Teaching experience and student feedback</a>
</section>
{% endcomment %}

<section class="section" aria-labelledby="contact">
  <h2 class="section__title" id="contact">Contact</h2>
  <p class="prose">
    <a href="mailto:{{ profile.email }}">{{ profile.email }}</a><br>
    {{ profile.department }}, {{ profile.institution }}<br>
    {{ profile.office }}
  </p>
  {% include social-links.html skip="Email" %}
</section>
