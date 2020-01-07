<html>
<head><meta charset="utf-8" />

<title>AnalyzeReddit</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://i.imgur.com/7uiZbR2.jpg" alt="" width="450" height="450" /></p></p>
<p><h1 style="text-align: center;">Rock The Upvote:</h1></p>
<p><h2 style="text-align: center;">Predicting the Success of a Reddit Post</h2></p>
<p><p style="text-align: center;">Neehar Peri, Wilson Orlando</p></p>
<hr />
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><h2 style="text-align: center;">Introduction</h2></p>
<p style="text-align: left;">Ever heard of Reddit? Maybe you already have; it's the <a href="https://www.alexa.com/topsites/countries/US">6th most visited website in the U.S.</a>&nbsp;If this is your first time hearing about it, Reddit is a "social news aggregation forum", which is the official way of saying it gathers content from all over the internet to display in one place. Users submit content to Reddit like links, text posts, and images, and that content gets liked ("upvoted") or disliked ("downvoted") by other users. Posts are grouped into user-created boards called "subreddits" focused on one topic- like <a href="https://www.reddit.com/r/aww/">cute animals</a>, <a href="https://www.reddit.com/r/worldnews/">world news</a>, or <a href="https://www.reddit.com/r/gameofthrones/">Game of Thrones</a>- and the most upvoted posts across all subreddits are shown on the site's <a href="reddit.com/r/all">front page</a>. You can read more about it <a href="https://mashable.com/2012/06/06/reddit-for-beginners/">here</a>.</p>
<p>With 330 million users and over 20 thousand daily submissions, it&rsquo;s hard to predict which posts will get popular enough to hit the front page. If your predictions were good enough to craft viral Reddit posts, though, you could get your ideas out to those millions of users in a matter of hours. Many users don&rsquo;t realize that Reddit can be- and is already being- manipulated to spread more than cute cats. <a href="https://www.forbes.com/sites/jaymcgregor/2017/02/20/reddit-is-being-manipulated-by-big-financial-services-companies/#109284f94c92">Large financial service companies use Reddit</a> to boost their online image, and just this month the Reddit team claimed <a href="https://time.com/5745917/reddit-uk-trade-documents-russia/">leaked U.S.-U.K. trade documents posted on their site</a> were part of a large-scale misinformation campaign originating from Russia. On top of getting your own upvotes, understanding what makes a Reddit post popular is critical for your informed online browsing.</p>
<p>Given the huge amount of data Reddit generates, it&rsquo;s also an interesting problem for data science: based on existing Reddit posts, can we identify the most important features of a successful post and predict a post&rsquo;s success before it&rsquo;s submitted? In this tutorial, our goal is to download and tidy data from Reddit, perform some exploratory analysis to identify important features, then use machine learning models to predict a post&rsquo;s upvote rating based on those features. For readers unfamiliar with Reddit, we hope our analysis will get you interested in the site and in some popular posts. For more experienced readers, we hope to give you some insight into how your favorite &ldquo;social news aggregation forum&rdquo; works, and show you how to get your own posts to the front page of the internet.</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 style="text-align: center;">Getting Started with the Data</h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We use Python 3 and some imported libraries, like <a href="https://pytorch.org/">torch</a>, <a href="https://pandas.pydata.org/">pandas</a>, <a href="https://matplotlib.org/">matplotlib</a>, <a href="https://scikit-learn.org/stable/">scikit-learn</a>, and more.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">textblob</span> <span class="k">import</span> <span class="n">TextBlob</span>
<span class="kn">import</span> <span class="nn">torch</span>
<span class="kn">import</span> <span class="nn">torch.nn</span> <span class="k">as</span> <span class="nn">nn</span>
<span class="kn">import</span> <span class="nn">torch.optim</span> <span class="k">as</span> <span class="nn">optim</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="k">import</span> <span class="n">Lasso</span><span class="p">,</span> <span class="n">LogisticRegression</span>
<span class="kn">import</span> <span class="nn">sklearn.metrics</span> <span class="k">as</span> <span class="nn">metrics</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="k">import</span> <span class="n">train_test_split</span>
<span class="kn">from</span> <span class="nn">tqdm</span> <span class="k">import</span> <span class="n">tqdm</span>
<span class="kn">from</span> <span class="nn">pprint</span> <span class="k">import</span> <span class="n">pprint</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">praw</span>
<span class="kn">import</span> <span class="nn">pdb</span>
<span class="kn">import</span> <span class="nn">operator</span>
<span class="kn">import</span> <span class="nn">warnings</span>
<span class="n">warnings</span><span class="o">.</span><span class="n">filterwarnings</span><span class="p">(</span><span class="s2">&quot;ignore&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3>Data Collection</h3><p>To scrape data from Reddit, we'll be using <a href="https://praw.readthedocs.io/en/latest/">PRAW (the Python Reddit API Wrapper)</a>. For this analysis, we chose to pull data into two datasets:</p>
<p><ol>
    <li> Top Posts: The 1000 most upvoted posts in the last year </li>
    <li> Controversial Posts: The 1000 most controversial posts in the last year (i.e. closest to 50% upvote ratio) </li>
</ol>
This gives us a good spread of recent posts that have been wildly successful and unsuccessful.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Establish connection using Reddit&#39;s API</span>
<span class="n">clientID</span> <span class="o">=</span> <span class="s1">&#39;VpVEXRwC5-nrbA&#39;</span>
<span class="n">clientSecret</span> <span class="o">=</span> <span class="s1">&#39;XMql3JHOqhq2NatetFMFPkhBaCE&#39;</span>
<span class="n">userAgent</span> <span class="o">=</span> <span class="s1">&#39;Reddit WebScraping&#39;</span>
<span class="n">reddit</span> <span class="o">=</span> <span class="n">praw</span><span class="o">.</span><span class="n">Reddit</span><span class="p">(</span><span class="n">client_id</span><span class="o">=</span><span class="n">clientID</span><span class="p">,</span> <span class="n">client_secret</span><span class="o">=</span><span class="n">clientSecret</span><span class="p">,</span> <span class="n">user_agent</span><span class="o">=</span><span class="n">userAgent</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Retrieve the top (most upvoted) 1k posts in the last year and add them to a Pandas dataframe</span>
<span class="n">topPosts</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">subReddit</span> <span class="o">=</span> <span class="n">reddit</span><span class="o">.</span><span class="n">subreddit</span><span class="p">(</span><span class="s1">&#39;all&#39;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">post</span> <span class="ow">in</span> <span class="n">tqdm</span><span class="p">(</span><span class="n">subReddit</span><span class="o">.</span><span class="n">top</span><span class="p">(</span><span class="n">time_filter</span> <span class="o">=</span> <span class="s1">&#39;year&#39;</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="mi">1000</span><span class="p">),</span> <span class="n">total</span><span class="o">=</span><span class="mi">1000</span><span class="p">):</span>
    <span class="n">topPosts</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">post</span><span class="o">.</span><span class="n">title</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">score</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">subreddit</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">url</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">num_comments</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">selftext</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">created_utc</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">author</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">is_self</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">over_18</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">spoiler</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">upvote_ratio</span><span class="p">])</span> 
<span class="n">topPosts</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">topPosts</span><span class="p">,</span><span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;title&#39;</span><span class="p">,</span> <span class="s1">&#39;score&#39;</span><span class="p">,</span> <span class="s1">&#39;id&#39;</span><span class="p">,</span> <span class="s1">&#39;subreddit&#39;</span><span class="p">,</span> <span class="s1">&#39;url&#39;</span><span class="p">,</span> <span class="s1">&#39;num_comments&#39;</span><span class="p">,</span> <span class="s1">&#39;body&#39;</span><span class="p">,</span> <span class="s1">&#39;created&#39;</span><span class="p">,</span> <span class="s1">&#39;author&#39;</span><span class="p">,</span> <span class="s1">&#39;is_self&#39;</span><span class="p">,</span> <span class="s1">&#39;over_18&#39;</span><span class="p">,</span> <span class="s1">&#39;spoiler&#39;</span><span class="p">,</span> <span class="s1">&#39;upvote_ratio&#39;</span><span class="p">])</span>
<span class="n">topPosts</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s2">&quot;top1KPosts.csv&quot;</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

<span class="c1"># Retrieve the most controversial (most downvoted) 1k posts in the last year and add them to a Pandas dataframe</span>
<span class="n">controvertialPosts</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">subReddit</span> <span class="o">=</span> <span class="n">reddit</span><span class="o">.</span><span class="n">subreddit</span><span class="p">(</span><span class="s1">&#39;all&#39;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">post</span> <span class="ow">in</span> <span class="n">tqdm</span><span class="p">(</span><span class="n">subReddit</span><span class="o">.</span><span class="n">controversial</span><span class="p">(</span><span class="n">time_filter</span> <span class="o">=</span> <span class="s1">&#39;year&#39;</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="mi">1000</span><span class="p">),</span> <span class="n">total</span><span class="o">=</span><span class="mi">1000</span><span class="p">):</span>
    <span class="n">controvertialPosts</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">post</span><span class="o">.</span><span class="n">title</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">score</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">subreddit</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">url</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">num_comments</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">selftext</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">created_utc</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">author</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">is_self</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">over_18</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">spoiler</span><span class="p">,</span> <span class="n">post</span><span class="o">.</span><span class="n">upvote_ratio</span><span class="p">])</span>
<span class="n">controvertialPosts</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">controvertialPosts</span><span class="p">,</span><span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;title&#39;</span><span class="p">,</span> <span class="s1">&#39;score&#39;</span><span class="p">,</span> <span class="s1">&#39;id&#39;</span><span class="p">,</span> <span class="s1">&#39;subreddit&#39;</span><span class="p">,</span> <span class="s1">&#39;url&#39;</span><span class="p">,</span> <span class="s1">&#39;num_comments&#39;</span><span class="p">,</span> <span class="s1">&#39;body&#39;</span><span class="p">,</span> <span class="s1">&#39;created&#39;</span><span class="p">,</span> <span class="s1">&#39;author&#39;</span><span class="p">,</span> <span class="s1">&#39;is_self&#39;</span><span class="p">,</span> <span class="s1">&#39;over_18&#39;</span><span class="p">,</span> <span class="s1">&#39;spoiler&#39;</span><span class="p">,</span> <span class="s1">&#39;upvote_ratio&#39;</span><span class="p">])</span>
<span class="n">controvertialPosts</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s2">&quot;controvertial1KPosts.csv&quot;</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">top1KPosts</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;top1kPosts.csv&quot;</span><span class="p">)</span>
<span class="n">controversial1KPosts</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;controversial1kPosts.csv&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>To avoid calling the Reddit API thousands of times, we have saved the results of 1000 "Top" posts and 1000 "Controversial" posts to a Pandas dataframe. For all future analysis, we will be reading and modifying these data frames.</p>
<p>Next, let's take a look at some of the subreddits that have broken the top 1000 and controversial 1000 posts:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Top 10 List of subreddits that have broken top 1k</span>
<span class="n">topSubReddit</span> <span class="o">=</span> <span class="n">top1KPosts</span><span class="o">.</span><span class="n">subreddit</span><span class="o">.</span><span class="n">unique</span><span class="p">()</span> 
<span class="n">topSubReddit</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">10</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[13]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([&#39;pics&#39;, &#39;gaming&#39;, &#39;AskReddit&#39;, &#39;Showerthoughts&#39;, &#39;news&#39;, &#39;memes&#39;,
       &#39;funny&#39;, &#39;YouFellForItFool&#39;, &#39;aww&#39;, &#39;videos&#39;], dtype=object)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> <span class="c1">#Top 10 subreddits that have broken most controversial 1k</span>
<span class="n">controversialSubReddits</span> <span class="o">=</span> <span class="n">controversial1KPosts</span><span class="o">.</span><span class="n">subreddit</span><span class="o">.</span><span class="n">unique</span><span class="p">()</span>
<span class="n">controversialSubReddits</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">10</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[14]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>array([&#39;motorcycles&#39;, &#39;unpopularopinion&#39;, &#39;IAmA&#39;, &#39;AmItheAsshole&#39;,
       &#39;TheMonkeysPaw&#39;, &#39;TrueOffMyChest&#39;, &#39;gadgets&#39;, &#39;leagueoflegends&#39;,
       &#39;DestinyTheGame&#39;, &#39;FortNiteBR&#39;], dtype=object)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Our sampling of subreddits in the top 1000 are pretty predictable; <a href="https://www.reddit.com/r/pics/">r/pics</a>, <a href="https://www.reddit.com/r/aww/">r/aww</a>, and <a href="https://www.reddit.com/r/AskReddit/">r/AskReddit</a> are some of the biggest subreddits on the site ("r/" denotes a subreddit's name), with AskReddit hosting over 25 million subscribed users. This would indicate that <b>bigger subreddits are more likely to break the top 1000</b>, so a post's subreddit should be a very important feature for its success.</p>
<p>The controversial sample of subreddits shows a few different trends. Of the 74 subreddits that have broken the controversial 1000, many (like <a href="https://www.reddit.com/r/unpopularopinion/">r/unpopularopinion</a> and <a href="https://www.reddit.com/r/TrueOffMyChest/">r/TrueOffMyChest</a>), are communities for people to vent <b>intentionally controversial ideas</b> to other people. There's also a sizeable chunk of <b>political</b> subreddits, like <a href="https://www.reddit.com/r/Libertarian/">r/Libertarian</a> and <a href="https://www.reddit.com/r/Conservative/">r/Conservative</a>, which also host a lot of controversial opinions (as is the nature of partisan politics). Surprisingly, though, the vast majority of controversial subreddits have to do with <b>popular entertainment</b>, like <a href="https://www.reddit.com/r/DestinyTheGame/">r/DestinyTheGame</a>, <a href="https://www.reddit.com/r/leagueoflegends/">r/leagueoflegends</a>, and <a href="https://www.reddit.com/r/FortNiteBR/">r/FortNiteBR</a>. Part of this is sampling bias; there's inherently just a lot of subreddits dedicated to popular entertainment on Reddit, so it makes sense that they'd make up a significant percentage of the controversial dataset. Interestingly, though, many of them reflect legitimate controversies in the past year! <a href="https://www.reddit.com/r/gameofthrones/">r/gameofthrones</a> is present, after many fans were disappointed with the show's final season, and <a href="https://www.reddit.com/r/Blizzard/">r/Blizzard</a> makes an appearance after the gaming company punished prominent players for supporting the Hong Kong riots.</p>
<p>For our analysis, then, we'd recommend posting to large generic subreddits and avoiding specific potentially-controversial ones, hypothesizing that <b>a post's subreddit is an important feature in its success</b>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3>Data Preprocessing</h3><p>Next, we'll have to clean up the data from PRAW to get it into a more usable format. We'll be combining the top and controversial posts into a single Pandas dataframe, adding a field to differentiate between them, and dropping some fields that could not be controlled by a user at the time of post submission (like url and reddit's internal post id).</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">tableRow</span> <span class="ow">in</span> <span class="n">top1KPosts</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
     <span class="n">top1KPosts</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s2">&quot;post_type&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span> <span class="c1">#Set topPost as post_type 1</span>

<span class="k">for</span> <span class="n">tableRow</span> <span class="ow">in</span> <span class="n">controversial1KPosts</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
    <span class="n">controversial1KPosts</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s2">&quot;post_type&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span> <span class="c1">#Set controversialPost as post_type 0</span>

<span class="n">dataSet</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">top1KPosts</span><span class="p">,</span> <span class="n">controversial1KPosts</span><span class="p">])</span>
<span class="n">dataSet</span> <span class="o">=</span> <span class="n">dataSet</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>
<span class="n">dataSet</span> <span class="o">=</span> <span class="n">dataSet</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s2">&quot;index&quot;</span><span class="p">,</span> <span class="s2">&quot;id&quot;</span><span class="p">,</span> <span class="s2">&quot;url&quot;</span><span class="p">,</span> <span class="s2">&quot;created&quot;</span><span class="p">,</span> <span class="s2">&quot;author&quot;</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span> <span class="c1">#Drop Features that cannot be controlled by the user</span>
<span class="n">dataSet</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[15]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>score</th>
      <th>subreddit</th>
      <th>num_comments</th>
      <th>body</th>
      <th>is_self</th>
      <th>over_18</th>
      <th>spoiler</th>
      <th>upvote_ratio</th>
      <th>post_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Given that reddit just took a $150 million inv...</td>
      <td>228918</td>
      <td>pics</td>
      <td>6491</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.94</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>I got off the horse by accident right before a...</td>
      <td>226498</td>
      <td>gaming</td>
      <td>2238</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.97</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Take your time, you got this</td>
      <td>224055</td>
      <td>gaming</td>
      <td>3360</td>
      <td>NaN</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0.97</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>People who haven't pooped in 2019 yet, why are...</td>
      <td>221862</td>
      <td>AskReddit</td>
      <td>8132</td>
      <td>NaN</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0.91</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Whoever created the tradition of not seeing th...</td>
      <td>218614</td>
      <td>Showerthoughts</td>
      <td>2098</td>
      <td>Damn... this got big...</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0.96</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>From here, we'll conduct all analysis on this master dataset. Although metrics such as number of comments, post type, and upvote ratio cannot be controlled at the time of submission, we'll be keeping them as potential target metrics for later classification and regression. We still need to perform some data cleaning to make these features useable in machine learning models:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">uniqueSubReddits</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;subReddit&quot;</span> <span class="p">:</span> <span class="p">[]}</span> <span class="c1">#Get unique subReddits.</span>

<span class="k">for</span> <span class="n">tableRow</span> <span class="ow">in</span> <span class="n">dataSet</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span> <span class="c1">#Iterate through all rows in data set.</span>
    <span class="n">title</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;title&quot;</span><span class="p">]</span>
    <span class="n">subReddit</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;subreddit&quot;</span><span class="p">]</span>
    <span class="n">body</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;body&quot;</span><span class="p">]</span>

    <span class="n">originalContent</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;is_self&quot;</span><span class="p">]</span>
    <span class="n">nsfw</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;over_18&quot;</span><span class="p">]</span>
    <span class="n">spoiler</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;spoiler&quot;</span><span class="p">]</span>

    <span class="n">titleBlob</span> <span class="o">=</span> <span class="n">TextBlob</span><span class="p">(</span><span class="n">title</span><span class="p">)</span>

    <span class="n">lenTitle</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">title</span><span class="p">)</span>
    <span class="n">titleSentiment</span> <span class="o">=</span> <span class="n">titleBlob</span><span class="o">.</span><span class="n">sentiment</span><span class="o">.</span><span class="n">polarity</span> <span class="c1">#Sentiment score from [-1, 1] -1 -&gt; Negative, 1-&gt; Positive</span>
    <span class="n">titleSubjectivity</span> <span class="o">=</span> <span class="n">titleBlob</span><span class="o">.</span><span class="n">sentiment</span><span class="o">.</span><span class="n">subjectivity</span> <span class="c1">#Opinion score from [0, 1] 0 -&gt; Factual, 1 -&gt; Opinion</span>
    <span class="n">titleQuestion</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="s2">&quot;?&quot;</span> <span class="ow">in</span> <span class="n">title</span> <span class="k">else</span> <span class="mi">0</span> <span class="c1">#Is the title a question?</span>
    
    <span class="k">if</span> <span class="n">subReddit</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">uniqueSubReddits</span><span class="p">[</span><span class="s2">&quot;subReddit&quot;</span><span class="p">]:</span>
        <span class="n">uniqueSubReddits</span><span class="p">[</span><span class="s2">&quot;subReddit&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">subReddit</span><span class="p">)</span>

    <span class="n">lenBody</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">np</span><span class="o">.</span><span class="n">isnan</span><span class="p">(</span><span class="n">body</span><span class="p">):</span> <span class="c1">#Setting empty body elements to empty strings to homogenize the data type within the column</span>
            <span class="n">body</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span>
            <span class="n">lenBody</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">except</span><span class="p">:</span> <span class="c1"># Body is not NAN (Throws Exception)</span>
        <span class="n">lenBody</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">body</span><span class="p">)</span>

    <span class="c1">#Set cleaned values and additional features</span>
    <span class="n">dataSet</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s2">&quot;len_title&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">lenTitle</span>
    <span class="n">dataSet</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s2">&quot;title_question&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">titleQuestion</span>
    <span class="n">dataSet</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s2">&quot;title_sentiment&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">titleSentiment</span>
    <span class="n">dataSet</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s2">&quot;title_subjectivity&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">titleSubjectivity</span>
    <span class="n">dataSet</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s2">&quot;body&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">body</span>
    <span class="n">dataSet</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s2">&quot;len_body&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">lenBody</span>
    
    <span class="c1">#Convert True -&gt; 1 and False -&gt; 0</span>
    <span class="n">dataSet</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s2">&quot;is_oc&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">originalContent</span> <span class="k">else</span> <span class="mi">0</span>
    <span class="n">dataSet</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s2">&quot;is_nsfw&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">nsfw</span> <span class="k">else</span> <span class="mi">0</span>
    <span class="n">dataSet</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="s2">&quot;is_spoiler&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">spoiler</span> <span class="k">else</span> <span class="mi">0</span>

<span class="n">dataSet</span> <span class="o">=</span> <span class="n">dataSet</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s2">&quot;is_self&quot;</span><span class="p">,</span> <span class="s2">&quot;over_18&quot;</span><span class="p">,</span> <span class="s2">&quot;spoiler&quot;</span><span class="p">,],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">subRedditLookUp</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">uniqueSubReddits</span><span class="p">)</span> <span class="c1">#Create table to iterate through all sub-reddits</span>
<span class="n">subRedditOneHotEncoding</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">get_dummies</span><span class="p">(</span><span class="n">subRedditLookUp</span><span class="p">)</span> <span class="c1">#One hot encoding of categorical feature for input into model</span>
<span class="n">dataSet</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[16]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>score</th>
      <th>subreddit</th>
      <th>num_comments</th>
      <th>body</th>
      <th>upvote_ratio</th>
      <th>post_type</th>
      <th>len_title</th>
      <th>title_question</th>
      <th>title_sentiment</th>
      <th>title_subjectivity</th>
      <th>len_body</th>
      <th>is_oc</th>
      <th>is_nsfw</th>
      <th>is_spoiler</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Given that reddit just took a $150 million inv...</td>
      <td>228918</td>
      <td>pics</td>
      <td>6491</td>
      <td></td>
      <td>0.94</td>
      <td>1.0</td>
      <td>241.0</td>
      <td>0.0</td>
      <td>0.245455</td>
      <td>0.484848</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>I got off the horse by accident right before a...</td>
      <td>226498</td>
      <td>gaming</td>
      <td>2238</td>
      <td></td>
      <td>0.97</td>
      <td>1.0</td>
      <td>67.0</td>
      <td>0.0</td>
      <td>0.028571</td>
      <td>0.311905</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Take your time, you got this</td>
      <td>224055</td>
      <td>gaming</td>
      <td>3360</td>
      <td></td>
      <td>0.97</td>
      <td>1.0</td>
      <td>28.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>People who haven't pooped in 2019 yet, why are...</td>
      <td>221862</td>
      <td>AskReddit</td>
      <td>8132</td>
      <td></td>
      <td>0.91</td>
      <td>1.0</td>
      <td>87.0</td>
      <td>1.0</td>
      <td>-0.100000</td>
      <td>0.433333</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Whoever created the tradition of not seeing th...</td>
      <td>218614</td>
      <td>Showerthoughts</td>
      <td>2098</td>
      <td>Damn... this got big...</td>
      <td>0.96</td>
      <td>1.0</td>
      <td>189.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.500000</td>
      <td>23.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The <a href="https://www.reddit.com/dev/api/">Reddit API</a> makes data cleaning fairly straightforward. There are very few missing values, and all elements in the table are uniformly formatted, making it easier to specify rules to clean them. In addition to the features we are given through the API, we decided to calcualte a few other metrics that might be useful in determining the quality of a post. Specifically, we also look at the sentiment of the tilte, the objectivity of the title, length of the title, and length of the body. For the sake of simplicity, we do not consider the raw text data in a post to avoid dealing with links, subreddit specific acronyms and internet slang in general. Using these hand-crafted features, we will attempt to both regress the upvote ratio, and classify whether a post is considered a top post or a controversial post. Note that we choose to regress the upvote ratio rather than the total score because the score contains a very large range of values, making it difficult to accurately regress the values.</p>
<p>Now that our cleaning process is complete, it may help to define exactly what each of our features represents:</p>
<ul>
    <li><b>title</b>: The title of the post</li>
    <li><b>score</b>: The raw number of upvotes that this post received</li>
    <li><b>subreddit</b>: The subreddit this post was made on</li>
    <li><b>num_comments</b>: The number of comments made on this post</li>
    <li><b>body</b>: The text written in the post's body, if any</li>
    <li><b>upvote_ratio</b>: The percentage of upvotes to total votes (upvotes + downvotes) on the post.</li>
    <li><b>post_type</b>: Whether this post came from our top (1) or controversial (0) dataset.</li>
    <li><b>len_title</b>: The number of characters in the post's title</li>
    <li><b>title_question</b>: Whether or not the post's title contains the '?' character.</li>
    <li><b>title_sentiment</b> and <b>title_subjectivity</b>: Sentiment and subjectivity ratings of the title, as given by TextBlob (https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis).</li>
    <li><b>len_body</b>: Number of characters in the post's body text</li>
    <li><b>is_oc</b>: 1 if the post is an original text post, 0 otherwise (i.e. it links to an external website with no body text)</li>
    <li><b>is_nsfw</b>: 1 if the post is "nsfw" (inappropriate for some audiences), 0 otherwise</li>
    <li><b>is_spoiler</b>: 1 if the post is tagged as a spoiler, 0 otherwise</li>
</ul>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 style="text-align: center;">Exploratory Data Analysis</h2><p>Now that our data has been assembled, we'd like to take a closer look at the kinds of subreddits in each category. If you're making a post, what kind of subreddit should you post on to ensure its success?</p>
<p>To answer this question, let's take a look at the subreddits that most frequently broke the top 1000 posts in the last year. The following plot shows the subreddits which had at least 10 posts in the top 1000 in the last year:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[78]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Plot subreddits that most frequently broke top 1000</span>
<span class="n">subs</span> <span class="o">=</span> <span class="p">{}</span>
<span class="k">for</span> <span class="n">tableRow</span> <span class="ow">in</span> <span class="n">dataSet</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
    <span class="c1"># Tally how many times each subreddit appears in dataset</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;post_type&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span><span class="p">):</span> <span class="c1"># Filter only top posts</span>
        <span class="n">subreddit</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;subreddit&quot;</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">subreddit</span> <span class="ow">in</span> <span class="n">subs</span><span class="p">:</span>
            <span class="n">subs</span><span class="p">[</span><span class="n">subreddit</span><span class="p">]</span> <span class="o">=</span> <span class="n">subs</span><span class="p">[</span><span class="n">subreddit</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">subs</span><span class="p">[</span><span class="n">subreddit</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">top_subs</span> <span class="o">=</span> <span class="n">subs</span>
        
<span class="c1"># Filter out subs that broke top 1000 less than 10 times</span>
<span class="n">consistent_subs</span> <span class="o">=</span> <span class="p">{}</span>
<span class="k">for</span> <span class="n">sub</span> <span class="ow">in</span> <span class="n">subs</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">subs</span><span class="p">[</span><span class="n">sub</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="mi">10</span><span class="p">:</span>
        <span class="n">consistent_subs</span><span class="p">[</span><span class="n">sub</span><span class="p">]</span> <span class="o">=</span> <span class="n">subs</span><span class="p">[</span><span class="n">sub</span><span class="p">]</span>
        
<span class="c1"># Create bar chart</span>
<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">consistent_subs</span><span class="p">)),</span> <span class="nb">list</span><span class="p">(</span><span class="n">consistent_subs</span><span class="o">.</span><span class="n">values</span><span class="p">()),</span> <span class="n">align</span><span class="o">=</span><span class="s1">&#39;center&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">consistent_subs</span><span class="p">)),</span> <span class="nb">list</span><span class="p">(</span><span class="n">consistent_subs</span><span class="o">.</span><span class="n">keys</span><span class="p">()),</span> <span class="n">rotation</span><span class="o">=</span><span class="s1">&#39;vertical&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Most Frequent Subreddits in Top 1000&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;Number of Posts&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;Subreddit Name&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAYUAAAFqCAYAAAD1MUYfAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nOzdd5wkVbn/8c+XnIOwKGldkiBxwQXlEgRUREFEyQICooAXvChGRJLoFUXhhyBhkSRXkmQJgpJB4hKWBUGykhdJS2aX7++Pc7qnt7dntruqenqGfd6vV79murrr9OmennqqTniObBNCCCEAzNTrCoQQQhg6IiiEEEKoi6AQQgihLoJCCCGEuggKIYQQ6iIohBBCqIugEEKHJG0g6ckuv4YlLdvPY7tIurHh/muSlq7gNY+XdEDZcsLwFkFhiJH0uKR3JC3ctP3ufKAYVbL8fg82+fFdJE3JB5ra7Zgyr9kLbbzP2ST9RtKT+T0+JunIwaxjVWzPY/tRAEmnSvpZwXL2tH1op/tJuq/huzJF0lsN939cpC4DvNbGkq6TNEnSAy0eX0bSDZLeyPVav+nxnSX9K9ftXEnzNzw2p6Q/SHpV0tOS9q6y7sNFBIWh6TFg+9odSasAcw7i69+cDzS1W8t/DkkzD2KdqrYfMAZYC5gX2BC4qxsvNMw/p+myvVLtuwLcAOzd8N3534pf7jVgLOnv18q5uQ4fAH4GXChpAQBJqwO/BbYFFgUEHNWw7/8CiwMjgU2AgyRtUHH9h7wICkPT6cBXG+7vDPyh8QmS5s9nNRMlPSHpJ5Jmyo8tm8+mXpH0gqSz8/br8+735DOlbTupVD4LPU7SZZJeBzaUNLukX+ezr+dyE8ScDft8X9Iz+czra41n8JKulfT1huc2N4usIOmvkl6U9KCkbZrq8jtJl+azxlslLdPB+1wTuMD2004et/2HhvKnutJodQYu6cf5831c0g5Vfk5Nr7OQpIvzGextwDJNjzv/zXcHdgB+kN/3n/PjP5T0VP6cHpT0qRafx1TvUbmJTNJ3JT2f67Zrq/2mR9LMkg5peO8nS5o3P7aCpMmS9mx4/9/qryzbf7f9R+DxFq+zKvAR4FDbb9k+E3gE2CI/ZSfgPNs3254EHAhsK2mO/PhXgUNsv2x7PHAqsEuR9zycRVAYmm4B5pP00XyWuS3wf03PORqYH1ga+CTpC137pz0UuBJYEFgiPxfbtUvp1fJZ3NkF6vYV4Oeks+sbgV+S/hFHA8uSzrQOBJC0CfA94DPAcsCn230RSXMDfwXOABYhXTkdK2mlhqdtDxyS3+fDuV7tvs9bgH0l/bekVSSp3bplHwIWJr3fnYGxkpZveLzKz+l3wFuks9uv5ds0bI8F/gj8Kr/vL+Q67Q2saXte4LO0OKAO8B7nz3XdDfidpAXb3LfRHsA2wHqk97cIcETD4zMDa5O+y5sCh0hat8DrrAT80/abDdvuydtrj99Te8D2ffm1l5G0KOnq4p5+9p1hRFAYumpXC58BHgCeqj3QECj2sz3J9uPAb0hnQgDvAh8GFstnTDfSmU9Iernh9omGxy6yfZPt94C3gW8A37H9Yj77+l9gu/zcbYBTbE+w/TpwcAd12Ax43PYptifbvhM4D9iq4Tnn277N9mTSwXB0B+X/gnSg3gG4A3hK0s4d7A9wgO23bV8HXEp6vzWVfE75b70lcKDt121PAE7roI5TgNmBFSXNmq+IHmlz33eBn9p+1/ZlpKab5aezTys7AIfbfsL2q8D+wA5Ngfgg22/avot0ArR9q4KmYx7glaZtr5ACc3+PT8qPz5Pvv9rPvjOMCApD1+mks81daGo6Ip2hzgY80bDtCdIZHcAPSO2ltyl1trU8sxzALbYXaLjd0vDYvxt+HwHMBYyrBRDgL3k7wGJNz2+s7/R8GPh4Y3AiHVw+1PCcZxt+f4O+f+zpsj3F9u9srwMsQDqrP1nSR9ss4qV8AK95gvR+a6r6nEYAswzw+IBsPwx8mxRonpd0lqTFBt6r7j854NZ09Bk3WIxpv6tzks7Ma5rfX7t1bPQaMF/TtvlIB/7+Hp83P/5aw/1W+84wIigMUbafIHU4fx44v+nhF+i7GqgZSb6asP2s7W/YXox06X6sBhiJ02nVmurxJrBSQwCZP3c4AjwDLNlUx0avkw6WNY0H/H8D1zUFp3lsf7Oi91GXz1B/B7wErJg3vzFA3QAWzE1cNSOBpxuLbfi9zOc0EZg8wOPTvJ1pNthn2F6X9H0x6QppMD3NtN/VN4EXG7Y1v7/Gz7Jd9wEfaegjAFgtb689vlrtAUkrkq6kHrH9TK7Pav3sO8OIoDC07QZs1HRGiu0pwDnAzyXNK+nDwL7kfgdJW0taIj/9JdKBYEq+/xyp7ba03DRyInCkpEXyay8u6bP5KecAu0haUdJcwEFNRdwNfFnSXDlo7dbw2CWkf/CdJM2ab2t2cCY/4PuU9O3cmTqnpFly09G89I1Auhv4Su4k3YTUb9PsEKWhreuRmrv+1Oq1ynxO+W99PnBw/pxWJPVhtPW+JS0vaSNJs5P6Jd6k77swWM4EvidpZO5g/hlwhqfO239Q/lusRmoGbdnfJWmmfNCfNd3VHJJmBcidww8BByh17G9D6r+5KO/+f8CWkj4haR5Sf9TZtt/Kj58OHKg0iGMV0lX6qVV9CMNFBIUhzPYjtu/o5+Fvkc60HyV1ZJ4BnJwfWxO4VdJrwMXAPrYfy48dDJyWmzG2obwfkjp5b5H0KvA3cruz7cuB/wdcnZ9zddO+RwLvkA5kp5H6Bcj7TgI2JrW7P01qKvolqX28HQcz8Pt8k9QP8yzpTH4vYMvaeH9gH+ALQK3Z6sKm/Z8lBdync733tD3NuPkGZT6nvUnNNs+SDlKnDPA6J5H6D16WdCHp8zosv8dnSZ28lc4daMNxpMD2d9JooBdJJzE1U4BbSVfGfyH1Y1zfXEi2Melvdz6p4/5N4M8Nj28NrE/6ux0MfMn2SwC5X+rbpGGrz5GOf/s07Ptj0mf0JGmgxk9tX1vg/Q5rciyyEwaRJAPL5bbuMIOTtAIwwfYsva5LSOJKIYQQQl0EhRBCCHXRfBRCCKEurhRCCCHURVAIIYRQN6x7/BdeeGGPGjWq19UIIYRhZdy4cS/YHtHqsWEdFEaNGsUdd/Q3jD+EEEIrkvpNlRLNRyGEEOoiKIQQQqiLoBBCCKEugkIIIYS6CAohhBDqIiiEEEKoi6AQQgihrmtBQdLJkp6XNKFh29mS7s63xyXdnbePkvRmw2PHd6teIYQQ+tfNyWunAsfQsL6w7W1rv0v6DVMvov2I7U4WXi9t1I8uLbX/44dtWlFNQghhaOhaULB9vaRRrR6TJGAbYKNuvX4IIYTO9apPYT3gOdsPNWxbStJdkq7La96GEEIYZL3KfbQ9aTHvmmeAkbb/I+ljwIWSVrL9avOOknYHdgcYOXLkoFQ2hBBmFIN+pSBpFuDLwNm1bbbftv2f/Ps40uLeH2m1v+2xtsfYHjNiRMskfyGEEArqRfPRp4EHbD9Z2yBphKSZ8+9LA8sBj/agbiGEMEPr5pDUM4GbgeUlPSlpt/zQdkzddASwPjBe0j3AucCetl/sVt1CCCG01s3RR9v3s32XFtvOA87rVl1CCCG0J2Y0hxBCqIugEEIIoS6CQgghhLoICiGEEOoiKIQQQqiLoBBCCKEugkIIIYS6CAohhBDqIiiEEEKoi6AQQgihLoJCCCGEuggKIYQQ6iIohBBCqIugEEIIoS6CQgghhLoICiGEEOoiKIQQQqiLoBBCCKEugkIIIYS6CAohhBDquhYUJJ0s6XlJExq2HSzpKUl359vnGx7bT9LDkh6U9Nlu1SuEEEL/unmlcCqwSYvtR9oenW+XAUhaEdgOWCnvc6ykmbtYtxBCCC10LSjYvh54sc2nfxE4y/bbth8DHgbW6lbdQgghtNaLPoW9JY3PzUsL5m2LA/9ueM6TeVsIIYRBNNhB4ThgGWA08Azwm7xdLZ7rVgVI2l3SHZLumDhxYndqGUIIM6hBDQq2n7M9xfZ7wIn0NRE9CSzZ8NQlgKf7KWOs7TG2x4wYMaK7FQ4hhBnMoAYFSYs23P0SUBuZdDGwnaTZJS0FLAfcNph1CyGEALN0q2BJZwIbAAtLehI4CNhA0mhS09DjwB4Atu+TdA5wPzAZ2Mv2lG7VLYQQQmtdCwq2t2+x+aQBnv9z4Ofdqk8IIYTpixnNIYQQ6iIohBBCqIugEEIIoS6CQgghhLoICiGEEOoiKIQQQqiLoBBCCKEugkIIIYS6CAohhBDqIiiEEEKoi6AQQgihLoJCCCGEuggKIYQQ6iIohBBCqOta6uwQihr1o0tLl/H4YZtWUJMQZjxxpRBCCKEugkIIIYS6CAohhBDqIiiEEEKoi6AQQgihrmtBQdLJkp6XNKFh2+GSHpA0XtIFkhbI20dJelPS3fl2fLfqFUIIoX/dvFI4FdikadtfgZVtrwr8E9iv4bFHbI/Otz27WK8QQgj9mG5QkLS1pHnz7z+RdL6kNaa3n+3rgRebtl1pe3K+ewuwRIE6hxBC6JJ2rhQOsD1J0rrAZ4HTgOMqeO2vAZc33F9K0l2SrpO0XgXlhxBC6FA7QWFK/rkpcJzti4DZyryopP2BycAf86ZngJG2Vwf2Bc6QNF8/++4u6Q5Jd0ycOLFMNUIIITRpJyg8JekEYBvgMkmzt7lfS5J2BjYDdrBtANtv2/5P/n0c8AjwkVb72x5re4ztMSNGjChajRBCCC20c3DfBrgC2MT2y8AHgO8XeTFJmwA/BDa3/UbD9hGSZs6/Lw0sBzxa5DVCCCEU105QOMH2+bYfArD9DLDT9HaSdCZwM7C8pCcl7QYcA8wL/LVp6On6wHhJ9wDnAnvafrFlwSGEELqmnSypKzXeyWf0H5veTra3b7H5pH6eex5wXht1CSGE0EX9XilI2k/SJGBVSa/m2yTgeeCiQathCCGEQdNvULD9C9vzAofbni/f5rW9kO39+tsvhBDC8NVOn8IlkuYGkLSjpCMkfbjL9QohhNAD7QSF44A3JK0G/AB4AvhDV2sVQgihJ9oJCpPzfIIvAkfZPoo0giiEEML7TDujjyZJ2o80DHW9PPpo1u5WK4QQQi+0c6WwLfA28DXbzwKLA4d3tVYhhBB6YrpBIQeCPwLzS9oMeMt29CmEEML7UDups7cBbgO2JqW8uFXSVt2uWAghhMHXTp/C/sCatp+HlKcI+BspHUUIIYT3kXb6FGaqBYTsP23uF0IIYZhp50rhL5KuAM7M97cFLutelUIIIfTKdIOC7e9L+jKwLiBgrO0Lul6zEEIIg27AoCBpC2BZ4F7b+w5OlUIIIfTKQFlSjwW+AywEHCrpgEGrVQghhJ4Y6EphfWA121MkzQXcABw6ONUKIYTQCwONInrH9hSAvHSmBqdKIYQQemWgK4UVJI3PvwtYJt8XYNurdr12IYQQBtVAQeGjg1aLEEIIQ0K/QcH2E4NZkRBCCL0XM5NDCCHUdS0oSDpZ0vOSJjRs+4Ckv0p6KP9csOGx/SQ9LOlBSZ/tVr1CCCH0b6B5Clfln78sWPapwCZN234EXGV7OeCqfB9JKwLbASvlfY7Ni/mEEEIYRANdKSwq6ZPA5pJWl7RG4216Bdu+HnixafMXgdPy76cBWzRsP8v227YfAx4G1uronYQQQihtoNFHB5LO5JcAjmh6zMBGBV7vg7afAbD9jKRF8vbFgVsanvdk3hZCCGEQDTT66FzgXEkH2O72TOZWE+Pc8onS7sDuACNHjuxmnUIIYYbTznKch0raXNKv822zEq/3nKRFAfLP2joNTwJLNjxvCeDpfuoz1vYY22NGjBhRoiohhBCatbMc5y+AfYD7822fvK2Ii4Gd8+87Axc1bN9O0uySlgKWIy0BGkIIYRC1s8jOpsBo2+8BSDoNuAvYb6CdJJ0JbAAsLOlJ4CDgMOAcSbsB/yKt+4zt+ySdQwo6k4G9anmXQgghDJ52ggLAAvSNJJq/nR1sb9/PQ5/q5/k/B37eZn1CCCF0QTtB4RfAXZKuIXUIr890rhJCCCEMT+0sx3mmpGuBNUlB4Ye2n+12xUIIIQy+tpqP8tyCi7tclxBCCD0WCfFCCCHUtdvRHEK/Rv3o0lL7P37YphXVJIRQ1oBXCpJmasxyGkII4f1twKCQ5ybcIynySYQQwgygneajRYH7JN0GvF7baHvzrtUqhBBCT7QTFA7pei1CCCEMCe3MU7hO0oeB5Wz/TdJcQCyAE0II70PtJMT7BnAucELetDhwYTcrFUIIoTfamaewF7AO8CqA7YeARQbcI4QQwrDUTp/C27bfkdI6OJJmoZ8FcEIYqmIuRQjtaedK4TpJPwbmlPQZ4E/An7tbrRBCCL3QTlD4ETARuBfYA7gM+Ek3KxVCCKE32hl99F5eWOdWUrPRg7aj+SiEEN6HphsUJG0KHA88QkqdvZSkPWxf3u3KhRBCGFztdDT/BtjQ9sMAkpYBLgUiKIQQwvtMO30Kz9cCQvYo8HyX6hNCCKGH+r1SkPTl/Ot9ki4DziH1KWwN3D4IdQshhDDIBmo++kLD788Bn8y/TwQWLPqCkpYHzm7YtDRwILAA8I1cPsCPbV9W9HVCCCF0rt+gYHvXbryg7QeB0QCSZgaeAi4AdgWOtP3rbrxuCCGE6Wtn9NFSwLeAUY3Pryh19qeAR2w/UZsxHUIIoXfaGX10IXASaRbzexW//nbAmQ3395b0VeAO4Lu2X6r49UIIIQygndFHb9n+re1rbF9Xu5V9YUmzAZuT0mYAHAcsQ2paeoY0FLbVfrtLukPSHRMnTmz1lBBCCAW1ExSOknSQpLUlrVG7VfDanwPutP0cgO3nbE/JS4CeCKzVaifbY22PsT1mxIgRFVQjhBBCTTvNR6sAOwEb0dd85Hy/jO1paDqStKjtZ/LdLwETSpYfQgihQ+0EhS8BS9t+p6oXzau3fYaUYK/mV5JGkwLO402PhRBCGATtBIV7SHMIKpvFbPsNYKGmbTtVVX6vlM3ZD5G3P4TQW+0EhQ8CD0i6HXi7trGiIakhhBCGkHaCwkFdr0UIIYQhoZ31FEoPPw0hhDA8tDOjeRJ9azLPBswKvG57vm5WLIQQwuBr50ph3sb7kragnzkEIYQQhrd2Jq9NxfaFlJ+jEEIIYQhqp/noyw13ZwLG0NecFEII4X2kndFHjesqTCZNLPtiV2oTQgihp9rpU+jKugqhN2KCXQhhIAMtx3ngAPvZ9qFdqE8IIYQeGuhK4fUW2+YGdiOlqIigEEII7zMDLcdZX89A0rzAPqQlM8+in7UOQgghDG8D9ilI+gCwL7ADcBqwRqyGFkII718D9SkcDnwZGAusYvu1QatVCCGEnhho8tp3gcWAnwBPS3o13yZJenVwqhdCCGEwDdSn0PFs5xBCCMNbHPhDCCHURVAIIYRQF0EhhBBCXQSFEEIIde0kxKucpMeBScAUYLLtMXlOxNnAKFLSvW1iTkQIIQyuXl4pbGh7tO0x+f6PgKtsLwdcle+HEEIYRD25UujHF4EN8u+nAdcCP+xVZUIYSGSbDe9XvbpSMHClpHGSds/bPmj7GYD8c5Ee1S2EEGZYvbpSWMf205IWAf4q6YF2d8xBZHeAkSNHdqt+IYQwQ+rJlYLtp/PP54ELgLWA5yQtCpB/Pt/PvmNtj7E9ZsSIEYNV5RBCmCEMelCQNHdOxY2kuYGNgQnAxcDO+Wk7AxcNdt1CCGFG14vmow8CF0iqvf4Ztv8i6XbgHEm7Af8Ctu5B3UIIYYY26EHB9qPAai22/wf41GDXJ4QQQp+Y0RxCCKEugkIIIYS6CAohhBDqIiiEEEKoi6AQQgihLoJCCCGEuggKIYQQ6iIohBBCqIugEEIIoS6CQgghhLoICiGEEOoiKIQQQqiLoBBCCKEugkIIIYS6CAohhBDqIiiEEEKoi6AQQgihLoJCCCGEuggKIYQQ6iIohBBCqBv0oCBpSUnXSPqHpPsk7ZO3HyzpKUl359vnB7tuIYQwo5ulB685Gfiu7TslzQuMk/TX/NiRtn/dgzqFEEKgB0HB9jPAM/n3SZL+ASw+2PUIYagZ9aNLS5fx+GGbVlpmc3nh/a+nfQqSRgGrA7fmTXtLGi/pZEkL9qxiIYQwg+pZUJA0D3Ae8G3brwLHAcsAo0lXEr/pZ7/dJd0h6Y6JEycOWn1DCGFG0Is+BSTNSgoIf7R9PoDt5xoePxG4pNW+tscCYwHGjBnj7te2t+LyP4QwmHox+kjAScA/bB/RsH3Rhqd9CZgw2HULIYQZXS+uFNYBdgLulXR33vZjYHtJowEDjwN79KBuIYQwQ+vF6KMbAbV46LLBrksIIYSpxYzmEEIIdT3paA4hhG7pxnyPGUkEhRBCT8UIu6Elmo9CCCHURVAIIYRQF81HIYS2RXv9+19cKYQQQqiLoBBCCKEugkIIIYS6CAohhBDqIiiEEEKoi9FHIYQwyIbyKK64UgghhFAXVwohhDAdM1IqjrhSCCGEUBdBIYQQQl0EhRBCCHURFEIIIdRFUAghhFAXQSGEEEJdBIUQQgh1Qy4oSNpE0oOSHpb0o17XJ4QQZiRDKihImhn4HfA5YEVge0kr9rZWIYQw4xhSQQFYC3jY9qO23wHOAr7Y4zqFEMIMY6gFhcWBfzfcfzJvCyGEMAhku9d1qJO0NfBZ21/P93cC1rL9rYbn7A7snu8uDzzYxSotDLwwhMvrRpnDoY7dKDPqODTLGy5lDoc6Nvqw7RGtHhhqCfGeBJZsuL8E8HTjE2yPBcYORmUk3WF7zFAtrxtlDoc6dqPMqOPQLG+4lDkc6tiuodZ8dDuwnKSlJM0GbAdc3OM6hRDCDGNIXSnYnixpb+AKYGbgZNv39bhaIYQwwxhSQQHA9mXAZb2uR1Z1M1U3mr1mxDp2o8yo49Asb7iUORzq2JYh1dEcQgiht4Zan0IIIYQeiqAQQgihLoJCmIqkBSWtWrKMlauqTwgzKkkzSZpvsF83gkITSXNLmin//hFJm0uatUR590oa33S7QdKRkhYqWOavJM0naVZJV0l6QdKOJep4bS7vA8A9wCmSjihaHnC8pNsk/bekBUqU01jHRyT9UdKeVeXDkrSOpLnz7ztKOkLSh0uUt0/+HCXpJEl3Stq4ZB23ljRv/v0nks6XtEbJMj/XYtueJcqr9Dte5eco6csD3QqW+YGBbkXKbCj7jPze5wbuBx6U9P0yZXYqgsK0rgfmkLQ4cBWwK3BqifIuBy4Fdsi3P+fXeLZEuRvbfhXYjDTh7yNAmS/O/Lm8LwOn2P4Y8Omihdlel/RelwTuyF/0z5SoH6QEiScACwG/lvSopAtKlnkc8Iak1YAfAE8AfyhR3tfy57gxMIL03TmsZB0PsD1J0rrAZ4HTSPUuVaakjWp3JP2QcjnGqv6OV/k5fiHfdgNOaqjj74GiJ1LjgDvyz+bbHQXLrFkxv/ctSKMwRwI7lSyzI0NuSOoQINtvSNoNONr2ryTdVaK8dWyv03D/Xkk32V6nxNl97crl88CZtl+UVKKKzCJpUWAbYP8yBdXYfkjST0j/JL8FVleq5I9tn1+gyCnAu/nne8BzwPMlqznZtiV9ETjK9kmSdi5RXu2P8HlScL1HJf8wpPcLsClwnO2LJB1csszNgUvyGegmwAp5W1FVf8cr+xxt7wog6RLSAfeZfH9RUkbmImUuVWS/Ns2aWya2AI6x/a6kQR0iGlcK05KktUlnE5fmbWWC5zySPt5Q+FrAPPnu5IJl/lnSA8AY4CpJI4C3StTxp6QJg4/Yvl3S0sBDRQuTtKqkI4F/ABsBX7D90fz7kQWLfRX4f8BjwM6217a9R9E6ZpMk7Uc6Y7xUKXV74aZCYJykK0kHsytys897Jev4lKQTSAH7MkmzU/L/1vYLpCDwO2AxYCvb75YosurveDc+x1G1gJA9R7rCLiw3b+0o6YB8f2R+72WcADwOzA1cn5szXy1ZZkdinkITSZ8EvgvcZPuX+QD5bdv/U7C8NYGTSf8kIv2Bvw7cB2xq+5wCZc4OzAW8antKbn+cx/ZzRepYNUnXky7P/2T7zabHdrJ9eoEyvwisS0qv/g7wd+B621cVKGt2229L+hDwFeB22zdIGglsYLtQE5JSX9Ro4FHbL+f29MVtjy9SXi5zLtLZ/L356mtRYBXbVxYoaxJg0vfQwGykg7YB2y7UqVn1d7xLn+MxwHLAmaT3ux0pTf+3Btxx4DKPIwWrjWx/VNKCwJW21yxaZj+vM4vtoieQnb9eBIXBIWl+0uf9cgVl3Wl7jelt66C8j5DaqT9oe2Wl0Ueb2/5Z2bpWTdIKpEWYvg0sYnvOAmXcaXsNSafbrqy9Njdx7AAsbfunOch8yPZtJctdF1jO9in5qnAe249VUOVKVfUdl/QH4AbgBtsPVFK5VO6XgPXz3ettl+qTavge3WV79bztHturFShr34Eet11m4EdHok+hiaS/AlvXvtg5+p9l+7MFy5sd2BIYRWq7B8D2TwuU9SHS+hJzSlqdvrbX+UhXDkWdSOqoPiHXbbykM4BCQUHSOsDBwIdJ3zGlYr100QpKOo909vgw6YDxVeDWgsXNlvsO/qvVCJSCfR4Ax5LPHElNcpOA84DCZ46SDiI1Ey4PnEJq3vo/YJ2B9ptOmV8Crrb9Sr6/AOkK6cKC5VX2Hc9OJV0VHp2v1O8mHcSPKlhezZ3AJNt/kzSXpHltTypR3ru5ydEAOWAXbeaaN/9cnvR9qSUC/QKp037QRFCY1ojGMx3bL0n6YInyLgJeIY1MeLtk3T4L7EJKKd545jAJ+HGJcueyfVtTX16Zy9WTgO+Q3vOU6Ty3XYcBd9quorw9SWf0C5D+6RoZKBoUPl47c4T6d2e24tUE4EvA6qQDGrafzm3sZRzUeJacm2gOAgoFBar9jmP7aknXkQ6OG5L+XisBhYOCpG+Q1mH5ALAM6eTqeOBTJar6W+ACYBFJPwe2An5SpCDbh+R6XgmsUQtWeVDBn0rUsWMRFKY1RdJI2/8CyB09ZTq5lrC9SRUVs30acJqkLW2fV0WZ2QuSlqHvjGcr4JmBd3DjCW0AACAASURBVBnQK7Yvr6RmfY4gdbzdQOrvKXyGZ/tG4EalfPUnVVbDas8ca97JI6RqZc5dsjxo3VFd5lhQ2XccQNJVpI7Wm0lXhWvaLjvSbC9Sf9StUB8dt0iZAm3/UdI4UmARsIXtf5Ss50hSn1nNO6QrsEETQWFa+5MOGNfl++vTt9JbEX+XtIrte8tXre4SSV8hX67XNpa4XN+LlJFxBUlPkUb4FJ4MB1wj6XDSGXf9zNH2nSXK3JnUpLAlcLikt0ltzt/ptCBJG9m+Gnip4uajys4cG5yTRx8tkM92v0Zq7ivjDqXJib8jBbBvkc7yi6r6Oz4e+BiwMukK5GVJNzcPWujQ27bfqV0NS5qFHLyLknQUcLbtQkNb+3E6cJvSHByTrhRPq7D86YqO5hYkLQx8ghT9b85D+IqWdT+wLOlA+zZ97euFU0lI+gt9l+v15hTbvylaZi53bmCmku2sSLqmxWbb3qjF9k7KXRT4JLAeqVnhX0XOUCUdYvsgSacw9Wic2t/mayXquAJ9Z45XVXDmiNLEv41zmVfY/mvJ8uYGDiBNUBRwJfAz268XLK/y73gudx7SxLXvkTrsZy9R1q+Al0l9Ud8C/hu433bheTm5X2pb0tDWC0gBouzkNZRmrK+X715vu8w8qc5fP4JCImkF2w+onxQCRc9y1U/aBNtPFCkvlznBdmX5hXJH41eZ9sqj0DDcbpD0CGm92jNITQp32y7VNCPpu/QFA/LvrwDjbN9dsMwFSTO5Gz/HMldItXLnayrzxbJlVqXq77jSQlvrka4WniB1tN6Qr+6K1nEm0qzmenAFfu8KDoBKqS22JA1zHWl7uRJ1HF/l/3YR0XzUZ19SM9FvmPqysnYW2dFZrqT5nKarlzrr7kfVl+uXAbcA91K+DXya0Si17SWatyA1zawLbE/qeL1O0vW2HylR5sdII3suJv2dNyUtCbunpD/Z/lUnhUk6lDQQ4BH6vkMdf3eaytyDNJLpTdLfpvZ9LDOS6xpaNJ10eiXXxe/4nKQ+pHFVjc/PJxAnUr7prZVlSbPCR5HyFRVi+z1J9zT2afZCXCk0kTQn6dJyXdI/zg2k9AIdzRiWdIntzSQ9xtRno1BweKake3NZs5Am4jxKBZfrKjHHoZ/yutK8lctubFJYwvbMJcq6AtjS9msNZZ9LascdZ7ujxHuSHiRNLHtnuk9uv8yHgLXLNGG2KPNjDXfnIAXwybZ/0GE5lX/HG8qudG5Gl4ZJ/5KUL+wR4GzgggrmaFxNGnV1G1BvzrNdJg1JR+JKYVqnkWZk/jbf356UJG2bTgqxvVn+WWWelM0qLKvR6bkT8xKm7hgu2kRR6WgUAEm/ITUp1EalHEgK2GU0j/R4F/iw7TdzR3anJpCGuZYdKdPoEeCNCsvDdnOn8k0NAys6Kacb3/GuzM2gO8OkH6PigA0cUmFZhURQmNbynnpG4jWS7ilToNIM4VFM3ZTS8QiXWhutWqfnLXMJ/w5wOGnkVWOzR9GzqG6MuLoF+DXpQF7rcFyCdLVU1BnALZIuyve/AJypvrTFnfoFcJekCUwdXMuc5e1H+jxvbSqzcH9P0/dnJlIz2odKlHeV7U9Nb1sHujE3oxvDpMcCX5FU2Qx229fleVG1CY+3VTActyMRFKZ1l6RP2L4FQCnR101FC5N0MrAqKQ9Mrb2+zAQpSP8sSwIvkS6DFwCekfQ88I0WZ4LTsy+wbIVnPOsCu+RmhapGoyxAGiWzBGmG6ydIVwyF2+ttHyrpslxfAXs2jB7ZoUCRpwG/pKK+mewE4OqKyxxHX3PPZNIZ726dFiJpDtJM+oVzB3vjDPvFStSvG3MzujFM+ndUP4N9G9IJ2rWkz/NoSd+3fW6JenYkgsK0Pg58VVKto2ck8I9ae36BA9snOm2bbsNfSO2XVwAoLUCyCXAOKdXCxwfYt5X7qLaJYppFXCrwP6R/tltsb5iHfpa+1M4BtMwY/UYv2P7t9J/Wkcm2B8yL0y5JW9v+E/Ap22WusGr2IOWgWoz0GdaCwqsUTEuddWNuRu1/YkzDtlKDAOjODPb9aZisl/tT/kbq6xoUERSmVWlbOHCzpBVtFx6V0MIY2/WVsmxfKel/be+bR/50agpwdx6VUkUTRTdGL7xl+y1JtSynD0havguvU8Y4Sb8gjWaq6mz0Gkm7kxauKdvfsx8pZcK5QOmBBU65iI6S9C3bR5ctr6HcX+e5Ga+S+hUOLDM3Iw/1PM4FMhJPRzdmsM/U1Fz0HwZ5iYMICk3KzB/ox2mkwPAs1TWlvKi0WtZZ+f62pNm5M1PsS3khxfPetHIpfc0TcwBLAQ+S8tcU9WSeT3Eh8FdJLwFPl61oxVbPPz/RsK3s2ehX8s/9msos0t/znxz4l5J0cfODJfo+nlVOLqe0sNIapMlwhYNhDgKlJuk1lPVenvtQdVDoxgz2v+RRcWfm+9uShowPmhiS2mWSHia12U/VJlxy8trCwEH0tYXfSGpKeYU0eebhAmXOmfd9sGi9Bih7DWAPl18Up1beJ4H5gb9UOfzz/S43baxBSqXw9ebHbXc8AimXO972qnkY6S9IAwJ+bLvTZsxaeV8m9c0sQvp+106kCi9ir7QQzpukoaONQz1LTQJUd2awb0kaaSUqSPHd8etHUOguSVd3OilosEn6AukfeTbbS0kaDfy0yrHRVc+FGIryqJH/BRaz/TlJK5KGLBZOuqe0yM6+pIC9u6TlSCPkLilR5gjbE/PvM5HmABRe3Ut5PYHcdHav7TPUsMZAgfIeJq3WV/oA21BmqzkORecLtRr911hox4FG0rdJA1ru8iAuqNNKNB913wNKaxM0twkXHn1U1YzUBgeTMkhem8u5W1LhseeaesGQ2pDHiUXLG0ZOJY2rr+XT+SfpzLRMJtZTSJ24/5XvP0nqFygcFEj9AHuS+pLGAfNLOsL24QXLqy0Z+mnglyq/ZOhzVQYEqHwuRePorfpLUG62+RKk1OArSBpPWlnwJlLutUFNaRJXCl2mlHStmV0u6VolM1IbyrvV9sc19QpS4zvt91BeyUzSy/StxTyZtObsee5wVvhwI+l222s2fY532x5dosw7bI9RBat7NZR5t+3RknYgBewfkmZwF50RX9mSobm8o0jzJi6kohOpXO7KwIqk/5lamYWWXu2W3MQ3hnQSsHa+vdyFEYz9iiuFLrO9axfKrGRGaoMJSqm4Z87NE/9DOlPp1MeUkqP9C2gejTIX8L4OCsDrSusJ10ajfILUz1PGO7m/p1bmMpRfyGZWSbMCWwDH2H63NiegCNtv5Dky6wIPkU4EHipRv/lIQ6Q3bnwZSsztUZolvQEpKFxGGjZ9IylbQdEyWzWHvgI8UaIJaE7S+58/354m9UcOmggKXZYn+OxGGnnTeIZS5kqh0hmppFTC+5MONmeQMkgeWqCc40lzKJYCGlMIl07iNkzsSxqOuoykm4ARpBEpZRxE+kyXlPRHUgfkLiXLPIF09XYPaeGiD5OGfxaiitNSdONEivR3WI3UZr9r7v/5fckyjyV13I8nfcdXIX2mC0nas5MrJUljSceISaSFgP4OHGH7pZJ17Fg0H3WZpD8BD5CGFv6UNFP2H7b3KVFmYwKy2ozUnzqtKFakvDGkoDCKvhOFwsNmJR1n+5tF9h3ulBZvWZ70t3nQ9rsVlLkQfet73FLhzPPG15il6NmtpLvJaSlKNj8ezQBzXErMm0HSbbbXUlopbUPSwXeC7cLDpCWdBRxq+758f0XSWueHAud30myolERyYVL+rL+TZutPcA8O0HGl0H3L2t5a0hdtn5Y7na8oU2DFnWYAfyRlHZ1ABakUZuCAMDPwefqC68aSsH3EgDtO3+LAzLnM9XOZZdvXN6Xp6pV00lJEVWkpaleX65Caec7O97em/KzzO/I8lxNzWa+RMpGWsUItIADYvl/S6rYf1dTrnU+X7U2UdlqJ1J/wXWBlSS+SOpsPKlnXtkVQ6L7ameLLuaPrWUquuZrbg79JWioU0qihE0qclU60/ecydQpAGmH2FhXmKVIXcmdJOp7Ux7MhqQllK8odICtJS+G0BjmSdgE2rH2fc30LdVo3lP3f+dfj81n5fLbHlykTeFDScUw9ifSfefRVx/+L+apgQh6o8Uq+bUYaGThoQSGaj7pM0tdJSbJWIQ1ZnAc4wPYJJcr8PandtrZ2607AFNvTTEhqs7xPkVKEX0WFoz1mNEWaTNoo8/6qR540TDar/ZyH1Nyx8XR37r/MypYMVVqXYu3aUEylZHu32C6c1iSfhe8AVJbRVFOvvVKbRHos6cRgLud1Otos639IVwjrkALKTaQmpJtIo7qqSoY4XXGl0H3zkxaFgb4kYZMljXbBJR9JCbMahyRerXLpvXclrRw1K9Vlcp0RXS5p46JDMfvRjdxZb+afb0hajJRfp1CTZG4yu8L2p6koLQVwGClbcW2t70+S5tKUcSwVZzS1/SZppcZWi0e1HRCyUaScVN+x/UzROlUhgkL31ZZ8rDXPlFryMZsiaRnnpSglLU25hUNWs71Kif1DcgtwQZ4l/C4VpGegO7mzLsnt64eT0rCbgiNxbE+R9Iak+W2XHX5bK/MUSZfTl9n0R7afLVls5RlNNe1qbuSyOx5l55wJV9KvJZ1c8UlARyIodN9CwBruW/LxINIZwfqkDq8iQeH7pOyZj5IOEh+m72qkiFu6cDY6I/oNabLRvRWOGjmZ1DxYWT+F7dpw4/MkXQLMUfKA/hZwr6S/MnVeoY5GC7UY9//v/HMxSYu5XLbZbmQ07cZqbg8AJ+ZRbKcAZ1YVbNsVQaH7ql7yEdtX5UlmtaGPD9guM6FpXWBnVbsozozoIaofRvgv29NkNC1DKeFc87ZXSMGsyCpfl+ZbWQOt4V0222w3MppWvpqb7d8Dv1dKC78rMD7PeTnR9jUD712N6GjuMqXsjF8CGpd8vJj0DzDWdpEVvpD0X0y7xGeh2Zl58tI0XH0a8fc1SaeSJuhdztQd9oWHpEo6lrTqXJW5sy4lXdHUDjIbkJq+PkKa73J6gTIrybKbm97Wtl14tcMByq40o6mkw0hDhatcza3WT7MZKSgsSUr5vS7wuu3typTd1utHUOg+pVxF9REK7lvysWh5pwPLkJalrF22uszknlBebhpsZttFx/93K3fWn4Gv234u3/8gcBwpnfb1tlfusLxKs+xKutn22kX2bVFW5RlNG8pudeZul8iKLOkI0onj1cBJjaOjJD1YZgRW23WIoDD8SPoHsGIvZjuG/kkaZfvxpm1r2r69R1VqSdK9jQML8nDNe22vrAIpr/Ms4Y2Aa903o3mq1+iwvENIqSPOL/sd19Sz/2vqGU2LdAp3k6SvAWfZnmZ53Co78wcSfQrD0wRSrqOeDl0L0zhP0ua2nwKQtD5pGHLhkV2SPkI6i/9gPmivCmxu+2cl6nlD7mD+U76/JSkH0tzAywXKm2z7laZZvGUO5vsCc5NG2b1JiVFcrn72P5J2tP1/mjpFfONrFmourHUu27akJUmjrx6xXRsxNSgdzhEUhpF82W9gXuB+SbcxdVtmZYvihEL2BC7MzSlrkBbc+XzJMk8kjTY7AcD2eKVUKWWCwl6kQFBb3esPpNTmJs1y7lRVWXYBsD1v0X2bSVrBaT3vlgs8FWz/r6XxqLKe3yCtNveapENJf/M7gdXzENVfVvVa061LtEAMH0rLUPbLBZdTDNWRtDbpAP4WsKnzCmclyqt8jYaqKa2nsD99qa6vICWKKzwiTtLmNKRxccGV5iSNdVqxrhvt/x9o7pOQtJTtVqu8Ta+s+0j9jvMC/yCNUHwhf7a3u0Tivk7FlcIwUjvoS/ql7R82Pibpl0AEhR5ouIKrmYuUt+YkpeR1Za7gXlBaQ6E2vn4rSjYbqvo1kDe1vT99K84haWv6mqc6rd9hpJnGf8yb9pG0ru0fdVqW7d3zzyJXQNPzZ0mfc17KVNJHSe+5o4767B2nNNkvSXrYOROu01oVg7oOeVwpDENqsd6xupB3J7Snm1dwebb6WFJenJdIadJ3bO7Q7rDMStdA7uf7WHhNbqXlKEc75/vJQzTvKvP9lnQHaSLgma5ojQKlTLM/IGUpWJ7UDLeDC6SvkfQAKf/YTKS1KL5CX8D+P9sfraLO7YgrhWFE0jdJCbiWyf84NfOSEmeFHuhms53tR4FP507gmWxPqqDYStZAlvQ5Up/J4pJ+2/DQfKR1PspYAKg1zcxfsiyA7Ujj/m/PAeIU4Moyo5tsX6qUsfhK0v/gFraLrjj3LHBEi99r9wdNXCkMI5LmBxYEfgE0XkpPKjPeOlSjC80yKOUo+irTTlQss+BMJWsgS1oNGE1KMHdgw0OTgGuKnpFL2o6UFO9a0me4PrCf7bMG2q/NsmciTQw7jpTm4mTgqE7+fzTtYkAbAY+SVrMr9bcZCiIoDDP5Sz2+0wlGofuqbpbJZf6dNNt4qtxHzmsPFCyz0glxkmZ1BSvMNZR3OillyEuk9b5vdfmEeOThvLuSrm6uIPVZrAvs1EnHvaSdB3q8yN+mVeqRpjIHLWNxBIVhSGmt3v1s/6vXdQl9JN1ku9C6xAOUWbhtfrBo2myhpSaGSdqIdLBej5Q25G7STOujStRxHGkOxkmk4bdvNzx2vu0BD8r9lDk38JbtKfn+zMDsrSaetVFWLVAvQuo/ujrf35A0+qrj+hUVQWEYknQ1aXTGbUydlTLmKfRQVc0yTWV+h5Sb/5KmMjtuLpT0A9u/atH8USuzULNH7iSdJluo7f8UKS+XOTPpO74haf7Hm7ZXKFHe0rl/pjKSbgE+7b4MyPOQ+in+q0SZlwDfcF5TQdKiwO8GMyhER/PwdEivKxBamg94g77x+lB+saJ3SOse7E/fgdykM+hO1Zq1SuXeaqHSbKGSriJNELsZuIG0qFSR7K11TusmT7MutUvkpSKlHK8vpmP7tTyvoIxRnnqRnedIiQoHTQSFYcj2dUqZTZez/bf8RZy51/Wa0dkus6ZFf/YFlq2NWy/Dfetwv2F7qjkEeV5BUddIOpzqsoWOJy1OtTJpvsfLSkny3hx4t/6p+nWpAV6XtEbtfSolvixcx+xaSVcAZ5KC/3b0ZbMdFNF8NAzlKfG7Ax+wvUxOLXC87U/1uGozNElzALsx7dlomYymFwPbFWmnHqDMqucVVD5bOJc7D6lj+Huk9ZRnL1FWN9alXhM4C3g6b1oU2Nb2uKJl5nK/RN9s7uttX1CmvE7FlcLwtBewFnArgO2HJC3S2yoF4HTSylmfJQ3T3IG+JpuipgB35wNv41l4x+3/3ZpXUPVsYUl7kzqZPwY8QRo2ekPJYitbl7rG9u1KazQ0LnZVxSisO0nDzP8maS5J81Y0P6UtERSGp7dtv6OclVIpu2Jc8vXesra3lvRF26cpJa67omSZF+ZbFZ4m9SdsTuoUrplE6ijuiLqULRSYkzR5a5ztspPgaipbl7pG0lebNq2e05oUWuwql1lvBSCtmbI4cDxpcaBBEUFheLpO0o+BOSV9hjTL+c/T2Sd0X+0s8WVJK5Nmoo4qU2AOLrPR19n4YNGzUdv3APdIOqNWhqQFgSULTjSrPFsogO3Dqywvl1n1utSQRkfVzEE6cN9JSndRVM9bAaJPYRjKE9h2I41yEels9PdlpuyH8iR9HTiPtH7CqcA8wAG2TyhR5gbAaaTZsiItz7iz7etLlHkt6WphFtIcgInAdbZbnvG3Ud402UKHisGcFJYzDpxeZmi4pFttf1w5K25uBbizTN6nTsWVwvC0AfBH2yf2uiIBmppPaiOQfpd/zk05vwE2dl77WGnRnTNJ7e1FzW/71RzETrF9UFMurU7dKuluUj6hy4fYyckX8s+Wk8IoN1y42RvAciXL6HkrQASF4WkX4HhJ/yF1wN1AWvu5kuyPoWO15pPlSU0KF+f7XwAKn9Fns9YCAoDtf+YkbGXMkidFbUNDuusSPgJ8GvgacLSks4FTbf+zgrJLqQ0Tzk1GKzZPCitTtqZOmT4TsCJwTpkySTnNdiOlNdkDuIySfR+diuajYSyPotiKNGRvMdsR5HtI0pXAlrWRIpLmBf5ke5MSZZ5MOvCcnjftCMxcZk5EnpNwAHCT7W8qpec+3PaWRctsKHtDUurnuYF7gB/ZvrlsuWVJmtCYL6xMDjFJs9t+W1OnTJ8MPGH7yRJ1nBk4zfaORcuoQgSFYUjSjqQhe6sALwA3AjcMhX++GVlO97BaLa+OpNmBe0qmZ5id1Pm4LqlP4XrgWJdY1axqkhYiBaudSDNwTyJdLY0mBcXK10nulKRjSE07jZPCHrb9rQJl3Wl7DUmn296p4npeQUqqOKgL6zSKM8vh6f8Bj5CGql3jEguuhEqdDtwm6QLSgedLpE7iwvLB/wjgCEkfAJYoGxByv8RxwAdtr6yUPXRz20XXfb6Z9N63aDpTviPPJO4523s3TQobW2JS2GxKmVL/q1VHdsnO68eBm/Kkxca8ZkWH93YsrhSGKUkrkb7g65LOgB6s+qwldE5pgfj18t3rbd9VsrxrqXCkUC7zOtLC8Ce4b93nCUWaUvK+GmKdyy1J+iBpuKeB24rmU5K0Lmli4jb09R/VuOQM9oNabbc9aPnO4kphGJI0HzCSlKp4FGllqvcG2icMjpwHp2jOn1aqHikEMJft22qTH7OOJ4k1drQ2lQUMray9krYhTVy7ltQMd7Sk79s+t9OybN8I3CjpPtvHNL1O4VQcuexDcjlz2359es/vhggKw9ONDbdjynRuhSGv6pFCAC9IWoa+A/pWwDMD79LSryuqz2DYn4Zsq5JGAH8DOg4KDb4GHNO07Wag8PoXktYm9cnMA4xUWt1uD9v/XbiWHYqgMAzVJrLk0S1D/rI9lPJT0uTEm3KunaVJq5KVsRcwFlhB0lPAY6TmkI64i2tTd8FMTc1F/yENI+2YpA+R0k/MKWl10pUHpBxSZVNn/z9S7qyLIc1Cl7T+wLtUK4LCMJRTKJxOyo8iSRNJs1wn9LZmoWpOKa7/1HD/UaDw0NE8FHOM7U8rrRw2U9Fka5LuZYCTksGchduGy9WXkhpgW9IcgCI+S5ortARpcmEtKLwK/LhEHQGw/e+m5rgp/T23GyIoDE9jgX1tXwP1VAhjSTM2w/tI1SOFbL+Xs5CeU0Gb9Wb55175Z20uxQ6k2b1DiYET6BvaOxb4RKGC0hrMp0na0vZ51VURgH9L+i/AOefV/1A+025HYvTRMCTpHturTW9bGP6qHimU9z+AlEr6bKYe9lgof5FarE3dalsvqfUaEuPLXM1IOh3Yu5ZYT2nhq5NdYl0TSQsDR5FmiAu4EtjHJZY27VRcKQxPj+Z/7MZZro/1sD6heyoZKdSkNmRyr4ZtRZf4BJhb0rp5VA75TLdszqdKSPomKX/Q0k2jtuYFbipZ/I2kvE/7kvoYvg98t0yBTivsddy/U6UICsPT10jrNJ9P3yzXbiwFGXqvqpFCdV2YYbwbcHLOEgrwMn2Bp9fOAC4HfkHKK1QzqWxmV9snSLqPtFzmC8Dqtp8tUpakoxm4f6bjRZWKiuajEIawPNqo1l/0EumKcMcys9iV1vTeFxhpe3el5VyXt31JybrORzqmlF2nYFiQtBMph9RBwKqkDuhdndat6LSsnfOv65AS652d729NWmyo40WQioqgMAzlzsfvkSau1a/2XHJN3DB0lR0p1FTW2aSV176aO6/nBG62PbrDcgacVT2YqRl6QdKFwO4Ncx/WIqXP6OhzbCrzGlKq9NoiSLMCV7riJU8HEs1Hw9OfSHmPfs8gD1cLg6O/A26tb6HkAXcZ29tK2j6X9aZaTUmevkpXXBtubG/RdP+2HBjKWIz0udaatubJ2wZNBIXhabLt43pdidBV3TzgvpOvDmr9FMsAHSfZG8x8PENRf8OFgaKJBQEOA+7KVwwAnwQOLlXRDkXz0TCSs2RCGrv8PHABDf/MZTvOwoxB0saktA8rkoY8rkNqC79mwB2nLecHtn/VXyfpYHaO9kI3EguSJsS9C3w8b761aOd1UXGlMLyMI/3z1S71v9f0eNEhhWGIkrQEcDTpwG3SMMh9yuS7sn2lpHGkyVvK5b1QoKjapKo7mDHTrVQ6XNi2JV1o+2PARaVrV1AEheFlW+Df7ltScGdSyoPHGeRLzDBoTiENq9w6398xb/tM0QIlXZUnWF3aYlvbbNfWDr6flN5hFH3HFAN/KFrHYaLy4cLALZLWtH176doVFM1Hw4ikO4FP234xJ8k6C/gWaYWrj9reqqcVDJWTdHfzaJZW29osaw5SwrZrgA2YOpHb5bY/WrCOD5KaUe6lIYW77SeKlDdc9DNceIcy71vS/aQ1r58gzTYX6SJi0PJIxZXC8DJzQ7/BtqThb+cB50m6u4f1Ct3zgtLyq7VEbtuTMnwWsQfwbdJolnFMncitzCL2E203LzYzI3iKdNV2DSk55avAzqTMtkV9roJ6lRJBYXiZWdIsticDnwJ2b3gs/pbvT7Wc/UeSmin+TsHZwraPAo6S9C3bR1dXRQ6S9HvgKqYe+FBmWcrh4CLS7O07gacrKrPnTTdxIBlezgSuk/QCKaHZDQCSlgVmiFmkMxrb/yINc6yyzKNzfqJRTD35sWgfwK7ACsCs9DUfmZSG5f1sCdubVFzmpfQNJpkDWAp4EFip4tfpVwSFYcT2zyVdBSxKmuVYO6uYidS3EN5n8gph32DaA3iZdYBPB5Yhrflcm/xYpmN4NdurFK3PMPZ3SavYvreqAps/R6U1v/eoqvx2REdzCEOYpL+TrgjH0TB7vUwef0n/AFZ0Rf/8kk4EjrR9fxXlDRe5U3hZUgfz23SpU7hV2u9uiiuFEIa2uWz/sOIyJwAfovzwyZp1gZ0ldfXgOARV3inclN5kJtJ6zxOrfp2BRFAIYWi7RNLnbRddOrKVhYH7Jd3GzVIAswAABNlJREFU1B3DRfsuqm5XHxa6NOS2Mb3JZFIfQ9Wruw0omo9CGIIkTaJvJMo8pIN3bbasbc9XouxPttpu+7qiZYb3jwgKIQxhuVP4BuAG24O6Vm8YPJIGnOdR4iqu87pEUAhh6JK0EanNfj1Sbqu7SAHiqAJl3Wh73aarEOjrAyh89RHKkTQR+Ddp2Pmt9E0sBAb3Ki6CQghDnKSZgTWBDYE9gTdtr9DbWoUq5b/xZ0gz1lcl9SWcafu+Qa9LBIUQhq48L2Vu4GZSM9KNtZW+wvuTpNlJweFw4KcVzz6frhh9FMLQNh74GLAyadb6y5Jutv1mb6sVqpaDwaakgDAK+C09mBUeVwohDAOS5iGlk/ge8CHbs/e4SqFCkk4jBf7LgbNsT+hZXSIohDB0Sdqb1Mn8MVI65etJHc1X97RioVKS3iOlyoYeDwKI5qMQhrY5gSOAcTk7bngfsj1Tr+tQE1cKIYQQ6oZMdAohhNB7ERRCCCHURVAIw5ak/SXdJ2m8pLslfXw6zz9Y0vcqfP1dJB3Tz2Ov5Z+LSTo3/z5a0uf7ef4GkizpCw3bLpG0QVX1DaEdERTCsCRpbWAzYI2covnTpDQBZcuduWwZjWw/bXurfHc00DIoZE8C+1f5+iF0KoJCGK4WBV6w/TaA7RdsPw0g6XFJC+ffx0i6tmG/1SRdLekhSd/Iz9lA0jWSzgDuzdt2lHRbvgI5oRYsJO0q6Z+SrgPWqRUqaSlJN0u6XdKhDdtHSZogaTbSgu7b5jK3bfGe7gFekfSZ5gckHZjLniBprCTl7ddKOlLS9ZL+IWlNSefn9/ezhv1bvp8QmkVQCMPVlcCS+QB9bH/poFtYlTRrdG3gQEmL5e1rAfvbXlHSR4FtgXVsjyateLaDpEWBQ0jB4DPAig3lHgUcZ3tN4NnmF7X9DnAgcLbt0bbP7qd+PwN+0mL7MbbXtL0yaZjqZg2PvWN7feB40mLye5EmQu0iaaH+3s8An1GYgUVQCMOS7ddIE7p2J61MdbakXdrY9SLbb9p+AbiGFAwAbrP9WP79U7ns2yXdne8vDXwcuNb2xHyQbzywr0PKcAlweon3dQOApPWaHtpQ0q2S7gU2YuqF3Gtpl+8F7rP9TL6CehRYcoD3E8I0YvJaGLZsTwGuBa7NB8udgVNJi9HUTnjmaN6tn/uvN2wTcJrt/RqfKGmLFvsPVHZRPyf1LUzOrzsHcCwwxva/JR3M1O+rtnraew2/1+7PQj/vJ4RW4kohDEuSlpe0XMOm0aQ0EACPk86MAbZs2vWLkuaQtBCwAXB7i+KvAraS9P/bu3+UBoIwDOPPV9gJokVACNjbeAUPoZA7WHiFBPEA1lbewDoKFkEUBQuLXCGNheABxmImw4g7gqX4/Kpll/lXvey38O2orLUTEXvkPveHpSSzARw3Y+6BSbnulWY++Pq7xUEppTmwDRyUW+sAeCs9kI4GB/b1ziN9Yyjor9oEriJiGRGv5Pr+tDybARcRsSDXz1tP5F71j8DZ+uN0K6W0JNf152XuG2A3pbQqazwAt8BLM+wUOImIZ2Crs+c7YP+HD82tc2Bc9vMOXJLLQ9cMB1lX7zy/mUP/h20uJEmVbwqSpMpQkCRVhoIkqTIUJEmVoSBJqgwFSVJlKEiSKkNBklR9AvqXfNRuvD0TAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>As expected, all of these are large, popular subreddits. All of them (except <a href="https://www.reddit.com/r/Showerthoughts">r/Showerthoughts</a>) primarily post links to external sites, like images, gifs, or videos. More notably, all of them have broad, generic themes, implying our previous hypothesis that more specific subreddits were more controversial had some merit. Next, then, let's plot the subreddits that broke the most controversial 1000 at least 10 times:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[79]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Plot subreddits that most frequently broke controversial 1000</span>
<span class="n">subs</span> <span class="o">=</span> <span class="p">{}</span>
<span class="k">for</span> <span class="n">tableRow</span> <span class="ow">in</span> <span class="n">dataSet</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
    <span class="c1"># Tally how many times each subreddit appears in dataset</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;post_type&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">):</span> <span class="c1"># Filter only controversial posts</span>
        <span class="n">subreddit</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;subreddit&quot;</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">subreddit</span> <span class="ow">in</span> <span class="n">subs</span><span class="p">:</span>
            <span class="n">subs</span><span class="p">[</span><span class="n">subreddit</span><span class="p">]</span> <span class="o">=</span> <span class="n">subs</span><span class="p">[</span><span class="n">subreddit</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">subs</span><span class="p">[</span><span class="n">subreddit</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">cont_subs</span> <span class="o">=</span> <span class="n">subs</span>

<span class="c1"># Filter out subs that broke controversial 1000 less than 10 times</span>
<span class="n">consistent_subs</span> <span class="o">=</span> <span class="p">{}</span>
<span class="k">for</span> <span class="n">sub</span> <span class="ow">in</span> <span class="n">subs</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">subs</span><span class="p">[</span><span class="n">sub</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="mi">10</span><span class="p">:</span>
        <span class="n">consistent_subs</span><span class="p">[</span><span class="n">sub</span><span class="p">]</span> <span class="o">=</span> <span class="n">subs</span><span class="p">[</span><span class="n">sub</span><span class="p">]</span>
        
<span class="c1"># Create bar chart</span>
<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">consistent_subs</span><span class="p">)),</span> <span class="nb">list</span><span class="p">(</span><span class="n">consistent_subs</span><span class="o">.</span><span class="n">values</span><span class="p">()),</span> <span class="n">align</span><span class="o">=</span><span class="s1">&#39;center&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">consistent_subs</span><span class="p">)),</span> <span class="nb">list</span><span class="p">(</span><span class="n">consistent_subs</span><span class="o">.</span><span class="n">keys</span><span class="p">()),</span> <span class="n">rotation</span><span class="o">=</span><span class="s1">&#39;vertical&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Most Frequent Subreddits in Controversial 1000&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;Number of Posts&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;Subreddit Name&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>As expected, there's a heavy presence of political subreddits like <a href="https://www.reddit.com/r/Sino">r/Sino</a>, <a href="https://www.reddit.com/r/politics">r/politics</a>, <a href="https://www.reddit.com/r/Conservative">r/Conservative</a>, and <a href="https://www.reddit.com/r/Libertarian">r/Libertarian</a>, as well as a popular entertainment subreddit (<a href="https://www.reddit.com/r/leagueoflegends">r/leagueoflegends</a>). Unfortunately, it looks like there's some overlap with our top 1000 subreddits; <a href="https://www.reddit.com/r/IAmA">r/IAmA</a> and <a href="https://www.reddit.com/r/videos">r/videos</a> are popular subreddits, so subscriber count may be a poor predictor. As a follow-up, let's try this: what percentage of subreddits appear in either the top 1000 or the controversial 1000, but not both?</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[55]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Count how many subreddits appear in either top or controversial, not both</span>
<span class="n">unique_subs</span> <span class="o">=</span> <span class="p">{}</span>
<span class="n">subs_count</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">top_subs</span><span class="p">)</span>

