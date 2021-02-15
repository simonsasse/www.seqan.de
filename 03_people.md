---
layout: page
title: People
permalink: /people/
categories: [Team, Contributor, User, Alumni]
---

{% for category in page.categories %}
## {{category}}
{% for person in site.people %}
{% if person.category == category %}
<details markdown="1">
<summary class="person">
{% if person.avatar %}
<img class="avatar" src="{{person.avatar  | relative_url}}">
{% else %}
<img class="avatar" src="/assets/images/people/avatar-dummy.png">
{% endif %}
{{ person.name }} - <small>{{ person.position }}</small>
</summary>
<div class="person-div" markdown="1">
<div class="bio" markdown="1">
{% if person.content.size > 1 %}
#### Biography:
{{ person.content | markdownify }}
{% endif %}
{%- if person.social_links %}
#### Get in touch:
  {%- include social.html social=person.social_links -%}
{% endif %}
</div>
</div>
</details>
{% endif %}
{% endfor %}
{% endfor %}

----

# Become a contributor!

We welcome contributions to SeqAn!
Just write an email to one of our developers above or send an email to our
[Mailing List](https://lists.fu-berlin.de/listinfo/seqan-dev#subscribe)
