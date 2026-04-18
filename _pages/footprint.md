---
layout: page
title: Footprint
permalink: /footprint/
body_class: footprint-page
---

<div class="footprint-hero">
  <p class="footprint-subtitle">足迹 · a record of places</p>
</div>

<div class="footprint-body">

  <main>
    {% for year_block in site.data.footprint %}
      <section class="fp-year" id="y{{ year_block.year }}">
        <div class="fp-year-head">
          <h2>{{ year_block.year }}</h2>
          {% if year_block.year_note %}<span class="fp-year-note">{{ year_block.year_note }}</span>{% endif %}
        </div>

        {% for trip in year_block.trips %}
          <article class="fp-trip">
            <header class="fp-trip-head">
              {% if trip.eyebrow %}<p class="fp-trip-eyebrow">{{ trip.eyebrow }}</p>{% endif %}
              <h3 class="fp-trip-title">
                <span class="cn">{{ trip.title_cn }}</span>
                {% if trip.title_en %}<span class="en">{{ trip.title_en }}</span>{% endif %}
              </h3>
            </header>
            <div class="fp-gallery">
              {% for img in trip.images %}
                <figure><img src="{{ site.baseurl }}/images/footprint/{{ img }}" alt="{{ trip.title_en | default: trip.title_cn }}" loading="lazy" decoding="async"></figure>
              {% endfor %}
            </div>
          </article>
        {% endfor %}
      </section>
    {% endfor %}
  </main>

  <nav class="footprint-rail" aria-label="Years">
    <h4>Years</h4>
    <ol>
      {% for year_block in site.data.footprint %}
        <li><a href="#y{{ year_block.year }}">{{ year_block.year }}</a></li>
      {% endfor %}
    </ol>
  </nav>

</div>

<!-- Lightbox (zero-dependency) -->
<div class="fp-lightbox" id="fp-lightbox" aria-hidden="true">
  <button class="close" aria-label="Close">&times;</button>
  <button class="prev" aria-label="Previous">&larr;</button>
  <img src="" alt="">
  <button class="next" aria-label="Next">&rarr;</button>
  <div class="counter"></div>
</div>

<script>
  (function () {
    var lb = document.getElementById('fp-lightbox');
    if (!lb) return;
    var lbImg = lb.querySelector('img');
    var counter = lb.querySelector('.counter');
    var list = [], idx = 0;

    function show(i) {
      idx = (i + list.length) % list.length;
      lbImg.src = list[idx].src;
      lbImg.alt = list[idx].alt;
      counter.textContent = (idx + 1) + ' / ' + list.length;
    }
    function open(gallery, startIdx) {
      list = Array.prototype.slice.call(gallery.querySelectorAll('img'));
      show(startIdx);
      lb.classList.add('open');
      lb.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }
    function close() {
      lb.classList.remove('open');
      lb.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    document.querySelectorAll('.fp-gallery').forEach(function (g) {
      g.querySelectorAll('figure').forEach(function (fig, i) {
        fig.addEventListener('click', function () { open(g, i); });
      });
    });

    lb.querySelector('.close').addEventListener('click', close);
    lb.querySelector('.prev').addEventListener('click', function (e) { e.stopPropagation(); show(idx - 1); });
    lb.querySelector('.next').addEventListener('click', function (e) { e.stopPropagation(); show(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
  })();
</script>