<span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">top_subs</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">cont_subs</span><span class="p">:</span>
        <span class="n">unique_subs</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">top_subs</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
        

<span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">cont_subs</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">top_subs</span><span class="p">:</span>
        <span class="n">subs_count</span> <span class="o">=</span> <span class="n">subs_count</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="n">unique_subs</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">cont_subs</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>

<span class="nb">len</span><span class="p">(</span><span class="n">unique_subs</span><span class="p">)</span><span class="o">/</span><span class="n">subs_count</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[55]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>0.9246376811594202</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Aha! This is good; 92% of our subreddits are unique to either the top or controversial lists, so only 8% of subreddits appear on both. Even though subscriber count isn't a good metric, then, it looks like subreddit still is! We'll expect our machine learning models to count subreddit as an important feature, and they should perform decently well.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 style="text-align: center;">Hot or Not?</h2><p>From here, we'd like to put our hypotheses to the test. Are our features good enough to predict a post's success at the time of submission?</p>
<p><h3>Linear Regression</h3>
First, we're going to shoot the moon; let's try predicting the exact upvote ratio that a post will achieve based on its initial conditions. This is a regression problem, so let's try fitting our data to a linear regression model with "upvote_ratio" as our labels.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[160]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">inputRegressionData</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">outputRegressionData</span> <span class="o">=</span> <span class="p">[]</span>

