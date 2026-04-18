---
layout: page
title: Now
permalink: /getting-started/
---

<style>
  /* ---------- Page scope ---------- */
  .now {
    max-width: 780px;
    margin: 0 auto;
    color: #222;
  }
  .now .subtitle {
    font-family: Georgia, "Times New Roman", serif;
    font-style: italic;
    color: #8a8f95;
    margin: -8px 0 32px;
    text-align: left;
    font-size: 16px;
  }

  /* ---------- Section heading (same vocabulary as CV) ---------- */
  .now-section { margin: 36px 0 48px; }
  .now-section h3 {
    font-family: Georgia, "Times New Roman", serif;
    font-weight: 400;
    font-size: 13px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #8a8f95;
    margin: 0 0 20px;
    padding-bottom: 6px;
    border-bottom: 1px solid #e4e6e8;
    text-align: left;
  }

  /* ---------- Book entry ---------- */
  .book {
    padding: 18px 0;
    border-bottom: 1px solid #f1f2f3;
  }
  .book:last-child { border-bottom: none; }

  .book-head {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    gap: 12px;
    margin-bottom: 4px;
  }
  .book-title {
    font-family: Georgia, "Times New Roman", serif;
    font-weight: 500;
    font-size: 18px;
    color: #1a1a1a;
    margin: 0;
  }
  .book-title a {
    color: inherit;
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: border-color 0.15s ease;
  }
  .book-title a:hover { border-bottom-color: #1a1a1a; }
  .book-author {
    font-family: Georgia, "Times New Roman", serif;
    font-style: italic;
    color: #666;
    font-size: 15px;
  }
  .book-date {
    margin-left: auto;
    font-family: Georgia, "Times New Roman", serif;
    font-style: italic;
    color: #8a8f95;
    font-size: 13px;
  }

  /* ---------- Review (final polished take) ---------- */
  .book-review {
    margin: 10px 0 0;
    color: #333;
    line-height: 1.75;
    font-size: 15.5px;
  }
  .book-review p { margin: 6px 0; }

  /* ---------- Notes (underlines / thoughts while reading) ---------- */
  .book-notes {
    margin: 12px 0 0;
  }
  .book-notes summary {
    cursor: pointer;
    color: #8a8f95;
    font-size: 12px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    list-style: none;
    padding: 4px 0;
    transition: color 0.15s ease;
  }
  .book-notes summary::-webkit-details-marker { display: none; }
  .book-notes summary::before {
    content: "+ ";
    font-family: Georgia, serif;
    font-weight: 400;
  }
  .book-notes[open] summary::before { content: "− "; }
  .book-notes summary:hover { color: #1a1a1a; }
  .book-notes ul {
    list-style: none;
    margin: 8px 0 0;
    padding: 0;
    border-left: 2px solid #e4e6e8;
  }
  .book-notes li {
    padding: 6px 0 6px 14px;
    color: #555;
    font-size: 15px;
    line-height: 1.7;
    font-style: italic;
  }
  .book-notes li + li { margin-top: 4px; border-top: 1px dotted #eef0f1; }

  /* ---------- Status pill for currently reading ---------- */
  .book-pill {
    display: inline-block;
    font-size: 11px;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #5a7a2a;
    background: #edf6d9;
    padding: 2px 8px;
    border-radius: 3px;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    font-style: normal;
    vertical-align: middle;
  }

  @media (max-width: 640px) {
    .book-date { margin-left: 0; width: 100%; }
  }
</style>

<div class="now">
  <p class="subtitle">What I'm reading now and recently.</p>

  {% assign reading = site.data.books | where: "status", "reading" %}
  {% assign finished = site.data.books | where: "status", "finished" %}

  {% if reading.size > 0 %}
  <section class="now-section">
    <h3>Currently Reading</h3>
    {% for book in reading %}
      <article class="book">
        <header class="book-head">
          <h4 class="book-title">
            {% if book.douban %}<a href="{{ book.douban }}" target="_blank" rel="noopener">《{{ book.title }}》</a>{% else %}《{{ book.title }}》{% endif %}
          </h4>
          {% if book.author %}<span class="book-author">— {{ book.author }}</span>{% endif %}
          <span class="book-pill">Reading</span>
        </header>

        {% if book.review %}
        <div class="book-review">{{ book.review | markdownify }}</div>
        {% endif %}

        {% if book.notes and book.notes.size > 0 %}
        <details class="book-notes">
          <summary>Notes ({{ book.notes.size }})</summary>
          <ul>
            {% for note in book.notes %}<li>{{ note }}</li>{% endfor %}
          </ul>
        </details>
        {% endif %}
      </article>
    {% endfor %}
  </section>
  {% endif %}

  <section class="now-section">
    <h3>Finished</h3>
    {% for book in finished %}
      <article class="book">
        <header class="book-head">
          <h4 class="book-title">
            {% if book.douban %}<a href="{{ book.douban }}" target="_blank" rel="noopener">《{{ book.title }}》</a>{% else %}《{{ book.title }}》{% endif %}
          </h4>
          {% if book.author %}<span class="book-author">— {{ book.author }}</span>{% endif %}
          {% if book.finished %}<span class="book-date">{{ book.finished }}</span>{% endif %}
        </header>

        {% if book.review %}
        <div class="book-review">{{ book.review | markdownify }}</div>
        {% endif %}

        {% if book.notes and book.notes.size > 0 %}
        <details class="book-notes">
          <summary>Notes ({{ book.notes.size }})</summary>
          <ul>
            {% for note in book.notes %}<li>{{ note }}</li>{% endfor %}
          </ul>
        </details>
        {% endif %}
      </article>
    {% endfor %}
  </section>
</div>
