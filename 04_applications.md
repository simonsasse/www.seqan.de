---
layout: page
title: Applications
permalink: /apps/
header:
  overlay_image: https://www.researchgate.net/publication/318738093/figure/fig1/AS:574227122057216@1513917822295/Workflow-for-the-identification-and-quantification-of-microorganisms-within-microbial.png
---

SeqAn is the foundation of many modern bioinformatics applications. Some of them are developed by the SeqAn team, mostly
at Freie Universität Berlin. These are listed as Official Applications on the left. The downloads for most official
apps, including some older (not listed) ones, can be found at the central [SeqAn package
repository](http://packages.seqan.de/).

Through our developer channels we know that many scientific groups and companies are using SeqAn for developing public
and internal tools, among them Steven Salzbergs team, PacBio, the Max-Planck-Institute for molecular Genetics and the
Charite university hospital. A selection of these applications is listed as “Third-Party Applications” on the left.

The permissive open source BSD-license of the library enables you to integrate SeqAn into your applications with proper
attribution being the only legal requirement. But, please also cite our most recent SeqAn publication when you use SeqAn
in your academic work.

### Official

{% for app in site.apps %}
* [{{ app.title }}]({{ app.url | relative_url }})
{% endfor %}
