---
layout: default
title: Teaching
heading: Teaching
permalink: /teaching/
description: >-
  Teaching experience of Ivan Dedyukhin: instructor of record for Fundamentals of
  Economics for Business I at Indiana University Bloomington, plus teaching assistant
  experience and selected student feedback.
intro: >-
  I have been instructor of record for a required Kelley School of Business economics
  course every term since Fall 2023, with full responsibility for course design,
  lecturing, assessment and grading.
---

{% assign teaching = site.data.teaching %}

<section class="section section--tight" aria-labelledby="teaching-profile">
  <h2 class="section__title" id="teaching-profile">Teaching profile</h2>
  <div class="prose">
    <p>
      My teaching is built around business students who take economics as a
      requirement rather than a choice. The course I teach asks them to apply economic
      reasoning — opportunity cost, gains from trade, market structure, externalities,
      information problems and basic game theory — to problems they have not seen
      before, rather than to reproduce definitions.
    </p>
    <p>
      Across {{ teaching.summary.terms_count }} terms as instructor of record, beginning
      in {{ teaching.summary.first_term }}, I have taught
      {{ teaching.summary.students_phrase }} in {{ teaching.summary.section_size }}.
      Earlier, I worked as a teaching assistant in microeconomics, public economics and
      introductory economics at Indiana University and the New Economic School.
    </p>
    {%- comment -%}
      TODO(confirm): no statement of teaching interests or a list of courses you are
      prepared to teach exists in this repository. The sentence below is limited to
      subjects already taught; extend it once a confirmed list is available.
    {%- endcomment -%}
    <p>
      My teaching competencies follow directly from that experience: principles of
      microeconomics and macroeconomics for business students, microeconomic theory,
      public economics, and game theory.
    </p>
  </div>
</section>

<section class="section" aria-labelledby="instructor-of-record">
  <h2 class="section__title" id="instructor-of-record">Instructor of record</h2>

  {% for course in teaching.instructor %}
  <article class="course">
    <h3 class="course__title">{{ course.course }}{% if course.code %} ({{ course.code }}){% endif %}</h3>
    <p class="course__meta"><em>{{ course.institution }}</em> &middot; {{ course.terms }}</p>
    <p class="course__meta">{{ course.enrollment }} &middot; {{ course.students_total }}</p>
    <p class="course__description">{{ course.description }}</p>

    {%- comment -%}
      Syllabus and the student-comment disclosure share one action row, so the
      course reads like a research entry: title, metadata, description, actions.
      All comments sit behind the disclosure, matching abstracts on Research.
    {%- endcomment -%}
    <div class="course__actions">
      {% if course.syllabus.url %}
      <a class="btn btn--quiet" href="{{ course.syllabus.url | relative_url | uri_escape }}" target="_blank" rel="noopener noreferrer">{{ course.syllabus.label }}</a>
      {% endif %}
      {% if course.feedback.size > 0 %}
      <button class="btn btn--quiet disclosure-trigger" type="button"
              aria-expanded="false" aria-controls="feedback-{{ course.id }}">
        Student feedback<span class="disclosure-trigger__marker" aria-hidden="true"></span>
      </button>
      {% endif %}
    </div>

    {% if course.feedback.size > 0 %}
    <div class="feedback">
      <div class="disclosure-panel feedback__panel" id="feedback-{{ course.id }}">
        <h4 class="feedback__title">Selected student comments</h4>
        {% for item in course.feedback %}
        <blockquote class="quote">
          <p>{{ item.quote }}</p>
          <footer>&mdash; {{ item.source }}</footer>
        </blockquote>
        {% endfor %}

        {% if course.feedback_note %}
        <p class="note">{{ course.feedback_note }}</p>
        {% endif %}
      </div>
    </div>
    {% endif %}
  </article>
  {% endfor %}
</section>

<section class="section" aria-labelledby="teaching-assistant">
  <h2 class="section__title" id="teaching-assistant">Teaching assistant</h2>

  {% for group in teaching.assistant %}
  <div class="ta-group">
    <h3 class="ta-group__institution">{{ group.institution }}</h3>
    <ul class="ta-group__list">
      {% for course in group.courses %}
      <li>
        <span>{{ course.name }}</span>
        <span class="ta-group__term">{{ course.term }}</span>
      </li>
      {% endfor %}
    </ul>
  </div>
  {% endfor %}
</section>
