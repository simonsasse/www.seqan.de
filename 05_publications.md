---
layout: page
title: Publications
permalink: /publications/
header:
  overlay_image: http://www.seqan.de/wp-content/uploads/2016/02/apps.png
---

On the left you have access to the archive of SeqAn-related publications. Please see [Google
Scholar](https://scholar.google.de/scholar?cites=6133524701503406018) for a complete list of applications that cite
SeqAn.

If you use SeqAn in any of your academic works, please cite the latest SeqAn paper:

{% include cite.html cite="fu_mi_publications2103" %}

## Publication by year

{%- assign publications_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse -%}

{% for year in publications_by_year %}

### {{ year.name }}

{% for publication in year.items %}
* {% include cite.html cite=publication.id %}
{% endfor %}

{% endfor %}
