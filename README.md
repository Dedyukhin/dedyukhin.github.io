# dedyukhin.github.io
Personal website

<h2>{{ site.data.navigation.docs_list_title }}</h2>
<style>
    .horizontal-nav {
        list-style-type: none;
        padding: 0;
        margin: 0;
        display: flex;
    }

    .horizontal-nav li {
        margin-right: 15px;
    }

    .horizontal-nav li:last-child {
        margin-right: 0;
    }

    .horizontal-nav a {
        text-decoration: none;
        color: #000;
    }
</style>
<ul class="horizontal-nav">
   {% for item in site.data.navigation.docs %}
      <li><a href="{{ item.url }}">{{ item.title }}</a></li>
   {% endfor %}
</ul>