<span class="c1">#Creating examples with all features and the corresponding label</span>
<span class="k">for</span> <span class="n">tableRow</span> <span class="ow">in</span> <span class="n">dataSet</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
    <span class="n">subReddit</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;subreddit&quot;</span><span class="p">]</span>
    <span class="n">SR_oneHotEncoding</span> <span class="o">=</span> <span class="n">subRedditOneHotEncoding</span><span class="p">[</span><span class="s2">&quot;subReddit_&quot;</span> <span class="o">+</span> <span class="n">subReddit</span><span class="p">]</span><span class="o">.</span><span class="n">to_list</span><span class="p">()</span>
    <span class="n">originalContent</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;is_oc&quot;</span><span class="p">]</span>
    <span class="n">nsfw</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;is_nsfw&quot;</span><span class="p">]</span>
    <span class="n">spoiler</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;is_spoiler&quot;</span><span class="p">]</span>
    <span class="n">lenTitle</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;len_title&quot;</span><span class="p">]</span>
    <span class="n">titleQuestion</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;title_question&quot;</span><span class="p">]</span>
    <span class="n">titleSentiment</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;title_sentiment&quot;</span><span class="p">]</span>
    <span class="n">titleSubjectivity</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;title_subjectivity&quot;</span><span class="p">]</span>
    <span class="n">lenBody</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;len_body&quot;</span><span class="p">]</span>
    <span class="n">ratio</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;upvote_ratio&quot;</span><span class="p">]</span>

    <span class="n">inputRegressionData</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">SR_oneHotEncoding</span> <span class="o">+</span> <span class="p">[</span><span class="n">titleQuestion</span><span class="p">,</span> <span class="n">lenTitle</span><span class="p">,</span> <span class="n">titleSentiment</span><span class="p">,</span> <span class="n">titleSubjectivity</span><span class="p">,</span> <span class="n">lenBody</span><span class="p">,</span> <span class="n">originalContent</span><span class="p">,</span> <span class="n">nsfw</span><span class="p">,</span> <span class="n">spoiler</span><span class="p">])</span>
    <span class="n">outputRegressionData</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">ratio</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We use a <a href="https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso">Lasso model</a> to build a linear model of the data since the traditional least squares method does not work well on sparse data.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[161]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">trainInput</span><span class="p">,</span> <span class="n">testInput</span><span class="p">,</span> <span class="n">trainOutput</span><span class="p">,</span> <span class="n">testOutput</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">inputRegressionData</span><span class="p">,</span> <span class="n">outputRegressionData</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.1</span><span class="p">)</span> <span class="c1">#Split data</span>
