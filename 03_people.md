---
layout: page
title: People
permalink: /people/
categories: [Team, Contributor, User, Alumni]
---

{% for category in page.categories %}
{% if category == "Team" %}
<details markdown="1" open>
{% else%}
<details markdown="1">
{% endif %}
<summary class="category">
{{category}}
</summary>
{% for person in site.people %}
{% if person.category == category %}
<details markdown="1">
<summary class="person">
{{ person.name }} - <small>{{ person.position }}</small>
</summary>

<div class="person-div" markdown="1">
{% if person.avatar %}
<img class="avatar" src="{{person.avatar  | relative_url}}">
{% endif %}

<div class="bio" markdown="1">
### Biography:
{{ person.content | markdownify }}

{%- if person.social_links %}
<h3>
Get in touch:
<span class="social-links">
  {%- include social.html social=person.social_links -%}
</span>
</h3>
</div>
</div>
{% endif %}
</details>
{% endif %}
{% endfor %}
</details>
{% endfor %}

----

# Become a contributor!

We welcome contributions to SeqAn!
Just write an email to one of our developers above or send an email to our
[Mailing List](https://lists.fu-berlin.de/listinfo/seqan-dev#subscribe)
