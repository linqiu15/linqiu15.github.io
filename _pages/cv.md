---
layout: page
title: CV
permalink: /cv/
---

<style>
  /* Scoped to the CV page only */
  .cv {
    max-width: 780px;
    margin: 0 auto;
    font-size: 16px;
    line-height: 1.65;
    color: #222;
  }
  .cv a { color: #1a1a1a; border-bottom: 1px solid #c9cdd1; }
  .cv a:hover { border-bottom-color: #1a1a1a; }

  /* Hero */
  .cv-header {
    padding-bottom: 24px;
    margin-bottom: 32px;
    border-bottom: 1px solid #e4e6e8;
    text-align: left;
  }
  .cv-name {
    font-family: Georgia, "Times New Roman", serif;
    font-weight: 400;
    font-size: 36px;
    line-height: 1.1;
    margin: 0 0 6px;
    text-align: left;
  }
  .cv-role {
    font-family: Georgia, "Times New Roman", serif;
    font-style: italic;
    color: #666;
    margin: 0 0 2px;
    font-size: 17px;
  }
  .cv-affiliation {
    color: #666;
    margin: 0 0 14px;
    font-size: 15px;
  }
  .cv-links {
    display: flex;
    flex-wrap: wrap;
    gap: 8px 18px;
    font-size: 14px;
    margin-top: 14px;
  }
  .cv-links a {
    color: #555;
    border-bottom: none;
  }
  .cv-links a:hover { color: #000; }
  .cv-download {
    display: inline-block;
    padding: 6px 14px;
    background: #1a1a1a;
    color: #fff !important;
    border-radius: 3px;
    font-size: 13px;
    letter-spacing: 0.5px;
    border-bottom: none !important;
    transition: background 0.15s ease;
  }
  .cv-download:hover { background: #333; color: #fff !important; }

  /* Section headings */
  .cv-section { margin: 36px 0; }
  .cv-section h3 {
    font-family: Georgia, "Times New Roman", serif;
    font-weight: 400;
    font-size: 13px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #8a8f95;
    margin: 0 0 18px;
    padding-bottom: 6px;
    border-bottom: 1px solid #e4e6e8;
    text-align: left;
  }

  /* Two-column entry: date | content */
  .cv-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .cv-list > li {
    display: grid;
    grid-template-columns: 110px 1fr;
    gap: 24px;
    padding: 10px 0;
    align-items: start;
  }
  .cv-date {
    font-family: Georgia, "Times New Roman", serif;
    font-style: italic;
    color: #8a8f95;
    font-size: 14px;
    padding-top: 2px;
  }
  .cv-entry strong {
    color: #1a1a1a;
    font-weight: 600;
  }
  .cv-entry .institution {
    color: #444;
  }
  .cv-entry .detail {
    color: #666;
    font-size: 14px;
    font-style: italic;
  }

  /* Research interests: prose, no two-column */
  .cv-prose p { margin: 8px 0; }
  .cv-prose ul { margin: 8px 0; padding-left: 22px; }

  /* PDF embed */
  .cv-pdf-embed {
    width: 100%;
    height: 900px;
    border: 1px solid #e4e6e8;
    border-radius: 3px;
    background: #f7f7f8;
    margin-top: 12px;
  }
  .cv-pdf-fallback {
    padding: 40px 24px;
    text-align: center;
    color: #666;
    background: #f7f7f8;
    border: 1px dashed #d0d4d8;
    border-radius: 3px;
  }

  /* Mobile: stack date above content */
  @media (max-width: 640px) {
    .cv-list > li {
      grid-template-columns: 1fr;
      gap: 4px;
      padding: 12px 0;
    }
    .cv-date { padding-top: 0; }
    .cv-pdf-embed { height: 600px; }
  }
</style>

<div class="cv">

  <!-- ========== HERO ========== -->
  <header class="cv-header">
    <h2 class="cv-name">Lin Qiu</h2>
    <p class="cv-role">Postdoctoral Researcher, Theoretical Physics</p>
    <p class="cv-affiliation">Old Dominion University · Jefferson Lab</p>
    <div class="cv-links">
      <a href="mailto:lqiu@odu.edu">lqiu@odu.edu</a>
      <a href="https://inspirehep.net/authors/2029017" target="_blank" rel="noopener">InspireHep</a>
      <a href="https://www.researchgate.net/profile/Lin_Qiu29" target="_blank" rel="noopener">ResearchGate</a>
      <a class="cv-download" href="{{ site.baseurl }}/assets/cv.pdf" download>Download PDF</a>
    </div>
  </header>

  <!-- ========== RESEARCH INTERESTS ========== -->
  <section class="cv-section cv-prose">
    <h3>Research Interests</h3>
    <p>
      My research sits at the intersection of hadron physics and modern analytical methods. I work on:
    </p>
    <ul>
      <li>Hadron spectroscopy through effective field theories and S-matrix techniques, in particular dispersion relations</li>
      <li>Spectroscopy in finite volume and its connections to lattice QCD</li>
      <li>Applications of machine learning to problems in hadron physics</li>
    </ul>
  </section>

  <!-- ========== EDUCATION ========== -->
  <!--
    TEMPLATE: Duplicate a <li> block and edit. Keep the two-column structure.
    Date formats that work: "2019 – 2024", "Sep 2019 – Jun 2024", "2024".
  -->
  <section class="cv-section">
    <h3>Education</h3>
    <ul class="cv-list">
      <li>
        <span class="cv-date">2019 – 2025</span>
        <div class="cv-entry">
          <strong>Ph.D. in Theoretical Physics</strong><br>
          <span class="institution">Institute of High Energy Physics</span><br>
          <span class="detail">Advisor: Prof. Qiang Zhao</span>
        </div>
      </li>
      <li>
        <span class="cv-date">2015 – 2019</span>
        <div class="cv-entry">
          <strong>B.S. in Physics</strong><br>
          <span class="institution">University of Chinese Academy of Sciences</span>
        </div>
      </li>
    </ul>
  </section>

  <!-- ========== POSITIONS ========== -->
  <section class="cv-section">
    <h3>Positions</h3>
    <ul class="cv-list">
      <li>
        <span class="cv-date">YYYY – present</span>
        <div class="cv-entry">
          <strong>Postdoctoral Researcher</strong><br>
          <span class="institution">Old Dominion University · Jefferson Lab</span><br>
          <span class="detail">Group / PI: JPAC</span>
        </div>
      </li>
    </ul>
  </section>

  <!-- ========== AWARDS & HONORS ==========
  <section class="cv-section">
    <h3>Awards &amp; Honors</h3>
    <ul class="cv-list">
      <li>
        <span class="cv-date">YYYY</span>
        <div class="cv-entry">
          <strong>Award name</strong><br>
          <span class="detail">Awarding body / context</span>
        </div>
      </li>
      <!-- duplicate <li> blocks as needed -->
    </ul>
  </section> -->

  <!-- ========== TALKS ==========
  <section class="cv-section">
    <h3>Selected Talks</h3>
    <ul class="cv-list">
      <li>
        <span class="cv-date">YYYY</span>
        <div class="cv-entry">
          <strong>Talk title</strong><br>
          <span class="institution">Conference / seminar name</span><br>
          <span class="detail">Location</span>
        </div>
      </li>
      <!-- duplicate <li> blocks as needed -->
    </ul>
  </section> -->

  <!-- ========== TEACHING / SERVICE ==========
  <section class="cv-section">
    <h3>Teaching &amp; Service</h3>
    <ul class="cv-list">
      <li>
        <span class="cv-date">YYYY</span>
        <div class="cv-entry">
          <strong>Role</strong> (e.g., Teaching Assistant)<br>
          <span class="institution">Course · Institution</span>
        </div>
      </li>
    </ul>
  </section> -->

  <!-- ========== FULL PDF ==========
  <section class="cv-section">
    <h3>Full CV</h3>
    <p style="color:#666; font-size:14px; margin: 0 0 12px;">
      <a href="{{ site.baseurl }}/assets/cv.pdf" download>Download the PDF</a> or preview it below.
    </p>
    <object class="cv-pdf-embed" data="{{ site.baseurl }}/assets/cv.pdf#view=FitH" type="application/pdf">
      <div class="cv-pdf-fallback">
        <p style="margin:0 0 8px;"><strong>PDF preview unavailable.</strong></p>
        <p style="margin:0; font-size:14px;">
          Your browser couldn't display the embedded preview, or the file isn't uploaded yet.<br>
          <a href="{{ site.baseurl }}/assets/cv.pdf" download>Download the PDF directly</a>.
        </p>
      </div>
    </object>
  </section> -->

</div>