<span class="n">ratioRegression</span> <span class="o">=</span> <span class="n">Lasso</span><span class="p">()</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">trainInput</span><span class="p">),</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">trainOutput</span><span class="p">))</span> <span class="c1"># Works better with sparse data</span>
<span class="n">predictedOutput</span> <span class="o">=</span> <span class="n">ratioRegression</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">testInput</span><span class="p">))</span> <span class="c1">#Test the fitted model against unseen data</span>

<span class="n">modelPerformance</span> <span class="o">=</span> <span class="p">[]</span>

<span class="n">testOutput</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">testOutput</span><span class="p">]</span>
<span class="n">predictedOutput</span> <span class="o">=</span> <span class="n">predictedOutput</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
<span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">output</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">testOutput</span><span class="p">,</span> <span class="n">predictedOutput</span><span class="p">)):</span>
    <span class="n">target</span><span class="p">,</span> <span class="n">prediction</span> <span class="o">=</span> <span class="n">output</span>
    <span class="n">modelPerformance</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="s2">&quot;Example&quot;</span> <span class="p">:</span> <span class="n">i</span><span class="p">,</span> <span class="s2">&quot;True Ratio&quot;</span> <span class="p">:</span> <span class="n">target</span> <span class="p">,</span> <span class="s2">&quot;Predicted Ratio&quot;</span> <span class="p">:</span> <span class="n">prediction</span><span class="p">,</span> <span class="s2">&quot;Residual&quot;</span> <span class="p">:</span> <span class="n">target</span> <span class="o">-</span> <span class="n">prediction</span><span class="p">})</span>
    
