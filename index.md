---
layout: page
title: Home
nav_order: 1
description: A week-to-week description of the content covered in the course.
---

# Camp Code: Learn to think like a programmer in two weeks!
{: .mb-2 }
Brown University, Summer 2023
{: .mb-0 .fs-6 .text-grey-dk-000 }

<!-- ## Note: This page is under construction. Everything on this website is subject to change. -->

<br><br>



<!-- dont add tabs it does not work -->
{% assign announcements = site.announcements | reverse %}
{% for announcement in announcements %}
{% assign today_date = 'now' | date: '%s' %}
{% assign assign_date = announcement.date | date: '%s' %}
{% if today_date > assign_date %}
{{ announcement }}
{% endif %}
{% endfor %}


{% for module in site.modules %}
{{ module }}
{% endfor %}