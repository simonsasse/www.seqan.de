---
layout: page
title: People
permalink: /people/
---

{% for person in site.people %}
# {{person.name}} - <small>{{person.position}}</small>

{% if person.avatar %}
![{{person.name}} Picture]({{person.avatar}})
{% endif %}

### Biography:
{{ person.content | markdownify }}

{%- if person.social_links %}
<h3>
Get in touch:
<span class="social-links">
  {%- include social.html social=person.social_links -%}
</span>
</h3>
{% endif -%}

{% endfor %}

----

# Become a contributor!

We welcome contributions to SeqAn!
Just write an email to one of our developers above or send an email to our
[Mailing List](https://lists.fu-berlin.de/listinfo/seqan-dev#subscribe)