<span class="n">modelPerformance</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">modelPerformance</span><span class="p">)</span>
<span class="n">MSE</span> <span class="o">=</span> <span class="n">metrics</span><span class="o">.</span><span class="n">mean_squared_error</span><span class="p">(</span><span class="n">testOutput</span><span class="p">,</span> <span class="n">predictedOutput</span><span class="p">)</span> <span class="c1">#How close are the predictions to the actual values?</span>
<span class="n">averageResidual</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">modelPerformance</span><span class="p">[</span><span class="s2">&quot;Residual&quot;</span><span class="p">])</span> <span class="c1">#Gives an idea if the model is consistently under predicting or overpredicting, indicating a poor fit</span>

<span class="n">modelPerformance</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[161]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Example</th>
      <th>True Ratio</th>
      <th>Predicted Ratio</th>
      <th>Residual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0.50</td>
      <td>0.760761</td>
      <td>-0.260761</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0.51</td>
      <td>0.668199</td>
      <td>-0.158199</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0.50</td>
      <td>0.703810</td>
      <td>-0.203810</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>0.47</td>
      <td>0.760761</td>
      <td>-0.290761</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>0.91</td>
      <td>0.760761</td>
      <td>0.149239</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[162]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Mean Squared Error: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">MSE</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Average Residual: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">averageResidual</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Mean Squared Error: 0.042469174299435246
