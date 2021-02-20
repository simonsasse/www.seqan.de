---
layout: page
title: Publications
permalink: /publications/
header:
  overlay_image: /assets/images/overlay/publications.png
---

On the bottom you have access to the archive of SeqAn-related publications. Please see [Google
Scholar](https://scholar.google.de/scholar?cites=6133524701503406018) for a complete list of applications that cite
SeqAn.

If you use SeqAn in any of your academic works, please cite the latest SeqAn paper:

<ul>
<li>{% include cite.html cite="fu_mi_publications2103" %}</li>
</ul>

## Publication by year

{%- assign publications_by_year = site.data.publications | group_by_exp: "item", "item.date | truncate: 4, ''" | sort: "name" | reverse -%}

{% for year in publications_by_year %}

### {{ year.name }}

<ul>
{% for publication in year.items %}
<li>{% include cite.html cite = publication.key %}</li>
{% endfor %}
</ul>

{% endfor %}
