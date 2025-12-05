HTML support in email clients is not the same as in web browsers.
Gmail, Outlook, Yahoo, Zoho, Apple Mail, Thunderbird → all use different rendering engines, and Outlook is by far the most restrictive because it uses Microsoft Word to render HTML.

Below is the reliable, industry-accepted list of HTML elements and CSS rules that are accepted safely across major email clients.

Basic structure:
<html>
<head> (limited support)
<body>
<table>
<tr>
<td>

Text, headers, and link content
<p>
<span>
<b>, <strong>
<i>, <em>
<u>
<br>
<hr>
<small>
<h1>, <h2>, <h3>, <h4>, <h5>, <h6>
<a>

Lists
<ul>
<ol>
<li>

Images
<img>
Must have width, height, alt attributes
Should NOT rely on CSS for sizing
Should NOT rely on external fonts inside SVG images

Divs
<div>

Supported, but limited CSS support in Outlook.
Use <table> for layout instead of <div>.

Styling/formatting
<font>  (deprecated on web but widely used in email)
<blockquote>
<code>
<pre> (monospace formatting not always reliable)

Tables (the core of all HTML emails)
<table>
<thead>
<tbody>
<tfoot>
<tr>
<td>
<th>


Tables behave consistently across all email clients → use tables for 100% of layout.

HTML TAGS TO AVOID (NOT SAFE IN EMAILS)

These tags are not supported in many major email clients:

❌ Layout & advanced HTML
<section>
<article>
<header>
<footer>
<aside>
<main>
<canvas>
<video>, <audio>
<svg> (partially supported, but Outlook breaks it)
<iframe>
<object>, <embed>
<form>, <input>, <button>, <select>
<nav> (use <table> structure instead for nav-like blocks)
<title> (stripped and ignored by Gmail, Outlook and others)
<meta> --> mostly stripped and ignored, with the exception of <meta charset="UTF-8"> --> without it some may assume Windows-1252 encoding. pple Mail supports some CSS-related meta tags, like: <meta name="x-apple-disable-message-reformatting"> --> This prevents Apple Mail from “smart formatting” emails.

❌ Scripts & dynamic content
<script>  (blocked everywhere)
<link rel="stylesheet">
<style>   (only partially supported; Gmail strips some) --> Inline CSS is required because most email clients strip external CSS. Use it only for non-critical enhancements, do not rely for important visual layouts. Many clients use them, though: Apple Mail, iOS Mail, Outlook.com, Gmail web, Yahoo.
You can use styles for tag resets (body, table, etc), basic elements settings like: img { border:0; }
table { border-collapse: collapse; }, Apple-specific meta and styles a[x-apple-data-detectors] { color: inherit; }, Mobile responsive styles (media queries) for most part (Gmail, Yahoo, Apple Mail, iOS Mail — but ignored by Outlook desktop )
Do not put in style block:
These are either stripped, ignored, or break in Outlook:

Flexbox
CSS Grid
position: absolute
display: flex
:root
Custom fonts via @font-face
Complex selectors (.header > p > span, attribute selectors)
CSS variables
These were removed from your rewritten template.



📌 CSS SUPPORT IS VERY LIMITED

To build reliable emails:

Use inline styles

Avoid Flexbox

Avoid Grid

Avoid floating layouts

Avoid background images (Outlook does not support them unless via VML)

Safe CSS properties include:

color
font-family
font-size
line-height
text-align
padding
margin (except margin on <p> sometimes removed)
background-color
border, border-radius (border-radius not supported everywhere but okay)
display: block (safe)
width, height
max-width (supported by Gmail/Apple Mail but not Outlook desktop)