Average Residual: -0.04101170171391546
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Directly regressing the ratio is extremely difficult since almost all ratios on reddit are between 0.5 and 1. In general, the linear model is able to minimize the loss function by predicting around 0.75 for each example. So, it looks like our data isn't fit well by a standard linear regression.</p>
<p>Given that this regression model performed badly, we'd like to pursue two different solutions:</p>
<ol>
    <li>What if we made the problem easier by turning it into a classification problem?</li>
    <li>What if a more complex regression model, like a neural network, would perform better?</li>
</ol><p><h3>Logistic Regression</h3>
Let's tackle the classification problem first. If we tried to categorize a post as either "top" or "controversial", instead of trying to regress its exact upvote ratio, we may see more success.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[163]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">inputClassificationData</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">outputClassificationData</span> <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span class="n">tableRow</span> <span class="ow">in</span> <span class="n">dataSet</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
    <span class="n">subReddit</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;subreddit&quot;</span><span class="p">]</span>
    <span class="n">SR_oneHotEncoding</span> <span class="o">=</span> <span class="n">subRedditOneHotEncoding</span><span class="p">[</span><span class="s2">&quot;subReddit_&quot;</span> <span class="o">+</span> <span class="n">subReddit</span><span class="p">]</span><span class="o">.</span><span class="n">to_list</span><span class="p">()</span>
    <span class="n">originalContent</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;is_oc&quot;</span><span class="p">]</span>
    <span class="n">nsfw</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;is_nsfw&quot;</span><span class="p">]</span>
    <span class="n">spoiler</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;is_spoiler&quot;</span><span class="p">]</span>
    <span class="n">titleQuestion</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;title_question&quot;</span><span class="p">]</span>
    <span class="n">lenTitle</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;len_title&quot;</span><span class="p">]</span>
    <span class="n">titleSentiment</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;title_sentiment&quot;</span><span class="p">]</span>
    <span class="n">titleSubjectivity</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;title_subjectivity&quot;</span><span class="p">]</span>
    <span class="n">lenBody</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;len_body&quot;</span><span class="p">]</span>
    <span class="n">post_type</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;post_type&quot;</span><span class="p">]</span>

    <span class="n">inputClassificationData</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">SR_oneHotEncoding</span> <span class="o">+</span> <span class="p">[</span><span class="n">titleQuestion</span><span class="p">,</span> <span class="n">lenTitle</span><span class="p">,</span> <span class="n">titleSentiment</span><span class="p">,</span> <span class="n">titleSubjectivity</span><span class="p">,</span> <span class="n">lenBody</span><span class="p">,</span> <span class="n">originalContent</span><span class="p">,</span> <span class="n">nsfw</span><span class="p">,</span> <span class="n">spoiler</span><span class="p">])</span>
    <span class="n">outputClassificationData</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">post_type</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[164]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">trainInput</span><span class="p">,</span> <span class="n">testInput</span><span class="p">,</span> <span class="n">trainOutput</span><span class="p">,</span> <span class="n">testOutput</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">inputClassificationData</span><span class="p">,</span> <span class="n">outputClassificationData</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.1</span><span class="p">)</span>
<span class="n">ratioRegression</span> <span class="o">=</span> <span class="n">LogisticRegression</span><span class="p">()</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">trainInput</span><span class="p">),</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">trainOutput</span><span class="p">))</span> <span class="c1">#Binary Classification task</span>
<span class="n">predictedOutput</span> <span class="o">=</span> <span class="n">ratioRegression</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">testInput</span><span class="p">))</span> <span class="c1"># Test model on unseen data</span>
<span class="n">modelPerformance</span> <span class="o">=</span> <span class="p">[]</span>

<span class="n">testOutput</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">testOutput</span><span class="p">]</span>
<span class="n">predictedOutput</span> <span class="o">=</span> <span class="n">predictedOutput</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>

<span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">output</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">testOutput</span><span class="p">,</span> <span class="n">predictedOutput</span><span class="p">)):</span>
    <span class="n">target</span><span class="p">,</span> <span class="n">prediction</span> <span class="o">=</span> <span class="n">output</span>
    <span class="n">modelPerformance</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="s2">&quot;Example&quot;</span> <span class="p">:</span> <span class="n">i</span><span class="p">,</span> <span class="s2">&quot;True Class&quot;</span> <span class="p">:</span> <span class="n">target</span> <span class="p">,</span> <span class="s2">&quot;Predicted Class&quot;</span> <span class="p">:</span> <span class="n">prediction</span><span class="p">})</span>
    
<span class="n">modelPerformance</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">modelPerformance</span><span class="p">)</span>
<span class="n">modelPerformance</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[164]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Example</th>
      <th>True Class</th>
      <th>Predicted Class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[165]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Accuracy</span> <span class="o">=</span> <span class="n">metrics</span><span class="o">.</span><span class="n">accuracy_score</span><span class="p">(</span><span class="n">testOutput</span><span class="p">,</span> <span class="n">predictedOutput</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Accuracy: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">Accuracy</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Accuracy: 0.9325842696629213
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Our <a href="https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html">logistic regression model</a> performs quite well on the limited data set. Intuitively, it makes sense that a model will perform better at classifying items into two buckets, rather than regressing a continuous variable.</p>
<p><h3>Neural Network Regression</h3>
Now that we have a working logistic model, let's revisit our regression model from earlier. Can we improve it? Since linear regression seems to lack the required horsepower, let's go a little overboard and try to use a fully connected neural network. PyTorch (<a href="https://pytorch.org/">https://pytorch.org/</a>) is great for building neural networks and training deep learning models.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[169]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">trainInput</span><span class="p">,</span> <span class="n">testInput</span><span class="p">,</span> <span class="n">trainOutput</span><span class="p">,</span> <span class="n">testOutput</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">inputRegressionData</span><span class="p">,</span> <span class="n">outputRegressionData</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.1</span><span class="p">)</span>
<span class="n">testOutput</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">testOutput</span><span class="p">]</span>

<span class="k">class</span> <span class="nc">PredictRedditPost</span><span class="p">(</span><span class="n">nn</span><span class="o">.</span><span class="n">Module</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">super</span><span class="p">(</span><span class="n">PredictRedditPost</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">linearClassifier</span> <span class="o">=</span> <span class="n">nn</span><span class="o">.</span><span class="n">Sequential</span><span class="p">(</span><span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="mi">353</span><span class="p">,</span> <span class="mi">64</span><span class="p">),</span> <span class="n">nn</span><span class="o">.</span><span class="n">Dropout</span><span class="p">(</span><span class="mf">0.5</span><span class="p">),</span> <span class="n">nn</span><span class="o">.</span><span class="n">ReLU</span><span class="p">(),</span> 
                                              <span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="mi">64</span><span class="p">,</span> <span class="mi">16</span><span class="p">),</span> <span class="n">nn</span><span class="o">.</span><span class="n">ReLU</span><span class="p">(),</span>
                                              <span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="mi">16</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
        <span class="c1">#Linear fully connected neural network with Dropout regularization to prevent overfitting and ReLU activations for added non-linearity</span>
    <span class="k">def</span> <span class="nf">forward</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">featureVector</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">linearClassifier</span><span class="p">(</span><span class="n">featureVector</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[170]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">LR</span> <span class="o">=</span> <span class="mf">1e-3</span> <span class="c1">#Learning Rate</span>
<span class="n">WEIGHTDECAY</span> <span class="o">=</span> <span class="mf">0.0005</span> <span class="c1">#L2 Penalty which forces smaller weights and simpler models</span>
<span class="n">EPOCH</span> <span class="o">=</span> <span class="mi">10</span> <span class="c1">#Number of iterations through entire dataset</span>

<span class="n">device</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">device</span><span class="p">(</span><span class="s2">&quot;cuda:0&quot;</span> <span class="k">if</span> <span class="n">torch</span><span class="o">.</span><span class="n">cuda</span><span class="o">.</span><span class="n">is_available</span><span class="p">()</span> <span class="k">else</span> <span class="s2">&quot;cpu&quot;</span><span class="p">)</span> <span class="c1">#Train on GPU, because training on CPUs is for normies</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">PredictRedditPost</span><span class="p">()</span>
<span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>
<span class="n">optimizer</span> <span class="o">=</span> <span class="n">optim</span><span class="o">.</span><span class="n">Adam</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">parameters</span><span class="p">(),</span> <span class="n">lr</span><span class="o">=</span><span class="n">LR</span><span class="p">,</span> <span class="n">weight_decay</span><span class="o">=</span><span class="n">WEIGHTDECAY</span><span class="p">)</span> <span class="c1">#Gradient descent, of the Adam variety. Less fussy than SGD</span>
<span class="n">MSE</span> <span class="o">=</span> <span class="n">nn</span><span class="o">.</span><span class="n">MSELoss</span><span class="p">()</span> <span class="c1">#Loss function minimizes mean squared error</span>

<span class="n">TestingMSE</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">TrainingLoss</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">STEP</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">EPOCH</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
    <span class="n">epochLoss</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">model</span><span class="o">.</span><span class="n">train</span><span class="p">()</span> <span class="c1">#Turn on Dropout</span>
    <span class="k">for</span> <span class="n">batchCount</span><span class="p">,</span> <span class="n">data</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">trainInput</span><span class="p">,</span> <span class="n">trainOutput</span><span class="p">)):</span>
        <span class="n">handCraftedFeatures</span><span class="p">,</span> <span class="n">ratio</span> <span class="o">=</span> <span class="n">data</span>

        <span class="n">handCraftedFeatures</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">tensor</span><span class="p">(</span><span class="n">handCraftedFeatures</span><span class="p">)</span> <span class="c1">#Format input to play nice with PyTorch</span>
        <span class="n">ratio</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">tensor</span><span class="p">(</span><span class="n">ratio</span><span class="p">)</span>

        <span class="n">handCraftedFeatures</span> <span class="o">=</span> <span class="n">handCraftedFeatures</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span> <span class="c1">#Send data to GPU</span>
        <span class="n">ratio</span> <span class="o">=</span> <span class="n">ratio</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="n">predictedRatio</span> <span class="o">=</span> <span class="n">model</span><span class="p">(</span><span class="n">handCraftedFeatures</span><span class="p">)</span> <span class="c1">#Generate predictions</span>

        <span class="n">optimizer</span><span class="o">.</span><span class="n">zero_grad</span><span class="p">()</span>
        <span class="n">Loss</span> <span class="o">=</span> <span class="n">MSE</span><span class="p">(</span><span class="n">predictedRatio</span><span class="p">,</span> <span class="n">ratio</span><span class="p">)</span>
        <span class="n">epochLoss</span> <span class="o">=</span> <span class="n">epochLoss</span> <span class="o">+</span> <span class="n">Loss</span><span class="o">.</span><span class="n">item</span><span class="p">()</span>

        <span class="n">Loss</span><span class="o">.</span><span class="n">backward</span><span class="p">()</span> <span class="c1">#Backpropagate loss through all layers of NN</span>
        <span class="n">optimizer</span><span class="o">.</span><span class="n">step</span><span class="p">()</span>

    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Epoch &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">STEP</span><span class="p">)</span> <span class="o">+</span><span class="s2">&quot; Loss: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">epochLoss</span> <span class="o">/</span> <span class="n">batchCount</span><span class="p">))</span>
    <span class="n">TrainingLoss</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">epochLoss</span> <span class="o">/</span> <span class="n">batchCount</span><span class="p">)</span>
    
    <span class="n">model</span><span class="o">.</span><span class="n">eval</span><span class="p">()</span> <span class="c1">#Turn off Dropout</span>
    <span class="n">testInput</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">tensor</span><span class="p">(</span><span class="n">testInput</span><span class="p">)</span>
    <span class="n">testInput</span> <span class="o">=</span> <span class="n">testInput</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>
    <span class="n">predictedRatio</span> <span class="o">=</span> <span class="n">model</span><span class="p">(</span><span class="n">testInput</span><span class="p">)</span> <span class="c1">#Forward pass with testing samples</span>

    <span class="n">predictedRatio</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">i</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">predictedRatio</span><span class="o">.</span><span class="n">tolist</span><span class="p">()]</span>
    <span class="n">MSError</span> <span class="o">=</span> <span class="n">metrics</span><span class="o">.</span><span class="n">mean_squared_error</span><span class="p">(</span><span class="n">testOutput</span><span class="p">,</span> <span class="n">predictedRatio</span><span class="p">)</span> <span class="c1">#Get MSE of testing samples</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Epoch &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">STEP</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot; MSE: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">MSError</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
    <span class="n">TestingMSE</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">MSError</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch 1 Loss: 6.891266821341723
Epoch 1 MSE: 2.028491573033708

Epoch 2 Loss: 0.4459851436810692
Epoch 2 MSE: 0.5827612359550562

Epoch 3 Loss: 0.10510524660981743
Epoch 3 MSE: 0.5935477528089887

Epoch 4 Loss: 0.04240793587532868
Epoch 4 MSE: 0.5825365168539326

Epoch 5 Loss: 0.025229115795357148
Epoch 5 MSE: 0.5827612359550562

Epoch 6 Loss: 0.028271939921202402
Epoch 6 MSE: 0.5825365168539326

Epoch 7 Loss: 0.029178444095596577
Epoch 7 MSE: 0.5825365168539326

Epoch 8 Loss: 0.027159262475763137
Epoch 8 MSE: 0.5825365168539326

Epoch 9 Loss: 0.02275792101252242
Epoch 9 MSE: 0.5825365168539326

Epoch 10 Loss: 0.02188337033990069
Epoch 10 MSE: 0.5825365168539326

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[171]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">lineplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">x</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">EPOCH</span><span class="p">)]),</span> <span class="n">y</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">TrainingLoss</span><span class="p">))</span> <span class="c1">#Plot training loss per epoch</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Loss Per Epoch&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;Epoch #&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;Loss&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">clf</span><span class="p">()</span>

<span class="n">sns</span><span class="o">.</span><span class="n">lineplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">x</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">EPOCH</span><span class="p">)]),</span> <span class="n">y</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">TestingMSE</span><span class="p">))</span> <span class="c1">#Plot MSE on testing set per epoch.</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;MSE Per Epoch&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;Epoch #&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;MSE&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">clf</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_text output_subarea ">
<pre>&lt;Figure size 432x288 with 0 Axes&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The plots above show that the model overfit to the training data. The training loss decreased to 0, while the MSE on the test set plateaued. Unsurprisingly, the neural network model predicted 0 for all test samples. Due to the small sample size, the network is unable to precisely regress the correct output value. Throwing more data at this model will likely help it generalize better since the upvote ratio is a continuous variable.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[172]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">modelPerformance</span> <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">output</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">testOutput</span><span class="p">,</span> <span class="n">predictedRatio</span><span class="p">)):</span>
    <span class="n">target</span><span class="p">,</span> <span class="n">prediction</span> <span class="o">=</span> <span class="n">output</span>
    <span class="n">modelPerformance</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="s2">&quot;Example&quot;</span> <span class="p">:</span> <span class="n">i</span><span class="p">,</span> <span class="s2">&quot;True Ratio&quot;</span> <span class="p">:</span> <span class="n">target</span> <span class="p">,</span> <span class="s2">&quot;Predicted Ratio&quot;</span> <span class="p">:</span> <span class="n">prediction</span><span class="p">})</span>
    
<span class="n">modelPerformance</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">modelPerformance</span><span class="p">)</span>
<span class="n">modelPerformance</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[172]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Example</th>
      <th>True Ratio</th>
      <th>Predicted Ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0.95</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0.50</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0.49</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>0.52</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>0.87</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[173]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">trainInput</span><span class="p">,</span> <span class="n">testInput</span><span class="p">,</span> <span class="n">trainOutput</span><span class="p">,</span> <span class="n">testOutput</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">inputClassificationData</span><span class="p">,</span> <span class="n">outputClassificationData</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.1</span><span class="p">)</span>
<span class="n">testOutput</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">testOutput</span><span class="p">]</span>

<span class="k">class</span> <span class="nc">PredictRedditPost</span><span class="p">(</span><span class="n">nn</span><span class="o">.</span><span class="n">Module</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">super</span><span class="p">(</span><span class="n">PredictRedditPost</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">linearClassifier</span> <span class="o">=</span> <span class="n">nn</span><span class="o">.</span><span class="n">Sequential</span><span class="p">(</span><span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="mi">353</span><span class="p">,</span> <span class="mi">64</span><span class="p">),</span> <span class="n">nn</span><span class="o">.</span><span class="n">Dropout</span><span class="p">(</span><span class="mf">0.5</span><span class="p">),</span> <span class="n">nn</span><span class="o">.</span><span class="n">ReLU</span><span class="p">(),</span>
                                              <span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="mi">64</span><span class="p">,</span> <span class="mi">16</span><span class="p">),</span> <span class="n">nn</span><span class="o">.</span><span class="n">ReLU</span><span class="p">(),</span>
                                              <span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="mi">16</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">sigmoid</span> <span class="o">=</span> <span class="n">nn</span><span class="o">.</span><span class="n">Sigmoid</span><span class="p">()</span>
        <span class="c1">#Same neural network architecture as above, now new and improved with a sigmoid activation function</span>
    <span class="k">def</span> <span class="nf">forward</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">featureVector</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sigmoid</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">linearClassifier</span><span class="p">(</span><span class="n">featureVector</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[174]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">LR</span> <span class="o">=</span> <span class="mf">1e-3</span> <span class="c1">#Learning Rate</span>
<span class="n">WEIGHTDECAY</span><span class="o">=</span><span class="mf">0.0005</span> <span class="c1">#L2 Penalty which forces smaller weights and simpler models. </span>
<span class="n">EPOCH</span> <span class="o">=</span> <span class="mi">10</span> <span class="c1">#Number of iterations through the entire dataset</span>

<span class="n">device</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">device</span><span class="p">(</span><span class="s2">&quot;cuda:0&quot;</span> <span class="k">if</span> <span class="n">torch</span><span class="o">.</span><span class="n">cuda</span><span class="o">.</span><span class="n">is_available</span><span class="p">()</span> <span class="k">else</span> <span class="s2">&quot;cpu&quot;</span><span class="p">)</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">PredictRedditPost</span><span class="p">()</span>
<span class="n">model</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>
<span class="n">optimizer</span> <span class="o">=</span> <span class="n">optim</span><span class="o">.</span><span class="n">Adam</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">parameters</span><span class="p">(),</span> <span class="n">lr</span><span class="o">=</span><span class="n">LR</span><span class="p">,</span> <span class="n">weight_decay</span><span class="o">=</span><span class="n">WEIGHTDECAY</span><span class="p">)</span>
<span class="n">BCEL</span> <span class="o">=</span> <span class="n">nn</span><span class="o">.</span><span class="n">BCELoss</span><span class="p">()</span> <span class="c1">#Binary Cross Entropy Loss used for two-class classifiation tasks</span>

<span class="c1">#Same training loop as regression case</span>
<span class="n">TestingAccuracy</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">TrainingLoss</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">STEP</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">EPOCH</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
    <span class="n">epochLoss</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">model</span><span class="o">.</span><span class="n">train</span><span class="p">()</span>
    
    <span class="k">for</span> <span class="n">batchCount</span><span class="p">,</span> <span class="n">data</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">trainInput</span><span class="p">,</span> <span class="n">trainOutput</span><span class="p">)):</span>
        <span class="n">handCraftedFeatures</span><span class="p">,</span> <span class="n">postType</span> <span class="o">=</span> <span class="n">data</span>

        <span class="n">handCraftedFeatures</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">tensor</span><span class="p">(</span><span class="n">handCraftedFeatures</span><span class="p">)</span> <span class="c1">#Formatting features to play nice with PyTorch</span>
        <span class="n">postType</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">tensor</span><span class="p">(</span><span class="n">postType</span><span class="p">)</span>

        <span class="n">handCraftedFeatures</span> <span class="o">=</span> <span class="n">handCraftedFeatures</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span> <span class="c1">#Send to GPU</span>
        <span class="n">postType</span> <span class="o">=</span> <span class="n">postType</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>

        <span class="n">predictedPostType</span> <span class="o">=</span> <span class="n">model</span><span class="p">(</span><span class="n">handCraftedFeatures</span><span class="p">)</span>

        <span class="n">optimizer</span><span class="o">.</span><span class="n">zero_grad</span><span class="p">()</span>
        <span class="n">Loss</span> <span class="o">=</span> <span class="n">BCEL</span><span class="p">(</span><span class="n">predictedPostType</span><span class="p">,</span> <span class="n">postType</span><span class="p">)</span>
        <span class="n">epochLoss</span> <span class="o">=</span> <span class="n">epochLoss</span> <span class="o">+</span> <span class="n">Loss</span><span class="o">.</span><span class="n">item</span><span class="p">()</span>

        <span class="n">Loss</span><span class="o">.</span><span class="n">backward</span><span class="p">()</span>
        <span class="n">optimizer</span><span class="o">.</span><span class="n">step</span><span class="p">()</span>

    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Epoch &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">STEP</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot; Loss: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">epochLoss</span> <span class="o">/</span> <span class="n">batchCount</span><span class="p">))</span>
    <span class="n">TrainingLoss</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">epochLoss</span> <span class="o">/</span> <span class="n">batchCount</span><span class="p">)</span>
    
    <span class="n">model</span><span class="o">.</span><span class="n">eval</span><span class="p">()</span>
    <span class="n">testInput</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">tensor</span><span class="p">(</span><span class="n">testInput</span><span class="p">)</span>
    <span class="n">testInput</span> <span class="o">=</span> <span class="n">testInput</span><span class="o">.</span><span class="n">to</span><span class="p">(</span><span class="n">device</span><span class="p">)</span>
    <span class="n">predictedPostType</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">round</span><span class="p">(</span><span class="n">model</span><span class="p">(</span><span class="n">testInput</span><span class="p">))</span>

    <span class="n">predictedPostType</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">i</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">predictedPostType</span><span class="o">.</span><span class="n">tolist</span><span class="p">()]</span>
    <span class="n">Accuracy</span> <span class="o">=</span> <span class="n">metrics</span><span class="o">.</span><span class="n">accuracy_score</span><span class="p">(</span><span class="n">testOutput</span><span class="p">,</span> <span class="n">predictedPostType</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Epoch &quot;</span><span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">STEP</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot; Accuracy: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">Accuracy</span><span class="p">)</span> <span class="o">+</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
    <span class="n">TestingAccuracy</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Accuracy</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch 1 Loss: 0.7118885397991939
Epoch 1 Accuracy: 0.7415730337078652

Epoch 2 Loss: 0.6699189038024655
Epoch 2 Accuracy: 0.7415730337078652

Epoch 3 Loss: 0.5273262527662723
Epoch 3 Accuracy: 0.7415730337078652

Epoch 4 Loss: 0.5522850346295222
Epoch 4 Accuracy: 0.848314606741573

Epoch 5 Loss: 0.4636425507706569
Epoch 5 Accuracy: 0.8876404494382022

Epoch 6 Loss: 0.45011415637895086
Epoch 6 Accuracy: 0.8595505617977528

Epoch 7 Loss: 0.4067802755341643
Epoch 7 Accuracy: 0.9438202247191011

Epoch 8 Loss: 0.45339107194554745
Epoch 8 Accuracy: 0.8539325842696629

Epoch 9 Loss: 0.40663455717023383
Epoch 9 Accuracy: 0.949438202247191

Epoch 10 Loss: 0.35305965436353764
Epoch 10 Accuracy: 0.9438202247191011

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[175]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">lineplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">x</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">EPOCH</span><span class="p">)]),</span> <span class="n">y</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">TrainingLoss</span><span class="p">))</span> <span class="c1">#Plot training loss per epoch</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Loss Per Epoch&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;Epoch #&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;Loss&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">clf</span><span class="p">()</span>

<span class="n">sns</span><span class="o">.</span><span class="n">lineplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">x</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">EPOCH</span><span class="p">)]),</span> <span class="n">y</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">TestingAccuracy</span><span class="p">))</span> <span class="c1">#Plot classification accuracy per epoch</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Accuracy Per Epoch&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;Epoch #&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;Accuracy&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">clf</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_text output_subarea ">
<pre>&lt;Figure size 432x288 with 0 Axes&gt;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Our classification neural network is able to outperform our simple logistic regression model by a few percent. This state-of-the-art result should be published in next year's NeurIPS conference! Despite the apparent performance increase, neural networks are not interpretable. For the sake of explainability, it makes more sense to analyze the linear models.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The key takeaway from these experiments is that although many state-of-the-art methods use neural networks and deep learning, the size of the dataset plays an important role in whether to stick with traditional machine learning based approaches, or try deep learning models. Let's try to understand our features to see what really goes into making a great post. We'll be generating a Pearson Correlation Matrix to visualize how closely different features are correlated. For more information, <a href="https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/">read here</a>. Here are the main takeaways:</p>
<ol>
    <li>Two variables have a significant correlation if their coefficient is at least 0.5</li>
    <li>A variable is "important" for our model if it has a significant correlation with our label (in our case, upvote ratio, which is "UR" in the last column</li>
</ol><p>As an important note, the limitations of the correlation function mean that we can only use numerical variables for this heatmap. That means we'll be omitting a categorical feature, subreddit, which we already know to be significant.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[125]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">numericalFeatureSelection</span> <span class="o">=</span> <span class="p">[]</span>

<span class="c1"># Get numerical and boolean features, and abbreviate their labels</span>
<span class="k">for</span> <span class="n">tableRow</span> <span class="ow">in</span> <span class="n">dataSet</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
    <span class="n">lenTitle</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;len_title&quot;</span><span class="p">]</span>
    <span class="n">titleSentiment</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;title_sentiment&quot;</span><span class="p">]</span>
    <span class="n">titleSubjectivity</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;title_subjectivity&quot;</span><span class="p">]</span>
    <span class="n">titleQuestion</span>  <span class="o">=</span><span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;title_question&quot;</span><span class="p">]</span>
    <span class="n">originalContent</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;is_oc&quot;</span><span class="p">]</span>
    <span class="n">nsfw</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;is_nsfw&quot;</span><span class="p">]</span>
    <span class="n">spoiler</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;is_spoiler&quot;</span><span class="p">]</span>
    <span class="n">lenBody</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;len_body&quot;</span><span class="p">]</span>
    <span class="n">post_type</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;post_type&quot;</span><span class="p">]</span>
    <span class="n">upvote_ratio</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;upvote_ratio&quot;</span><span class="p">]</span>

    <span class="n">numericalFeatureSelection</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="s2">&quot;TQ&quot;</span><span class="p">:</span> <span class="n">titleQuestion</span><span class="p">,</span> <span class="s2">&quot;LT&quot;</span> <span class="p">:</span> <span class="n">lenTitle</span><span class="p">,</span> <span class="s2">&quot;TSEN&quot;</span> <span class="p">:</span> <span class="n">titleSentiment</span><span class="p">,</span> <span class="s2">&quot;TSUB&quot;</span> <span class="p">:</span> <span class="n">titleSubjectivity</span><span class="p">,</span>
                                      <span class="s2">&quot;OC&quot;</span> <span class="p">:</span> <span class="n">originalContent</span><span class="p">,</span> <span class="s2">&quot;NSFW&quot;</span> <span class="p">:</span> <span class="n">nsfw</span><span class="p">,</span> <span class="s2">&quot;SP&quot;</span> <span class="p">:</span> <span class="n">spoiler</span><span class="p">,</span> 
                                      <span class="s2">&quot;LB&quot;</span> <span class="p">:</span> <span class="n">lenBody</span><span class="p">,</span> <span class="s2">&quot;PT&quot;</span> <span class="p">:</span> <span class="n">post_type</span><span class="p">,</span> <span class="s2">&quot;UR&quot;</span> <span class="p">:</span> <span class="n">upvote_ratio</span><span class="p">})</span>

<span class="n">featureSelection</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">numericalFeatureSelection</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">16</span><span class="p">,</span><span class="mi">10</span><span class="p">))</span>
<span class="n">pearsonCorrelation</span> <span class="o">=</span> <span class="n">featureSelection</span><span class="o">.</span><span class="n">corr</span><span class="p">()</span> <span class="c1"># Pearson&#39;s correlation coeff.</span>
<span class="n">sns</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">pearsonCorrelation</span><span class="p">,</span> <span class="n">annot</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="n">plt</span><span class="o">.</span><span class="n">cm</span><span class="o">.</span><span class="n">Reds</span><span class="p">)</span> <span class="c1"># Using Seaborn to generate a heatmap</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
    
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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oPUPxWmBP63B7/Z/NnmXjM8lpgXeiP1zOTcAA4A/GGP6W5YVDuwGRmLfB70euMcYs/1y6+xvcNUS+6kqxcBG7FRZP+ynW40zxlRrPlhdGVzVRcEeXIW8AA+uflCCOLgKeTU5uApFepLwxQV5cBXygji4CnlBHlyFvCAOrkKdBlf+XWpwZVnWv7B/7qYJkA38Bvu33DDGvGXZI+M/YT+spAh4yBizwbvtDdi//RYGTDXGvBKIOvu752quMaaPZVkjsR9RaAELjDFLA/HBIiIiIiISWhzBmrH0PRhj7r7EegM8fpF1nwOfB7pO/gZXlveDlwIaUImIiIiIiPjhb3CVaFnWsxdbaYz5nyDUR0RERERE6ihN8vTP3+AqDIil6kcVioiIiIiISAX+BldHjTH/VWM1ERERERGROs2htItf/jJ7Cp2IiIiIiEg1+ctcjayxWoiIiIiISJ2ne678u2h8jDE5NVkRERERERGRUOYvcyUiIiIiIlKuLv3OVV2kzJ6IiIiIiEgAaHAlIiIiIiISAJoWKCIiIiIi1aLMjH+Kj4iIiIiISAAocyUiIiIiItWiHxH2T5krERERERGRAFDmSkREREREqkWZGf8UHxERERERkQBQ5kpERERERKrF0o8I+6XMlYiIiIiISAAocyUiIiIiItWizIx/io+IiIiIiEgAKHMlIiIiIiLVot+58k+ZKxERERERkQBQ5kpERERERKpFmRn/FB8REREREZEACHrm6s1//CLYHxGyHn/wd7VdhTrtzQ+fr+0q1Fnmm421XYU6y2rUqLarIKGqflRt16BuKyut7RrUXXm5tV2Dui0isrZrIAHk0O9c+aXMlYiIiIiISABocCUiIiIiIhIAeqCFiIiIiIhUizIz/ik+IiIiIiIiAaDMlYiIiIiIVIt+RNg/Za5EREREREQCQJkrERERERGpFmVm/FN8REREREREAkCZKxERERERqRYHuunKH2WuREREREREAkCZKxERERERqRY9LdA/Za5EREREREQCQJkrERERERGpFmVm/FN8REREREREAkCZKxERERERqRbdc+WfMlciIiIiIiIBoMyViIiIiIhUi37nyj9lrkRERERERAJAgysREREREZEA0LRAERERERGpFj3Qwj9lrkRERERERAJAmSsREREREakWZWb8U3xEREREREQCQJkrERERERGp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7zLPWGvPsV/aFRERERGR0zlXIp2+UtWcqz8DjYE21tpe1toLgLZAQ+Avvi6ciIiIiIhIoKhqztU1QEdbZuygtTbHGPMAsBV41JeFExERERGROkRzrryqKnJlbSWTsqy1Ts78l5JERERERETOWVV1rjYbY24vv9EYcyvuyJWIiIiIiPxc6HeuvKpqWOCDwFRjzC9xL8VugYuAMGC0j8smIiIiIiISMLx2rqy1+4FLjDGDga64VwucY61d5I/CiYiIiIhI3aHVAr2rKnIFgLU2CdAPXIiIiIiIiJxGVXOuREREREREpBqqFbkSERERERHRUuzeKXIlIiIiIiJSAxS5EhERERGRatGCFt4pciUiIiIiIlIDFLkSEREREZHq0ZwrrxS5EhERERERqQGKXImIiIiISPVozpVXilyJiIiIiIjUAEWuRERERESkWozmXHmlyJWIiIiIiEgNUORKRERERESqR3OuvFLkSkREREREpAYociUiIiIiItWjOVdeKXIlIiIiIiJSAxS5EhERERGRajGac+WVIlciIiIiIiI1wFhrffoBzk9f9e0HyLmrXkhtl6DuCgqq7RLUXUWFtV2COu3Bm1+s7SLUWW+++1htF6Fui25Y2yWou8Ija7sEEqCCrr434MJAxQ9d47d7++B/fhVw7aPIlYiIiIiISA1Q50pERERERKQGaEELERERERGpHi1o4ZUiVyIiIiIiIjVAnSsREREREakeY/z3r1rFMcONMduMMTuNMb+rZP8txpj1Jf+WG2N6ltm3xxizwRjzgzFmdU00j4YFioiIiIhIwDHGBAFvAkOBNOA7Y8yX1trNZZLtBgZYa48aY64C3gEuKbN/kLX2UE2VSZ0rERERERGpnro15+piYKe1NgXAGDMJGAmUdq6stcvLpF8BtPBlgTQsUERERERE6hxjzL3GmNVl/t1bLklzYF+Z12kl207nLmBOmdcWmG+MWVPJe/8kilyJiIiIiEj1OPwXm7HWvoN7GN/pVBZGq/RHjo0xg3B3rvqV2XyZtfaAMSYOWGCM2WqtTf7JBUaRKxERERERCUxpQMsyr1sAB8onMsb0AN4FRlprD/+43Vp7oOS/mcA03MMMz4o6VyIiIiIiUj11a7XA74AOxpg2xpgQYDzwpWdxTStgKnCbtXZ7me0RxpioH/8GhgEbz7Z5NCxQREREREQCjrW2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mUF2QRH1ghw8dVVf+rZrUfMVCPdtNMxay4tTF7Fs6x5C69XjpZuupFvJnNX73pnKCzcOI65BJPsOZ/Pkh7PILiiiS4s4Xr3lKkKC3YOU/pv0HdO+24jDGMZe0p3bB1wIwJMffcWqnWlk5xcSExXOQ1deypg+3X1an5rkq7ZZk5LGbf+cTMemTU59Z43ox4DEiovKnI2gq+8NuB5E8bO31+i9vTfB/+/DgGufqjpXLmAt8FdgirX2xJl+QE13ruRnxIedq4Dnw85VwPNB5+pcUlc6V3WRrztXAc+HnauA5+POlZy7ArFz5XzuTr/d2wc990HAtU9Vc64uA/oCo4HHjTF7gG9L/q221h73bfFEREREREQCg9fOlbX2x47U6wDGmNbAtbjnXbUAAveHEURERERERGpQVZErjDGdOTXv6jKgEe4O1799WzQREREREalTAnShCX+p6neuDgEHcS+9vhR4xVq70x8FExERERERCSRVRa7aWWuP+aUkIiIiIiJStyly5VVVP1M+5cc/jDFP+7gsIiIiIiIiAauqzlVsmb/H+bIgIiIiIiJSx+lHhL2qqnOl36gSERERERGphqrmXLU1xnwJmDJ/l7LWXuezkomIiIiISN3iqCo28/NWVedqZJm//+LLgoiIiIiIiASyqn5EeEnZ18aYekA3YL+1NtOXBRMRERERkTomQOdC+YvXuJ4x5t/GmK4lfzcA1gEfAt8bY27yQ74qJzkAACAASURBVPlEREREREQCQlWDJvtbazeV/P0LYLu1tjtwIfCUT0smIiIiIiJ1i1YL9KqqztWJMn8PBaYDWGvTfVYiERERERGRAFTVghbZxphrgP3AZcBdAMaYYCDMx2UTEREREZG6JEAjSv5SVefqPuANIAF4rEzEaggwy5cFExERERERCSRVrRa4HRheyfZ5wDxfFUpEREREROog/c6VV147V8aYZ73sttbaF2q4PCIiIiIiIgGpqmGB+ZVsCwfuBmIAda5ERERERESoeljgaz/+bYyJAh4FfglMAl47XT4RERERETkHaUELr6qKXGGMaQw8DtwC/A/oZa096uuCiYiIiIiIBJKq5lz9GbgeeAfobq3N80upRERERESk7lHkyquqlvt4AmgG/B9wwBiTU/Iv1xiT4/viiYiIiIiIBIaq5lxprUUREREREXHTUuxeqXVERERERERqQJULWpy1kyd8/hEBK/T/s3fn8VFV9//HXyf7SgKBJOz7FgigIiKiIJuiKLtSFa0LiNtXqtZWbG2pCGir9udSCyptXSiKGhZF1ggBUZB9X8ISErJCyL4Qkvv7Y2LIkBCizEwy9v18POZBZu7nzpxzuPfOPfdz7hn/ui5B/VagW/wuytOzrktQf51MrOsS1Gtvvze1rotQbz320N/rugj12tuv3V/XRai/oq+q6xKIuI7uuaqRMlciIiIiIiIO4PzMlYiIiIiI/DIoc1UjZa5EREREREQcQJkrERERERGpHWWuaqTMlYiIiIiIiAMocyUiIiIiIrWj37mqkVpHRERERETEAZS5EhERERGR2tE9VzVS5kpERERERMQB1LkSERERERFxAA0LFBERERGR2tGwwBopcyUiIiIiIuIAylyJiIiIiEjtGOVmaqLWERERERERcQBlrkREREREpHY8dM9VTZS5EhERERERcQBlrkREREREpHZ0z1WN1DoiIiIiIiIOoMyViIiIiIjUjn7nqkbKXImIiIiIiDiAMlciIiIiIlI7HsrN1EStIyIiIiIi4gDKXImIiIiISO3onqsaKXMlIiIiIiLiAMpciYiIiIhI7eh3rmqk1hEREREREXEAt85crT9yklkrt1BqWYzr1YFJ/brbLbcsi5krfyDuSDL+3p7MHNGPqKZhpOTk89ySbzmVV4gxhjuu6MjEPl3t1p33/V7+tmYb3/5mPA0D/FxZLYexLIuZyzYSdygRf28vZo4ZSFSzxlXiks7k8PSna8guKCaqWWNmj70RHy9PjmZk8XzMWvYln+LJIVfzQP+eAKRk5/Hc599wKre8/a7uwsRro11dvcvijG3nrbidfLb9cMX2MvXGKxjQobnL63a51scnMWvFZkrLLMZd0ZFJ/XvYLbcsi5krNhN3OMm2XY3sT1TTMACeX7KBdYeSaBTox5JHRlWss3zfcd5et4OjGVl88tAIulezHbqltlF4DB4PxmDt2oi1aaX98kYReAyfCBEtsdYvxfphte11Ty887noKPL3AwwPr4Hasb79yffkdbP3RFGat2W7br3q0Y1Jf++OqZVnMXLOduKMptv1qeB+iIhtVLC8tK2P8B6uICPLnnXE32K07b/MB/rZ2J98+PoqGAb4uqU9dmfj+20SPuJnc9AxejO5b18VxufUnMpj17X5KLRjX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y6U6V68DJcB6YDgQBTzp7EKJiIiIiEg95Ha5JNe6VOcqyrKsaABjzPvU89+9EhERERERqSuX6lyV/PiHZVnnHDZRgYiIiIiIuCH1B2pyqc5VT2PMjz/KYQD/8ue23w+1rAYXX1VEREREROR/R42dK8uyPF1VEBERERERqec0kq1Gl/oRYREREREREamFSw0LFBERERERsVHmqkbKXImIiIiIiDiAOlciIiIiIiIOoGGBIiIiIiJSSxoWWBNlrkRERERERBxAmSsREREREakdTWhRI2WuREREREREHECZKxERERERqSVlrmqizJWIiIiIiIgDKHMlIiIiIiK1o3uuaqTMlYiIiIiIiAMocyUiIiIiIrWjzFWNlLkSERERERFxAGWuRERERESklpS5qokyVyIiIiIiIg6gzJWIiIiIiNSK0T1XNVLmSkRERERExAGUuRIRERERkdpR5qpGzu9ceSg5dlHePnVdAnFXHp51XYL6Swd9ESfRvnUx/7+9Ow+vojofOP59kxAISwh7QECickZAWRWLS6EglFotFLFaBdGi1qpttVb9FVo1VRG1FK1orRWrdWkpCqiguBAxiiwCIosw7DskYcsCBAic3x8zCTfbTYS7ZHk/z3OfZOaemZzzZubMPcvMjdd6J6ij1kY7C0pFjLZ8lFJKKaWUUioEdFqgUkoppZRSqpJ0pDYYHblSSimllFJKqRDQkSullFJKKaVU5eg9hkHpyJVSSimllFJKhYCOXCmllFJKKaUqR0eugtKRK6WUUkoppZQKAR25UkoppZRSSlWSjlwFoyNXSimllFJKKRUCOnKllFJKKaWUqhy95yooHblSSimllFJKqRDQkSullFJKKaVU5ejAVVA6cqWUUkoppZRSIaAjV0oppZRSSqlK0qGrYHTkSimllFJKKaVCQEeulFJKKaWUUpWjTwsMSkeulFJKKaWUUioEtHGllFJKKaWUUiGg0wKVUkoppZRSlaPTAoPSkSullFJKKaWUCgEduVJKKaWUUkpVko5cBaMjV0oppZRSSikVAjpypZRSSimllKocvecqKB25UkoppZRSSqkQ0JErpZRSSimlVOXoyFVQOnKllFJKKaWUUiFQrUeurLWMm5ZG+uqNJNSJY9z1V9C5XatS6bbvPcC9r84k+9BhOrdtxfgRPyY+LpbJaYuYufhbAI6fsGzM2MsX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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[128]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Look Up Table for Above Plot</span>
<span class="n">pprint</span><span class="p">({</span><span class="s2">&quot;TQ&quot;</span><span class="p">:</span> <span class="s2">&quot;Title Contains Question&quot;</span><span class="p">,</span><span class="s2">&quot;LT&quot;</span> <span class="p">:</span> <span class="s2">&quot;Length of Tilte&quot;</span><span class="p">,</span> <span class="s2">&quot;TSEN&quot;</span> <span class="p">:</span> <span class="s2">&quot;Title Sentiment&quot;</span><span class="p">,</span> <span class="s2">&quot;TSUB&quot;</span> <span class="p">:</span> <span class="s2">&quot;Title Subjectivity&quot;</span><span class="p">,</span>
                                      <span class="s2">&quot;OC&quot;</span> <span class="p">:</span> <span class="s2">&quot;Original Content&quot;</span><span class="p">,</span> <span class="s2">&quot;NSFW&quot;</span> <span class="p">:</span> <span class="s2">&quot;Not Safe for Work&quot;</span><span class="p">,</span> <span class="s2">&quot;SP&quot;</span> <span class="p">:</span> <span class="s2">&quot;Spoiler&quot;</span><span class="p">,</span> 
                                      <span class="s2">&quot;LB&quot;</span> <span class="p">:</span> <span class="s2">&quot;Length of Body&quot;</span><span class="p">,</span> <span class="s2">&quot;PT&quot;</span> <span class="p">:</span> <span class="s2">&quot;Post Type&quot;</span><span class="p">,</span> <span class="s2">&quot;UR&quot;</span> <span class="p">:</span> <span class="s2">&quot;Upvote Ratio&quot;</span><span class="p">})</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>{&#39;LB&#39;: &#39;Length of Body&#39;,
 &#39;LT&#39;: &#39;Length of Tilte&#39;,
 &#39;NSFW&#39;: &#39;Not Safe for Work&#39;,
 &#39;OC&#39;: &#39;Original Content&#39;,
 &#39;PT&#39;: &#39;Post Type&#39;,
 &#39;SP&#39;: &#39;Spoiler&#39;,
 &#39;TQ&#39;: &#39;Title Contains Question&#39;,
 &#39;TSEN&#39;: &#39;Title Sentiment&#39;,
 &#39;TSUB&#39;: &#39;Title Subjectivity&#39;,
 &#39;UR&#39;: &#39;Upvote Ratio&#39;}
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Throughout this tutorial, we have been trying to predict if a post will join the ranks of other top posts, or be condemned as a controversial post. The correlation matrix above shows that most numerical features of our dataset didn't actually affect the results of our linear models. Interestingly, both the length post body and the use of original content negatively correlated with both the post type (PT) and upvote ratio (UR). In order to have a hot post, make sure to always repost material and never write well-thought-out content!</p>
<p>Using this information, we can test our logistic regression model using only len_body and is_oc to predict post_type to see if we can get the same level of performance:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[129]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">inputClassificationData</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">outputClassificationData</span> <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span class="n">tableRow</span> <span class="ow">in</span> <span class="n">dataSet</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
    <span class="n">originalContent</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;is_oc&quot;</span><span class="p">]</span>
    <span class="n">lenBody</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;len_body&quot;</span><span class="p">]</span>
    <span class="n">post_type</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;post_type&quot;</span><span class="p">]</span>

    <span class="n">inputClassificationData</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">lenBody</span><span class="p">,</span> <span class="n">originalContent</span><span class="p">])</span>
    <span class="n">outputClassificationData</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">post_type</span><span class="p">])</span>
    
<span class="n">trainInput</span><span class="p">,</span> <span class="n">testInput</span><span class="p">,</span> <span class="n">trainOutput</span><span class="p">,</span> <span class="n">testOutput</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">inputClassificationData</span><span class="p">,</span> <span class="n">outputClassificationData</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.1</span><span class="p">)</span>
<span class="n">ratioRegression</span> <span class="o">=</span> <span class="n">LogisticRegression</span><span class="p">()</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">trainInput</span><span class="p">),</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">trainOutput</span><span class="p">))</span>
<span class="n">predictedOutput</span> <span class="o">=</span> <span class="n">ratioRegression</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">testInput</span><span class="p">))</span>
<span class="n">modelPerformance</span> <span class="o">=</span> <span class="p">[]</span>

<span class="n">testOutput</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">testOutput</span><span class="p">]</span>
<span class="n">predictedOutput</span> <span class="o">=</span> <span class="n">predictedOutput</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>

<span class="n">Accuracy</span> <span class="o">=</span> <span class="n">metrics</span><span class="o">.</span><span class="n">accuracy_score</span><span class="p">(</span><span class="n">testOutput</span><span class="p">,</span> <span class="n">predictedOutput</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Accuracy: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">Accuracy</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Accuracy: 0.7303370786516854
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Although our logistic regression predictor is able to acheive "better than random" accuracy, the performance is still much lower than when we included other features. A noteable feature that we are missing is the subreddit itself.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[130]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">inputClassificationData</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">outputClassificationData</span> <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span class="n">tableRow</span> <span class="ow">in</span> <span class="n">dataSet</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
    <span class="n">subReddit</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;subreddit&quot;</span><span class="p">]</span>
    <span class="n">SR_oneHotEncoding</span> <span class="o">=</span> <span class="n">subRedditOneHotEncoding</span><span class="p">[</span><span class="s2">&quot;subReddit_&quot;</span> <span class="o">+</span> <span class="n">subReddit</span><span class="p">]</span><span class="o">.</span><span class="n">to_list</span><span class="p">()</span>
    <span class="n">originalContent</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;is_oc&quot;</span><span class="p">]</span>
    <span class="n">lenBody</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;len_body&quot;</span><span class="p">]</span>
    <span class="n">post_type</span> <span class="o">=</span> <span class="n">tableRow</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="s2">&quot;post_type&quot;</span><span class="p">]</span>

    <span class="n">inputClassificationData</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">SR_oneHotEncoding</span> <span class="o">+</span> <span class="p">[</span><span class="n">lenBody</span><span class="p">,</span> <span class="n">originalContent</span><span class="p">])</span>
    <span class="n">outputClassificationData</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">post_type</span><span class="p">])</span>
    
<span class="n">trainInput</span><span class="p">,</span> <span class="n">testInput</span><span class="p">,</span> <span class="n">trainOutput</span><span class="p">,</span> <span class="n">testOutput</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">inputClassificationData</span><span class="p">,</span> <span class="n">outputClassificationData</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.1</span><span class="p">)</span>
<span class="n">ratioRegression</span> <span class="o">=</span> <span class="n">LogisticRegression</span><span class="p">()</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">trainInput</span><span class="p">),</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">trainOutput</span><span class="p">))</span>
<span class="n">predictedOutput</span> <span class="o">=</span> <span class="n">ratioRegression</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">testInput</span><span class="p">))</span>
<span class="n">modelPerformance</span> <span class="o">=</span> <span class="p">[]</span>

<span class="n">testOutput</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">testOutput</span><span class="p">]</span>
<span class="n">predictedOutput</span> <span class="o">=</span> <span class="n">predictedOutput</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>

<span class="n">Accuracy</span> <span class="o">=</span> <span class="n">metrics</span><span class="o">.</span><span class="n">accuracy_score</span><span class="p">(</span><span class="n">testOutput</span><span class="p">,</span> <span class="n">predictedOutput</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Accuracy: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">Accuracy</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Accuracy: 0.9101123595505618
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>With the subreddit included, our accuracy jumps from 73% to 91%! As suspected, the subreddit that you post in significantly impacts the likelihood of going viral on Reddit.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 style="text-align: center;">Conclusion</h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>To review, we scraped thousands of Reddit's best and worst posts, processed their features, performed some exploratory subreddit analysis, and attempted to predict a new post's performance with four different machine learning models. In the end, we have a working logistic regression model that can predict whether a post is more likely to be "top" or 
"controversial" with over 90% accuracy! If you'd like to make your own viral Reddit post, here are some of our suggestions:</p>
<p><ol>
    <li>Be persistent. Reddit has over 20 thousand daily submissions across all subreddits; it may take a few posts before people catch on to your content.</li>
    <li>Post on a large, generic-topic subreddit. The ones that most frequently broke the top 1000 posts were r/pics, r/aww, r/funny, r/gifs, and r/gaming.</li>
    <li>Post a link to an image or a video instead of original content. Posts with text had a significant negative correlation with upvote_ratio.</li>
</ol>
If you're interested in Reddit, there's so much data left to explore; the site hosts over 50 thousand subreddits and over 330 million users, so we've only touched on a small subset of the data that the site generates. Even if you're not interested, we hope this tutorial gave you some insight into how a hugely popular social news site chooses its favorite (and least favorite) posts. All in all, you're ready to go viral, and we hope it was worth the read!</p>

</div>
</div>
</div>
    </div>
  </div>
</body>

 


</html>
